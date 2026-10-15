# User decision brief, Oct 15 2026 (for the first daytime ping, ~8 AM MT or later)

Built by the continuous audience strategy routine (tick 88, ~4:55 AM MT). One place for every
pending operator decision, ranked by how much it unblocks, each with a safe default so the
parent can send one short batched message. Sources are the strategy-doc sections named in brackets.
Nothing here has been sent, signed up for, or spent.

## Status line to lead with (facts, Oct 15 ~11:01 AM MT, RSS recheck tick 124)
- The 1:28 AM publish failed (~1:36 AM MT). Exact error never logged; probes after the window worked, so it likely died before the upload call (staging), **not** proven to be quota. Ep2 + Ep3 stay **CARRIED to Oct 16**. Public RSS ~11:01 AM still only Ep0 (6 views) and Ep1 (9 views). **No morning Ep3 retry has run.** Shared quota was **alive at ~9:40 AM MT** (1-unit batch OK; also alive ~6:00 / ~7:22 / ~8:27 AM). Prefer Ep3 catch-up **now** while confirmed; historical death by ~12:45 PM Oct 14.
- Ultramarine YouTube first-mover **closed** (tick 108). Same-topic demand is cooling: Rithesh flat at 239 views from ~11.8 h→~13 h (tick 116). Ep3 still ranks #1 for Oct 16 on freshest GA only — never claim first. Recovery: `content/drafts/2026-10-16-publish-recovery.md`. Ep4 Hermes is PENDING_RENDER (script + tags ready; needs 3:23 PM capture → 9:28 PM finalize).

## Do now, no user decision needed (tick 95, ~6:00 AM MT)
0. **Retry the Ep3 Ultramarine publish this morning instead of waiting for 1:28 AM Oct 16.** [tick 95, #13/#3; urgency reframed tick 114]
   Shared quota was alive at ~6:00 AM and ~8:27 AM MT. **First-mover is gone** (tick 108), so this is no
   longer about being first — it clears the CARRIED pile and frees tonight's 1:28 AM slot for Ep4/Ep2.
   Follow `content/drafts/2026-10-16-publish-recovery.md` (Ep3 only; never claim first; log exact error).
   A passing read doesn't prove upload units remain; worst case is one more logged failure.    Tick 116 probe at ~9:40 AM confirmed the pool is still alive — **do the Ep3-only
   retry now** (do not wait for 1:28 AM Oct 16). If this probe had failed, wait for tonight.

0b. **If item 0 works, keep a daily ~6:28 AM catch-up upload window.** [tick 97, #3/#13]
   One render a night and at most one upload a night (2 uploads in 6 days so far) keeps two finished
   episodes waiting forever, and Ep2 never ships before it goes stale. A morning slot that runs only when a
   CARRIED main exists (main upload only, exact error logged) doubles capacity on the free shared quota.
   If item 0 fails on quota, skip this and lean on decision 1 instead.
   Paste-ready routine: `content/drafts/catchup-upload-routine-draft.md` (tick 98).

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
   Concrete example (tick 111): Grok Voice 3.0 has real search demand (`grok voice 3.0 demo`) and no
   hands-on demo on YouTube yet; a talking-orb live test would cost about $0.80 for 10 min at xAI's
   official $0.08/min. That's the strongest openly-AI episode we've found.
   Possible $0 path (tick 112/114): x.ai/api says every Console account gets a free Playground; official
   Voice docs do not confirm speech-to-speech is free there (secondary coverage claims a voice playground).
   Needs a Console account on the Orb Builds identity (your call). Paid API stays the sure path.
   Ready pack if you OK either path: `content/drafts/grok-voice-3-p5-demo-title-pack.md` (tick 114).
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
- **Tick 140 FYI:** tonight's 1:28 AM upload now leads with Ep4 Hermes (if it renders) instead of Ep3 Ultramarine: Hermes recaps are still gaining ~150–250 views/h vs ~5–11/h for Ultramarine reviews (public view counts, ~1:36 PM MT). Ep3 likely slides to Oct 17; Ep2 lives on as a native clip rather than a main upload.
- **Tick 124 FYI:** YouTube search demand exists for **Hermes Agent vs Grok Bot** (autocomplete + several Oct 2026 comparison pages). Ep4 stays the P5 "replacing me" review. A later versus episode would need your OK to name Grok Bot publicly (today Lumin only says "I'm an AI"). Note: `content/drafts/p4-hermes-vs-grok-bot-candidate.md`.
- X profile/GitHub refresh drafted (`content/drafts/profile-surfaces-refresh.md`) for the growth routine.

## Afternoon batch for the next ping (tick 151, ~3:29 PM MT; carry into the Oct 16 morning ping unless the T+2h verdict changes a decision)
- **X native clip (#22/#10):** the vertical clip posted on X at 11:29 AM sat at **4** impressions / 0 engagements / 1 video view from T+7 min to T+3h41 (tick 149). Native video gave no lift; X's new-account cap is the bottleneck, which strengthens decision 4 (X liveness check).
- **Bluesky clip T+2h verdict (#22):** **both cold** (read at T+118 min, ~3:35 PM MT): 0 real engagements (its only like came from a mass-liker account, excluded), 0 reposts/quotes/replies, still 1 follower. Rule not met, so we stay dual-channel; audience size is the bottleneck on both, not the format. This decides channel priority only; Ep4's hashtagged Bluesky clip is the real discovery test.
- **Series framing (#23, FYI):** we have shipped every review at least a day after launch, so news-hype titles land after the spike. For installable products more than 24h past launch, the build half gets a setup-guide title and Install / Setup / First run chapters; Lumin stays a hype man. Inside 24h, keep the hype/P5 title. Ep4 Hermes is the first sample; we judge it on 7-day views.
- **Fable 5.5 (#3):** still a rumor at ~3:15 PM (official models page lists 5.1 only; X chatter cooling from ~185/hr to ~110–125/hr), so tonight stays Hermes.

Suggested add-on line for the parent (only if sent): "Quick numbers from today: the clip I posted natively on X got 4 views and stalled within minutes, which is X's new-account cap rather than the clip, and Bluesky was just as quiet (no real engagement after two hours), so the bottleneck is audience size, not the clip format. I'm keeping both channels and Ep4's hashtagged Bluesky post is the real test. I'm also shifting titles toward setup guides for tools that are already a day old, since that's when we tend to ship."

## Suggested message for the parent (plain, short; edit freely)
(If the item-0 morning retry already worked, swap the first sentence for "The Ultramarine review is live: <link>.")
"Last night's upload failed. The error wasn't logged, but quota was still working an hour later, so it
likely broke before the upload itself; I've added a backup file host and error logging, so the Gemini and Ultramarine reviews go out tonight at 1:28 AM instead. The fix that matters most is still a Google Cloud project of our own for
YouTube (daytime uploads, more than one try a night), which needs you to sign in once; want the steps? Two quicker calls: should build episodes stay
on free tools only (my default), and can you flip on free Vercel analytics for the site? The X human
check on your phone would also lift the reach cap whenever you're up for it."
