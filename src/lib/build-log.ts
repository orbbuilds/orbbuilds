import { cacheLife } from "next/cache";
import { readFile } from "node:fs/promises";
import path from "node:path";

export type BuildLogBlock =
  | { type: "p"; text: string }
  | { type: "ul"; items: string[] };

export type BuildLogEntry = {
  date: string;
  title: string;
  blocks: BuildLogBlock[];
};

/** Parses BUILD_LOG.md: entries start with `## YYYY-MM-DD: Title`. */
export async function getBuildLog(limit = 3): Promise<BuildLogEntry[]> {
  "use cache";
  cacheLife("max");
  let raw: string;
  try {
    raw = await readFile(path.join(process.cwd(), "BUILD_LOG.md"), "utf8");
  } catch {
    return [];
  }

  const entries: BuildLogEntry[] = [];
  const sections = raw.split(/^## /m).slice(1);
  for (const section of sections) {
    const [heading, ...rest] = section.split("\n");
    const match = heading.match(/^(\d{4}-\d{2}-\d{2})\s*[:\-–—]\s*(.+)$/);
    if (!match) continue;

    const blocks: BuildLogBlock[] = [];
    let items: string[] | null = null;
    let para: string[] = [];
    const flushPara = () => {
      if (para.length) blocks.push({ type: "p", text: para.join(" ") });
      para = [];
    };
    const flushList = () => {
      if (items) blocks.push({ type: "ul", items });
      items = null;
    };
    for (const line of rest) {
      const bullet = line.match(/^\s*[-*]\s+(.*)$/);
      if (bullet) {
        flushPara();
        (items ??= []).push(bullet[1].trim());
      } else if (line.trim() === "") {
        flushPara();
        flushList();
      } else {
        flushList();
        para.push(line.trim());
      }
    }
    flushPara();
    flushList();

    entries.push({ date: match[1], title: match[2].trim(), blocks });
  }
  // Newest first by date, even if the file gets out of order. Sort is stable,
  // so same-day entries keep their file order.
  entries.sort((a, b) => b.date.localeCompare(a.date));
  return entries.slice(0, limit);
}
