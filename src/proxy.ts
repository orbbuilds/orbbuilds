import { clerkMiddleware } from "@clerk/nextjs/server";
import { type NextRequest, NextResponse } from "next/server";
import { findEpisode } from "@/lib/episodes";

// Clerk is only active when keys are configured, so the starter runs without secrets.
const clerkEnabled = Boolean(process.env.CLERK_SECRET_KEY);
const clerk = clerkEnabled ? clerkMiddleware() : null;

const EPISODE_PATH = /^\/episodes\/([^/]+)\/?$/;

// Episode pages stream (Cache Components), so notFound() can't change the status code
// once rendering starts. Catch unknown episode numbers here and serve the not-found
// page with a real 404 instead of a 200.
function unknownEpisode(req: NextRequest): NextResponse | null {
  const match = EPISODE_PATH.exec(req.nextUrl.pathname);
  if (!match) return null;
  let slug: string;
  try {
    slug = decodeURIComponent(match[1]);
  } catch {
    slug = "";
  }
  if (findEpisode(slug)) return null;
  return NextResponse.rewrite(new URL("/episodes/not-found", req.url), { status: 404 });
}

export default function proxy(req: NextRequest, event: Parameters<NonNullable<typeof clerk>>[1]) {
  const missing = unknownEpisode(req);
  if (missing) return missing;
  return clerk ? clerk(req, event) : NextResponse.next();
}

export const config = {
  matcher: [
    "/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)",
    "/(api|trpc)(.*)",
  ],
};
