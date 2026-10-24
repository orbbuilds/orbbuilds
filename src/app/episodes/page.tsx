import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { focus } from "@/components/landing/build-log";
import { YouTubeIcon } from "@/components/landing/icons";
import { EPISODES, episodeSlug, youTubeId } from "@/lib/episodes";
import { LINKS, SITE_NAME, getSiteUrl } from "@/lib/site";

/** schema.org ItemList of VideoObjects so search engines can show these as videos. */
function episodesJsonLd() {
  const site = getSiteUrl();
  return {
    "@context": "https://schema.org",
    "@type": "ItemList",
    name: `${SITE_NAME} episodes`,
    itemListElement: EPISODES.map((ep, i) => {
      const id = youTubeId(ep.url);
      return {
        "@type": "ListItem",
        position: i + 1,
        item: {
          "@type": "VideoObject",
          name: ep.title,
          description: ep.summary,
          uploadDate: ep.publishedTime,
          thumbnailUrl: `${site}${ep.thumbnail}`,
          url: `${site}/episodes/${episodeSlug(ep)}`,
          sameAs: ep.url,
          ...(id ? { embedUrl: `https://www.youtube.com/embed/${id}` } : {}),
        },
      };
    }),
  };
}

export const metadata: Metadata = {
  title: "Episodes",
  description:
    "Every Orb Builds video, newest first: Lumin, an AI host, reviews new AI releases and then builds with them.",
  alternates: { canonical: "/episodes" },
  openGraph: {
    url: "/episodes",
    title: "Episodes | Orb Builds",
    description:
      "Every Orb Builds video, newest first: Lumin, an AI host, reviews new AI releases and then builds with them.",
    images: [
      {
        url: "/episodes-og.png",
        width: 1200,
        height: 630,
        alt: "Orb Builds Episodes — Lumin reviews new AI releases, then builds with them",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Episodes | Orb Builds",
    description:
      "Every Orb Builds video, newest first: Lumin, an AI host, reviews new AI releases and then builds with them.",
    images: ["/episodes-og.png"],
  },
};

export default function EpisodesPage() {
  return (
    <div className="landing relative isolate min-h-dvh overflow-x-clip bg-[#081538] text-slate-200">
      <a
        href="#main"
        className={`sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-50 focus:rounded-md focus:bg-white focus:px-4 focus:py-2 focus:text-slate-900 ${focus}`}
      >
        Skip to content
      </a>
      <div aria-hidden className="landing-stars absolute inset-0 -z-10" />
      <script
        type="application/ld+json"
        // JSON.stringify output with "<" escaped so a title can't close the tag.
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(episodesJsonLd()).replace(/</g, "\\u003c"),
        }}
      />

      <header className="mx-auto flex w-full max-w-5xl items-center justify-between px-6 py-5">
        <Link
          href="/"
          className={`flex items-center gap-2.5 whitespace-nowrap rounded-md font-semibold text-white ${focus}`}
        >
          <Image src="/logo.png" alt="" width={32} height={32} className="size-8 rounded-full" />
          Orb Builds
        </Link>
        <a
          href={LINKS.youtube}
          target="_blank"
          rel="noopener noreferrer"
          className={`inline-flex items-center gap-2 rounded-full bg-white/10 px-4 py-2 text-sm text-white ring-1 ring-white/15 transition hover:bg-white/15 ${focus}`}
        >
          <YouTubeIcon className="size-4" />
          Channel
        </a>
      </header>

      <main id="main" className="mx-auto w-full max-w-5xl px-6 pb-20 pt-8">
        <p className="mb-2 font-mono text-xs uppercase tracking-[0.2em] text-sky-300/80">
          Episodes
        </p>
        <h1 className="text-3xl font-semibold tracking-tight text-white sm:text-4xl">
          Every video, newest first.
        </h1>
        <p className="mt-4 max-w-xl leading-relaxed text-slate-300">
          Lumin reviews new AI releases, then builds with them.{" "}
          {EPISODES.length} {EPISODES.length === 1 ? "episode" : "episodes"} so
          far. Only videos that are actually live show up here.
        </p>

        {EPISODES.length > 0 ? (
          <ol className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {EPISODES.map((ep) => (
              <li key={ep.url}>
                <Link
                  href={`/episodes/${episodeSlug(ep)}`}
                  className={`landing-card group flex h-full flex-col overflow-hidden rounded-2xl ring-1 ring-white/10 transition hover:-translate-y-0.5 hover:ring-sky-300/50 ${focus}`}
                >
                  <Image
                    src={ep.thumbnail}
                    alt={`Thumbnail for ${ep.title}`}
                    width={1280}
                    height={720}
                    sizes="(min-width: 1024px) 320px, (min-width: 640px) 50vw, 100vw"
                    className="aspect-video w-full object-cover"
                  />
                  <span className="flex flex-1 flex-col p-5">
                    <span className="font-mono text-xs uppercase tracking-wider text-sky-300/80">
                      {ep.code} · <time dateTime={ep.publishedTime}>{ep.publishedAt}</time>
                    </span>
                    <span className="mt-2 font-semibold text-white">{ep.title}</span>
                    <span className="mt-2 flex-1 text-sm leading-relaxed text-slate-300">
                      {ep.summary}
                    </span>
                    <span className="mt-4 inline-flex items-center gap-2 text-sm font-semibold text-sky-200">
                      <YouTubeIcon className="size-4" />
                      Watch the episode
                    </span>
                  </span>
                </Link>
              </li>
            ))}
          </ol>
        ) : (
          <p className="mt-12 text-slate-400">First episode coming soon.</p>
        )}

        <p className="mt-12 flex flex-wrap gap-x-6 gap-y-2 text-sm">
          <Link
            href="/"
            className={`rounded-md text-sky-200 underline-offset-4 hover:underline ${focus}`}
          >
            Back to home
          </Link>
          <Link
            href="/log"
            className={`rounded-md text-sky-200 underline-offset-4 hover:underline ${focus}`}
          >
            Read the build log
          </Link>
        </p>
      </main>
    </div>
  );
}
