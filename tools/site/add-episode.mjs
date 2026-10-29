#!/usr/bin/env node
// Adds a newly published episode to the top of src/lib/episodes.ts and copies
// its thumbnail into public/episodes/, then runs the episode check.
//
// Usage:
//   node tools/site/add-episode.mjs --number 11 --video-id <id> \
//     --published-time 2026-10-30T07:31:00Z --thumb path/to/thumb.jpg \
//     --title "..." --summary "..." [--short-id <id>] [--dry-run]
//
// publishedAt (the calendar date shown on the site) is derived from
// --published-time in Mountain Time, so the two can't disagree.
import { copyFileSync, existsSync, readFileSync, writeFileSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { resolve } from "node:path";

const root = resolve(import.meta.dirname, "../..");
const file = resolve(root, "src/lib/episodes.ts");

function parseArgs(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (!a.startsWith("--")) fail(`unexpected argument: ${a}`);
    const key = a.slice(2);
    if (key === "dry-run") { out.dryRun = true; continue; }
    const val = argv[++i];
    if (val === undefined) fail(`missing value for --${key}`);
    out[key] = val;
  }
  return out;
}

function fail(msg) {
  console.error(`add-episode: ${msg}`);
  process.exit(1);
}

const args = parseArgs(process.argv.slice(2));
for (const k of ["number", "video-id", "published-time", "thumb", "title", "summary"]) {
  if (!args[k] || !String(args[k]).trim()) fail(`--${k} is required`);
}

const num = Number(args.number);
if (!Number.isInteger(num) || num < 1) fail("--number must be a positive integer");
const idRe = /^[A-Za-z0-9_-]{11}$/;
if (!idRe.test(args["video-id"])) fail("--video-id must be an 11-character YouTube id");
if (args["short-id"] && !idRe.test(args["short-id"])) fail("--short-id must be an 11-character YouTube id");

const when = new Date(args["published-time"]);
if (!/(Z|[+-]\d\d:\d\d)$/.test(args["published-time"]) || Number.isNaN(when.getTime())) {
  fail("--published-time must be ISO 8601 with a timezone, e.g. 2026-10-30T07:31:00Z");
}
const publishedAt = new Intl.DateTimeFormat("en-CA", {
  timeZone: "America/Denver", year: "numeric", month: "2-digit", day: "2-digit",
}).format(when);

const thumbSrc = resolve(process.cwd(), args.thumb);
if (!existsSync(thumbSrc)) fail(`thumbnail not found: ${args.thumb}`);
const thumbName = `rr-${String(num).padStart(3, "0")}.jpg`;
const thumbDest = resolve(root, "public/episodes", thumbName);

const src = readFileSync(file, "utf8");
const code = `Episode ${num}`;
if (src.includes(`code: ${JSON.stringify(code)}`)) fail(`${code} is already listed`);
if (src.includes(args["video-id"])) fail(`video id ${args["video-id"]} is already listed`);

const marker = "export const EPISODES: Episode[] = [\n";
const at = src.indexOf(marker);
if (at < 0) fail("could not find the EPISODES array in src/lib/episodes.ts");

const lines = [
  "  {",
  `    code: ${JSON.stringify(code)},`,
  `    title: ${JSON.stringify(args.title.trim())},`,
  "    summary:",
  `      ${JSON.stringify(args.summary.trim())},`,
  `    publishedAt: ${JSON.stringify(publishedAt)},`,
  `    publishedTime: ${JSON.stringify(args["published-time"])},`,
  `    url: ${JSON.stringify(`https://www.youtube.com/watch?v=${args["video-id"]}`)},`,
  ...(args["short-id"] ? [`    shortUrl: ${JSON.stringify(`https://www.youtube.com/shorts/${args["short-id"]}`)},`] : []),
  `    thumbnail: ${JSON.stringify(`/episodes/${thumbName}`)},`,
  "  },",
];
const entry = lines.join("\n") + "\n";
const next = src.slice(0, at + marker.length) + entry + src.slice(at + marker.length);

if (args.dryRun) {
  process.stdout.write(entry);
  console.log(`(dry run) would copy ${args.thumb} to public/episodes/${thumbName}`);
  process.exit(0);
}

const hadThumb = existsSync(thumbDest);
if (!hadThumb) copyFileSync(thumbSrc, thumbDest);
writeFileSync(file, next);
try {
  execFileSync(process.execPath, [resolve(root, "tools/site/check-episodes.mjs")], { stdio: "inherit" });
} catch {
  writeFileSync(file, src);
  if (!hadThumb) {
    try { (await import("node:fs")).unlinkSync(thumbDest); } catch {}
  }
  fail("episode check failed, so the change was rolled back");
}
console.log(`Added ${code} (${publishedAt}) with thumbnail public/episodes/${thumbName}.`);
