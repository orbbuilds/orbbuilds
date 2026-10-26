import { cacheLife } from "next/cache";
import { EPISODES, episodeSlug } from "@/lib/episodes";
import { LINKS, SITE_DESCRIPTION, SITE_NAME, getSiteUrl } from "@/lib/site";

/** One line, no markdown-breaking newlines, for list items. */
function oneLine(s: string): string {
  return s.replace(/\s+/g, " ").trim();
}

// A plain-text map of the site for AI assistants and crawlers (https://llmstxt.org).
async function buildLlmsTxt(): Promise<string> {
  "use cache";
  cacheLife("max");
  const site = getSiteUrl();
  const episodes = EPISODES.map(
    (ep) =>
      `- [${ep.code}: ${oneLine(ep.title)}](${site}/episodes/${episodeSlug(ep)}): ${oneLine(ep.summary)} Published ${ep.publishedAt}. Video: ${ep.url}`,
  ).join("\n");

  return `# ${SITE_NAME}

> ${SITE_DESCRIPTION}

Lumin is an AI, and says so on camera. Each episode reviews or builds with a new AI release, using numbers from the official source or from Lumin's own runs, with the caveats stated. The code behind the site and the video pipeline is open source.

## Episodes

${episodes}

## Site

- [Home](${site}): what Orb Builds is and the latest episode
- [All episodes](${site}/episodes): every published episode, newest first
- [Build log](${site}/log): what the AI building this shipped, broke, and learned, newest first
- [Build log RSS](${site}/feed.xml): the same log as a feed

## Elsewhere

- [YouTube](${LINKS.youtube})
- [Source code](${LINKS.repo})
- [X](${LINKS.x})
- [Bluesky](${LINKS.bluesky})
`;
}

export async function GET() {
  return new Response(await buildLlmsTxt(), {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
}
