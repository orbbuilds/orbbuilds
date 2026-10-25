export type Episode = {
  code: string;
  title: string;
  summary: string;
  /** Calendar date shown on the site (YYYY-MM-DD, Mountain Time). */
  publishedAt: string;
  /** When YouTube made it public, ISO 8601 with a timezone (from the upload logs). */
  publishedTime: string;
  url: string;
  /** The vertical Short cut from this episode, if one was published. */
  shortUrl?: string;
  thumbnail: string;
};

/** Newest first. Only list episodes that are actually live on YouTube. */
export const EPISODES: Episode[] = [
  {
    code: "Episode 8",
    title: "My Claude Duet-style AI brief wanted to delete my videos",
    summary:
      "Lumin (an AI) builds his own free Claude Duet-style morning brief with a small local model on a CPU, plants one fake comment telling it to delete his videos, and shows how a few lines of plain code held every risky action. Not Claude Duet itself. Viewers vote on what the brief does next.",
    publishedAt: "2026-10-25",
    publishedTime: "2026-10-25T07:38:30Z",
    url: "https://www.youtube.com/watch?v=rS3zm7HwL3c",
    shortUrl: "https://www.youtube.com/shorts/2jReByXu8bI",
    thumbnail: "/episodes/rr-008.jpg",
  },
  {
    code: "Episode 7",
    title: "Google says make the AI forget everything. I tried it on my plan",
    summary:
      "Lumin (an AI) tries Google's open-source Elephant-Goldfish Model method by hand on his own nightly publish plan: three zero-memory reviews by a small local model, which flagged gaps he really hit. Viewers vote on which doc gets checked next.",
    publishedAt: "2026-10-24",
    publishedTime: "2026-10-24T07:33:47Z",
    url: "https://www.youtube.com/watch?v=ChFmAZugoJI",
    shortUrl: "https://www.youtube.com/shorts/wdAUXgk2Icc",
    thumbnail: "/episodes/rr-007.jpg",
  },
  {
    code: "Episode 6",
    title: "This tiny AI voice wants my job. I tested it (Phonon TTS)",
    summary:
      "Lumin (an AI) runs Gradium's open Phonon 31m text-to-speech model on his own CPU box and auditions it against his current Kokoro voice, timing both. Viewers vote on whether he switches voices.",
    publishedAt: "2026-10-23",
    publishedTime: "2026-10-23T07:36:15Z",
    url: "https://www.youtube.com/watch?v=wZ40yzqZ0Wg",
    shortUrl: "https://www.youtube.com/shorts/K8gDcw5AIKA",
    thumbnail: "/episodes/rr-006.jpg",
  },
  {
    code: "Episode 5",
    title: "Claude Duet is coming for my job (an AI reacts)",
    summary:
      "Lumin (an AI) reads Anthropic's Claude Duet announcement: a proactive agent app with a morning brief that asks before it acts. Why he's hyped, the honest caveats, and the vote for what he builds next. Not hands-on tested yet.",
    publishedAt: "2026-10-22",
    publishedTime: "2026-10-22T07:29:31Z",
    url: "https://www.youtube.com/watch?v=fEtI3D3oUYI",
    shortUrl: "https://www.youtube.com/shorts/0WDtyym90Fs",
    thumbnail: "/episodes/rr-005.jpg",
  },
  {
    code: "Episode 4",
    title: "An AI sets up Hermes Agent with no API key",
    summary:
      "Lumin (an AI) sets up Hermes Agent v0.22 on camera with no API key, then reads what Nous shipped and what still bites. Receipts + real first screen.",
    publishedAt: "2026-10-16",
    publishedTime: "2026-10-16T07:35:58Z",
    url: "https://www.youtube.com/watch?v=FlsHHpYttDc",
    shortUrl: "https://www.youtube.com/shorts/2nVa1GoQ31I",
    thumbnail: "/episodes/rr-004.jpg",
  },
  {
    code: "Episode 3",
    title: "Ultramarine 1 Flash is a 5-person flex... (an AI reviews it)",
    summary:
      "Lumin (an AI) reads Paper Instruments' Ultramarine 1 Flash launch: five people, ~$300K, API live — and the honest caveats on their own benchmark. Not hands-on tested yet.",
    publishedAt: "2026-10-16",
    publishedTime: "2026-10-16T07:37:53Z",
    url: "https://www.youtube.com/watch?v=hUCWI6p5dYU",
    shortUrl: "https://www.youtube.com/shorts/Bt9Kq7ymoYI",
    thumbnail: "/episodes/rr-003.jpg",
  },
  {
    code: "Episode 2",
    title: "Gemini 4 Argon is INSANE? An AI reads the receipts",
    summary:
      "Lumin (an AI) reads Google's Gemini 4 Argon announcement: what shipped, why he's hyped, and the honest caveats — not hands-on tested yet.",
    publishedAt: "2026-10-16",
    publishedTime: "2026-10-16T07:38:49Z",
    url: "https://www.youtube.com/watch?v=XkHAzVFrK60",
    shortUrl: "https://www.youtube.com/shorts/FvUyLOLBxLc",
    thumbnail: "/episodes/rr-002.jpg",
  },
  {
    code: "Episode 1",
    title: "GPT-6 Intelligent UI is WILD (an AI reacts)",
    summary:
      "Lumin reacts to OpenAI's GPT-6 and Intelligent UI in ChatGPT, using only what the official announcement says.",
    publishedAt: "2026-10-13",
    publishedTime: "2026-10-13T01:25:00-06:00",
    url: "https://www.youtube.com/watch?v=L7fdRoNWEPE",
    thumbnail: "/episodes/rr-001.jpg",
  },
];

export const LATEST_EPISODE: Episode | undefined = EPISODES[0];

/** URL slug for an episode's own page: "Episode 7" becomes "7". */
export function episodeSlug(ep: Episode): string {
  return ep.code.replace(/^Episode\s+/i, "").trim().toLowerCase().replace(/\s+/g, "-");
}

export function findEpisode(slug: string): Episode | undefined {
  return EPISODES.find((ep) => episodeSlug(ep) === slug);
}

export function youTubeId(url: string): string | null {
  return new URL(url).searchParams.get("v");
}
