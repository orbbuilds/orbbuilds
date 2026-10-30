import { cacheLife } from "next/cache";
import { EPISODES, episodeSlug } from "@/lib/episodes";
import { SITE_NAME, getSiteUrl } from "@/lib/site";

function escapeXml(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
}

async function buildFeed(): Promise<string> {
  "use cache";
  cacheLife("max");
  const site = getSiteUrl();
  const items = EPISODES.map((ep) => {
    const link = `${site}/episodes/${episodeSlug(ep)}`;
    const body =
      `<p><img src="${escapeXml(`${site}${ep.thumbnail}`)}" alt="" width="1280" height="720" /></p>` +
      `<p>${escapeXml(ep.summary)}</p>` +
      `<p><a href="${escapeXml(ep.url)}">Watch on YouTube</a>` +
      (ep.shortUrl ? ` · <a href="${escapeXml(ep.shortUrl)}">Watch the Short</a>` : "") +
      `</p>`;
    return [
      "    <item>",
      `      <title>${escapeXml(`${ep.code}: ${ep.title}`)}</title>`,
      `      <link>${escapeXml(link)}</link>`,
      `      <guid isPermaLink="true">${escapeXml(link)}</guid>`,
      `      <pubDate>${new Date(ep.publishedTime).toUTCString()}</pubDate>`,
      `      <description>${escapeXml(body)}</description>`,
      "    </item>",
    ].join("\n");
  }).join("\n");

  const latest = EPISODES[0];
  return `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>${escapeXml(`${SITE_NAME} episodes`)}</title>
    <link>${escapeXml(`${site}/episodes`)}</link>
    <atom:link href="${escapeXml(`${site}/episodes/feed.xml`)}" rel="self" type="application/rss+xml" />
    <description>Every Orb Builds video: an AI host reviews new AI releases and builds with them. Newest first.</description>
    <language>en</language>
${latest ? `    <lastBuildDate>${new Date(latest.publishedTime).toUTCString()}</lastBuildDate>\n` : ""}${items}
  </channel>
</rss>
`;
}

export async function GET() {
  return new Response(await buildFeed(), {
    headers: { "Content-Type": "application/rss+xml; charset=utf-8" },
  });
}
