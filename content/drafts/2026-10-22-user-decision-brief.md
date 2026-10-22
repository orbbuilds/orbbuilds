# User decision brief, Oct 22 2026 (skeleton, tick 248; fill stats in the daytime, batch into one late-morning ping)

Supersedes the Oct 16 brief (stale: Muse free window closed Oct 18; Ep5 shipped Oct 22, not Sat Oct 17).

## Step 0 (read-only, before sending)
1. Read view counts for Ep2 to Ep5 and Short 0WDtyym90Fs in the post-reset Data API window, or from `https://www.youtube.com/@orbbuilds/videos` (browser UA). Never quote a number you didn't just read.
2. Bluesky Ep5 post `3myh5fuszc326`: read likes/reposts/replies at ~4 to 6 h after 1:30 AM MT (so ~6 to 8 AM MT or later).
3. Confirm Ep5 is still public and on the site.

## Status line (ACTUAL from tick 247, re-verify before sending)
"Ep5 is up: Lumin reacts to [Claude Duet](https://www.youtube.com/watch?v=fEtI3D3oUYI), with a Short. We were about 12 hours behind the first hands-on review, so I leaned on the AI-reacts angle instead of speed. [FILL: Ep5 views at read time] so far; Ep4 [FILL], Ep3 [FILL]."

## Decisions, ranked (defaults unchanged unless noted)
1. **Own Google OAuth app for YouTube (dedicated quota).** Uploads have now succeeded on recent nights in the 1:28 AM window, so this is lower urgency than Oct 16. Default: keep the shared window. Raise only if a publish fails again.
2. **Turn on free Vercel Web Analytics for orbbuilds.vercel.app.** Default: off; site stays unmeasured.
3. **Build episodes: small API budget or free paths only?** Muse time-box expired (Oct 18). Default: free paths only.
4. **X liveness check** (phone, private to X). Default: X stays a slow side channel.
5. **Ben's Bites account.** Default: skip.

## Parent-only (not user questions)
- **Bluesky overnight drop still breaks POSTING_RULES (ticks 216, 247).** Ep5's 1:30 AM drop was a native video embed (better), but still used `#AI` (rule B4) and went out overnight on a weekday (rule B2). Suggested publish-routine prompt fix: follow `docs/POSTING_RULES.md` for any Bluesky post (topic tag + `#LLM`/`#AIagents`, never `#AI`); on weekdays skip the overnight drop and leave Bluesky to the 10 AM to 2 PM runs; keep it Sat/Sun only (compliant). Routine edit, parent's call.
- **Weekend social gap (tick 213):** posting runs are weekday-only while episodes publish daily. Suggested: audience growth routine daily (`23 11 * * *`) with the same caps.
- **Routine health:** the snapshot shows the daily build session, news scan, content drafts, weekly review and audience growth routines' last runs as `failed` (Oct 21). Worth checking why before the 8:23 AM scan.

## Suggested message (plain, short)
[Status line], then one sentence on decision 2 (analytics, easy yes/no), and one optional line on decision 1.
