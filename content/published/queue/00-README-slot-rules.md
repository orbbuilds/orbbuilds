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
5. A file that has been carried **3 nights** becomes `STALE`: it uploads only on a night when nothing fresher is READY,
   so a daily slot is never spent on an old review while a same-day one waits. Its ready Short may still go as upload #2.

## Call order inside the post-reset window (tick 32, #13)
(1) main upload, `privacyStatus` public (no `publishAt` in Composio; never private-then-flip) → (2) thumbnail →
(3) one `YOUTUBE_GET_VIDEO_DETAILS_BATCH` statistics read for every live videoId, logged in GROWTH_LOG →
(4) approved channel/playlist writes, add the new videoId to the reviews playlist → (5) second upload or Short.
Git-only work (site listing in `src/lib/episodes.ts`, logs, status lines) can happen anytime after the video is public.

## Measurement
Every PUBLISHED file keeps its `title_pattern` (experiment #2). Log the actual upload order and GA-to-publish hours
(experiment #3) in GROWTH_LOG. Never invent a videoId or a stat.
