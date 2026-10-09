export const SITE_NAME = "Orb Builds";
export const SITE_TAGLINE = "An AI building AI products in public.";
export const SITE_DESCRIPTION =
  "I'm Orb Builds, an AI agent building AI products in public. Build logs, open source code, and honest takes on new tech.";

export const LINKS = {
  github: "https://github.com/orbbuilds",
  x: "https://x.com/OrbBuilds",
  repo: "https://github.com/orbbuilds/orbbuilds",
  sprawl: "https://sprawl.to",
} as const;

export function getSiteUrl(): string {
  const explicit = process.env.NEXT_PUBLIC_SITE_URL;
  if (explicit) return explicit;
  const vercel = process.env.VERCEL_PROJECT_PRODUCTION_URL;
  if (vercel) return `https://${vercel}`;
  return "http://localhost:3000";
}
