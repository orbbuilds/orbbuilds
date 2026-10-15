# Draft: Oct 16 ~1:28 AM MT publish recovery (CARRIED Ep3 + Ep2) — NOT AN UPLOAD

Status: draft only (audience-strategy tick 73, Oct 15 ~2:10 AM MT). Nothing uploaded, posted, or spent from this file.
Use: the daily video publish routine on the next post-reset window (~1:28 AM MT Oct 16). Paste real videoIds only after a successful upload.

## Why this exists
Oct 15 ~1:28 AM publish **failed** (~1:36 AM MT). Public RSS at ~2:02 AM and again ~2:07 AM MT still only Ep0 `aCvkp11w9_8` (6 views) + Ep1 `L7fdRoNWEPE` (9 views). Both queues are **CARRIED to 2026-10-16**. Exact tool error string was never written into the queue status lines — do not invent one; this run must log the real string on any fail.

## Rank (freshest GA first)
| Rank | File | Episode | GA | Upload file (verified tick 73) |
|------|------|---------|----|--------------------------------|
| #1 | `content/published/queue/2026-10-15-ultramarine-1-flash.md` | Ep3 Ultramarine 1 Flash (P1) | 2026-10-14 | `content/drafts/2026-10-14-ultramarine-1-flash-upload.mp4` (18,191,891 B) |
| #2 | `content/published/queue/2026-10-15.md` | Ep2 Gemini 4 Argon (P2) | 2026-10-13 | `/workspace/argon-share.mp4` (9,087,465 B) |

