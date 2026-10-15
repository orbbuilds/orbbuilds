# User decision brief, Oct 15 2026 (for the first daytime ping, ~8 AM MT or later)

Built by the continuous audience strategy routine (tick 88, ~4:55 AM MT). One place for every
pending operator decision, ranked by how much it unblocks, each with a safe default so the
parent can send one short batched message. Sources are the strategy-doc sections named in brackets.
Nothing here has been sent, signed up for, or spent.

## Status line to lead with (facts, Oct 15 ~5:55 AM MT, refreshed tick 94)
- The 1:28 AM publish failed (~1:36 AM MT). The exact error was not logged; a 1-unit quota probe at ~2:22 AM worked and the run wrote nothing in-window, so it likely died before the upload call (staging), **not** proven to be quota. Ep2 (Gemini 4 Argon) and Ep3 (Ultramarine 1 Flash)
  are carried to the Oct 16 1:28 AM window. Public RSS and a Data API read at ~6:00 AM still show only Ep0 (6 views) and Ep1 (9 views); shared quota was alive at ~6:00 AM (see item 0).
- Ultramarine 1 Flash still has **no** AI-review video on YouTube (tick 89: web=blogs only; X→YT=0; CEO ~1.23M impressions), so Ep3 can still be the first YouTube review if Oct 16 lands. Recovery: `content/drafts/2026-10-16-publish-recovery.md`. Ep4 Hermes queue is now PENDING_RENDER for a three-way rank if it renders tonight.

## Do now, no user decision needed (tick 95, ~6:00 AM MT)
0. **Retry the Ep3 Ultramarine publish this morning instead of waiting for 1:28 AM Oct 16.** [tick 95, #13/#3]
   A 1-unit Data API read (video stats) AND two Analytics reads all succeeded at ~6:00 AM MT, about 4.5 h
   after the reset. Earlier daytime reads failed at ~12:45 PM, ~1:28 PM and ~7:14 PM, so the shared pool
   is known alive until at least ~6 AM and dead by early afternoon. A morning Ep3 upload (follow
   `content/drafts/2026-10-16-publish-recovery.md`, Ep3 only, log the exact error on any failure) gains
   ~19 h on the still-open first-YouTube-review window and frees tonight's 1:28 AM slot for Ep4/Ep2, which
   puts the daily cadence back on track. A passing read doesn't prove ~1,600 upload units remain; the
   worst case is one more logged failure and Ep3 stays carried. Do it before ~10 AM MT.

0b. **If item 0 works, keep a daily ~6:28 AM catch-up upload window.** [tick 97, #3/#13]
   One render a night and at most one upload a night (2 uploads in 6 days so far) keeps two finished
   episodes waiting forever, and Ep2 never ships before it goes stale. A morning slot that runs only when a
   CARRIED main exists (main upload only, exact error logged) doubles capacity on the free shared quota.
   If item 0 fails on quota, skip this and lean on decision 1 instead.

## Decisions, ranked
1. **Own Google OAuth app for YouTube (dedicated quota).** [tick 4, #3/#13]
   Why now: shared Composio quota blocked uploads on Oct 11, 12 and 14 (Oct 15's cause is unknown, see
   status line); two finished episodes are waiting and the shared window is one try per night. Own project = 100 uploads/day in its own bucket, daytime publishing and stats.
   Needs the operator: a Google Cloud project under the Orb Builds Google account (Google blocks the
   box browser sign-in), YouTube Data API on, OAuth client with Composio's redirect URI, then a fresh
   Composio connection. Watch-out: an OAuth app left in "Testing" has ~7-day refresh tokens.
   Default if no answer: keep using the 1:28 AM shared window.
2. **Build episodes: small API budget, or free paths only?** [ticks 85-87, #20]
   Why: every script promises a "Lumin builds with it" episode; 0 of 3 exist, and Ep2/Ep3 builds need
   paid API access. YouTube's spam policy example is same music + AI imagery + an AI script read out;
   real hands-on footage is what makes each episode ours. The renderer can now show build screenshots.
   Default if no answer: free paths only (Hermes no-key desktop trial for Ep4, open-source paper-xlsx
   for Ultramarine), and stop promising paid builds in `build_teaser`.
3. **Turn on free Vercel Web Analytics for orbbuilds.vercel.app.** [tick 81, #18]
   Why: no site analytics, so footer/bio/site experiments can't be measured. Hobby tier is free
   (50K events/month, referrer-only, no UTMs). Needs a dashboard toggle on the Orb Builds Vercel
   project (the box's Vercel CLI is on a different team), then a two-line code add we can push.
   Default if no answer: leave off; site experiments stay unmeasured.
4. **X liveness check.** [tick 23, #10]
   Why: @OrbBuilds is in graduated access (replies got 0 impressions). Passing X's check (phone
   biometrics or selfie video, private to X) restores full access. Only the operator can do it.
   Skip the public "Automated by @..." label unless a pseudonymous managing account exists.
   Default if no answer: X stays a slow side channel, 1-2 spaced replies per session.
5. **Ben's Bites News account.** [tick 9, #9] Low priority. Only free submit-and-maybe-digest
   newsletter path found; draft in `content/drafts/bens-bites-submit-draft.md`.
   Default if no answer: skip.

## FYI only (no decision needed)
- Shipped overnight (#20): per-episode **music** + **background** variation (spam-policy hygiene), a
  `screen` field so reviews can show real build captures, and `tools/video/capture.sh` so the 3:23 PM
  Hermes session can record stills. Ordered checklist: `content/drafts/ep4-hermes-build-capture-checklist.md`.
- Oct 16 publish now has an owned staging fallback (a temporary GitHub prerelease on our own repo,
  deleted after upload) behind litterbox, and the run must log the exact error this time (tick 93).
- Cross-promo outreach (Nim review-partner email first) stays gated until 3 reviews are live.
- Mastodon signup was researched and dropped for now; Bluesky goes first.
- X profile/GitHub refresh drafted (`content/drafts/profile-surfaces-refresh.md`) for the growth routine.

## Suggested message for the parent (plain, short; edit freely)
(If the item-0 morning retry already worked, swap the first sentence for "The Ultramarine review is live: <link>.")
"Last night's upload failed. The error wasn't logged, but quota was still working an hour later, so it
likely broke before the upload itself; I've added a backup file host and error logging, so the Gemini and Ultramarine reviews go out tonight at 1:28 AM instead. The fix that matters most is still a Google Cloud project of our own for
YouTube (daytime uploads, more than one try a night), which needs you to sign in once; want the steps? Two quicker calls: should build episodes stay
on free tools only (my default), and can you flip on free Vercel analytics for the site? The X human
check on your phone would also lift the reach cap whenever you're up for it."
