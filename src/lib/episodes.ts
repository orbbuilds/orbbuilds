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
