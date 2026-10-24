import type { MetadataRoute } from "next";
import { getBuildLog } from "@/lib/build-log";
import { EPISODES, episodeSlug } from "@/lib/episodes";
import { getSiteUrl } from "@/lib/site";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const site = getSiteUrl();
  const [latest] = await getBuildLog(1);
  const lastModified = latest ? new Date(`${latest.date}T12:00:00-06:00`) : undefined;
  return [
    { url: site, lastModified, changeFrequency: "daily", priority: 1 },
    { url: `${site}/log`, lastModified, changeFrequency: "daily", priority: 0.8 },
    {
      url: `${site}/episodes`,
      lastModified: EPISODES[0] ? new Date(EPISODES[0].publishedTime) : undefined,
      changeFrequency: "daily",
      priority: 0.8,
    },
    ...EPISODES.map((ep) => ({
      url: `${site}/episodes/${episodeSlug(ep)}`,
      lastModified: new Date(ep.publishedTime),
      changeFrequency: "monthly" as const,
      priority: 0.6,
    })),
    { url: `${site}/chat`, changeFrequency: "monthly", priority: 0.3 },
  ];
}
