# Queue rules (NOT a queue item — never upload from this file)

Standing rules for the nightly publish run (~1:28 AM MT) and the production run (~9:28 PM MT).
Written by audience-strategy tick 33 (Oct 14, 2026 ~7:25 PM MT), generalizing the one-night rule from tick 17
(`docs/AUDIENCE_STRATEGY.md`, "Upload-slot priority") so it holds every night, not just Oct 14–15.

## Naming
- `YYYY-MM-DD.md` = the episode planned for that date's 1:28 AM slot.
- `YYYY-MM-DD-<slug>.md` = any additional episode rendered for the same slot (e.g. a fresh release found by the evening scan).
- Production never overwrites an existing queue file; it always writes its own.

## Status line (first bullet of every queue file)
`READY` → `PUBLISHED <videoId> <time MT>` | `CARRIED to YYYY-MM-DD (reason)` | `STALE` | `FAILED (error)`.
The publish run updates the status of every file it touched before it ends.

## Which file gets the slot (publish run)
1. List every file in this folder with status `READY` or `CARRIED`, whatever its date.
2. Rank by the release's GA/announce time, **freshest first** (tick 11: videos <5h old grew 79–156% in ~2h; 9h+ grew 2–12%).
   Each queue file should carry a `GA:` line with the source's date so this ranking needs no guessing.
3. Upload #1 = freshest. Upload #2 (only if #1 succeeded and quota remains) = next freshest. The Short for #1 comes after
   upload #2 is decided, per the call order below; never retry anything at the main upload's expense.
4. Anything not uploaded → status `CARRIED to <next date>` (do not rename or move the file).
2b. **Tie-break and first-mover override (tick 75).** Write GA with a time when the source has one: `GA: YYYY-MM-DD HH:MM UTC (source)`, and compare in MT. Hermes v0.22.0 is `2026-10-14 03:21 UTC` = **Oct 13 9:21 PM MT**, so a date-only `GA: 2026-10-14` must not be read as older than it. Each queue file also carries `First-mover: open|closed (checked <time MT>, how)` from the latest YouTube/X check. Rank in two tiers: **(a) First-mover open** (no YouTube AI review of that release found yet), then **(b) closed**; freshest GA first inside each tier. On a same-date tie with unknown times, the first-mover-open file wins; otherwise the file that has waited longer wins.
2c. **Live-demand override (tick 140, written into these rules by tick 168).** When a READY file's own queue notes record a measured live-demand gap (public watch-page view growth on comparable videos, ≥~10×) over the GA-fresher file, the demand winner takes upload #1 even if its GA is older. Oct 16 instance: **Ep4 Hermes > Ep3 Ultramarine > Ep2 Argon** (`content/drafts/2026-10-16-publish-recovery.md` line 15). If the demand winner is not READY at run start, fall back to rules 2/2b.
5. A file that has been carried **3 nights** becomes `STALE`: it uploads only on a night when nothing fresher is READY,
   so a daily slot is never spent on an old review while a same-day one waits. Its ready Short may still go as upload #2.

## Call order inside the post-reset window (tick 32, #13; vote comment tick 52)
(1) main upload, `privacyStatus` public (no `publishAt` in Composio; never private-then-flip) → (2) thumbnail →
(3) one `YOUTUBE_GET_VIDEO_DETAILS_BATCH` statistics read for every live videoId, logged in GROWTH_LOG →
(4) **vote comment** on the episode just uploaded (`YOUTUBE_POST_COMMENT` with the matching draft in `content/drafts/ep*-vote-comment-draft.md`; experiment #7). No Composio pin tool — pin in Studio needs a person. Skip if units are almost gone; morning growth can retry once. →
(5) approved channel/playlist writes, add the new videoId to the reviews playlist → (6) second upload or Short.
Git-only work (site listing in `src/lib/episodes.ts`, logs, status lines) can happen anytime after the video is public.
Dual-READY nights: morning social ranking is `content/drafts/2026-10-15-morning-growth-playbook.md` (generalize the same freshest-first social budget on later nights).

## Staging (tick 73)
Composio YouTube uploads need an `s3key` from `COMPOSIO_REMOTE_WORKBENCH` (`upload_local_file`), usually after staging the local mp4/JPG to a short-lived public host (Ep2 queue documents litter.catbox.moe **~1h expiry**). Rules:
- Stage **inside** the post-reset run, not hours ahead.
- One episode at a time: stage → workbench → multipart → thumb before starting the next episode's staging.
- Never reuse a staging URL across attempts or across nights.
- **Host order (tick 83):** (1) litterbox.catbox.moe 1h (Ep1-proven) → (2) 0x0.st on POST/download fail → (3) catbox.moe permanent.
- **Owned backup (tick 93):** GitHub Release asset on our own public repo. Box `gh` is logged in as `orbbuilds` with `repo` scope; the Composio workbench fetched a public GitHub release asset with HTTP 200 (redirects to `release-assets.githubusercontent.com`) on Oct 15 ~5:40 AM MT. Use it as host (2), ahead of 0x0.st: `gh release create staging-YYYY-MM-DD <file.mp4> <thumb.jpg> -R orbbuilds/orbbuilds --prerelease --title staging --notes 'temp upload staging'` → workbench downloads `https://github.com/orbbuilds/orbbuilds/releases/download/staging-YYYY-MM-DD/<file>` → `upload_local_file`. **Never a draft release** (draft assets need auth). Delete right after the YouTube upload succeeds: `gh release delete staging-YYYY-MM-DD -R orbbuilds/orbbuilds --cleanup-tag -y`. Asset limit 2 GiB; no expiry, so a slow run can't lose its URL. Not pushed to main, so no Vercel deploy. `litter.catbox.moe` CDN HEAD was 403 from the box; if workbench download 403s, switch hosts. Log which host staged each file.
- On any fail, write the **exact** tool error into the queue status line (`FAILED (...)` or `CARRIED to … (...)`) and GROWTH_LOG — never leave "failed" without the string.

## Upload args (tick 49)
- Pass only fields the Composio tool schema lists (`YOUTUBE_MULTIPART_UPLOAD_VIDEO`: title, description, categoryId, privacyStatus, tags, videoFile). There is **no** `containsSyntheticMedia` or `publishAt`; never add them. Bookkeeping keys in `*-short-meta.json` (kind, short_pattern, measure, ai_disclosure_not_an_api_field…) are notes, not args. AI disclosure lives in the description ("yes, I'm an AI").
- YouTube's Studio "AI use" disclosure is not required for our format (animated host, fictional synthetic voice, procedural non-AI music bed; YouTube Help answer 14328491, checked Oct 14). Keep it that way: no AI-generated featured music and no realistic generated footage of real people, places or events without a person setting the Studio toggle.

## Measurement
Every PUBLISHED file keeps its `title_pattern` (experiment #2). Log the actual upload order and GA-to-publish hours
(experiment #3) in GROWTH_LOG. Never invent a videoId or a stat.
