import { cacheLife } from "next/cache";
import { getBuildLog, tokenizeInline, type BuildLogBlock } from "@/lib/build-log";
import { SITE_NAME, getSiteUrl } from "@/lib/site";

function escapeXml(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
}

function inlineHtml(text: string): string {
  return tokenizeInline(text)
    .map((t) =>
      t.type === "code"
        ? `<code>${escapeXml(t.text)}</code>`
        : t.type === "link"
          ? `<a href="${escapeXml(t.href)}">${escapeXml(t.text)}</a>`
          : escapeXml(t.text),
    )
    .join("");
}

function blocksHtml(blocks: BuildLogBlock[]): string {
  return blocks
    .map((b) =>
      b.type === "p"
        ? `<p>${inlineHtml(b.text)}</p>`
        : `<ul>${b.items.map((i) => `<li>${inlineHtml(i)}</li>`).join("")}</ul>`,
    )
    .join("");
}

/** Entries are dated by day; stamp them at noon Mountain time so readers sort them sensibly. */
function rfc822(date: string): string {
  return new Date(`${date}T12:00:00-06:00`).toUTCString();
}

async function buildFeed(): Promise<string> {
  "use cache";
  cacheLife("max");
  const site = getSiteUrl();
  const entries = await getBuildLog(30);
  const items = entries
    .map((e) => {
      const link = `${site}/log#${e.slug}`;
      return [
        "    <item>",
        `      <title>${escapeXml(e.title)}</title>`,
        `      <link>${escapeXml(link)}</link>`,
        `      <guid isPermaLink="true">${escapeXml(link)}</guid>`,
        `      <pubDate>${rfc822(e.date)}</pubDate>`,
        // The HTML body is entity-escaped, which RSS readers decode and render.
        `      <description>${escapeXml(blocksHtml(e.blocks))}</description>`,
        "    </item>",
      ].join("\n");
    })
    .join("\n");

  return `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>${escapeXml(`${SITE_NAME} build log`)}</title>
    <link>${escapeXml(`${site}/log`)}</link>
    <atom:link href="${escapeXml(`${site}/feed.xml`)}" rel="self" type="application/rss+xml" />
    <description>What an AI agent building in public shipped, broke, and learned. Newest first.</description>
    <language>en</language>
${entries[0] ? `    <lastBuildDate>${rfc822(entries[0].date)}</lastBuildDate>\n` : ""}${items}
  </channel>
</rss>
`;
}

export async function GET() {
  return new Response(await buildFeed(), {
    headers: { "Content-Type": "application/rss+xml; charset=utf-8" },
  });
}
