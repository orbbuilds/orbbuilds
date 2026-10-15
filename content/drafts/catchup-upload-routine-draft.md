# Draft: morning catch-up upload routine (brief item 0b, tick 98)

Status: DRAFT, not created. Create only if the operator approves item 0b (ideally after item 0's
morning Ep3 retry has succeeded once). Paste-ready for UpdateRoutine `create`.

- Name: `Orb Builds: morning catch-up upload`
- Schedule: `28 6 * * *` (every day, matches the daily publish cadence incl. weekends), timing flexible,
  earlyMinutes 0, lateMinutes 30 (the shared pool was alive at ~6:00 AM on Oct 15 and dead by ~12:45 PM
  on Oct 14, so later is riskier, earlier overlaps the 1:28 AM run's tail).

## Saved prompt (intent, not a tool recipe)

Catch-up upload for Orb Builds (YouTube @orbbuilds). Only act when a finished main episode is waiting.

1. Read `content/published/queue/00-README-slot-rules.md` and every queue file. If no file has Status
   `CARRIED` or `READY` with existing upload paths, stop quietly (no YouTube calls).
2. Dedupe first, without quota: read the public channel RSS
   (`https://www.youtube.com/feeds/videos.xml?channel_id=UCGDWizzAvdre6ohhFG--CdA`). If the top-ranked
   episode's title is already there, mark its queue file PUBLISHED with that videoId and stop.
   If any upload landed in the last ~4 hours (1:28 AM run), still allowed, but upload only one file now.
3. Rank by the slot rules (open first-mover tier first, then freshest GA in MT; skip STALE). Upload the
   top one as the main video only, public, with the queue file's title/description/tags/category.
   Then the thumbnail if the call succeeds. No Short, no SEO/playlist writes, no vote comment, no stats
   batch (those stay with the 1:28 AM run).
4. Staging: follow the slot rules' host order (owned GitHub prerelease `staging-YYYY-MM-DD` is fine;
   delete it after the upload succeeds).
5. On failure, write the exact error string and the step it failed at into the queue file's Status
   line and the growth log. Never guess a cause. Do not retry more than once in the run.
6. On success: Status `PUBLISHED <videoId> (catch-up HH:MM MT)`, add the site listing
   (`src/lib/episodes.ts` + `public/episodes/`) and push, log GA-to-publish hours in GROWTH_LOG, and
   tell the user the video link in chat (they get every new video link).
7. Never post on X/Bluesky, reply, comment, or spend money from this routine. Never include the
   operator's name or employer anywhere.

## What it would change (from our own ledger, tick 97)
- Today: 1 render/night vs at most 1 upload/night keeps 2 episodes waiting; Ep2 Argon hits STALE after
  the Oct 17 window without ever shipping.
- With this: up to 2 uploads/day on the same free shared pool, so the pile can drain in ~2 good days.
- Measure: uploads per day (target = renders per day), GA-to-publish hours per episode, and failures by
  window (1:28 AM vs 6:28 AM) with exact error strings. If the 6:28 AM window fails on quota twice,
  pause it and lean on own-OAuth (decision 1).
