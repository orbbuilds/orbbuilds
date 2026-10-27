// Fails if src/lib/episodes.ts has a mistake the site would ship quietly:
// a missing thumbnail, a bad YouTube link, a duplicate or out-of-order episode, or a bad date.
import { readFileSync, existsSync } from "node:fs";
import ts from "typescript";

const root = new URL("../../", import.meta.url);
const src = readFileSync(new URL("src/lib/episodes.ts", root), "utf8");
const js = ts.transpileModule(src, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText;
const { EPISODES } = await import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);

const errors = [];
const seenCodes = new Set();
const seenIds = new Set();
let prevNum = Infinity;
let prevDate = "9999-99-99";

for (const [i, ep] of EPISODES.entries()) {
  const at = `${ep.code || `entry ${i}`}`;
  for (const key of ["code", "title", "summary", "publishedAt", "publishedTime", "url", "thumbnail"]) {
    if (typeof ep[key] !== "string" || !ep[key].trim()) errors.push(`${at}: missing ${key}`);
  }
  const m = /^Episode (\d+)$/.exec(ep.code ?? "");
  if (!m) errors.push(`${at}: code should look like "Episode 10"`);
  else {
    const n = Number(m[1]);
    if (n >= prevNum) errors.push(`${at}: list must be newest first (came after Episode ${prevNum})`);
    prevNum = n;
  }
  if (seenCodes.has(ep.code)) errors.push(`${at}: duplicate code`);
  seenCodes.add(ep.code);

  if (!/^\d{4}-\d{2}-\d{2}$/.test(ep.publishedAt ?? "")) errors.push(`${at}: publishedAt should be YYYY-MM-DD`);
  else {
    // Order is by episode number. Upload times can interleave (Episodes 2-4 went up the same morning), dates can't go backwards.
    if (ep.publishedAt > prevDate) errors.push(`${at}: publishedAt is newer than the episode above it`);
    prevDate = ep.publishedAt;
  }
  const t = Date.parse(ep.publishedTime ?? "");
  if (!/(Z|[+-]\d{2}:\d{2})$/.test(ep.publishedTime ?? "") || Number.isNaN(t)) {
    errors.push(`${at}: publishedTime should be ISO 8601 with a timezone`);
  } else {
    if (t > Date.now() + 60 * 60 * 1000) errors.push(`${at}: publishedTime is in the future (only list live episodes)`);
  }

  try {
    const u = new URL(ep.url);
    const id = u.searchParams.get("v");
    if (u.hostname !== "www.youtube.com" || u.pathname !== "/watch" || !/^[\w-]{11}$/.test(id ?? "")) {
      errors.push(`${at}: url should be https://www.youtube.com/watch?v=<11-char id>`);
    } else if (seenIds.has(id)) errors.push(`${at}: YouTube id ${id} used twice`);
    else seenIds.add(id);
  } catch {
    errors.push(`${at}: url is not a valid URL`);
  }
  if (ep.shortUrl !== undefined && !/^https:\/\/www\.youtube\.com\/shorts\/[\w-]{11}$/.test(ep.shortUrl)) {
    errors.push(`${at}: shortUrl should be https://www.youtube.com/shorts/<11-char id>`);
  }

  if (!/^\/episodes\/[\w.-]+\.(jpg|jpeg|png|webp)$/.test(ep.thumbnail ?? "")) {
    errors.push(`${at}: thumbnail should be /episodes/<file>.jpg`);
  } else if (!existsSync(new URL(`public${ep.thumbnail}`, root))) {
    errors.push(`${at}: thumbnail file public${ep.thumbnail} does not exist`);
  }
}

if (!EPISODES.length) errors.push("no episodes listed");
if (errors.length) {
  console.error(`episodes.ts check failed:\n- ${errors.join("\n- ")}`);
  process.exit(1);
}
console.log(`episodes.ts ok (${EPISODES.length} episodes)`);
