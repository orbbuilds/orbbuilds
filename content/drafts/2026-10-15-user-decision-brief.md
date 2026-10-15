# User decision brief, Oct 15 2026 (for the first daytime ping, ~8 AM MT or later)

Built by the continuous audience strategy routine (tick 88, ~4:55 AM MT). One place for every
pending operator decision, ranked by how much it unblocks, each with a safe default so the
parent can send one short batched message. Sources are the strategy-doc sections named in brackets.
Nothing here has been sent, signed up for, or spent.

## Status line to lead with (facts, Oct 15 ~4:55 AM MT)
- The 1:28 AM publish failed (~1:36 AM MT), so Ep2 (Gemini 4 Argon) and Ep3 (Ultramarine 1 Flash)
  are carried to the Oct 16 1:28 AM window. Public RSS still shows only Ep0 (6 views) and Ep1 (9 views).
- Ultramarine 1 Flash still had no AI-review video on YouTube at the last check (tick 83), so Ep3
  can still be the first YouTube review if Oct 16 lands. Recovery plan: `content/drafts/2026-10-16-publish-recovery.md`.

## Decisions, ranked
1. **Own Google OAuth app for YouTube (dedicated quota).** [tick 4, #3/#13]
   Why now: shared Composio quota has failed uploads on Oct 11, 12, 14 and 15; two finished episodes
   are waiting. Own project = 100 uploads/day in its own bucket, daytime publishing and stats.
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
- Shipped overnight: per-episode music variation (spam-policy risk) and a `screen` field so reviews
  can show real build captures.
- Cross-promo outreach (Nim review-partner email first) stays gated until 3 reviews are live.
- Mastodon signup was researched and dropped for now; Bluesky goes first.
- X profile/GitHub refresh drafted (`content/drafts/profile-surfaces-refresh.md`) for the growth routine.

## Suggested message for the parent (plain, short; edit freely)
"Last night's upload failed again on the shared YouTube quota, so the Gemini and Ultramarine reviews go
out tonight at 1:28 AM instead. The fix that matters most is a Google Cloud project of our own for
YouTube, which needs you to sign in once; want the steps? Two quicker calls: should build episodes stay
on free tools only (my default), and can you flip on free Vercel analytics for the site? The X human
check on your phone would also lift the reach cap whenever you're up for it."
