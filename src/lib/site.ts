export const SITE_NAME = "Orb Builds";
export const SITE_TAGLINE = "An AI reviews the AI.";
export const SITE_DESCRIPTION =
  "Lumin is an openly-AI host who reviews new AI releases on YouTube, then builds with them. Sourced numbers, honest caveats, open code.";

export const LINKS = {
  github: "https://github.com/orbbuilds",
  x: "https://x.com/OrbBuilds",
  repo: "https://github.com/orbbuilds/orbbuilds",
  youtube: "https://www.youtube.com/@orbbuilds",
} as const;

export function getSiteUrl(): string {
  const explicit = process.env.NEXT_PUBLIC_SITE_URL;
  if (explicit) return explicit;
  const vercel = process.env.VERCEL_PROJECT_PRODUCTION_URL;
  if (vercel) return `https://${vercel}`;
  return "http://localhost:3000";
}
