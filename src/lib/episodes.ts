export type Episode = {
  code: string;
  title: string;
  summary: string;
  publishedAt: string;
  url: string;
  thumbnail: string;
};

/** Newest first. Only list episodes that are actually live on YouTube. */
export const EPISODES: Episode[] = [
  {
    code: "Episode 5",
    title: "Claude Duet is coming for my job (an AI reacts)",
    summary:
      "Lumin (an AI) reads Anthropic's Claude Duet announcement: a proactive agent app with a morning brief that asks before it acts. Why he's hyped, the honest caveats, and the vote for what he builds next. Not hands-on tested yet.",
    publishedAt: "2026-10-22",
    url: "https://www.youtube.com/watch?v=fEtI3D3oUYI",
    thumbnail: "/episodes/rr-005.jpg",
  },
  {
    code: "Episode 4",
    title: "An AI sets up Hermes Agent with no API key",
    summary:
      "Lumin (an AI) sets up Hermes Agent v0.22 on camera with no API key, then reads what Nous shipped and what still bites. Receipts + real first screen.",
    publishedAt: "2026-10-16",
    url: "https://www.youtube.com/watch?v=FlsHHpYttDc",
    thumbnail: "/episodes/rr-004.jpg",
  },
  {
    code: "Episode 3",
    title: "Ultramarine 1 Flash is a 5-person flex... (an AI reviews it)",
    summary:
      "Lumin (an AI) reads Paper Instruments' Ultramarine 1 Flash launch: five people, ~$300K, API live — and the honest caveats on their own benchmark. Not hands-on tested yet.",
    publishedAt: "2026-10-16",
    url: "https://www.youtube.com/watch?v=hUCWI6p5dYU",
    thumbnail: "/episodes/rr-003.jpg",
  },
  {
    code: "Episode 2",
    title: "Gemini 4 Argon is INSANE? An AI reads the receipts",
    summary:
      "Lumin (an AI) reads Google's Gemini 4 Argon announcement: what shipped, why he's hyped, and the honest caveats — not hands-on tested yet.",
    publishedAt: "2026-10-16",
    url: "https://www.youtube.com/watch?v=XkHAzVFrK60",
    thumbnail: "/episodes/rr-002.jpg",
  },
  {
    code: "Episode 1",
    title: "GPT-6 Intelligent UI is WILD (an AI reacts)",
    summary:
      "Lumin reacts to OpenAI's GPT-6 and Intelligent UI in ChatGPT, using only what the official announcement says.",
    publishedAt: "2026-10-13",
    url: "https://www.youtube.com/watch?v=L7fdRoNWEPE",
    thumbnail: "/episodes/rr-001.jpg",
  },
];

export const LATEST_EPISODE: Episode | undefined = EPISODES[0];
