import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { notFound } from "next/navigation";
import { focus } from "@/components/landing/build-log";
import { ArrowUpRightIcon, YouTubeIcon } from "@/components/landing/icons";
import { EPISODES, episodeSlug, findEpisode, youTubeId } from "@/lib/episodes";
import { LINKS, SITE_NAME, getSiteUrl } from "@/lib/site";

type Params = { slug: string };

export function generateStaticParams(): Params[] {
  return EPISODES.map((ep) => ({ slug: episodeSlug(ep) }));
}

export async function generateMetadata({ params }: { params: Promise<Params> }): Promise<Metadata> {
  const { slug } = await params;
  const ep = findEpisode(slug);
  if (!ep) return {};
  const path = `/episodes/${slug}`;
  const title = `${ep.code}: ${ep.title}`;
  return {
    title,
    description: ep.summary,
    alternates: { canonical: path },
    openGraph: {
      type: "video.other",
      url: path,
      title: `${title} | ${SITE_NAME}`,
      description: ep.summary,
      images: [{ url: ep.thumbnail, width: 1280, height: 720, alt: `Thumbnail for ${ep.title}` }],
      videos: [{ url: ep.url }],
    },
    twitter: {
      card: "summary_large_image",
      title: `${title} | ${SITE_NAME}`,
      description: ep.summary,
      images: [ep.thumbnail],
    },
  };
}

export default async function EpisodePage({ params }: { params: Promise<Params> }) {
  const { slug } = await params;
  const ep = findEpisode(slug);
  if (!ep) notFound();

  const site = getSiteUrl();
  const id = youTubeId(ep.url);
  const index = EPISODES.indexOf(ep);
  const newer = index > 0 ? EPISODES[index - 1] : undefined;
  const older = index < EPISODES.length - 1 ? EPISODES[index + 1] : undefined;

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "VideoObject",
    name: ep.title,
    description: ep.summary,
    uploadDate: ep.publishedTime,
    thumbnailUrl: `${site}${ep.thumbnail}`,
    url: `${site}/episodes/${slug}`,
    ...(id ? { embedUrl: `https://www.youtube.com/embed/${id}` } : {}),
    publisher: { "@id": `${site}/#org` },
    sameAs: ep.url,
  };

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
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd).replace(/</g, "\\u003c") }}
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

      <main id="main" className="mx-auto w-full max-w-3xl px-6 pb-20 pt-8">
        <p className="mb-2 font-mono text-xs uppercase tracking-[0.2em] text-sky-300/80">
          {ep.code} · <time dateTime={ep.publishedTime}>{ep.publishedAt}</time>
        </p>
        <h1 className="text-2xl font-semibold tracking-tight text-white sm:text-3xl">{ep.title}</h1>

        <div className="mt-8 overflow-hidden rounded-2xl ring-1 ring-white/10">
          {id ? (
            <iframe
              src={`https://www.youtube-nocookie.com/embed/${id}`}
              title={ep.title}
              loading="lazy"
              allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
              referrerPolicy="strict-origin-when-cross-origin"
              allowFullScreen
              className="aspect-video w-full"
            />
          ) : (
            <Image
              src={ep.thumbnail}
              alt={`Thumbnail for ${ep.title}`}
              width={1280}
              height={720}
              className="aspect-video w-full object-cover"
            />
          )}
        </div>

        <p className="mt-6 leading-relaxed text-slate-300">{ep.summary}</p>
        <a
          href={ep.url}
          target="_blank"
          rel="noopener noreferrer"
          className={`mt-6 inline-flex items-center gap-2 rounded-md text-sm font-semibold text-sky-200 ${focus}`}
        >
          <YouTubeIcon className="size-4" />
          Watch on YouTube
          <ArrowUpRightIcon className="size-3.5" />
        </a>

        <nav aria-label="More episodes" className="mt-12 grid gap-4 sm:grid-cols-2">
          {older ? (
            <Link
              href={`/episodes/${episodeSlug(older)}`}
              className={`landing-card rounded-2xl p-5 ring-1 ring-white/10 transition hover:ring-sky-300/50 ${focus}`}
            >
              <span className="font-mono text-xs uppercase tracking-wider text-sky-300/80">
                Previous · {older.code}
              </span>
              <span className="mt-1 block font-semibold text-white">{older.title}</span>
            </Link>
          ) : (
            <span />
          )}
          {newer ? (
            <Link
              href={`/episodes/${episodeSlug(newer)}`}
              className={`landing-card rounded-2xl p-5 text-right ring-1 ring-white/10 transition hover:ring-sky-300/50 ${focus}`}
            >
              <span className="font-mono text-xs uppercase tracking-wider text-sky-300/80">
                Next · {newer.code}
              </span>
              <span className="mt-1 block font-semibold text-white">{newer.title}</span>
            </Link>
          ) : null}
        </nav>

        <p className="mt-12 flex flex-wrap gap-x-6 gap-y-2 text-sm">
          <Link href="/episodes" className={`rounded-md text-sky-200 underline-offset-4 hover:underline ${focus}`}>
            All episodes
          </Link>
          <Link href="/log" className={`rounded-md text-sky-200 underline-offset-4 hover:underline ${focus}`}>
            Read the build log
          </Link>
        </p>
      </main>
    </div>
  );
}
