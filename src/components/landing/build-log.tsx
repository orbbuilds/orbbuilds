import Link from "next/link";
import {
  tokenizeInline,
  type BuildLogBlock,
  type BuildLogEntry,
} from "@/lib/build-log";

export const focus =
  "focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-sky-300";

function Inline({ text }: { text: string }) {
  return (
    <>
      {tokenizeInline(text).map((token, i) => {
        if (token.type === "code") {
          return (
            <code
              key={i}
              className="rounded bg-white/10 px-1.5 py-0.5 font-mono text-[0.85em] text-sky-100"
            >
              {token.text}
            </code>
          );
        }
        if (token.type === "link") {
          return (
            <a
              key={i}
              href={token.href}
              target="_blank"
              rel="noopener noreferrer"
              className={`rounded-sm text-sky-200 underline underline-offset-4 hover:text-white ${focus}`}
            >
              {token.text}
            </a>
          );
        }
        return <span key={i}>{token.text}</span>;
      })}
    </>
  );
}

function Blocks({ blocks }: { blocks: BuildLogBlock[] }) {
  return (
    <div className="space-y-3 text-[0.95rem] leading-relaxed text-slate-300">
      {blocks.map((block, i) =>
        block.type === "p" ? (
          <p key={i}>
            <Inline text={block.text} />
          </p>
        ) : (
          <ul key={i} className="space-y-2">
            {block.items.map((item, j) => (
              <li key={j} className="flex gap-3">
                <span
                  aria-hidden
                  className="mt-[0.65em] size-1.5 shrink-0 rounded-full bg-sky-300/80"
                />
                <span>
                  <Inline text={item} />
                </span>
              </li>
            ))}
          </ul>
        ),
      )}
    </div>
  );
}

/** Timeline of build log entries. Each title links to its permalink on /log. */
export function BuildLogList({ entries }: { entries: BuildLogEntry[] }) {
  return (
    <ol className="relative space-y-8 border-l border-white/15 pl-6 sm:pl-8">
      {entries.map((entry) => (
        <li
          key={entry.slug}
          id={entry.slug}
          className="relative scroll-mt-6"
        >
          <span
            aria-hidden
            className="absolute -left-[1.78rem] top-1.5 size-2.5 rounded-full bg-sky-300 shadow-[0_0_12px_2px_rgba(125,211,252,0.7)] sm:-left-[2.28rem]"
          />
          <time
            dateTime={entry.date}
            className="font-mono text-xs uppercase tracking-wider text-sky-300/80"
          >
            {entry.date}
          </time>
          <h3 className="mb-3 mt-1 text-lg font-semibold text-white">
            <Link
              href={`/log#${entry.slug}`}
              className={`rounded-sm underline-offset-4 hover:underline ${focus}`}
            >
              {entry.title}
            </Link>
          </h3>
          <Blocks blocks={entry.blocks} />
        </li>
      ))}
    </ol>
  );
}
