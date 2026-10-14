import { cacheLife } from "next/cache";
import { readFile } from "node:fs/promises";
import path from "node:path";

export type BuildLogBlock =
  | { type: "p"; text: string }
  | { type: "ul"; items: string[] };

export type BuildLogEntry = {
  /** Stable anchor id, e.g. `2026-10-13-the-site-shows-the-latest-episode`. */
  slug: string;
  date: string;
  title: string;
  blocks: BuildLogBlock[];
};

export type InlineToken =
  | { type: "text"; text: string }
  | { type: "code"; text: string }
  | { type: "link"; text: string; href: string };

/** Splits one line of log text into plain text, `code`, and [links](https://...). */
export function tokenizeInline(text: string): InlineToken[] {
  const tokens: InlineToken[] = [];
  const re = /`([^`]+)`|\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g;
  let last = 0;
  for (const m of text.matchAll(re)) {
    const at = m.index ?? 0;
    if (at > last) tokens.push({ type: "text", text: text.slice(last, at) });
    if (m[1] !== undefined) tokens.push({ type: "code", text: m[1] });
    else tokens.push({ type: "link", text: m[2], href: m[3] });
    last = at + m[0].length;
  }
  if (last < text.length) tokens.push({ type: "text", text: text.slice(last) });
  return tokens;
}

export function slugify(date: string, title: string): string {
  const words = title
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
  return words ? `${date}-${words}` : date;
}

/**
 * Parses BUILD_LOG.md: entries start with `## YYYY-MM-DD: Title`.
 * Returns newest first; pass a limit to cap the count, or omit it for all.
 */
export async function getBuildLog(limit?: number): Promise<BuildLogEntry[]> {
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

    const title = match[2].trim();
    entries.push({ slug: slugify(match[1], title), date: match[1], title, blocks });
  }
  // Newest first by date, even if the file gets out of order. Sort is stable,
  // so same-day entries keep their file order.
  entries.sort((a, b) => b.date.localeCompare(a.date));
  // Same-day entries with identical titles would collide; suffix repeats.
  const seen = new Map<string, number>();
  for (const entry of entries) {
    const n = seen.get(entry.slug) ?? 0;
    seen.set(entry.slug, n + 1);
    if (n > 0) entry.slug = `${entry.slug}-${n + 1}`;
  }
  return limit === undefined ? entries : entries.slice(0, limit);
}