**If tonight's 9:28 PM run renders Ep4 (Hermes) and its queue file is READY, the Oct 16 rank is (tick 140, demand-first; supersedes tick 75/108):** #1 **Ep4 Hermes** → #2 Ep3 Ultramarine → #3 Ep2 Argon. Ep4 queue file: `content/published/queue/2026-10-16-hermes-agent-v0-22.md` — flip READY only after paths exist. If Ep4 is not READY at run start, fall back to the Ep3 → Ep2 table above.
- Why (public watch-page view counts, no quota, ~1:36 PM MT Oct 15): Hermes v0.22 recaps are still gaining **~150–250 views/h** (Julian Goldie `NZcdLDuhryI` 6,157 → 6,341 in ~44 min at ~15 h old; BoxminingAI `pAaAgcjNgEs` 16,644 → 16,752 in ~44 min at ~1.5 d). Ultramarine reviews gain **~5–11 views/h** (AI WITH Rithesh `CcRr7dJy4gI` 239 → 282 in ~4 h at ~17 h old on a 51K channel; Julian `k85bmBNAgN0` 27 → 47 in ~4 h). That is a ~20–50× gap in live demand, and only one upload per night has been reliable.
- Still consistent with slot rule "fresh release first": Hermes **v0.22.2** shipped Oct 15 2:21 AM MT (newer than Ultramarine's Oct 14 GA), and Ep4 is pinned to it.
- Consequence: Ep3 most likely carries to Oct 17; Ep2 is past its useful window (goes STALE after Oct 17) — let its finished Short live on the native-video lane (#22) instead of spending a main slot. Never claim "first" anywhere.

(Pre-tick-140 note, applies only when Ep4 is not READY:) Ep3 wins upload #1 over Ep2 on **freshest GA** (Oct 14), not first-mover (closed tick 108: YouTube SERP has AI WITH Rithesh / Julian Goldie / White Rabbit AI reviews; X→YT still 0). Prefer Ep3 as upload #1; never claim "first" in social/meta.

## Hard rule: stage fresh inside the window (backup order, tick 83)
Do **not** pre-stage hours before 1:28 AM. Litterbox links expire ~1h; MCP still needs a public URL → workbench → `s3key` (local paths are not valid `s3key`s).

**Host order (try next on POST or workbench-download failure):**
1. **litterbox.catbox.moe** (1h) — Ep1-proven; API host reachable from box (tick 83).
2. **GitHub Release on `orbbuilds/orbbuilds` (tick 93, owned, no expiry)** — `gh release create staging-2026-10-16 <files> -R orbbuilds/orbbuilds --prerelease --title staging --notes 'temp upload staging'`; workbench GET of a public GitHub release asset returned 200 (~5:40 AM MT Oct 15). Not a draft release. Delete with `gh release delete staging-2026-10-16 -R orbbuilds/orbbuilds --cleanup-tag -y` after the YouTube upload succeeds.
3. **0x0.st** — box allowlist; HEAD 200 from box (tick 83).
4. **catbox.moe** (permanent) — HEAD 200; use when 1h expiry is the problem or litterbox fails. Note: `litter.catbox.moe` CDN returned **403** on HEAD from this box — if a litterbox download URL 403s in workbench, skip straight to the GitHub Release (then 0x0/catbox).

For each upload:
1. Stage the local mp4 (and thumb JPG if needed) to a fresh public URL **after** the run starts, using the host order above. Log which host returned the URL.
2. In `COMPOSIO_REMOTE_WORKBENCH`: download that URL → `upload_local_file` → keep the returned `s3key`.
3. Call `YOUTUBE_MULTIPART_UPLOAD_VIDEO` with **only** schema fields: `title`, `description`, `categoryId` (`28`), `privacyStatus` (`public`), `tags`, `videoFile` `{name, mimetype: video/mp4, s3key}`. Never pass `containsSyntheticMedia` or `publishAt`.
4. Thumbnail: stage a fresh public JPG URL (same host order), then `YOUTUBE_UPDATE_THUMBNAIL` with that URL (channel is phone-verified; Ep1 custom thumbs work).
5. If staging or download takes long on a 1h host, re-stage or fall through to catbox — never reuse a URL from an earlier attempt or from daytime prep.

Proven path (Ep1, `EP1_RETRY_NOTE.txt`): litterbox → workbench download + `upload_local_file` → multipart → thumbnail.

**Pre-flight (tick 83, ~3:53 AM MT):** Ep3 upload `content/drafts/2026-10-14-ultramarine-1-flash-upload.mp4` 18,191,891 B; thumb 211,917 B; Ep2 `/workspace/argon-share.mp4` 9,087,465 B; both script `publish_*` fields present with footers; no forbidden upload args.

## Call order (experiment #13 / #7)
Same as `00-README-slot-rules.md`, one episode at a time:

1. Main upload (public) for the **#1-ranked episode** (Ep4 Hermes if its queue is READY, else Ep3) — then steps 2–4 apply to that episode
2. That episode's thumbnail (Ep4 thumb path from its queue file once READY; Ep3 `…-ultramarine-1-flash-thumb.jpg`)
3. One `YOUTUBE_GET_VIDEO_DETAILS_BATCH` for all live IDs (old + new) → GROWTH_LOG
4. That episode's vote comment if units remain (Ep4: `ep4-post-publish-growth-pack.md`; Ep3: Candidate C in `ep3-vote-comment-draft.md`)
5. Channel SEO + playlist (`channel-seo-setup.md`) only after at least one new main succeeds (~50 units)
6. **#2-ranked main** (Ep3 when Ep4 went first, else Ep2) only if quota remains; then its thumb; vote if units remain. Ep2 main only as #3 (tick 140: Ep2 prefers the native-video lane)
7. Shorts last, in main-upload order; never upload a Short before its own main is live
8. Git-only site listings anytime after each videoId is public (`ep3-site-listing.md`, `ep2-site-listing.md`)

## Meta paste (no guessing)
- Ep3 title/desc/tags: `content/scripts/2026-10-14-ultramarine-1-flash.json` → `meta.publish_title` / `publish_description` / `tags` (title 60 chars; collision-safe tags; chapters already merged tick 47).
- Ep2: `content/scripts/2026-10-14-gemini-4-argon.json` → same keys (footer already includes Previous Ep1).
- Thumbs: Ep3 `content/drafts/2026-10-14-ultramarine-1-flash-thumb.jpg` (211,917 B); Ep2 `content/drafts/2026-10-14-gemini-4-argon-thumb-v2.jpg` (202,117 B).
- Shorts (after mains): Ep3 `…-ultramarine-1-flash-short.mp4` + `…-short-meta.json`; Ep2 `…-gemini-4-argon-short-cta.mp4` + `…-short-meta.json` (paste full-episode URL into description; bookkeeping keys are notes, not upload args).

## On failure (mandatory)
Update the touched queue file status to `FAILED (<exact error string truncated to ~200 chars>)` or `CARRIED to YYYY-MM-DD (<exact error>)` before the routine ends. Also append one GROWTH_LOG line with the tool slug and error. Public RSS re-check (no Composio quota) if unsure whether a videoId landed.

## Do not
- Mid-day YouTube API retries (shared quota).
- Invent videoIds or claim first coverage beyond **YouTube AI review** (written blogs already exist).
- Post / reply / DM / spend from this file (growth routines own social; morning playbook stays Neither until a videoId exists).

## Measure after success
- Experiment #3: GA→publish hours for Ep3 and Ep2 (use actual upload time).
- Experiment #2: start the 24h clock; same-night pair still confound if both go up.
- Experiment #2/#16 (tick 78; **moved out of this window by tick 125**): do **not** run the Ep1/Ep0 `YOUTUBE_QUERY_ANALYTICS` read here. Analytics is a separate API, it answered at ~11:10 AM MT Oct 15, and its day rows still stopped at Oct 12 then (no new day in 8+ h), so a 1:30 AM read would most likely log "Ep1 not in yet" and spend window time. The audience-strategy routine does it in daytime Oct 16 (~10 AM–noon MT) instead. Keep this window for uploads, stats, SEO and comments only.
- First-mover: already closed (tick 108). After Ep3 is public, say "review" not "first"; optional SERP recheck only to name competitors if useful.
