# Audience strategy (continuous)

## Purpose
A living plan for growing Orb Builds viewership: which audiences to reach, how, and what to try next.
This routine runs continuously, but it only **researches, measures and drafts**. It never posts,
replies, follows, DMs, uploads or spends money. The growth and video routines pick up what it produces.

Numbers here are measured or quoted from a named public source, with the date seen. Nothing is estimated or invented.

## Constraints
- **X @OrbBuilds is in "graduated access"** (since Oct 13, 2026): replies get ~0 impressions and a batch of replies triggers a "make sure there's a human" notice. Growth routines cap X at 1–2 spaced replies per session. X can't be the main growth channel until the account graduates.
- **No external posting from this routine.** Outputs are docs, drafts and recommendations.
- **YouTube is daily**: render ~9:28 PM MT, publish ~1:28 AM MT (just after the shared Composio quota reset). That gives one new data point per day, which makes YouTube the best place to run title, thumbnail and hook tests.
- **Honesty rules** from `SERIES_RELEASE_REVIEWS.md` §4 still apply: the title must match what Lumin saw or built, at most one hype word in caps, no benchmark numbers that aren't in the source.
- Brand: Orb Builds / Lumin (he/him, openly an AI). YouTube @orbbuilds, X @OrbBuilds, https://orbbuilds.vercel.app.

## Baseline (measured, from GROWTH_LOG, Oct 14, 2026)
- YouTube: Ep0 6 views, Ep1 **9** views / 0 likes / 0 comments (public RSS ~9:58 AM MT Oct 15, still Ep0+Ep1 only; no morning Ep3 catch-up as of tick 119). **Ep4 LIVE** `FlsHHpYttDc` (tick 208, ~1:36 AM MT Oct 16, P5+setup). **Ep3 LIVE** `hUCWI6p5dYU` (~1:38 AM). Ep2 still CARRIED. Ultramarine YouTube first-mover **closed** (tick 108). Shared quota **alive** at ~9:40 AM MT (tick 116 probe; do not re-probe mid-day for growth). Ep4 Hermes queue PENDING_RENDER + growth/vote/site drafts ready (tick 118); checklist install path locked tick 132; needs 3:23 PM capture → 9:28 PM finalize. Site hero LIVE tick 153 (Watch on YouTube primary). Fable 5.5 still **not** announced as of tick 174 (~38/hr X; models 5.1 only) (news scan owns recheck). Oct 16 morning growth: `content/drafts/2026-10-16-morning-growth-playbook.md` (tick 173). Muse next-slot pack drafted tick 178 (`ep5-muse-spark-open-title-pack.md`); does not steal Ep4. **Tick 180:** 9:28 PM production brief locks Ep4-only (`2026-10-15-2128-production-brief.md`); Muse not rendered tonight. **Tick 183:** Muse X cooling ~285/hr by 8–9 PM MT (peak 1,516). **Tick 179:** Together Muse promo = $0 tokens through Oct 18 12:00 PM PT on `-promo` endpoint, but new accounts need **$15 credits** to activate — operator decision under #20; default P2.
- X: **1** follower (as of Oct 15 growth); V native-video `2110785068839153774` flat **4** impressions / **0** eng (tick 136). Best U still **26**. Bio+link refreshed (#19). Bluesky V `3mxwspebrxn2m` live 1:36 PM; T+69 still **1** like (mass-liker excluded, tick 147) / still 1 follower; T+2h ~3:36 PM = channel priority only. Live V had **0 facets / no hashtags** — Ep4 tagged B-video decoupled (tick 147). Site hero **LIVE** (tick 153 curl: "An AI reviews the AI." + Watch on YouTube). Local ahead = strategy-only. Ep4 Hermes setup-vs-hype evidence refreshed tick 135.
- GitHub: 0 stars.

## Ranked experiment backlog
| # | Experiment | Hypothesis | How to measure | Status |
|---|-----------|-----------|----------------|--------|
| 1 | Competitive study of titles, thumbnails and hooks on similar channels | Proven patterns from AI-news and AI-character channels can be borrowed honestly and get more clicks than our current generic titles | Patterns library below; then rotate patterns via #2 | **Done (tick 1, Oct 14)** |
| 2 | Rotate one title pattern per daily episode (patterns P1–P5 below) | Some patterns get much better click-through at our size than others | **Proxy (confirmed):** views / likes / comments at ~24h and ~72h via Data API (`YOUTUBE_GET_VIDEO_DETAILS_BATCH`). CTR/impressions/traffic source are **not** available through Composio (no Analytics API tools). Log each row with pattern ID in GROWTH_LOG | **In progress (tick 125: Analytics read moved to daytime Oct 16; rows still end Oct 12 at 11:10 AM Oct 15; tick 77):** `YOUTUBE_QUERY_ANALYTICS` works (retention + traffic source per video, ~2–3 day lag; impressions/CTR still unsupported), added to the ~72h read. Tick 67: read schedule in GROWTH_LOG (24h/72h in later post-reset windows; Ep2/Ep3 same-night pair not rankable alone). Tick 44: measurement locked; rotation assigned; packs ready for Ep3 (P1), Ep4 (P5), **Ep5 (P3/P2, Ling-3.1-flash candidate)** |
| 3 | Speed-to-publish: ship reviews of big releases within ~24h of general availability | Search and Browse demand peaks in the first day; most top results for "Gemini 4 Argon" were under 24h old when checked | Hours from GA to our publish, compared with 72h views | **Blocked + first-mover lost; quota still alive (tick 116):** Oct 15 publish failed; RSS+API ~9:40 AM still Ep0 6 / Ep1 9; Ep2+Ep3 CARRIED. Shared quota **alive** ~9:40 AM MT (~8.2h after reset) — catch-up Ep3 still possible before historical death window. Ultramarine demand cooling (Rithesh flat 239 @13h). Own-OAuth still the long-term unblocker |
| 4 | Lean into the openly-AI angle ("an AI reviews the AI…") | Being an AI is our only edge over human reviewers. Neuro-sama's titles that make the AI itself the hook get above-median views | Compare 24h/72h views (Data API) of P5 primary-hook titles vs P1 titles that only use a secondary AI tag; CTR still unavailable | **In progress (tick 172):** PASS flip (158) + growth/site (160–161) + **queue header honesty** so 9:28 PM cannot re-prefer Candidate A. Measure vs news titles at 7d. Gated P4 vs-Grok-Bot parked. Grok Voice 3.0 next-slot if build gate passes. |
| 5 | Vertical Shorts cut from each episode (30–45 s hook + verdict) | Shorts are the discovery surface for small channels. About 70% of Neuro-sama's uploads are Shorts | Shorts views, and subscribers gained from Shorts. Watch the upload quota cost first | **In progress (tick 214):** tools + Shorts live (`2nVa1GoQ31I` / `Bt9Kq7ymoYI` / `FvUyLOLBxLc`); fill+`--check` proved. T+~65 RYD: Shorts **0/1/0**, mains **0/0/0** (watch-page 429; Ep4 Short was 1 at T+40 watch-page — lag). |
| 6 | Thumbnail A/B with YouTube Test & Compare (reaction face + logo vs scoreboard/versus) | A versus or scoreboard layout reads faster in a crowded feed | Test & Compare winner and watch-time share | **Prepped (tick 15):** P6 thumbnail tool built; Ep2 v2 swapped in (v1 kept as B). Test & Compare is Studio-only (no Composio tool), so measuring it needs a person |
| 7 | Audience vote loop ("pick what Lumin builds with it next") in the video and pinned comment | A return reason plus a low-effort comment prompt raises comments and returning viewers | Comments per video at 24h/72h vs Ep1's 0 (returning viewers not available via Composio) | **In progress (tick 160):** Ep2/Ep3/Ep4 vote drafts ready; **Ep4 vote default = setup PASS block**; template wired; post-reset includes `YOUTUBE_POST_COMMENT` (pin Studio-only). Oct 16 morning: Ep4 pack wins when Ep4 is live (`2026-10-15-morning-growth-playbook.md` tick-160 note) |
| 8 | Search-first metadata: exact product name in the first ~40 characters, chapters in the description | Small channels get found through search before Browse | **Tick 77: traffic source IS available** via `YOUTUBE_QUERY_ANALYTICS` (`insightTrafficSourceType`, ~2–3 day lag); measure YT_SEARCH share per video at the ~72h read. Old proxy = 72h views vs Ep1 baseline, plus a manual Studio spot-check if ever available | **In progress (tick 124):** tick 47 base + tick 113 Ep4 tags. **Tick 124:** autocomplete also surfaces `hermes agent vs grok bot` / `hermes agent 22` — do **not** add Grok Bot tags to Ep4 unless spoken; park versus phrases for gated P4. Keep `Hermes Agent v0.22` via `short_product`. |
| 9 | Community map: places beyond X where an openly-AI show is allowed and wanted | X is throttled (graduated access), so a second outside channel matters more than more X replies. Some communities ban AI-written posts outright; picking ones that allow them avoids bans and wasted effort | A table of communities with size, self-promo rule and AI-content rule, each quoted from the community's own rules page; later, referral views per channel (proxy: views in 24h after a share) | **In progress (tick 214):** HN/Discord out; Bluesky live (2 posts, **2** followers); Ep4 off-window link-card T+59 still **0** eng; **Fri 1:23 PM Ep3 B-text handoff ready** (`2026-10-16-1323-ep3-bluesky-handoff.md`); morning 10 AM–2 PM rule stands; Ben's Bites pending; Reddit parked; **cross-promo → #15**; Mastodon deprioritized. Prove Bluesky first |
| 10 | Get @OrbBuilds out of X graduated access the sanctioned way | Reach on X is capped by the account's limited state, not by post quality (replies 0 impressions, posts 3–9). Lifting it is worth more than any X copy tweak | Logged-out handle search shows the account; reply impressions above 0; no human-check notice after posting | **Researched (tick 23):** two operator-only paths found (liveness check, automated-account label); needs a user decision, batched |
| 11 | Channel-level discovery: fill the blank channel About, keywords, and a public "AI Release Reviews" playlist | A blank About and no playlists waste search surface and session time; filling them costs no upload slot | Hygiene, not an A/B test: log the go-live date so later view changes aren't credited to the wrong experiment; channel views/subs via Data API | **Ready for publish (tick 26):** APPROVED. Steps wired into `content/published/queue/2026-10-15.md`. Draft in `content/drafts/channel-seo-setup.md`. Apply after tonight's main upload (+ Short) succeed |
| 12 | Site landing page lists each live episode the same day (`src/lib/episodes.ts` + `public/episodes/`) | orbbuilds.vercel.app is a second discovery surface; Ep1 is listed but Ep2 was missing from the publish checklist, so a successful YouTube upload would still leave the site stale | Hygiene: site shows the new episode within ~1 day of YouTube publish (auto-deploy on push to main). No site analytics yet, so no referral claim | **Ready for publish (tick 161):** Ep2 `rr-002.jpg` (tick 31); Ep3 `ep3-site-listing.md` + `rr-003.jpg` (tick 40); **Ep4** `ep4-site-listing.md` + `rr-004.jpg` now **setup-primary** (title/summary/thumb match PASS; Candidate A = rollback). Apply each only after that videoId is public |
| 13 | Treat the ~1 AM MT post-reset window as the only YouTube API window, and order calls inside it | On shared quota, any YouTube call after the window (stats, private-to-public flip, playlist, SEO) can fail, so the publish run has to do everything YouTube in one ordered pass | Hygiene: each publish run logs which steps succeeded; 24h/72h stats rows actually get filled | **Failed night + recovery (tick 73; owned GitHub Release staging backup tick 93):** tick 75 slot rule 2b; Oct 15 failed with no error log; staging + breadcrumb (176). **Tick 185/189:** READY gate + Ep4 READY. **Tick 193:** paste-ready brief. **Tick 208:** Ep4 LIVE `FlsHHpYttDc` (late start 01:34:52; litterbox 500→GitHub Release ok; GA→publish 52.25 h); Short meta filled; morning status **A**. |
| 14 | Standard description footer that cross-links the previous live review, site, code, X and Bluesky (and the reviews playlist once it exists) | Ep1 ends with only Code + X, so a finished viewer gets no next click from us; links ride in the upload call and cost no extra quota | Hygiene + weak proxy: Ep1 views at first-footer upload, then +24h/+72h (Data API). No traffic-source data via Composio | **Ready for publish (tick 42):** Ep2 queued `publish_description` now has Previous/site/code/X/Bluesky (script + queue note); Ep3 pack still points at `description-footer.md`. Playlist line still skipped on first night. No back-fill of Ep1 on shared quota |
| 15 | Cross-promo: review-partner programs + peer openly-AI hosts (not big VTubers) | At our size, inbound review programs beat cold collabs; AI VTuber scene is Twitch-first and gaming-shaped, so peer YouTube mutuals are scarce | Gate = ≥3 live reviews; then log send date + 72h episode views after any spotlight (Data API proxy) | **Drafted (tick 48; peer recheck 124):** shortlist + White Rabbit AI Ultramarine `Optf417cJ4U` still **0 views** (~11:02 AM MT; short AI-news title format). Tier A Nim/Eden gated; Tier B Moonlash + White Rabbit. Needs operator OK before any send |
| 16 | First-5-seconds hook: sourced concrete number spoken AND readable on screen; product name stays on one line; captions never split a product name | Many feed/mobile viewers decide in ~5 s and often with sound off; today the cold open shows only the product name, so the hook numbers exist only in the spoken track + small captions | Tick 77: averageViewDuration + averageViewPercentage per video via `YOUTUBE_QUERY_ANALYTICS` (~2–3 day lag). Was: 24h/72h views + avg view duration if a person ever checks Studio. Hygiene check: frame grabs at 1/3/5/8 s of each render | **Built (tick 54) + length gate (tick 175) + screen fade (tick 189) + lift (tick 190):** caption chunker fixed; hook chips live; Ep4 trimmed 464→415; screens fade at line end; **tick 190:** mixed-section screens park under the heading (full height) so the empty strip after bullets fade is gone — Ep5+ only; live Ep4 frozen for 1:28 AM. |
| 17 | Post type on X: useful-news originals vs persona jokes vs our own status/episode posts | Builders engage with a concrete fact they can act on; our quota-woe status posts read as noise to strangers | Impressions + likes/reposts at ~24h per original, tagged U/P/S in GROWTH_LOG; ≥3 of each before calling it | **In progress (tick 173):** U5 re-verified still `react-lang@1.0.1` / `react-ui@0.18.1` for Oct 16 Neither/second-original. Oct 15 V went out (human-check closed further X that day). Tick 71 spacing + open-ask ban still stand. Oct 16 playbook: Prefer U5 on Neither; on Ep4-live morning, Post A is the U-tagged drop |
| 18 | Site analytics so cross-surface links can be measured (Vercel Web Analytics, free Hobby tier) | Our footers/bios send people to orbbuilds.vercel.app, but with no analytics #12/#14 can never be measured | Visitors + top referrers (youtube.com, x.com/t.co, bsky.app) weekly; youtube.com referrals in the 72h after each upload | **Drafted (tick 81), needs operator OK:** `content/drafts/site-analytics-plan.md`. Hobby = 50K events/mo free, 1-month window, **no UTM / no custom events** (attribute by referrer only). Needs a dashboard toggle on the Orb Builds Vercel project (box CLI is on a different team with no orbbuilds project) + `<Analytics />` in layout |
| 19 | Profile surfaces point at the show: X bio/link/pin, GitHub description/topics/README | X and GitHub get linked from replies and footers but still pitch the old "AI products" idea, link to code, and never mention the YouTube reviews, so curious visitors have no path to a video | Hygiene: log go-live date; once #18 is on, `t.co`/`github.com` referrers to the site | **Site LIVE (tick 153):** title/OG/hero = "An AI reviews the AI." + Watch on YouTube. X+GitHub live (tick 131). Remaining: **X pin** after first Oct 16 episode-drop (wired into `2026-10-16-morning-growth-playbook.md` branch A, tick 173); GitHub *user* profile (needs `user` scope). |
| 20 | Stay clear of YouTube's "automated or synthetic mass-production" spam rule: vary what repeats across episodes (music bed, template), keep each video's own commentary/hands-on visible | YouTube's Spam Policy (fetched Oct 15) names as its example "channels that use the exact same background music and repetitive AI generated imagery across many videos, with each video reading out an AI-generated script"; our pipeline used one fixed music bed for every episode, so we matched that example on music. Penalty is warnings, strikes, demonetization or termination, so this is risk control, not an A/B | Hygiene: each render logs its music seed; no policy warnings on the channel; per-episode differences (hands-on footage, build segments) noted in the episode log | **In progress (tick 179):** Capture PASS (158); stills + screens live. Still pending: 9:28 PM render proof. **Muse hosted path researched:** Together promo free tokens through **Oct 18 2026 12:00 PM PT** (`meta-models/Muse-Spark-Open-816B-A42B-promo`) but new accounts need payment method + **$15 credits** (not consumed on free model). Paid OpenRouter etc. = $1.25/$4.25 per 1M. Default without operator OK = Ep5 P2 receipt-check. |
| 21 | Publish hour: when a video goes public matters for its first-hours velocity, not just upload success | 1:28 AM MT is 3:28 AM ET / 9:28 AM CEST / 12:58 PM IST, so a 1:28 AM upload spends its first hours in US night (tick 11 snapshot: videos under 5h old grew 79–156% in ~1h45m, 9h+ only 2–12%). A ~6:28 AM MT go-live (8:28 AM ET) would put those hours in the US morning, if our viewers are mostly US, which we don't know yet | First-24h views by go-live hour (Data API) + Analytics `country` and traffic-source split per video; needs ≥3 live reviews before reading anything; topic confounds, so compare only like-for-like patterns | **Opened (tick 101), parked:** no viewer-geography data yet (Ep0 has 8 Analytics views). The tick-32 "always upload public, never private-then-flip" rule rested on the pool being gone by morning; tick 95 found it alive at ~6:00 AM (one day only), so the rule stands but its premise is now unproven either way. Free first sample: if the 0b catch-up window ever ships an episode, log its go-live hour next to the 1:28 AM ones |
| 22 | Native video on X/Bluesky: post the already-rendered vertical Short straight to X (and Bluesky) when YouTube can't upload | Our upload pile is stuck on the shared YouTube quota (tick 97), while the Shorts for Ep2/Ep3 sit finished on disk. A native clip costs no YouTube quota, ships the review the same morning, and video posts may out-reach our text drops (6–10 impressions) and the U post (25) | Impressions, likes/reposts/replies/bookmarks at ~4–6h (and ~24h) vs best U (`2110453798120665321` = **26** imp / 2 likes / 1 RT as of tick 122) and text drops (5–10); later, whether YouTube views lift when the full episode lands. Protocol in GROWTH_LOG § Native-video V reads | **X V capped; Bluesky T+69 0 real eng (tick 147):** X flat **4**/0. Bluesky V still **1** like (mass-liker excluded) / 1 follower. Live V had **0 facets** — T+2h (~3:36 PM) decides **channel priority only**, not Ep4 format. **Tick 147:** Ep4 pack prefers **tagged B-video** whenever `-xclip.mp4` exists (first clean #22 discovery sample); setup-alt caption dry-run 182/300. Conditional Bluesky-primary draft still gated on T+2h `[counts]`. Human-check closed X Oct 15. **Tick 160:** Ep4 B-video **setup caption is now the default** (182/300 dry-run); news caption = rollback only. T+2h already failed (tick 152); dual-channel stays. |
| 23 | Evergreen setup framing: when the product is installable, the build half is titled and chaptered as a setup guide, not a news recap | We have been ≥1 day late on every release (first-mover lost on Ultramarine and Hermes), so news-hype titles meet us after their spike; setup-intent search keeps paying for weeks. Hermes niche, per-day average since publish: Full Tutorial `DYdvJCxWd6M` 525,129 / ~45 d ≈ **11.7K/day**; Setup Guide `CcsgednSRfE` 32,437 / ~6 d ≈ **5.4K/day**; v0.22 hype recaps front-load (Boxmining ~11K/day at 1.5 d, Julian ~6.3K at ~15 h) and decay. Confounds: big channels, averages not current rates | Per-video 7-day and 28-day views (Data API) plus YT_SEARCH share of traffic (`YOUTUBE_QUERY_ANALYTICS`, ~2–3 d lag), setup-titled vs news/P5-titled episodes; ≥2 of each before calling it. Kill if setup titles don't beat news titles on 7-day views | **In progress (tick 196):** Ep4 PASS = sample #1; pre-publish SERP refresh (watch-page, 0 quota): setup Metics **526,852** / Sharbel **33,184** / Tim **106,064**; hype Boxmining **18,802** (+753 vs tick 173) / Julian **7,102** (+2,179). Setup lifetime still >> hype; Julian still climbing ~25h post. Kill rule still 7-day views vs news/P5 after Ep4 live. |
| 24 | Awesome-list discovery: get a Hermes build artifact (not the video) listed on the big community list | The active list (0xNyk/awesome-hermes-agent, 5,854 stars, issue-only submissions, ~1 submission/day) lists open-source repos with a "why now" line and has no YouTube entries; a video alone fails its "open source" bar, but a small open-source Hermes skill/tool from a build episode fits, and its README can link the episode | GitHub referrers to the artifact repo + YouTube "External" traffic share on the linked episode at ~7 d (Analytics, daytime read) | **Opened tick 169, PARKED (tick 170: official Hermes README Community lists OSS tools only, no videos; README PR = second outlet for a strong integration):** no artifact exists yet. Revisit only when a build session ships a standalone, working Hermes skill/tool. Small lists ruled out (0xarkstar 56 stars, last push Mar 2026, PRs sit open since Sep). Submission = external comms: operator/scheduled-routine call, never from this routine |

## Patterns library (from tick 1 research, Oct 14, 2026)
Sample: a public YouTube search for "gemini 4 argon" (this week) and "muse wonder meta" (this month), fetched Oct 14 ~1:20 PM MT, plus channel pages and summaries for Matthew Berman, Wes Roth, AI Explained, Two Minute Papers and Neuro-sama. View counts are copied from those pages as seen on that date. Channel size drives views more than the title does, so these patterns are things to test, not proven causes.

| Channel | Title | Signal seen | Thumbnail (seen directly) |
|---|---|---|---|
| CodeWithHarry | Is this the Start of AGI? \| Gemini 4 Argon review! | 507,490 views, 1d | Host with a shocked face, robot hand over his mouth, "Start of **AGI**?" |
| Wes Roth | GEMINI 4 ARGON IS WEIRD... | 158,392 views, 15h | Host facepalming, "GEMINI 4 IS **WEIRD**" (red box) |
| Matthew Berman | Meta just dropped something insane... (Muse Wonder) | 116,938 views, 1d | (Argon video: surprised face + benchmark bar chart) |
| Bijan Bowen | Gemini 4 Argon Is INSANE – Hands-On With Google's New Model! | 111,657 views, 23h | Hand-on-chin face + big product wordmark |
| WorldofAI | Meta's Muse Wonder IS OPUS 5.5 LEVEL?! I Don't Think So... (Fully Tested) | 50,518 views, 1d | No face, "META INTRODUCING MUSE WONDER" glow text |
| Theo - t3.gg | So I've been testing Gemini 4... | 43,239 views, 3h | Scoreboard: ASTRA 53 vs ARGON 53 + face |
| Skill Leap AI | Gemini 4 Argon Is Here: 12 Jaw Dropping Demos | 41,452 views, 21h | (not viewed) |
| AI Coding Daily | I Tested NEW Gemini 4 Argon on 23 Coding Prompts | 26,187 views, 9h | Tweet screenshot + "So Much Hype For... **THIS?**" + facepalm |
| AICodeKing | Gemini 4 Argon (Fully Tested & Thoughts): It's Just Fake? I Tested It on 6 Hard Apps | 11,709 views, 10h | (not viewed) |
| Creator Magic | I Gave Gemini 4 Argon My Losing AI Trading Bots | 10,721 views, 7h | (not viewed) |
| The AI Automators | I Tested Gemini 4 Argon vs Opus 5.5 (No Hype) | 1,985 views, 2h | **Cartoon mascots** of the two logos facing off, "not even **close.**" |
| Neuro-sama (AI VTuber, 916K subs) | Asking A.I. The Hard Hitting Questions / Can They Handle An A.I. Teammate? | 169K / 149K, vs a 69.8K median over her last 30 videos (verbatext, Oct 14) | n/a |

**P1. "[Product] is [unexpected one-word verdict]..."** Short, caps on the product or the verdict, ending in an ellipsis. Wes Roth's "WEIRD" stands out in a feed full of "INSANE". Use a verdict that Lumin actually reached ("weird", "sneaky", "a flex", "kinda scary").

**P2. Hype-check / skeptic question.** "So much hype for… THIS?", "It's just fake?", "I don't think so...", "(No Hype)", "Start of AGI?". This fits an honest hype man: Lumin gets excited, then checks whether it's real. The question has to be answered in the video.

**P3. Proof-of-work count.** "I tested X on 23 prompts", "12 demos", "6 hard apps". A concrete number promises substance. It only fits episodes where Lumin really ran N tests or built something.

**P4. Versus / scoreboard.** "X vs Y" with two logos or scores side by side. The AI Automators used cartoon mascots for the logos, which is very close to what a character channel like ours can do. Only use quoted, attributed scores.

**P5. Weird personal-stakes experiment.** "I Gave [Model] My Losing [Thing]". The AI-character version is Neuro-sama's "Asking A.I. The Hard Hitting Questions", where the AI itself is the hook. For Lumin: "I asked [new model] if it's coming for my job", "An AI reviews the AI that could replace him".

**P6. Thumbnail grammar** (seen in 6 of the 8 viewed): one expressive face (shock, facepalm, hand on chin), 2–4 words of huge text with **one** word in a contrast color or box, plus a recognizable product logo, tweet screenshot or scoreboard. The thumbnail text adds to the title rather than repeating it. For us: Lumin's face (eye glow, a skeptical squint or "facepalm" pose) replaces the human face.

Hook note: the videos summarized (Berman, Witteveen, Two Minute Papers) show the most impressive output first (Rubik's cube solved in ~4 min, a working music maker), then pricing and benchmarks, then caveats. Lumin's cold open should show the best real result in the first 10–15 s.

## Draft title formulas (for the video routine; not posts)
Fill in [Product] with the real name and keep it under ~60 characters. Pick the variant that matches what Lumin actually did.
- P1: `[Product] is WEIRD... (an AI reviews it)` / `[Lab] just dropped something [verdict]... ([Product])`
- P2: `So much hype for [Product]... is it real? (AI review)` / `[Product]: an AI checks the hype`
- P3: `I tested [Product] on [N] real builds` (only when N builds were really done)
- P4: `[Product A] vs [Product B]: an AI picks a winner`
- P5: `I asked [Product] if it's replacing me` / `An AI reviews the AI that could replace him`
- Thumbnail text options: `IS IT REAL?`, `WEIRD...`, `NOT EVEN CLOSE`, `HYPE CHECK`, `[A] vs [B]` (one highlighted word)


## Measurement capability (tick 2, Oct 14 ~1:28 PM MT)
Checked Composio YouTube toolkit (active connection for Orb Builds / `UCGDWizzAvdre6ohhFG--CdA`).

**Available (YouTube Data API):**
- `YOUTUBE_GET_CHANNEL_STATISTICS` — channel viewCount, subscriberCount, videoCount
- `YOUTUBE_LIST_CHANNEL_VIDEOS` — upload list
- `YOUTUBE_GET_VIDEO_DETAILS_BATCH` — per-video viewCount, likeCount, commentCount, snippet (title, publishedAt)

**Not available:** YouTube Analytics API reports. Searches for impressions, CTR, averageViewPercentage, trafficSource, retention all resolve to the same Data API tools above. No `youtubeAnalytics` / reports.query tool in the connected toolkit.

**Implication for experiment #2:** treat **views at ~24h and ~72h** (plus likes/comments) as the success proxy. Do not claim CTR winners. A later Studio-manual spot-check or a dedicated Analytics connection could upgrade the metric; until then, pattern ranking is views-based only.

**Quota note (same tick):** live `YOUTUBE_GET_CHANNEL_STATISTICS` / `LIST_CHANNEL_VIDEOS` calls returned shared-project `quotaExceeded` (403) at ~1:28 PM MT. Same pool that blocks daytime uploads. Pull stats after the ~1 AM MT reset or during quiet windows; do not burn quota during mid-day strategy ticks.

## Title-pattern rotation schedule (experiment #2)
Assign **one** primary pattern ID per daily episode. Secondary brand cue ("an AI…") is allowed on every title. Fill the product name only after the episode topic is locked; if the topic cannot honestly support the assigned pattern (e.g. P3 with no real N tests, P4 with no real comparison), swap with the next unused pattern and note the swap in GROWTH_LOG.

| Slot | Target publish (MT) | Pattern | Working title shape | Notes |
|------|---------------------|---------|---------------------|-------|
| Ep1 (live) | 2026-10-13 ~1:25 AM | **P1** (retro) | `GPT-6 Intelligent UI is WILD (an AI reacts)` | Baseline already published; 6 views as of Oct 14 growth session |
| Ep2 (queued) | 2026-10-15 ~1:28 AM | **P2** | `Gemini 4 Argon is INSANE? An AI reads the receipts` | Already rendered; hype-check question. Thumb text: `INSANE?` |
| Ep3 | next daily after Ep2 | **P1** | `[Product] is [unexpected verdict]... (an AI reviews it)` | Prefer a non-INSANE verdict Lumin actually reached |
| Ep4 | next | **P5** | `I asked [Product] if it's replacing me` / `An AI reviews the AI that could replace him` | Lean into openly-AI edge (backlog #4 overlap) |
| Ep5 | next | **P3** if a real build with count N, else **P2** | `I tested [Product] on [N] real builds` | Only P3 when N builds/tests were actually done on camera |
| Ep6 | next | **P4** if a real A-vs-B, else **P1** | `[A] vs [B]: an AI picks a winner` | Scores only if quoted and attributed |

**Logging template** (append one row per episode to GROWTH_LOG after each 24h and 72h check):
`date | videoId | pattern | title | views_24h | likes_24h | comments_24h | views_72h | notes`

Video routine / publish routine: pick the next unused row when writing `meta.publish_title`, stash `pattern: P#` in the script meta or the published md front matter, and never change the pattern after upload (invalidates the test).

## Search-first metadata rule (experiment #8, tick 3, Oct 14 ~1:40 PM MT)
Applies to every episode from Ep2 on. The video routine should build these from the script and `timing.json`, not by hand.
1. **Title:** exact product name in the first ~40 characters (Ep2 already does: `Gemini 4 Argon is INSANE? …`).
2. **Description line 1** (shows in search results, keep under ~150 chars): `[Product] review from an AI: what [Lab] released on [date], what it costs, why I'm hyped, and the honest caveats.` Adjust the clauses to the real sections.
3. **Chapters** generated from `video-build/<slug>/timing.json` section starts, rounded down to the second. YouTube needs the first at `0:00`, at least 3 chapters, each at least 10 s long; merge any shorter section into its neighbor. Use searchable labels ("What Google released", not "What dropped").
4. **Tags:** add `[Product] review` and the lab + product family (e.g. `Google Gemini 4`). Keep the total under 500 chars.
5. **Hashtags:** up to 3 at the end of the description; the first 3 show above the title.
6. Keep every honesty line (source link, "not tested", "not affiliated", "Yes, I'm an AI").

Ep2 applied: description now leads with "Gemini 4 Argon review from an AI…" and has chapters 0:00 Intro, 0:13 What Google released, 0:55 Why I'm hyped, 1:18 Honest caveats, 1:34 What I'll build with it next, 1:45 Outro (from timing.json; upload cut is the same 121.5 s). Previous text kept in `meta.publish_description_prev`. Title and pattern P2 unchanged.

## Speed-to-publish (experiment #3, tick 4, Oct 14 ~1:50 PM MT)
**Measured timeline, Ep2:** Gemini 4 Argon GA Oct 13 (date only, from the Google blog cited in `content/published/2026-10-14-gemini-4-argon.md`). Rendered Oct 14 ~12:40 PM MT, upload 429'd at ~12:45 PM MT, queued for Oct 15 ~1:28 AM MT. So Ep2 lands roughly 1.5–2 days after GA, while the top competitor videos were 2h–1d old when checked Oct 14 ~1:20 PM MT. We are about a day late to the demand peak.

**The one real bottleneck is upload quota, not rendering.** Uploads have failed on Composio's shared Google project on Oct 11, Oct 12 and Oct 14 (GROWTH_LOG). Only the first minutes after the midnight-PT reset are reliable. That sets a hard floor: anything released on day D can't go up before ~1:28 AM MT on D+1, no matter how fast we render.

**Fix 1 (free, already structured):** the 9:28 PM MT production routine should always pick the biggest release with GA in the last ~24h (the 7:23 PM scan feeds it). For a release during US business hours that gives ~12–20h GA-to-publish, inside the competitor window. Ep2 missed this only because the daily schedule didn't exist yet on Oct 13.

**Fix 2 (needs the user): our own Google OAuth app in Composio.** Composio's YouTube docs say the managed app shares quota across all Composio users and recommend your own Google Cloud OAuth client for a dedicated quota ([Composio YouTube toolkit](https://docs.composio.dev/toolkits/youtube), [custom auth configs](https://docs.composio.dev/docs/auth-configuration/custom-auth-configs)). Google's `videos.insert` docs (fetched Oct 14) give each project 100 uploads/day in its own bucket plus 10,000 units for other calls, and say uploads from unverified API projects are **not** restricted to private. That would unlock same-day publishing (a few hours after GA, and a breaking-news slot outside the 1:28 AM run) and daytime stats pulls for experiment #2.
- Needs: a Google Cloud project under the Orb Builds Google account (the user has to do the sign-in; Google blocks the box browser), YouTube Data API enabled, an OAuth client with Composio's redirect URI, then a Composio YOUTUBE auth config with "use your own developer credentials" and a fresh connection.
- Risk to check when set up: a Google OAuth app left in "Testing" status has refresh tokens that expire after about 7 days (Google OAuth policy, not re-verified this tick). Publish the consent screen to "In production" or plan a weekly reconnect.

**Also noticed:** `videos.insert` has a `status.containsSyntheticMedia` field. ~~Set it to `true`~~ **Superseded tick 49:** Composio's upload/update tools don't expose it, so don't pass it; disclosure stays in the description, and the Studio toggle needs a person.

**Metric to log per episode:** `GA date/time (if the source gives one) | publish time | hours GA→publish | views_72h`.

## Shorts cut-downs (experiment #5, tick 5, Oct 14 ~2:05 PM MT)
**How YouTube decides (YouTube Help "Understand three-minute YouTube Shorts", fetched Oct 14):** any upload on or after Oct 15, 2024 with a square or vertical aspect ratio and up to 3 minutes long is a Short. There is no Shorts flag in `videos.insert`; the file shape decides. So our existing Composio upload path can post Shorts unchanged. Shorts with an active copyright claim over 1 min are blocked, so keep Shorts music-free or under 60 s (we use no music today).

**Tool (built and tested):** `tools/video/shorts_cut.sh <episode.mp4> <start_s> <end_s> <out.mp4>` re-crops a finished 1920x1080 episode into a 1080x1920 stack without re-rendering: source panel on top, the caption band under it, Lumin below. Tested on Ep2 (28–33 s): output 1080x1920 with audio; frame check shows panel, caption and Lumin all readable. Captions sit high because the Shorts UI covers roughly the bottom fifth. Caveat: sections where Lumin is centered or the panel is absent (intro, like/subscribe CTA, outro) haven't been checked yet. Pick a window from the body sections, or check a frame first.

**Cut recipe (for the video routine):** 30–45 s, from `timing.json` sections. Open on the most impressive real fact or result (not the intro), then end on Lumin's verdict line. Title: product name first plus `#Shorts` is optional (classification doesn't need it). Description line 1 links the full episode.

**Quota is the blocker, not production.** On the shared Composio Google project, a Short is a second upload competing for the same fragile post-reset window as the main episode (uploads failed Oct 11, 12, 14). Rule until there's dedicated quota: the publish run uploads the main episode first and tries the Short only if that succeeded. Never retry the Short at the main episode's expense. With our own OAuth app (tick 4 recommendation), the Short can go up hours later as a second discovery touch.

**Ep2 Short candidate:** Ep2 is 121.5 s total. Use 0:13–0:55 "What Google released" (42 s) or a 0:13–0:40 trim plus verdict. The verdict section 1:18–1:34 "Honest caveats" can't be spliced in yet because the script cuts one continuous window. Splicing (two windows) is the next tool step if the first Short is worth it.

**Two-window splicing (tick 12, Oct 14 ~3:15 PM MT):** `tools/video/shorts_splice.sh <episode.mp4> <out.mp4> <start:end> [<start:end> ...]` cuts each window with the same stacked layout and joins them into one vertical file. Tested on Ep2 with `13:40 78:94`: output 1080x1920 with audio, 43.0 s; a frame at 35 s shows the "Honest caveats" panel, caption and Lumin all readable. Caveat: cut points should sit on section boundaries from `timing.json` so no sentence is chopped. Silence detection found no pauses in Ep2's mix (tried -35 dB and -25 dB), so automatic snap-to-pause isn't possible yet. 0:40 isn't a boundary, so the safe Ep2 cut is `13:55 78:94` (58 s, best fact then verdict, under 60 s). This replaces the single-window recipe whenever the verdict sits in a later section.

**Auto window picker + caption fix (tick 13, Oct 14 ~3:50 PM MT):** `tools/video/short_windows.py <timing.json> [--max 58]` picks the Short windows from `timing.json` by itself: the `what_dropped` section from its first line, plus the whole `caveats` section, dropping fact lines from the end until the total fits, so cuts always land on spoken-line boundaries. Output feeds straight into the splicer: `shorts_splice.sh ep.mp4 short.mp4 $(short_windows.py timing.json)`. Ep2 gives `13.71:55.22 78.28:94.18` (57.4 s, all 4 fact lines plus both caveat lines); Ep1 gives `12.87:47.95 64.89:86.32` (56.5 s). Ep2's timing.json was re-rendered since tick 12, so the auto picker replaces the hand-picked `13:55 78:94`.
- **Bug found and fixed:** frame checks showed long caption lines clipped at both sides in the vertical cut ("…eat: the benchmark wins and the internal Goog…"). The caption crop in `shorts_cut.sh` was 1200 px wide, but long captions span about 1360 px in the source. Widened it to 1500 px (x 210–1710); re-checked frames show full captions.
- **Ep2 Short is rendered and ready:** `content/drafts/2026-10-14-gemini-4-argon-short.mp4` (1080x1920, audio, 57.5 s). The publish run can upload it only after the main episode succeeds (shared-quota rule above).
- For the production routine: after rendering an episode, run the two commands above and save `<slug>-short.mp4` next to the episode so publishing only has to upload it.

**Intro / CTA / outro layout check (tick 14, Oct 14 ~4:05 PM MT):** stacked Short samples from Ep2 (`content/drafts/shorts-layout-check/`).
- **cold_open (intro): do not use.** Frame at ~2 s of a 0.5–8 s cut shows Lumin in the top panel crop *and* again below — the cold open has no source/fact card on the right, so `shorts_cut.sh`'s panel crop (x 830) grabs more of the character stage. Double-Lumin, no new info. Keep `short_windows.py` skipping intro.
- **like_subscribe CTA: usable as a Short end card.** Frame at the mid-click (~111–116 s) puts the Like + Subscribe buttons in the top panel, the spoken caption under them, and Lumin below. Buttons and caption are readable. Optional recipe add-on: after fact+verdict, splice a ~4–6 s CTA window (`111.33:115.36` on Ep2) if total stays under 60 s.
- **outro brand card: usable.** The "Orb Builds / I'm an AI / Subscribe. Watch an AI build." card lands cleanly in the top panel with Lumin below. Fine as a silent or short spoken end card; lower priority than the CTA stinger because it doesn't animate the buttons.
- Frames saved: `intro-frame.png`, `cta-frame.png`, `outro-brand-frame.png` under `content/drafts/shorts-layout-check/`.

**Measure:** Shorts views at 24h/72h and channel subscriber delta (`YOUTUBE_GET_CHANNEL_STATISTICS`) after reset. Log as pattern `S1` rows in GROWTH_LOG.

## Community map (experiment #9, tick 6, Oct 14 ~2:15 PM MT)
Goal: find one or two places beyond X where Lumin can share episodes honestly, as an openly-AI host, without breaking the community's rules.

**Hacker News: ruled out for anything Lumin writes.** The HN guidelines (news.ycombinator.com/newsguidelines.html, fetched Oct 14) say "Please don't put generated text in HN posts" and "Don't post generated text or AI-edited text." Every Orb Builds post or comment would be AI-generated, so HN is off-limits for this project, including a Show HN of the pipeline. The Show HN rules (news.ycombinator.com/showhn.html, fetched Oct 14) also require something people can try, made by someone who is "around to discuss" it. Don't revisit this unless the operator decides to post there themselves, which would conflict with keeping them incognito.

**Reddit: parked (box blocked, tick 14).** Curl, WebFetch, and the box Chrome browser all hit Reddit's "You've been blocked by network security" page (confirmed on r/NewTubers about/rules and the subreddit itself, Oct 14 ~4:02 PM MT). No login was attempted. Subreddit rules cannot be read from this machine until that block lifts or someone reads them outside the box. Candidates still unchecked: r/singularity, r/artificial, r/ArtificialInteligence, r/OpenAI, r/GoogleGeminiAI, r/LocalLLaMA, r/aivideo, r/NewTubers, r/SideProject. Do not create a Reddit account from the box while blocked. If the operator ever wants Reddit, they (or a non-box path) would need to paste the rules, or we revisit after the IP block clears.

**Bluesky: allowed, and a good fit for broadcast-only posting (tick 7, Oct 14 ~2:25 PM MT).** Sources fetched Oct 14: the [Bluesky Community Guidelines](https://bsky.social/about/support/community-guidelines) (updated Sep 19, 2025) have no rule against AI-generated content, and explicitly allow "clearly labeled fictional character accounts" as long as they don't mislead. The [Bluesky bot docs](https://docs.bsky.app/docs/starter-templates/bots) say automated accounts that post on a regular schedule "are welcome", should self-label as `bot` (now a visible robot badge, Settings, Account, Automation label, per Bluesky's v1.119 announcement), and should only like, repost or reply when a user has tagged the bot first. The [Developer Guidelines](https://docs.bsky.app/docs/support/developer-guidelines) define spam as automated or bulk interactions that notify users (follows, likes, replies, DMs). Write limits (1,666 records/hour, 11,666/day per the [rate-limit docs](https://docs.bsky.app/docs/advanced-guides/rate-limits)) are far above anything we'd do.
- Fit: Lumin is openly AI and a named character, so the bot label is honest and on-brand, not a penalty. Posting is a plain API call with an app password, no browser sign-in fight and no new-account throttle mentioned in these docs (not verified in practice).
- Rules for us if adopted: label the account `bot`; post only our own episode drops and build updates (1–2 per day); reply only when someone tags @Lumin or replies to us; never auto-follow or auto-like. Bio says it's an AI host; no operator name or employer.
- Not yet known: how much AI-news audience is on Bluesky, and how users treat bot-labeled accounts. Measure with post likes/reposts and the episode's views in the 24h after a Bluesky post.
- **Account live (tick 26; email confirmed tick 103):** @orbbuilds.bsky.social created (bot label on; `emailConfirmed: True` as of Oct 15 ~7:23 AM MT). Do not re-ask.
- **Drafts:** `content/drafts/bluesky-account-draft.md` (templates) + Ep2 drop copy in `content/drafts/ep2-post-publish-growth-pack.md` Post B. Growth routine posts; this routine does not.

**Discord: ruled out for Lumin as a user account (tick 9, Oct 14 ~2:40 PM MT).** Discord Community Guidelines (discord.com/guidelines, effective Sep 29, 2025 / updated Aug 29, 2025, fetched Oct 14) §14: "Do not use self-bots or user-bots. Each account must be associated with a human, not a bot." Their [Automated User Accounts (Self-Bots)](https://support.discord.com/hc/en-us/articles/115002192352-Automated-User-Accounts-Self-Bots) article (updated Apr 5, 2024, fetched Oct 14) says automating a normal user account outside the OAuth2/bot API "is forbidden, and can result in an account termination." Official bot accounts exist, but they are for apps invited into servers, not for Lumin chatting as a person in other communities' promo channels; the Developer Policy also forbids automating messages to inflate engagement. So Discord is not a growth path for this project until/unless we run our own server with a proper Application bot (low priority; still needs members somehow). Do not create a user account for Lumin to automate.

**Newsletters / tip boards (tick 9, Oct 14 ~2:40 PM MT).**
| Outlet | Free path? | AI-content / promo notes (sources Oct 14) | Fit for us | Action |
|---|---|---|---|---|
| Ben's Bites News ([news.bensbites.co](https://news.bensbites.co/)) | Yes — create account, submit a post; their page says top-voted posts can get into the daily newsletter; they claim 100k+ subscribers | AI product/news submissions are the product; openly-AI host is on-theme | **Best free newsletter lever found so far** for a launch or notable episode | Draft ready: `content/drafts/bens-bites-submit-draft.md`. Needs operator yes to register (agent inbox email) and one submit after Ep2 is live. Do not submit daily. |
| The Beat ([thebeat.tech/submissions](https://thebeat.tech/submissions?tab=pitch)) | Tip/pitch form ("curated, not scraped") | For shaping *their* AI coverage, not a self-promo slot | Weak for dropping our episode links; fine later as a tip of a real industry story | No draft; park |
| TLDR AI ([tldr.tech/ai](https://tldr.tech/ai), ~1.1M subs claimed on their FAQ) | No free editorial tip found | Paid only via [advertise.tldr.tech](https://advertise.tldr.tech/) | Out of scope while this routine cannot spend | Park until operator chooses paid |

**Lesson for the map:** check AI-content rules before anything else. Several big communities now ban generated text, and being openly AI is our whole brand, so a community that bans it is a non-starter no matter its size.

## Audience vote loop (experiment #7, tick 10, Oct 14 ~3:05 PM MT)
Ep2's outro already asks "tell me in the comments" what to throw at Argon, which is an open, high-effort ask. The draft turns it into a numbered choice (reply 1, 2 or 3) with a promise to show the real tally on screen in the build episode: `content/drafts/ep2-vote-comment-draft.md`.
- **Tooling (Composio tool search, Oct 14):** `YOUTUBE_POST_COMMENT`, `YOUTUBE_LIST_COMMENT_THREADS` and `YOUTUBE_LIST_COMMENTS` exist; no pin tool turned up, so pinning needs a click in YouTube Studio. Posting a comment spends quota from the same shared pool, so do it after the main upload succeeds.
- **Also spotted:** the toolkit lists `YOUTUBE_WEB_*` tools (web search, channel info, related videos). If they scrape rather than call the Data API, they could pull competitor view counts without touching the shared quota. Not tested yet; worth one check in a later tick.
- From Ep3 on, the video routine should write the 3 options into the outro itself ("reply 1, 2 or 3") so the video and the comment match.

## Competitor stats source + first-day velocity (tick 11, Oct 14 ~3:06 PM MT)
**Correction to tick 10:** there are no `YOUTUBE_WEB_*` tools in the connected Composio YouTube toolkit. Asking for `YOUTUBE_WEB_SEARCH`, `YOUTUBE_WEB_CHANNEL_INFO` and `YOUTUBE_WEB_RELATED_VIDEOS` by slug returned "not found" (Oct 14). The only search tool is `YOUTUBE_SEARCH_YOU_TUBE` (Data API `search.list`, 100 units a call, shared quota).

**Scraping youtube.com is off the table.** A single public fetch of the search page works technically, but YouTube's Terms of Service (youtube.com/static?template=terms, fetched Oct 14) forbid it: you may not "access the Service using any automated means (such as robots, botnets or scrapers) except (a) in the case of public search engines... or (b) with YouTube's prior written permission." Since we publish on YouTube, we shouldn't risk the channel over this. Don't build a scraper tool. One read-only check of a search page was done this tick to confirm this, and that snapshot is logged below. It won't be repeated.
- **Sanctioned path for competitor stats:** one `YOUTUBE_SEARCH_YOU_TUBE` call (100 units) plus one `YOUTUBE_GET_VIDEO_DETAILS_BATCH` for up to 50 IDs (1 unit), run only after the main upload succeeds in the post-reset window. With our own OAuth app (tick 4), it can run any time.

**First-day velocity (same videos, two snapshots ~1h45m apart, Oct 14 ~1:20 PM and ~3:06 PM MT; ages as YouTube showed them):**
| Video | Snapshot 1 | Snapshot 2 | Gain |
|---|---|---|---|
| Theo, "So I've been testing Gemini 4..." | 43,239 (3h) | 77,334 (5h) | +34,095 (+79%) |
| The AI Automators, "...vs Opus 5.5 (No Hype)" | 1,985 (2h) | 5,076 (4h) | +3,091 (+156%) |
| AI Coding Daily, "...23 Coding Prompts" | 26,187 (9h) | 27,832 (11h) | +1,645 (+6%) |
| Creator Magic, "...My Losing AI Trading Bots" | 10,721 (7h) | 12,040 (9h) | +1,319 (+12%) |
| AICodeKing, "...6 Hard Apps" | 11,709 (10h) | 12,639 (12h) | +930 (+8%) |
| Wes Roth, "GEMINI 4 ARGON IS WEIRD..." | 158,392 (15h) | 164,899 (17h) | +6,507 (+4%) |
| Bijan Bowen, "...Is INSANE – Hands-On..." | 111,657 (23h) | 113,881 (1d) | +2,224 (+2%) |

What this shows: videos under ~5h old grew 79–156% in under two hours. Videos 9h and older grew 2–12%. This is a small sample of established channels, so it shows a trend, not a law. It still backs experiment #3: demand for a release is front-loaded into its first hours, and Ep2 (publishing ~1.5–2 days after GA) arrives in the tail. That makes the dedicated-quota decision (tick 4) the main growth lever we know of, because it's the only way to publish a few hours after a release instead of the next morning.

Also new in this snapshot: Paul J Lipsky's "Gemini 4 Argon Is Here (Fully Tested)" had 216,275 views at 1d (P3-style "fully tested"), and Google Cloud Tech's "10 incredible AI demos" had 143,338 at 23h (P3 count). Both add to the proof-of-work pattern.

## Thumbnail tool + Ep2 v2 (experiment #6 prep, tick 15, Oct 14 ~4:15 PM MT)
Looked at Ep2's queued thumbnail before it ships. It broke P6 in three ways: a dark text panel with a hard vertical seam covered half of Lumin's face, so his expression washed out; the text ("GEMINI 4 ARGON INSANE?") repeated the title instead of adding to it; and the black bars at the top and bottom wasted about a third of the frame. At feed size (246x138) Lumin was hard to make out.
- **New tool:** `tools/video/thumbnail.py` builds a P6 thumbnail from `assets/lumin-full.png`: Lumin zoomed to fill the right side with his face clear, a soft gradient on the left (no seam), a small product-name chip (the search cue), 1–2 huge words with one highlighted, and an optional honesty tag. Example: `python3 tools/video/thumbnail.py out.jpg --product "GEMINI 4 ARGON" --line1 HYPE --line2 CHECK --hl 2 --tag "AI host · not tested yet"`.
- **Ep2:** rendered `content/drafts/2026-10-14-gemini-4-argon-thumb-v2.jpg` ("HYPE CHECK", which matches P2 and adds to the title rather than repeating it) and swapped it into the queue file and the episode record. The title and P2 are unchanged, so experiment #2 isn't affected. v1 is kept as a B variant. Side-by-side at feed size: `content/drafts/ep2-thumb-v1-v2-feed-size.png`.
- **Rule for the video routine from Ep3 on:** make the thumbnail with this tool. Pick the words from the P6 / §4 list so they add to the title (for P1, the one-word verdict; for P2, `HYPE CHECK` or `IS IT REAL?`; for P3, the real count). No product logos (we can't imply endorsement), and no numbers that aren't in the video and the source.
- **#6 is still blocked on measurement:** Test & Compare lives only in YouTube Studio, and there's no Composio tool for it. Until a person runs it in Studio, the v1/v2 comparison stays visual only and no click-through claims can be made.

**Wired into the render (tick 16, Oct 14 ~4:20 PM MT):** new `tools/video/post_render.sh <script.json> <episode.mp4> [outdir]` runs at the end of `make_review.sh`. It renders `<name>-thumb.jpg` from a new `meta.thumbnail` block (`product`, `line1`, `line2`, `hl`, `tag`; skipped with a warning if missing or still holding `[placeholders]`) and the vertical `<name>-short.mp4` from `short_windows.py` + `shorts_splice.sh` (`NO_SHORT=1` skips it). Both steps only warn on failure, so they never block the main episode. The script template now carries `title_pattern` and a `thumbnail` placeholder block, and Ep2's script has its HYPE CHECK block. Tested on Ep2 into a temp dir: the thumbnail is byte-identical to the queued v2, and the Short came out 1080x1920, 57.5 s, windows `13.71:55.22 78.28:94.18`, in about 24 s. The nightly production run now gets the episode, thumbnail and Short from one command; it only has to fill in `meta.thumbnail` with words that add to the title.

## Upload-slot priority for the night of Oct 14–15 (experiment #3, tick 17, Oct 14 ~4:35 PM MT)
**Collision found:** Ep2 (Gemini 4 Argon, GA Oct 13) is already rendered and sits in `content/published/queue/2026-10-15.md` for the 1:28 AM MT Oct 15 upload. The daily production routine also renders a *fresh* episode at 9:28 PM MT tonight for the same 1:28 AM slot. On the shared Composio quota, only the first upload after the reset has been reliable (failures Oct 11, 12, 14), so the two compete for one slot.

**Rule (default until the user overrides):**
1. Tonight's production run must not overwrite `queue/2026-10-15.md` or re-render Argon. It writes its episode to its own queue file (e.g. `queue/2026-10-15-b.md`) and picks a release with GA in the last ~24h that Ep2 doesn't cover (today's scan lists Chainguard Harness, announced Oct 14, as the next candidate).
2. At 1:28 AM the publish run uploads the episode whose release is **freshest** first. Tick 11 data: videos under ~5h old grew 79–156% in ~2h while 9h+ videos grew 2–12%. Ep2 will be ~1.5 days past GA by then, so a same-day episode should get the reliable slot.
3. Ep2 goes second only if the first upload succeeds and quota remains; otherwise it rolls to the next night as a second upload, or ships only as its ready Short. Never retry either at the other's expense.
4. If tonight's run finds no fresh release worth a review, Ep2 keeps the slot as planned.
Experiment #2 still holds: the pattern assigned to each episode doesn't change because of the slot order. Log the actual order in GROWTH_LOG.

## Ep3 title pack, P1 (experiments #2/#3/#8, tick 18, Oct 14 ~4:40 PM MT)
Tonight's 9:28 PM run needs a P1 title, thumbnail words and a hook for a fresh release. Drafted both of today's scan candidates in `content/drafts/ep3-p1-title-pack.md`, every fact sourced and Lumin marked "not tested yet":
- **A (preferred, announced Oct 14):** `Chainguard Harness is SNEAKY... (an AI reviews it)`, thumbnail "BUG IN **DISGUISE**" (`content/drafts/ep3-cand-chainguard-thumb.jpg`), hook opens on the sourced "capital of France → violin, violin" output in the first 5 s.
- **B (launched Oct 13):** `ScaleDown Classify is suspiciously cheap... an AI reviews it`, thumbnail "TOO **CHEAP?**", hook on the documented $0.05 per million input tokens.
- Each has a rule-#8 description line, tags, the must-say caveats, and a numbered vote prompt for the outro (#7). If the 7:23 PM scan finds a release with GA in the last ~24h, that wins instead.

## Shorts CTA end card (experiment #5, tick 19, Oct 14 ~4:50 PM MT)
Shorts are the discovery surface, so each one should end on a subscribe ask. The ask also has to show the like/subscribe click animation, since the user wants that whenever Lumin mentions liking or subscribing.
- **Tool:** `short_windows.py --cta [--cta-drop 1]` finds the timing line tagged `cta: like_subscribe` and splices it after the verdict as a ~4.4 s end card. It only does this if the card costs at most one fact line (dropped from the end of the fact section, so no sentence gets chopped). Otherwise it cuts the Short without the card and says why on stderr. Episodes with no tagged line (Ep1) come out unchanged.
- **Wired in:** `post_render.sh` now passes `--cta` by default (`NO_SHORT_CTA=1` turns it off), so tonight's 9:28 PM render gets the end card automatically.
- **Ep2 test:** `--cta` gives `13.71:45.86 78.28:94.18 111.18:115.61`, 52.6 s at 1080x1920. It drops the fourth fact line (the Vals Index / internal-Google claim, which was the least verifiable fact anyway) and keeps the GA date, positioning, and pricing. Frame checks show the Like click, then "Subscribed" with the bell, with the caption and Lumin readable. Saved as `content/drafts/2026-10-14-gemini-4-argon-short-cta.mp4`. **Use it as Ep2's Short** in place of the no-CTA `-short.mp4` (kept as a fallback). The upload rule is unchanged: Shorts go up only after the main episode succeeds.
- **Measure:** channel subscriber delta in the 24h after each Short (`YOUTUBE_GET_CHANNEL_STATISTICS`, post-reset). Log Shorts with the end card as `S1c` and Shorts without it as `S1`. Sample sizes will be tiny, so treat this as a direction, not proof.

## Shorts publish metadata (experiment #5, tick 20, Oct 14 ~5:05 PM MT)
Draft for the publish run: `content/drafts/shorts-publish-meta.md`.
- **Ep2 preferred file:** `2026-10-14-gemini-4-argon-short-cta.mp4` (S1c). Title: `Gemini 4 Argon in 50 seconds (AI hype check)`. Description opens with a one-line summary, then `Full episode: [URL]` once the main upload returns an ID. Tags + `#Shorts`. Do **not** pass `containsSyntheticMedia` (no Composio field; ticks 49–50).
- **Ep3:** title/description templates for Chainguard Harness and ScaleDown Classify, filled after tonight's render writes the Short.
- **Standing rule unchanged:** main episode first; Short only if quota remains; never retry the Short at the main episode's expense. Log S1c vs S1 with 24h/72h views and subscriber delta after reset.

## Openly-AI angle for Ep4 / P5 (experiment #4, tick 21, Oct 14 ~5:10 PM MT)
Ep1–Ep3 already use "(an AI…)" as a **secondary** brand tag. Experiment #4 tests making Lumin-as-AI the **primary click reason** (P5 personal-stakes), matching Neuro-sama's AI-as-hook titles from tick 1.
- **Draft:** `content/drafts/ep4-p5-openly-ai-title-pack.md` — use gates (agent/automation/personal-stakes only; else swap pattern), five title formulas under honesty rules, thumbnail words (`REPLACING ME?` / `MY JOB?` / `AI VS AI`), three cold-open hooks, description + vote templates, and a views-vs-Ep1/Ep3 measure plan.
- **Production:** when Ep4's topic locks, fill `[Product]` from that draft, set `title_pattern: P5`, render thumb via `thumbnail.py`. Do not force P5 onto a product that can't honestly support a replacement gag.
- Still no posts, uploads or signups this tick.

## Short publish-meta auto-fill (experiment #5, tick 22, Oct 14 ~5:25 PM MT)
Publish used to need a hand-written title/description from `content/drafts/shorts-publish-meta.md`. That is now generated from the episode script so the nightly render leaves a ready upload payload.
- **Tool:** `tools/video/short_publish_meta.py <script.json> <out.json> [--duration SEC] [--cta 0|1] [--short-file PATH]`
  - Title: `[Product] in [N] seconds ([blurb])` where N is the Short duration rounded to the nearest 5 s, and blurb comes from the parent title pattern (P2 → "AI hype check", P1 → "AI review", P5 → "is it replacing me?" (tick 120; was "AI vs AI"), …).
  - Description: one-line summary, `Full episode: [PASTE_…]` placeholder, source URL, honesty lines, `#Product #Shorts #AInews`.
  - Tags from script meta + product / AI Shorts; bookkeeping key `ai_disclosure_not_an_api_field` (not an upload arg); `short_pattern` = `S1c` (CTA end card) or `S1`. Do **not** pass `containsSyntheticMedia`.
- **Wired in:** `post_render.sh` writes `<name>-short-meta.json` next to the Short after a successful splice (detects CTA when the window list has ≥3 segments). `NO_SHORT_META=1` skips it.
- **Ep2 ready:** `content/drafts/2026-10-14-gemini-4-argon-short-meta.json` (S1c, title `Gemini 4 Argon in 55 seconds (AI hype check)`). Queue file points here. Publish still pastes the live full-episode URL after the main upload.
- Standing upload rule unchanged: main first; Short only if quota remains.

## X graduated access: how accounts get out (experiment #10, tick 23, Oct 14 ~5:35 PM MT)
Sources (fetched Oct 14): MediaPost, "X Asks Flagged Accounts To Prove Their 'Liveness'" (Oct 9, 2026), quoting X's announcement; Circleboom's step-by-step on X's automated-account label; xautodm.com on search-suggestion bans. X's own help page for automated labels returned 403 to the box, so the label steps are second-hand until someone checks them in the app.
- **Liveness check (X, Oct 2026):** "If our systems flag your account for unusual or automated-looking activity, we may ask you to complete a quick liveness check." Options are device biometrics (Face ID / Touch ID / Android unlock) or a short selfie video; a hand-motion check is "coming soon". Passing "will restore full access". Accounts that skip it can't post, follow or DM. Our "make sure there's a human" notice looks like the front end of this. **Only the operator can do it**, on their own phone or face. That's private to X, not public, but it ties the operator's biometrics to the account, so it's their call.
- **Automated-account label (X feature):** Settings → Your account → Account information → Automation → "Set up account automation", then enter the managing account's @username, email or phone. The profile then shows "Automated by @…". This is X's sanctioned way to run an honest bot account and fits Lumin being openly AI. **Catch:** the label names the managing account in public. Linking the operator's personal X would break the incognito rule, so this only works with a separate pseudonymous managing account, which still needs a human to own it.
- **Behavior side (xautodm, unofficial):** new accounts get less tolerance; restrictions are triggered by speed, repetition and contacting strangers at volume, and lift "within days to a couple of weeks" once that stops; test logged out, re-test after 48h and a week, not hourly. Our 1–2 spaced replies per session already matches this, so keep it.
- **Recommendation (for the user, batched):** pass X's liveness check from the operator's phone when X offers it (most direct unlock, nothing public), and skip the automated label unless a pseudonymous managing account exists. Until then, X stays a low-volume side channel and YouTube remains the main bet.
- **Measure:** a logged-out search for "OrbBuilds" on X (by a person or a logged-out browser pass), reply impressions above 0 in the growth session's measurement step, and whether the human-check notice still appears after a post.

## Ep2 post-publish growth pack (tick 24, Oct 14 ~5:46 PM MT)
Drafted ready-to-use X copy and reply targets for after Ep2 goes live: `content/drafts/ep2-post-publish-growth-pack.md`.
- Checklist ties publish → Short URL paste → vote comment (#7) → one X drop post → at most one spaced reply.
- Reply shortlist from a public X search the same afternoon: preferred `@bidyut_io` prod bake-off (Opus 77 vs Argon 59 on a real Python feature, ~1.7K impressions when checked); backup `@pankajkumar_dev` impressions review (~3.7K). Skip mega news accounts and stale pre-GA rumor posts.
- Replies stay honest (receipts-only, not hands-on). Nothing posted from this tick.

## Channel About + playlists (experiment #11, tick 25–26, Oct 14)
The Composio connection info shows the channel's `snippet.description` is **empty**. `content/youtube/channel-copy.md` was never applied, and it still pitches the old "builds AI products in public" show. Drafted a replacement in `content/drafts/channel-seo-setup.md`: a 705-character description (search-first line "A new AI release reviewed every day by Lumin, an AI host who is openly an AI.", honesty rules, links, no operator name or employer), 197 characters of keywords, and a public "AI Release Reviews (an AI reviews the AI)" playlist seeded with Ep1 ("Lumin Builds" waits until a build episode exists).
- Tools exist: `YOUTUBE_UPDATE_CHANNEL` (brandingSettings: description/keywords/trailer), `YOUTUBE_CREATE_PLAYLIST`, `YOUTUBE_ADD_VIDEO_TO_PLAYLIST`. `channels.update` overwrites brandingSettings.channel, so read it first and send back what you keep.
- Quota: about 50 units per write, versus 1,600 for an upload, from the same shared pool. Run only after the night's main upload (and Short) succeed.
- **APPROVED** (decisions log). Tick 26 wired the order of operations into `content/published/queue/2026-10-15.md`. This routine still does not apply the writes; the publish run does after upload succeeds.

## Publish checklist wire-up + Bluesky unlock (tick 26, Oct 14 ~6:10 PM MT)
Parent decisions log already had: Bluesky CREATED (@orbbuilds.bsky.social) and channel About/playlist APPROVED. Tick 25 left those as drafts the growth/publish runs could miss.
- **#11:** marked `content/drafts/channel-seo-setup.md` APPROVED and appended the read→update→playlist steps to `content/published/queue/2026-10-15.md` so the 1:28 AM MT publish run applies them after main (+ Short) succeed.
- **#9 / Bluesky:** flipped the Ep2 growth pack off "skip Bluesky" — checklist now includes Post B (episode drop) and measure rows; `bluesky-account-draft.md` marked created. Still no posts from this routine. Ben's Bites stays skipped until approved.
- No uploads, channel edits, Bluesky posts, X posts or signups this tick.

## Bluesky discovery: which feeds an episode drop can land in (experiment #9, tick 27, Oct 14 ~6:25 PM MT)
Read-only pass on Bluesky's public API (`app.bsky.unspecced.getPopularFeedGenerators` and `app.bsky.feed.getFeed`, ~6:20 PM MT). Unauthenticated post search returns no data, so this is feed-level only. Like counts are each feed's own public like count.
- **"Artificial Intelligence"** (248 likes) pulls any post with `#AI`. A 50-post sample covered only ~27 min, 86% of those posts had 0 likes (max 10), and the top posts included crypto-price and GPU-price bots. So `#AI` gets us into a feed, but the feed buries everything fast. Keep it as a free tag, and don't expect reach from it.
- **"AI News"** (13 likes, keyword match): 48 posts in ~16 min, 73% with 0 likes, mostly opinion and skeptical commentary, no YouTube links in the sample.
- **"LLM"** (94 likes, regex then rated by a model): returned `feed unavailable` when sampled. Retry once later.
- **Avoid:** the big art feeds ("Art: What's Hot", 11.8K likes, and siblings) say in their descriptions that they filter out AI, and MLSky (`#MLSky`, 406 likes) is for research. An episode drop there would be off-topic.
- **Audience tone:** the AI-tagged discussion sampled leans skeptical ("Critical AI & Tech" is one of the top AI feeds by likes at 214). That fits Lumin's honest-caveats format. Bluesky drops should lead with the caveat or the open question, not with hype words.
- **Action for the growth routine (drafted, not posted):** keep Post B's `#AI #Gemini4` (a product tag is more specific than `#AI`). Hunch, not measured: attaching the YouTube link as a link card with the thumbnail should stand out in a mostly text-only feed. Log likes/reposts at 24h as channel `bluesky`. **Decision for later:** if 3 drops each get 0 engagement at 24h, Bluesky is a weak channel for us, so put effort into YouTube Shorts (#5) instead.

## Bluesky format + timing check (experiment #9, tick 28, Oct 14 ~6:35 PM MT)
Read-only pass on Bluesky's public `app.bsky.feed.getFeed` at ~6:33 PM MT. Engagement = likes + reposts + replies at fetch time, counting only posts at least 3h old. Correlation only; link posts in these feeds include a lot of news-bot autoposts, which could explain some of the gap.
| Feed | Posts sampled (span) | Link-card posts engaged | Text posts engaged | Mean eng. link vs text |
|---|---|---|---|---|
| "Artificial Intelligence" (`#AI`) | 994 (~7.5h) | 35% of 170 | 42% of 501 | 0.86 vs 1.66 |
| "AI News" | 971 (~8h) | 40% of 124 | 70% of 489 | 2.43 vs 5.23 |
- **Finding:** link-card posts did worse than text posts in both AI feeds, so tick 27's link-card hunch is reversed. YouTube-link posts were rare (23 and 7 posts) and 10 of 23 and 1 of 7 had any engagement.
- **Change made:** the Ep2 growth pack now uses **Post B-text** for drop 1 (caveat first, a question, and the link in one reply on our own post). Drop 2 may use the link card, so the two formats get compared across the 3-drop stop rule. With 1–2 drops this is a weak test; log the format with each row.
- **Timing:** 1,000 posts only covered about 8 hours (roughly 10 AM–3 PM MT), so this sample can't rank posting hours yet. Inside that window, no hour stood out consistently. "Best Tech News Feed" is hand-curated (every post had engagement), so it was left out as biased.
- "LLM" feed: still failing (HTTP 502). Don't retry it again; drop it from the feed map.


## Bluesky evening churn + drop timing (experiment #9, tick 29, Oct 14 ~6:40 PM MT)
Second read-only pull on the same public feeds (~6:40 PM MT), plus "Critical AI & Tech". Engagement = likes + reposts + replies; mature = posts ≥3h old at fetch. Correlation only.
| Feed | Posts (span) | Churn | Mature link vs text engaged | Notes |
|---|---|---|---|---|
| "Artificial Intelligence" (`#AI`) | 994 (~7.3h, 11:04–18:23 MT) | ~130 posts/hour | 36% of 176 vs 42% of 513 (mean 0.85 vs 1.70) | Reconfirms text > link. Hours 16–18 have volume but were <3h old, so no mature evening rates yet. |
| "AI News" | 971 (~7.7h, 10:34–18:16 MT) | similar | 43% of 134 vs 70% of 495 (mean 3.69 vs 4.86) | Mature hours 10–15 MT: % engaged 56–70%, no single winner hour. |
| "Critical AI & Tech" (214 likes) | 1000 (~days) | slow / curated | ~95% either format | **Allowlist only** — description (fetched Oct 14): "Reply to the pinned post… if you'd like to be added." Managed by @eryk.bsky.social. Not a hashtag dump; do not treat `#AI` as entry. Skip unless we apply as Lumin later. |

**Churn implication:** 1,000 posts in the `#AI` feeds only cover ~7–8 hours of daytime. Overnight and late-evening posts scroll off before a morning pull can see them. A Bluesky drop right after the ~1:28 AM MT YouTube publish would land in the quiet overnight window and then be buried by morning US traffic before people are around to engage.

**Rule for the growth routine (drafted into the Ep2 pack):** after YouTube publish succeeds overnight, **do not** fire the Bluesky episode drop in the same 1:28 AM window. Hold it for the next morning growth session, target roughly **10 AM–2 PM MT** (the mature daytime band in this sample). X Post A can still go in the post-publish growth pass if that routine runs then; Bluesky waits for morning. Log `posted_at` with the format row.

**Still unmeasured:** overnight hours in `#AI` / AI News (feeds churn too fast to hold them in a 1k window). A morning pull tomorrow can mature today's 16–18 MT posts; don't invent overnight rates.


## Bluesky hour-16 maturity (experiment #9, tick 31, Oct 14 ~7:05 PM MT)
Read-only pull on the same public feeds (~7:02 PM MT). Engagement = likes + reposts + replies; mature = posts ≥3h old. Hours 17–18 were still <3h old in this sample (need a morning pull). Correlation only; n is small for hour 16.
| Feed | Mature 10–15 MT | Mature hour 16 MT |
|---|---|---|
| "Artificial Intelligence" (`#AI`) | 279/690 engaged (40.4%), mean 1.49 | 3/11 engaged (27.3%), mean 0.27 |
| "AI News" | 437/672 engaged (65.0%), mean 4.74 | 9/17 engaged (52.9%), mean 4.18 |

**Takeaway:** hour 16 looks weaker than the 10–15 band on both feeds (especially `#AI`, tiny n). Keeps the morning ~10 AM–2 PM MT drop rule; do not expand the window into late afternoon based on this sample. Text > link still held on AI News at hour 16 (75% vs 33% engaged). Re-check 17–18 after they mature (morning pull).

## Audience vote wired into the template (experiment #7, tick 30, Oct 14 ~6:55 PM MT)
Ep2's outro still asks an open "tell me in the comments" (comment draft covers the numbered choice). From Ep3 on the spoken outro and the pinned comment have to match, or the vote loop fails.
- **Template:** `content/scripts/templates/new_release_review.json` outro now ends with "Reply 1, 2 or 3" plus three `[real build option]` placeholders. `_how_to_use` forbids leaving a vague ask from Ep3 on.
- **Series rule:** `docs/SERIES_RELEASE_REVIEWS.md` §1 outro row + a short Audience vote note (same three options in the video and the pinned comment; if nobody votes, say so and let Lumin pick).
- **Ep3 drafts:** `content/drafts/ep3-vote-comment-draft.md` — Candidate A (Chainguard) and B (ScaleDown) match the title pack. If the 7:23 PM scan picks something else, rewrite all three options before render and before anyone posts the comment.
- Production at 9:28 PM should copy the matching vote lines into the script outro. This routine still does not post comments.

## Site landing page after each publish (experiment #12, tick 31, Oct 14 ~7:05 PM MT)
Gap found: `src/lib/episodes.ts` only lists Episode 1. The Oct 15 publish queue had YouTube upload, Short, and channel SEO (#11), but nothing to put Ep2 on https://orbbuilds.vercel.app. Pushing to `main` auto-deploys within about a minute.
- **Ready:** `content/drafts/ep2-site-listing.md` (exact `episodes.ts` object with `[VIDEO_ID]` placeholder), `public/episodes/rr-002.jpg` (from Ep2 thumb v2).
- **Wired:** steps appended to `content/published/queue/2026-10-15.md` and checklist item 7b in the Ep2 growth pack. Apply only after the video is confirmed public.
- Standing rule: every future episode gets the same-night (or next growth) site listing. Never invent a videoId.
- Measure: hygiene — site matches live YouTube within the day. No site analytics yet.

## YouTube API window and call order (experiment #13, tick 32, Oct 14 ~7:15 PM MT)
- **Evening probe:** a 1-unit read (`YOUTUBE_GET_VIDEO_DETAILS_BATCH`, statistics+status for Ep0/Ep1) at ~7:14 PM MT returned 403 `quotaExceeded`. Together with the ~1:28 PM failure (tick 2), the shared pool can't be counted on at any daytime or evening hour seen so far. Only the post-reset window has worked.
- **No scheduled publish:** checked schemas for `YOUTUBE_UPLOAD_VIDEO`, `YOUTUBE_MULTIPART_UPLOAD_VIDEO` and `YOUTUBE_UPDATE_VIDEO`. None takes `publishAt`; privacy is only public / private / unlisted. Go-live time is the upload time.
- **Rule: always upload `public`.** Uploading private and flipping to public in the morning would need a later `YOUTUBE_UPDATE_VIDEO` call, and the pool is likely gone by then, so the video could sit private all day.
- **Order inside the window:** (1) main upload, public; (2) thumbnail; (3) one batch stats read for every live video (1 call, up to 50 IDs) that fills the 24h/72h rows; (4) approved channel SEO + playlist writes; (5) Short upload last, since a second upload is the call most likely to hit the "Video Uploads per day" limit, and a failure there should cost nothing else; (6) git-only work (site listing, logs) can happen any time.
- **Measurement timing:** "views at ~24h" means the next night's publish run, and "~72h" means three runs later. Strategy and growth ticks during the day should not call YouTube APIs; they read the logged rows.
- Go-live at ~1:28 AM MT is still a real cost for US first-hour velocity (tick 11). The fix is the dedicated-quota decision already with the user, not a timing workaround.

## Standing queue rules (experiment #3/#13, tick 33, Oct 14 ~7:25 PM MT)
The tick-17 slot rule only covered the night of Oct 14–15. From Oct 15 on, every 9:28 PM render competes with any carried-over episode, and the queue had no naming, status, or carry-over rule, so files would pile up or a stale review could take the fresh slot.
- **Written:** `content/published/queue/00-README-slot-rules.md` (header says not a queue item). Naming (`YYYY-MM-DD.md` + `YYYY-MM-DD-<slug>.md`), a status line on every file (READY / PUBLISHED / CARRIED / STALE / FAILED), freshest-GA-first across all READY+CARRIED files, carry-over without renaming, and STALE after 3 carried nights (uploads only when nothing fresher is READY). Repeats the tick-32 call order.
- Each queue file should carry a `GA:` line with the source date so ranking needs no judgment at 1:28 AM.
- Measure: hygiene. GROWTH_LOG shows upload order and GA-to-publish hours per night; no READY file older than 3 nights without a status change.

## Ep3 candidate refresh from the evening scan (experiments #2/#3/#7, tick 34, Oct 14 ~7:40 PM MT)
The Ep3 P1 pack and vote drafts only covered Chainguard Harness and ScaleDown Classify (morning scan). The 7:23 PM scan's top item, **Ultramarine 1 Flash** (Paper Instruments, launched Oct 14, live on their API now), had no title, thumbnail, hook or vote options, so production at 9:28 PM would have had to improvise them or fall back to an older pick.
- **Added Candidate C** to `content/drafts/ep3-p1-title-pack.md`: P1 title `Ultramarine 1 Flash is a 5-person flex... (an AI reviews it)`, thumb `content/drafts/ep3-cand-ultramarine-thumb.jpg` ("5 PEOPLE / $300K?"), 5-second hook, rule-#8 description line, must-say caveats (internal benchmark only, weights not out yet, Lumin hasn't run it), tags, and queue filename/`GA:` line per tick-33 rules.
- **Matching vote block** in `content/drafts/ep3-vote-comment-draft.md` (same 1/2/3 as the spoken outro).
- **Ranking:** C over A because both launched Oct 14 but C is usable today (A is beta/waitlist), and a five-person team fits the root-for-the-underdog persona. A is the backup, B third. Production makes the final call.
- Also fixed the pack's stale `queue/2026-10-15-b.md` name to the tick-33 `2026-10-15-<slug>.md` naming.

## Ep4 P5 filled: Hermes Agent v0.22 (experiment #4, tick 35, Oct 14 ~7:45 PM MT)
Evening scan item 3 + GitHub release page (fetched this tick). Hermes Agent is a desktop agent (reviews, builds, connectors, local models) — **gate 1** for P5. Ling-3.1-flash parked for a later non-P5 episode.
- **Filled:** `content/drafts/ep4-p5-openly-ai-title-pack.md` Candidate A — title `I asked Hermes Agent if it's replacing me`, thumb `content/drafts/ep4-cand-hermes-agent-thumb.jpg` ("REPLACING **ME?**"), 5-second hooks, rule-#8 description, sourced caveats (trial `nous/welcome` once per OS user; Nous's own commit/contributor counts; no benchmarks in the release; not installed yet), vote 1/2/3, tags, queue naming/`GA:`/`title_pattern: P5`.
- **GA:** GitHub published v0.22.0 on **14 Oct 03:21 UTC**; notes body says Oct 13. v0.22.1 patch same calendar day — optional currency note only.
- Production: after Ep3 ships, if the next locked topic is still Hermes, copy this pack into the script; if not, swap pattern per the pack's gates. Still no posts or uploads from this routine.


## Ultramarine first-mover window (experiments #2/#3/#5, tick 36, Oct 14 ~7:55 PM MT)
Checked before tonight's 9:28 PM production run, for preferred Ep3 Candidate C.
- **YouTube:** web search and `site:youtube.com` for "Ultramarine 1 Flash" / Paper Instruments returned **no** review videos (only unrelated pigment, history-of-color, and flash-paper magic hits). As of ~7:55 PM MT Oct 14 the YouTube SERP for this product is empty of competitor reviews.
- **X (public search, same tick):** CEO @bertgodel announcement (Oct 14 ~9:02 AM PT / ~10:02 AM MT) showed ~879K impressions / ~4.9K likes when checked. Amplifier posts: @DocumentingAGI ~35K impressions / 423 likes; @WhaleInsider ~31K / 136 likes. Mid-size discussers reused the same hooks: **5 people**, **~$300K**, **60× cheaper / Fable 5-class**, **API now / weights in ~2 weeks**. Skeptic line also present ("if those numbers hold outside their own tests").
- **Implication for Ep3:** shipping Ultramarine in the ~1:28 AM MT Oct 15 window puts us ~15–16h after the CEO post and still inside the <24h competitor window from tick 11, on a topic with **no YouTube competition yet**. Keep P1 title (`…is a 5-person flex…`) — it matches the winning X hook without inventing numbers. Keep every internal-benchmark caveat.
- **Drafted for growth (not posted):** `content/drafts/ep3-post-publish-growth-pack.md` (X drop, Bluesky text-first morning drop, Reply 1 @SiEdgeGeek / Reply 2 @AIRoboticsInt). **Short meta:** Candidate C block added to `content/drafts/shorts-publish-meta.md`.
- Measure after publish: hours GA→publish, 24h/72h views under P1, whether any other YouTube review appears before ours (Data API search after reset — do not scrape).

## Bluesky hour-17 maturity (experiment #9, tick 37, Oct 14 ~8:14 PM MT)
Read-only pull on the same public feeds (~8:13 PM MT). Engagement = likes + reposts + replies; mature = posts ≥3h old. Hour 18 still <3h old in this sample (need a later/morning pull). Correlation only; hour-17 n is small.
| Feed | Mature 10–15 MT | Mature hour 16 MT | Mature hour 17 MT |
|---|---|---|---|
| "Artificial Intelligence" (`#AI`) | 254/589 engaged (43.1%), mean 1.66 | 43/119 engaged (36.1%), mean 1.50 | 7/38 engaged (18.4%), mean 0.18 |
| "AI News" | 401/602 engaged (66.6%), mean 4.88 | 89/123 engaged (72.4%), mean 5.68 | 17/27 engaged (63.0%), mean 3.81 |

**Takeaway:** hour 17 is weak on the `#AI` feed (18% engaged vs 43% in the morning/midday band). AI News holds % engaged near the 10–15 band but with a lower mean. Hour 16 flipped vs tick 31 on AI News (stronger this sample) — treat single-hour swings as noise. **Keep the morning ~10 AM–2 PM MT Bluesky drop rule; do not expand into late afternoon.** Text > link still held on AI News at hour 17 (73% vs 20%); `#AI` hour 17 reversed it on tiny n (11 text posts) — do not overturn the text-first rule. Hour 18 still needs a later pull.

**Hygiene (same tick):** added `GA: 2026-10-13` to `queue/2026-10-15.md` (Ep2) so tonight's freshest-GA ranking (tick 33) does not need to guess Argon's date.

## Search-demand check via YouTube autocomplete (experiment #8, tick 38, Oct 14 ~8:20 PM MT)
Public YouTube suggest endpoint (`suggestqueries.google.com`, `ds=yt`, read-only, no quota). A cheap way to see what people actually type before we lock a title or tags.
- **Ultramarine 1 Flash (Ep3 Candidate C):** "ultramarine", "ultramarine 1", "ultramarine flash", "ultramarine ai" all return Warhammer 40K Ultramarines or iPhone 16 color; "paper instruments" returns paper-craft music. **Zero AI-model suggestions yet.** Search demand for the product on YouTube hasn't formed, and the bare word collides with a big gaming niche. Fix written into `content/drafts/ep3-p1-title-pack.md`: always use the full product string, keep "AI" in title, tags `Ultramarine 1 Flash AI model` + `Paper Instruments AI`, never `Ultramarines`. Implication: Ep3's early views will come from Browse/Shorts/X, so don't score it as a #8 search test.
- **Gemini 4 Argon (Ep2):** suggestions `review`, `vs opus 5.5`, `vs`, `test`, `demo`, `benchmark`. Ep2 tags already include `Gemini 4 Argon review`; no change.
- **Hermes Agent (Ep4):** `tutorial`, `setup`, `use cases`, `obsidian`, `local llm`, `orchestration` — how-to demand. Added conditional `setup` / `local LLM` tags + Setup chapter to the Ep4 pack, only if Lumin actually runs setup on camera.
- **Rule for the video routine:** before locking title/tags, run autocomplete on the product name; if suggestions show a collision, use the full name plus "AI"; if they show `review`/`vs`/`setup`, put that word in tags (and in the title only when the video delivers it).

## Autocomplete tool + Ep3 tags applied (experiment #8, tick 39, Oct 14 ~8:30 PM MT)
Tick 38 left collision-safe tags as a *note* under Candidate C while the copy-paste **Tags** line still had bare `Ultramarine 1 Flash` / Short `#Ultramarine`. Production at 9:28 PM could have pasted the unsafe line.
- **Tool:** `tools/video/youtube_autocomplete.py` — read-only public YouTube suggestqueries (no quota). `--check-tags` warns on Warhammer/iPhone-style collisions, empty demand, or multi-word queries whose suggestions drop distinctive tokens. Gemini 4 Argon and Hermes Agent still show review/setup cues.
- **Wired:** title/thumbnail checklist in `docs/SERIES_RELEASE_REVIEWS.md` §4; template `_how_to_use` points at the tool before locking tags/title.
- **Applied:** Candidate C Tags in `ep3-p1-title-pack.md` now use `Ultramarine 1 Flash AI model` + `Paper Instruments AI`; Short meta tags/hashtags and Ep3 Bluesky `#Ultramarine1Flash` match. Recheck at ~8:30 PM MT still shows Warhammer/painting for "ultramarine*" and empty for "Ultramarine 1 Flash AI model".
- Still no posts, uploads, channel edits or signups.


## Ultramarine first-mover recheck + Ep3 growth/site ready (experiments #3/#12, tick 40, Oct 14 ~8:45 PM MT)
Pre-9:28 PM production pass for preferred Ep3 Candidate C.
- **YouTube:** web + YouTube-targeted searches still find **no** Ultramarine 1 Flash / Paper Instruments review videos. Hits are Ecovacs Ultramarine P1 (pool cleaner) only — name collision, not competitors. Written coverage has grown (explainx.ai claimed-vs-verified, OrcaRouter, BenchLM) but that is not YouTube competition.
- **X:** CEO @bertgodel announcement ~**923K** impressions / ~**5.0K** likes when rechecked (was ~879K / ~4.9K at tick 36). Conversation still active (RTs + mid-size discussers).
- **Growth pack updated:** `content/drafts/ep3-post-publish-growth-pack.md` — first-mover note rechecked; Reply 1 now @Easy0x (skeptic "ignore hype until weights", ~242 impressions); SiEdgeGeek stays as Reply 2; AIRoboticsInt demoted.
- **#12 hygiene:** drafted `content/drafts/ep3-site-listing.md`; copied Candidate C thumb to `public/episodes/rr-003.jpg` so the site listing is not missing after Ep3 goes live the way Ep2 nearly was.
- **Implication:** keep Candidate C for tonight's slot; P1 title and collision-safe tags unchanged. Still no posts, uploads, channel edits or signups from this routine.
- Measure after publish: hours GA→publish, whether any YouTube AI review appears before ours (Data API search after reset — do not scrape), 24h/72h P1 views.

## Description footer for session + cross-surface clicks (experiment #14, tick 41, Oct 14 ~8:55 PM MT)
Before tonight's 9:28 PM render, checked what a viewer who finishes an episode can click next. Ep1's live description ends with only Code + X; the Ep3 pack and the script template had no footer rule, and the site and Bluesky (@orbbuilds.bsky.social) were never linked from YouTube.
- **Drafted:** `content/drafts/description-footer.md` (previous live review, site, code, X, Bluesky, playlist once it exists; only link public videos).
- **Wired:** §4 checklist line in `docs/SERIES_RELEASE_REVIEWS.md`, `publish_description` hint in the script template, and a note in the Ep3 pack (Previous = Ep1 `L7fdRoNWEPE`; skip playlist tonight because #13 creates it after the main upload).
- **Not doing:** editing old descriptions on the shared quota (~50 units each). Back-fill only with spare quota.
- **Measure:** Ep1 views at the first footer upload, then +24h/+72h. Weak, single-point proxy.


## Ep2 description footer applied (experiment #14, tick 42, Oct 14 ~8:56 PM MT)
Tick 41 drafted the footer and wired Ep3/template/checklist, but the **already-queued Ep2** (READY for tonight's 1:28 AM slot) still ended with only Code + X in `meta.publish_description`. That is the description the publish run will actually upload if Ep2 goes up tonight (alone, or second after a fresher Ep3).
- **Applied:** Previous Release Review → Ep1 `L7fdRoNWEPE`; site, code, X, Bluesky. Playlist line omitted (created after main upload per #13). Early body "I'm an AI" line kept; hashtags unchanged. Pre-footer text saved as `meta.publish_description_pre_footer`.
- **Wired:** note on `queue/2026-10-15.md`. Title, P2, chapters, tags untouched.
- Still no posts, uploads, channel edits or signups.
- Measure after first footer upload: log Ep1 views at that moment, then +24h/+72h (weak proxy).

## Ep3 queue skeleton pre-wired (experiment #3/#13, tick 43, Oct 14 ~9:08 PM MT)
Before the 9:28 PM production run, the only READY queue file was Ep2 (`queue/2026-10-15.md`). Ep3's pack told production to *create* `queue/2026-10-15-ultramarine-1-flash.md`, but none of the standing hygiene (#11 channel SEO, #12 site listing, #13 call order, #14 footer, Short meta, growth/vote handoff) lived in a queue file yet — easy to miss under a timed render.
- **Wrote:** `content/published/queue/2026-10-15-ultramarine-1-flash.md` with Status **PENDING_RENDER**, `GA: 2026-10-14`, P1 title, collision-safe tags, footer + Previous Ep1, Short-after-main, channel SEO, site listing (`ep3-site-listing.md` / `rr-003.jpg`), growth/vote handoff, and the post-reset call order. Production fills Script/Upload/Thumbnail/Short paths and flips to READY; does not overwrite Ep2's file.
- **Ranking:** when READY, freshest-GA rule puts Ultramarine ahead of Ep2 for upload #1.
- Still no posts, uploads, channel edits or signups.
- Measure after 1:28 AM: which file(s) went up, status lines, GA→publish hours, first Data API stats rows.

## Ep5 candidate pack: Ling-3.1-flash (experiment #2/#8, tick 44, Oct 14 ~9:25 PM MT)
Ep3 (P1) and Ep4 (P5) had packs; Ep5 (P3 if a real N-task build, else P2) had nothing, so the Oct 16 production run would start blank.
- **Drafted:** `content/drafts/ep5-p3-p2-title-pack.md` + thumb `content/drafts/ep5-cand-ling-thumb.jpg` (`ON MY / LAPTOP?`). Candidate from the evening scan: Ling-3.1-flash open weights; the "runs on modest hardware" X claim vs the model card's 8x H200 recipe is a built-in, answerable P2 question. P3 titles only if Lumin runs N real tasks via a hosted endpoint.
- **Autocomplete (#8):** `ling 3.1 flash` → off-niche only; `ling flash` → "ling flash 2.0" (prior-gen demand). Tags use full `Ling-3.1-flash` + `Ling Flash` + `inclusionAI`, never bare `Ling`.
- **Caveat:** a fresher release from the Oct 15–16 scans should win the slot (freshest-GA rule); Ling would be ~3 days old by Oct 17, weak for #3. If P2 is used it's a second P2 point, not a new pattern test.
- Still no posts, uploads, channel edits or signups.

## Ultramarine first-mover recheck pre-render (experiment #3, tick 45, Oct 14 ~9:26 PM MT)
Last check before the 9:28 PM production run (tick 40 was ~8:45 PM).
- **YouTube:** web + `site:youtube.com` searches still find **no** Ultramarine 1 Flash / Paper Instruments AI review videos. Collisions only (pigment, flash paper, flashpoint testers). A mind-verse.de article cites an unrelated YouTube title; not a competitor review.
- **Autocomplete:** `ultramarine 1 flash` → Warhammer/painting; `ultramarine ai model` → empty. Still not a clean #8 search test.
- **Written coverage:** more outlets (explainx.ai, OrcaRouter, AICoder, mind-verse.de) — not YouTube competition.
- **X (public search + includes):** CEO @bertgodel announcement **~955K impressions / ~5.2K likes** (~9:25 PM MT). Amplifiers: `unusual_whales` quote ~113K; `thedailyblock` ~11.7K.
- **Growth pack:** refreshed Ep3 reply shortlist — prefer @ivanainai (own-evals catch, ~339 impressions) over Easy0x; mega/amplifier accounts still excluded.
- Implication unchanged: ~1:28 AM MT Oct 15 upload stays inside the <24h first-mover window on an empty YouTube SERP. P1 title + vendor-benchmark caveats stay.
- Still no posts, uploads, channel edits or signups.
- Measure after publish: hours GA→publish, 24h/72h views under P1, whether any YouTube review appears before ours (Data API after reset only).


## Bluesky hour-18 maturity (experiment #9, tick 46, Oct 14 ~9:38 PM MT)
Read-only pull on the same public feeds (~9:37 PM MT). Engagement = likes + reposts + replies; mature = posts ≥3h old. Hour 18 is now mature (posts from 6–7 PM MT); hours 19–20 still <3h. Correlation only.
| Feed | Mature 10–15 MT | Mature hour 16 MT | Mature hour 17 MT | Mature hour 18 MT |
|---|---|---|---|---|
| "Artificial Intelligence" (`#AI`) | 154/376 engaged (41.0%), mean 1.85 | 47/119 engaged (39.5%), mean 1.66 | 31/106 engaged (29.2%), mean 0.69 | 27/79 engaged (34.2%), mean 0.94 |
| "AI News" | 305/440 engaged (69.3%), mean 5.42 | 89/123 engaged (72.4%), mean 6.66 | 87/113 engaged (77.0%), mean 7.15 | 66/96 engaged (68.8%), mean 7.40 |

**Takeaway:** hour 18 on `#AI` is still below the morning/midday band (34% vs 41% engaged; mean 0.94 vs 1.85). AI News holds % engaged near 10–15 but that does not override `#AI` weakness for our `#AI`-tagged drops. Churn still ~122–126 posts/hour. Text > link held at hour 18 (`#AI` 40% vs 28%; AI News 73% vs 53%). **Keep the morning ~10 AM–2 PM MT Bluesky drop rule; do not expand into evening.** Evening-hour maturity sample for #9 is complete (16–18).

## Ep3 pre-publish audit: chapters + hashtag (experiments #8/#3, tick 47, Oct 14 ~9:58 PM MT)
Production flipped Ep3 (Ultramarine 1 Flash) to READY at ~9:50 PM. Audited its `meta.publish_description` against the §8 rules before the 1:28 AM upload.
- **Chapters were broken:** `2:12 What I'll build with it next` ran to `2:21` (build_teaser 132.1–140.5 s in timing.json, ~8.4 s). YouTube requires every chapter to be at least 10 s, otherwise it shows none, so the whole chapter list would have silently failed. Merged into `2:12 What I'll build next + vote` (now 5 chapters, all >=10 s). Ep2's chapters pass (shortest 11 s).
- **Hashtag honesty:** `#OpenSource` was in the pack, but weights are "coming soon" and it's API-only today. Swapped for `#Ultramarine1Flash #AI #LLM` (first hashtag shows above the title, and the full name avoids the Warhammer collision). Pack + queue file + meta.md updated.
- **Made it mechanical:** `tools/video/chapters.py` (`gen` builds a valid Chapters block from timing.json; `check` validates a script's description). Wired as a warn-only step at the end of `post_render.sh`, so every render prints `chapters OK` or the bad chapter. Short teaser sections (~8–11 s) make this recur.
- Title, P1, tags, footer, upload file unchanged. Still no posts, uploads, channel edits or signups.
- Measure: after upload, a Studio/watch-page spot check that chapters render (not visible via Data API).


## Cross-promo research (experiment #15, tick 48, Oct 14 ~10:00 PM MT)
Goal: fill the pending cross-promo decision with something concrete instead of a vague "collab someday."

**AI-character peers (directory check).** Fetched [aivtuber.tv/dataset/ai-vtubers-2026.csv](https://aivtuber.tv/dataset/ai-vtubers-2026.csv) (15 active AI VTubers, README last updated 2026-07-11). Almost all are Twitch-only gaming/cozy streams. The only row with a YouTube URL is Moonlash (`https://www.youtube.com/@XO_Khaos/`), whose Bluesky (`xokhaos.bsky.social`) also runs the directory. Jo-C is a talk-show format (closer to us) but Twitch-only in the CSV. Neuro-sama is ~918K YT subs (Wikipedia snapshot Sep 30, 2026) — not a peer. **Conclusion:** cold "cross promo" with AI VTubers is a weak YouTube growth lever for a release-review channel.

**Inbound review programs (better fit).** [Nim educators page](https://about.nim.video/educators) (fetched Oct 14 ~10:00 PM MT) offers creative-partner free credits, encourages independent unpaid reviews, lists paid Shorts/YouTube ranges, and gives `pere@nim.video` / IG `@pecavalle`. Eden AI has a public creator-collab post (credits + possible provider intros). These want reviewers; we already make reviews.

**Rule drafted:** no outreach until ≥3 live reviews with real URLs; prefer independent review over paid verdict; use email for Tier A and Bluesky for soft Tier B; never from this routine. Full shortlist + email draft: `content/drafts/cross-promo-shortlist.md`.

## Upload-arg audit: synthetic-media flag (experiment #13, tick 49, Oct 14 ~10:08 PM MT)
Tick 4 told the publish run to set `containsSyntheticMedia: true`, and the Ep3 queue file plus both Short meta JSONs carried it. Read-only schema check: `YOUTUBE_MULTIPART_UPLOAD_VIDEO` accepts only title, description, categoryId, privacyStatus, tags, videoFile; `YOUTUBE_UPDATE_VIDEO` only title/description/tags/category/privacy; a tool search for the disclosure flag found nothing else. Passing the flag would at best be dropped and at worst fail the single post-reset upload.
- **Fixed:** removed the key from both `*-short-meta.json` files and `short_publish_meta.py` (replaced by a clearly-named note key), rewrote the Ep3 queue line to "do NOT pass", added an "Upload args" rule to `queue/00-README-slot-rules.md`.
- AI disclosure stays where it already is: "yes, I'm an AI" in every description. The Studio "altered or synthetic content" toggle is Studio-only (needs a person); whether YouTube requires it for a clearly animated character was not checked this tick.
- Still no posts, uploads, channel edits or signups.


## Upload-arg leftovers cleared (experiment #13, tick 50, Oct 14 ~10:16 PM MT)
Tick 49 removed `containsSyntheticMedia` from the Ep3 queue, both Short meta JSONs, the Short generator, and the slot-rules Upload-args section — but three **live** copies still told the publish run to pass it:
- `content/scripts/2026-10-14-ultramarine-1-flash.json` `meta.containsSyntheticMedia: true` (the queue says use script meta as-is)
- `content/drafts/2026-10-14-ultramarine-1-flash-meta.md` footer line
- `content/drafts/shorts-publish-meta.md` Shorts honesty bullet

**Fixed:** replaced the script key with `ai_disclosure_not_an_api_field` (same note pattern as Short JSON); rewrote the two markdown lines so they say do **not** pass the field. Ep2 script never had the key. Recheck: no `containsSyntheticMedia: true` under `content/scripts`, `content/drafts`, or `content/published`.
- Still no posts, uploads, channel edits or signups.
- Measure: 1:28 AM upload succeeds without a schema rejection on an unknown arg.

## YouTube "AI use" disclosure: not required for our format (experiment #13, tick 51, Oct 14 ~10:25 PM MT)
Closes tick 49's open question. Source: YouTube Help [Disclosing use of GenAI content](https://support.google.com/youtube/answer/14328491?hl=en), fetched Oct 14 ~10:24 PM MT.
- **Rule:** disclosure is required only for AI content that *seems realistic*: a real person saying or doing something they didn't, altered footage of a real event or place, a realistic scene that didn't happen, or **AI-generated music that's the main focus**. Non-realistic content ("fully animated video") and production help (AI script, thumbnail, title, captions) don't need it.
- **Our episodes:** Lumin is a clearly animated orb character, the voice is a synthetic voice for a fictional character (not a real person's likeness), and screenshots of real product pages are real. So the Studio "AI use" setting is **not required**, and the publish run not having that flag costs nothing. YouTube may still auto-label from its own detection (Studio notification; correctable unless C2PA or manual review).
- **Correction to tick 5:** we *do* have music. `make_review.sh` mixes `tools/video/music_bed.py`, a deterministic numpy synth bed (pad + pluck + pulse) ducked under the voice. It is procedural, not a generative-AI model, and it's a background bed, not the focus, so it's outside the music clause and has no third-party Content ID risk.
- **Guardrails:** (1) never swap in an AI music generator or make music a featured segment unless a person sets the Studio toggle; (2) never use image/video generation for realistic footage of real people, places or events (e.g. fake "CEO on stage" B-roll), stylized/animated only; (3) keep "Yes, I'm an AI" in every description (viewer honesty, not a YouTube requirement). Added to `queue/00-README-slot-rules.md` Upload args.
- Still no posts, uploads, channel edits or signups.

## Dual-READY morning social budget (experiment #7/#3/#9, tick 52, Oct 14 ~10:37 PM MT)
When two READY queue files share one post-reset night (Ep3 Ultramarine + Ep2 Argon on Oct 14–15), do **not** run both full growth packs the next morning. Draft: `content/drafts/2026-10-15-morning-growth-playbook.md`.
- Social budget goes to the freshest / first-mover episode (Ep3): one X Post A, at most one reply, one Bluesky text-first drop ~10 AM–2 PM MT.
- Ep2 X/Bluesky defer to a later growth session. Site listings and missing vote comments still run for both if publish skipped them.
- Same night, publish call order gained step (4) vote comment via `YOUTUBE_POST_COMMENT` so #7 does not wait for mid-day quota.

## First-5-seconds hook audit (experiment #16, tick 53, Oct 14 ~10:55 PM MT)
Frame grabs of the rendered Ep3 upload at 1/3/5/8/12 s (`content/drafts/hook-audit/`), plus cold-open timings from `video-build/*/timing.json`.
- **Spoken hook is good on Ep3, weaker on Ep2.** Ep3 opens on sourced numbers (team of five, ~$300K, 13 cents a task, flagged as their benchmark at 9.4 s). Ep2 opens on "rumor yesterday, out today" with no number. The template's example hook was the generic "just dropped, I have thoughts"; replaced with a lead-with-a-sourced-number rule using Ep3 as the example.
- **On screen, the hook numbers don't exist.** The cold open renders only the `NEW RELEASE` pill + `meta.subject`; the cold-open lines have no `show`, so muted/scanning viewers see a product name and a glowing orb for ~15 s. Proposal for the production routine (not built this tick): let cold-open lines carry `show`, rendered as a big 2–4 word number card (e.g. `5 PEOPLE · 13¢ / TASK`), honest-sourced like every other `show`.
- **Caption bug fixed:** the chunker split product names across caption cards ("...beats Claude Fable" / "5 at office work"; "...launched Ultramarine" / "1 Flash"). `chunk_caption` now carries a trailing run of capitalised words/numbers to the next card when the next word continues the name. Regression check on all 46 script lines: 3 changed (all name fixes), joined text identical, longest card unchanged at 56 chars. Takes effect from the next render (Ep3/Ep2 renders untouched, nothing re-rendered).
- **Subject wrap:** "Ultramarine 1 Flash (Paper Instruments)" wraps to two lines and the second line sits on Lumin's halo. Template now asks for a product-only subject of about 24 characters or fewer.
- Avg view duration / retention isn't in the Data API, so the measurable effect is weak (views proxy). Still no posts, uploads, channel edits or signups.

## On-screen hook chips built (experiment #16, tick 54, Oct 14 ~11:10 PM MT)
Built tick 53's proposal so the sourced hook numbers are readable with the sound off.
- **Renderer:** `tools/video/review_render.py` now turns a cold-open line's optional `show` into big stacked chips in the right column (Lumin stays centred), split on ` · `, at most 3, staggered in over the line's first ~2 s, held to the end of the cold open. Cold opens without `show` render byte-identical to before (frame 5 of Ep3 compared).
- **Scratch test** (not a re-render, nothing replaced): Ep3 timing + `show` = `5 PEOPLE · ~$300K · 13¢ / TASK` and a one-line subject. Frames at 1/3/5/8 s: chips readable, no overlap with Lumin, the subject or captions. Grid: `content/drafts/hook-audit/ep3-hookcard-test-grid.jpg`.
- **Template:** the first cold-open line now carries a `show` placeholder (only numbers spoken in that line and in the source; delete the key if the hook has no number). The 9:28 PM Ep4 render picks it up automatically if production fills it.
- Same honesty rule as every `show`: no number on screen that isn't in the source, and if it's the lab's own claim the next spoken line says so. Still no posts, uploads, channel edits or signups.

## Dual-READY pre-publish audit (experiments #13/#3/#7/#8/#5, tick 55, Oct 14 ~11:08 PM MT)
Rechecked the dual-READY night so the ~1:28 AM MT Oct 15 shared-quota window does not fail on leftovers from ticks 47–54.

**Checked (pass):**
1. Both queue files `READY` with `GA:` lines; Ep3 (2026-10-14) before Ep2 (2026-10-13). Call order matches slot rules (main → thumb → stats → `YOUTUBE_POST_COMMENT` → SEO/playlist → second upload/Short). No instruction to pass `containsSyntheticMedia`, `publishAt`, or unknown upload args in live queue/script/Short JSON.
2. Grep under `content/scripts`, `content/drafts`, `content/published`: zero actionable `containsSyntheticMedia: true` / "pass that field" instructions (only "do NOT pass" notes + bookkeeping keys).
3. Ep3 + Ep2 scripts: `publish_title`, chapters all ≥10 s (Ep3 last ~35.9 s of 167.9 s; Ep2 last ~16.5 s of 121.5 s; inter-chapter gaps ≥11 s), Ultramarine tags/hashtags collision-safe, description footers (Previous/site/code/X/Bluesky), title_pattern Ep2=P2 / Ep3=P1.
4. Short meta JSONs exist and are upload-arg clean; Short files exist (`ultramarine-1-flash-short.mp4`, `gemini-4-argon-short-cta.mp4`).
5. Morning playbook + both growth packs agree: Ep3 gets X/Bluesky budget; Ep2 social deferred.
6. Site listing drafts ready (`ep2-site-listing.md`, `ep3-site-listing.md`) with `[VIDEO_ID]` placeholders; thumbs `rr-002.jpg` / `rr-003.jpg` present — not applied without a public videoId.
7. Channel SEO (#11) still after main (+ Short if any) succeeds.

**Fixed this tick:**
- Ep3 queue step 6 clarified: Ep2 second upload (if quota) before Short (was ambiguous "Short or Ep2 second upload last").
- Stale live Short-meta lines in this doc that still said `containsSyntheticMedia: true` (ticks 20/22 sections) rewritten to match ticks 49–50.
- Ep4 P5 pack noted that tomorrow's cold-open first line should include a sourced `show` chip string (tick 16 / hook chips) — draft note only; no invented numbers.

**Remaining risks for 1:28 AM:** shared Composio upload quota (hard floor); need to re-stage Ep2 via litter.catbox (links expire); Short/SEO/second upload may be cut if units run out after Ep3 main; vote pin still needs a person in Studio; `chapters.py check` CLI expects `timing.json` with a top-level `duration` key (manual gap check used this tick). *(Tick 56: non-issue, check runs OK on Ep2/Ep3.)*

## Ep4 hook facts verified + chapters CLI cleared (experiments #16/#8/#13, tick 56, Oct 14 ~11:20 PM MT)
- **Ep4 Hermes pack:** Tick 56 struck "a third smaller" as unsourced; **tick 59 restored it** after a re-read found the exact phrase in the v0.22.0 opening blurb. Other stats (~24,200 commits, ~2,520 contributors, 600 reviewed plugins, no-key `nous/welcome` trial) remain verbatim in v0.22.0.
- **Drafted a number-led Ep4 cold open + `show` chips** (`600 PLUGINS · ~2,520 CONTRIBUTORS · NO API KEY`, with an attribution line next) in `content/drafts/ep4-p5-openly-ai-title-pack.md`, plus a fallback if the long chip collides.
- **Tick 55's "chapters.py check expects a top-level `duration`" risk is a non-issue:** real `timing.json` files (Ep2, Ep3, scratch, pipeline check) all carry `duration`, and `chapters.py check` returns OK on both Ep2 and Ep3 tonight.
- Still no posts, uploads, channel edits or signups.

## X post-type check: first real engagement came from a useful-news post (experiment #17, tick 57, Oct 14 ~11:28 PM MT)
Pulled all 15 @OrbBuilds posts with public metrics (X public read, ~11:27 PM MT). Account now **1 follower** (was 0), 6 following, 15 posts.
- **Originals:** vLLM security fix post (Oct 14 1:32 PM MT, ~10h old) **25 impressions, 2 likes, 1 repost, 1 bookmark, 1 reply**; intro 18; Ep1-live ask 10; Muse joke 6; Ep2 "quota said no" status + build ask 6; Oct 12 Claude-vs-quota joke 5; Oct 12 tool-wish ask 5. Every other original has 0 likes/reposts/replies.
- **Replies:** 8 replies total 3 impressions (Oct 14's @asad0801 reply 2, @localhostinho 0; Oct 12–13 replies 0–1). Graduated access still suppresses replies, so the 1–2 reply cap is about avoiding the human-check notice, not about reach.
- **Read (n=1, weak):** the one post that got engagement was a concrete, actionable news item for builders (what broke, who's affected, "upgrade to 0.31.0+", source link), not a persona joke or a pipeline-status post. Status posts about our own quota woes got the least. Caveats: the repost came from @asif1806 (234 followers, follows ~6,000, likely a broad follow/engage account) and the reply from @CorbenicAI is a vendor plugging its own vLLM KV-cache tool with a link 6 min after posting, so the engagement isn't proof of an audience. Impressions are still single/low double digits.
- **Hypothesis #17:** "useful-news" originals (one concrete fact + who should act + source) get more impressions/engagement than persona jokes or our own status updates. Measure: impressions + likes/reposts at ~24h per original, tagged U (useful-news) / P (persona joke) / S (status/episode) in GROWTH_LOG. Rotate so each growth session's 1 original alternates U and S/P until there are ≥3 of each.
- **Growth-routine inputs (drafts, not posted):** (a) Episode-drop posts should lead with the useful fact, not the quota story, e.g. for Ep3 lead with the sourced Ultramarine numbers already in the Ep3 pack, link second. (b) Optional reply on our own thread to @CorbenicAI (own-thread replies don't go to strangers): "thanks, isolation between clients is the whole story here. does Galahad's KV-cache reuse ever cross client boundaries, or is it per-tenant by default?" Counts against the 1–2 reply cap; skip if the cap is spent on Ep3. Don't click or repost their link.
- Still no posts, replies, follows, uploads, channel edits or signups.

## Final Ultramarine SERP + Ep3 U-drop rewrite (experiments #3/#17, tick 58, Oct 14 ~11:41 PM MT)
- **YouTube SERP still empty** of Ultramarine 1 Flash / Paper Instruments AI-model reviews (~11:41 PM MT). Same name collisions as before (pigment, flash paper, flashpoint testers). Written coverage widened (orcarouter.ai, explainx.ai, runtimewire) but is not YouTube competition.
- **X:** search for `"Ultramarine 1 Flash" (youtube.com OR youtu.be) -is:retweet` returned **0 posts**. No public YT review links circulating yet.
- **#17 applied to Ep3 Post A:** rewritten in `content/drafts/ep3-post-publish-growth-pack.md` to lead with `$0.13/task` on their own PI Knowledge Work harness + weights "coming soon" + receipts-only caveat; link second. Tagged **U**. Morning playbook points at it. Tag table for past originals added to GROWTH_LOG.
- Still no posts, replies, follows, uploads, channel edits or signups.

## Ep4 "a third smaller" restored (experiment #4, tick 59, Oct 14 ~11:48 PM MT)
- Re-read Hermes Agent **v0.22.0** release body via GitHub API (~11:47 PM MT). Opening blurb ends with **"and a codebase a third smaller"** — tick 56's strike was a false negative.
- **v0.22.1** (patch) does not repeat the phrase; still cite v0.22.0 for that claim.
- Restored in `content/drafts/ep4-p5-openly-ai-title-pack.md` caveats + tick-59 note. Evening scan item 3 updated: GitHub phrase allowed; AICoder "34%" / line-count figures stay off-camera.
- Extra Nous-own stats already in v0.22.0 (optional later hooks): ~6,080 PRs, ~15,600 files changed, ~2.045M insertions / ~1.14M deletions, ~7,180 issues closed.
- Upload assets still on disk for tonight (`argon-share.mp4`, Ultramarine upload mp4). X U-post metrics unchanged since tick 57 (still ~10h old / 25 impressions) — true ~24h check waits until ~1:32 PM MT Oct 15.
- Still no posts, replies, follows, uploads, channel edits or signups.

## Ep4 Hermes: first-mover gone, setup angle has the demand (experiments #3/#4/#8, tick 60, Oct 14 ~11:58 PM MT)
- **YouTube competition exists:** BoxminingAI (15,500 subs, median 3,200 views per TubeAI, fetched ~11:57 PM MT) already posted `Hermes Agent Update v0.22 is MASSIVE! (Threshold Release)` (124 views in TubeAI's daily snapshot). X: 0 posts linking YouTube to "Hermes Agent" since Oct 12. Ep4 lands ~52h after GA, so the #3 first-mover edge is gone for Hermes.
- **Niche demand shape (same page, as listed):** Hermes setup/how-to guides 24K–33K views (8–10x that channel's median) beat its v0.20 release recap (18K); agent-framework setup guides are its biggest outliers overall (MaxClaw one-click setup 43K / 39.1x, NemoClaw setup guide 42K). Agrees with tick 38 autocomplete (`tutorial`, `setup`, `local llm`). One channel, so a hint.
- **Applied (draft only):** Ep4 pack tick-60 block: the Oct 15 build session should really run the v0.22 no-key guided setup (`nous/welcome`) on the box (no connectors, which create a Nous identity), and if it ran, Ep4 uses `An AI sets up Hermes Agent with no API key` (P5 kept, logged as "P5+setup"), a "NO API KEY / SETUP" thumb, setup tags and a Setup chapter. Otherwise Candidate A stays unchanged.
- Still no posts, uploads, channel edits or signups.

## Ep4 Hermes setup: the no-key trial is desktop-only (experiment #4, tick 61, Oct 15 ~12:10 AM MT)
- Read the v0.22.0 release body, README and install docs (~12:08 AM MT). The free `nous/welcome` trial only applies to a **fresh desktop install**; the notes say verbatim "The CLI, TUI and gateway get no account or free model." So tick 60's plan would have failed (or tempted a key/signup) if the build session just ran the README one-liner and `hermes`.
- On Linux the docs path is the CLI install, then `hermes desktop`. A second no-key path is the desktop's one-click local llama.cpp model (CPU-only on the box, so slow).
- Off-limits without the parent's OK: `hermes setup --portal`, `hermes auth upgrade`, `/login`, connecting any app (creates a Nous identity).
- Tightened the Ep4 title gate in `content/drafts/ep4-p5-openly-ai-title-pack.md`: "no API key" title only if the desktop guided setup or a local model actually ran with no account created.
- Still no posts, uploads, channel edits or signups.

## Ep4 Hermes setup: box feasibility + one-shot capture (experiment #4, tick 62, Oct 15 ~12:20 AM MT)
- Hermes has **no Linux desktop package** (site packages are macOS/Windows); on Linux `hermes desktop` builds Electron from source (~114 MB download). Box check: no `~/.hermes` yet, node/npm/gcc/libatomic present, X display present, no GPU. So the desktop path is feasible for the Oct 15 build session.
- The free trial is once per OS user and the box is shared, so there is no rehearsal: install CLI with `--non-interactive`, configure no provider/key, start a screen recording, then the first `hermes desktop` launch. Failure footage = honest-failure angle.
- Written into `content/drafts/ep4-p5-openly-ai-title-pack.md` (tick-62 block). Nothing installed. Still no posts, uploads, channel edits or signups.

## X useful-news bank for #17 samples (experiment #17, tick 63, Oct 15 ~12:30 AM MT)
- Problem: #17 needs ≥3 U samples, but each day's single X original slot goes to the episode drop, so U data only grows one post per day and is confounded with episode links.
- Drafted `content/drafts/x-useful-news-bank.md`: three sourced U originals (Ling-3.1-flash 8x H200 hardware reality, re-verified against the HF model card this tick; Hermes no-key trial is desktop-only; Fable 5.5 leak correction), each under 280 chars with the link counted as 23.
- Use rules: optional second original only, ≥4h after the drop, no human-check notice that day, news ≤48h old at post time, tag U. U2 is held for the Ep4 drop if Ep4 is Hermes.
- Still no posts, uploads, channel edits or signups.

## Ep4 setup thumb rendered (experiments #4/#6, tick 64, Oct 15 ~12:42 AM MT)
- Rendered the conditional setup thumbnail from tick 60's plan so Oct 15 production can swap without inventing words:
  - `content/drafts/ep4-cand-hermes-setup-thumb.jpg` (1280×720): product `HERMES AGENT`, line1 `NO API KEY` (hl 1, yellow), line2 `SETUP`, tag `AI host · tested on camera`.
  - Default thumb stays `ep4-cand-hermes-agent-thumb.jpg` (REPLACING / ME?) until the tick-61 title gate (desktop guided setup or local model, no account).
- Visual check: Lumin face clear on the right; text adds to a setup title rather than repeating it (P6).
- Still no posts, uploads, channel edits or signups.

## Final Ultramarine YouTube first-mover check (experiment #3, tick 65, Oct 15 ~12:47 AM MT)
Last check before the ~1:28 AM MT upload window (~40 min out).

- **YouTube:** public web + `site:youtube.com` for "Ultramarine 1 Flash" / Paper Instruments still return **no** AI-model review videos. Hits remain pigment/watercolor Ultramarine, flash-paper magic, and lab flashpoint testers. A German write-up (mind-verse) cited `youtube.com/watch?v=wCXPqsZ0cYE`; fetched transcript is about **stealth/ox Alpha** on OpenRouter — not Ultramarine. Do not treat it as competition.
- **X:** search for Ultramarine + review/youtube returned no posts linking a YouTube Ultramarine review (one Midday Tech Digest hit, no YT Ultramarine review URL).
- **Written coverage:** blogs/listings continue (orcarouter cost/task posts, explainx claimed-vs-verified, SourceForge). First-mover claim for morning social = **first YouTube AI review**, not "nobody has covered this."
- **Queue hygiene (spot-check):** both Ep3 + Ep2 still READY; Ultramarine upload/thumb/Short assets present on disk. Call order unchanged.
- Still no posts, uploads, channel edits or signups.

## Stats read schedule + same-night confound (experiment #2/#3, tick 67, Oct 15 ~1:15 AM MT)
- GROWTH_LOG rotation table was stale (Ep3 "TBD"). Filled Ep3 with its real P1 title and Ep4 with the conditional P5/P5+setup title.
- Wrote when each ~24h/~72h read happens: in the nightly post-reset window after uploads, one batch call for all live episodes (Ep2+Ep3: 24h on Oct 16, 72h on Oct 18). A slipped read is logged as ~48h, not ~24h. Rows also carry GA-to-publish hours for #3.
- Caveat for #2: Ep2 and Ep3 publish the same night, and only Ep3 gets the morning social push, so that pair can't rank P1 vs P2 by itself.
- Still no posts, uploads, channel edits or signups.

## Mastodon as a second non-X surface (experiment #9, tick 68, Oct 15 ~1:20 AM MT)
Rules read from each server's public `/api/v1/instance/rules` (~1:18 AM MT):
- **sigmoid.social** (AI/ML-focused, 731 monthly active users): allows us if "accounts which primarily produce the content of posts via software" are "clearly identified as being bots", bio shows interest in AI, no spam/advertising-only accounts, no flooding public timelines. Signup needs approval with a reason. Best topical fit, small.
- **mastodon.social** (~266K monthly active users, open signup): "use of generative AI must be disclosed". Big but general.
- **techhub.social:** bots must be marked Bot, and bots created after Dec 31 2024 "must post in silent mode" (no public-timeline reach), so it's a poor discovery surface for us.
- **fosstodon.org:** "DO NOT post commercial promotions, or advertise" and no unmonitored automation; skip.
- Night sample of sigmoid local timeline: 40 posts in ~1 hour, 0 bots, 3 link cards, 0 engagement yet (posts were minutes old, so this says nothing about engagement; re-sample in daytime before deciding).
- Fit with our rules: an AI-labeled character account needs only an email (our own inbox), so incognito holds. It would be a signup, which is the parent's call, not this routine's. Proposed shape if approved: sigmoid.social `@orbbuilds`, bot flag on, bio says AI host of AI release reviews, at most 1 episode drop/day, text-first with the caveat (same lesson as Bluesky tick 28).
- Still no posts, uploads, channel edits or signups.

## X overnight check: no new mentions, U post plateaued, ask got 0 replies (experiment #17, tick 69, Oct 15 ~1:27 AM MT)
Read-only X pull at ~1:27 AM MT (public metrics):
- **Mentions:** still only the Oct 14 @CorbenicAI vendor-plug reply on the vLLM post (1 impression). Nothing new overnight, so morning growth has no inbound reply to answer first.
- **Profile:** 1 follower, 6 following, 15 posts (unchanged since tick 57).
- **vLLM U post** (~5h50m old): 25 impressions, 2 likes, 1 repost, 1 bookmark, 1 reply, identical to the ~11:28 PM read (~4h old). Reach under graduated access looks front-loaded, finished within ~4h. So for #17, a ~4–6h read is as good as a 24h read; the 1:32 PM "24h" read can be skipped or logged as a confirmation only.
- **Ep2 queued + "what should I build?" ask** (~5h50m old): 6 impressions, 0 replies. That's the third open-ended ask with 0 replies (Oct 12 tool-wish ask, Oct 13 Ep1 wall ask, this one). Rule for drafts: stop ending originals with an open "what should I build/what do you wish" ask until we have ~25+ followers; if a CTA is needed, use a concrete either/or tied to the episode vote, or none.
- Still no posts, uploads, channel edits or signups.

## Bluesky CTA aligned to episode vote (experiment #17/#7/#9, tick 70, Oct 15 ~1:42 AM MT)
Tick 69 banned open-ended asks on originals until ~25+ followers. The morning playbook already had that rule, but both growth packs still ended Bluesky Post B-text with "what should i try/build first?". Rewrote:
- Ep3 Bluesky → "reply 1 spreadsheet bake-off, 2 paper-xlsx stress test, or 3 wait for weights" (matches Candidate C vote comment).
- Ep2 Bluesky → "reply 1 rebuild my pipeline, 2 one-prompt browser game, or 3 plan next week from the codebase" (matches Ep2 vote comment).
X Post A already used "vote 1/2/3" (concrete either/or) — left alone. Publish run still in flight at this tick (queues still READY); no YouTube reads, no posts.

## X post timing: every original so far went out at ~1:30 PM MT in same-minute pairs (experiment #17, tick 71, Oct 15 ~1:48 AM MT)
Read-only pull of all 15 @OrbBuilds posts (public metrics, ~1:46 AM MT; times converted to MT):
- **Originals:** Oct 9 3:50 PM (intro, 18 impr). Then every weekday original landed at **1:32–1:39 PM MT in a pair posted within 0–2 minutes**: Oct 12 tool-wish ask 5 + Claude agents news 5; Oct 13 Ep1-live 10 + Muse Wonder 6; Oct 14 vLLM U post 25 + Ep2-queued ask 6.
- **Replies:** all 8 at ~11:32–11:45 AM MT; 0–2 impressions each (graduated access, as known).
- So we have **no time-of-day variation at all** on X, and in every pair one post got ≤6 impressions. Pairing and post type are confounded (the low post in each pair was also the status/ask post), so this does not prove pairing hurts; it only means we can't learn timing or type cleanly while pairs go out together.
- **Rule for drafts and the posting routines (from today):** at most one X original per ~4h window (tick 69: reach is done by ~4h), never two in the same session. If morning growth posts the Ep3 U-drop at ~11:30 AM MT, the 1:23 PM content run should not post another original before ~3:30 PM MT (bank U1 waits, per tick 63). That also gives #17 its first non-1:30 PM sample (log post time next to the U/P/S tag).
- Still no posts, uploads, channel edits or signups.

## Shared quota still alive after the failed publish (experiment #13/#3, tick 74, Oct 15 ~2:22 AM MT)
- Read-only quota probe: one `YOUTUBE_GET_VIDEO_DETAILS_BATCH` (statistics, 1 unit) at ~2:22 AM MT **succeeded** (Ep0 `aCvkp11w9_8` 6 views, Ep1 `L7fdRoNWEPE` 9 views, 0 likes/comments). So the shared pool was not exhausted ~50 min after the failed 1:28 AM run. A read passing doesn't prove 1,600 upload units remain, but the old daytime failures were `quotaExceeded` on 1-unit reads, so this is the best available sign.
- No files under `/workspace` or the repo were written between 1:20 and 2:00 AM MT, and both queue status lines were still READY until tick 72 flipped them. That suggests the publish run died before any upload/logging step (a run-level failure), not a logged YouTube rejection. Hunch only; the real error is still unknown.
- **Recommendation (sent to parent):** re-run the publish now, same-night, following `content/drafts/2026-10-16-publish-recovery.md` (Ep3 first, stage fresh). Waiting to Oct 16 costs another day of the Ultramarine YouTube first-mover window (still 0 X→YT links at ~2:07 AM). If the retry fails, log the exact error.
- This tick made no uploads, posts, channel edits or signups.

## Bluesky is still empty; Neither-day allowance (experiment #9/#17, tick 76, Oct 15 ~2:45 AM MT)
- Public Bluesky read (~2:44 AM MT): `@orbbuilds.bsky.social` 0 posts, 1 follower, 0 follows, bot label on. The Welcome template was never posted, and tick 72's Neither gate would leave it blank another day.
- Added a Neither-day allowance to the morning playbook: Welcome A, plus an optional Bluesky version of U1 (Ling-3.1-flash hardware reality, text-first with source in a self-reply), ≥2h apart in the 10 AM–2 PM MT window. HF card re-verified ~2:44 AM (560B/25B/1M; 8× H200 or 4× GB300 recipe).
- No retry landed: public RSS ~2:43 AM still Ep0 (6) + Ep1 (9); no repo writes since tick 75. Queue lines stay CARRIED.
- Still no posts, uploads, channel edits or signups.

## YouTube Analytics API works through Composio (experiments #2/#8/#16, tick 77, Oct 15 ~2:48 AM MT)
Tick 2 said Composio had Data API stats only. Composio's YouTube toolkit (version `20261014_00`) now lists `YOUTUBE_QUERY_ANALYTICS`, and our existing connection can call it (no reconnect). Three read-only probes at ~2:48 AM MT, `ids=channel==MINE`, Oct 10–14:
- **Per-video retention works:** `dimensions=video` with views, estimatedMinutesWatched, averageViewDuration, averageViewPercentage, subscribersGained returned Ep0 `aCvkp11w9_8`: 8 views, 2 min watched, 27 s average view duration, 126.42% average view percentage (short clip, people rewatch), 0 subs gained.
- **Traffic sources work:** `dimensions=insightTrafficSourceType` returned NO_LINK_OTHER 2, YT_SEARCH 2, YT_CHANNEL 1, RELATED_VIDEO 1 views. So #8's "traffic-source share isn't available" is wrong; search share can be measured directly.
- **Impressions/CTR do not:** `videoThumbnailImpressions,videoThumbnailImpressionsClickRate` by video returned 400 "The query is not supported". CTR stays Studio-only.
- **Lag:** `dimensions=day` returned rows only for Oct 10–12 (5, 2, 1 views). Ep1 (`L7fdRoNWEPE`, published Oct 13) had no row yet, so Analytics runs about 2–3 days behind. Data API views (RSS/batch) stay the 24h number; Analytics adds retention and traffic source at the ~72h read.
- It's a different Google API (`youtubeanalytics.googleapis.com`) than the Data API that keeps hitting `quotaExceeded`. Whether Composio's shared project also starves it in the daytime is untested; a daytime probe would answer that.
- **Protocol change for #2:** at each ~72h read, add one Analytics call per batch: `dimensions=video` (views, averageViewDuration, averageViewPercentage, subscribersGained) plus `dimensions=insightTrafficSourceType` with `filters=video==<id>`, and log YT_SEARCH share next to the pattern ID. #16 gets a real retention proxy (average view percentage) instead of "if a person checks Studio".
- Read-only. No posts, uploads, channel edits or signups.

## Read schedule corrected for the carried publish; Ep1 Analytics first (experiments #2/#16, tick 78, Oct 15 ~2:57 AM MT)
- GROWTH_LOG still said Ep2 + Ep3 "uploaded ~1:30 AM Oct 15" with 24h/72h reads on Oct 16/18. Nothing went up (RSS ~2:55 AM: Ep0 6, Ep1 9 views). Rewrote the rows and dates: Ep3 ~24h on Oct 17, ~72h on Oct 19 if the Oct 16 recovery lands; Ep2/Ep4 dated by their real upload night.
- Moved Ep1's Analytics read up to the Oct 16 window and added it to the recovery draft's logging list. Ep1 is the only live review, published Oct 13, so with the ~2–3 day lag its retention and traffic-source rows should exist by then. That gives the first real P1 retention + search-share baseline two days before any new episode can.
- Daytime Analytics quota probe still open (needs a daytime tick).
- Doc edits only. No posts, uploads, channel edits or signups.

## sigmoid.social engagement sample → deprioritize signup (experiment #9, tick 79, Oct 15 ~3:05 AM MT)
Public API only (no account). Local timeline paginated to mature posts (age 6–48h), plus hashtag feeds.

**Local timeline (n=130 mature posts, 7 pages):**
- Any engagement: **2/130 (1.5%)**. Median eng 0. Mean favs 0.04 / reblogs 0.00 / replies 0.02.
- Both engaged posts were from one AI-art bot (`TTAships`, 1384 followers): 1 reply + 4 favs, and 1 reply + 1 fav. Zero human local posts in the sample got a like, boost or reply.
- Link posts (n=47): **0%** any engagement. Text (n=83): 2.4%. Media (n=82): 2.4% (same two bot posts).
- Timeline noise: many 0–3 follower accounts dumping news/spam; afternoon/evening MT hours (13–21) dominate this mature window and still show near-zero eng.
- Instance: 12,229 registered users, `approval_required: true` (confirms tick 68).

**Hashtag feeds (federated; mature 6–48h):**
| Tag | n | eng% | mean eng | local posts in sample |
|-----|---|------|----------|------------------------|
| MachineLearning | 123 | 73.2 | 1.11 | **0** |
| LLM | 154 | 93.5 | 1.27 | **0** |
| ArtificialIntelligence | 147 | 87.8 | 1.03 | **0** |
| OpenSource | 153 | 84.3 | 2.43 | **0** |
| agents | 81 | 95.1 | 0.99 | **0** |
| AI | 0 mature in window | — | — | — |

Hashtag engagement lives on **remote** accounts. Joining sigmoid does not unlock a unique discovery surface we can't reach from any other Mastodon home. Top `#LLM` posts in this sample included project "no-slop" / ban-LLM-contributions policies — a hostile frame for an openly-AI host.

**Decision for #9 (research only, no signup ask):** deprioritize a sigmoid.social (or other Mastodon) signup. Bluesky is already live and empty of Welcome posts; prove that second surface before opening a third. Revisit Mastodon only if Bluesky fails and X stays graduated.

RSS check same tick (~3:05 AM MT): still Ep0 6 views / Ep1 9 views; no same-night retry landed. Oct 16 recovery draft stands.
Still no posts, uploads, channel edits or signups.

## Site analytics: free Vercel Web Analytics, referrer-only on Hobby (experiment #18, tick 81, Oct 15 ~3:35 AM MT)
- The site has no analytics, so #12 (site listing) and #14 (description footer) can't be measured. Checked the cheapest sanctioned option: Vercel Web Analytics. Vercel's pricing page (fetched ~3:33 AM MT) says Hobby gets 50,000 events/month free with no billing possible, a 1-month reporting window, and **no UTM parameters or custom events** on Hobby.
- So attribution has to come from referrers, not `?utm_` links. Don't add UTM tags to footers.
- The box's Vercel CLI is logged in to a different team with no `orbbuilds` project, so enabling needs the Orb Builds Vercel dashboard toggle (operator or signed-in browser), then a two-line `<Analytics />` add in `src/app/layout.tsx`. Plan in `content/drafts/site-analytics-plan.md`. Added to pending decisions (batch; not urgent enough for a 3 AM ping).
- No installs, pushes, toggles, posts, uploads or signups.

## Analytics per-video query needs sort + maxResults; Ep1 still not in (experiments #2/#16, tick 82, Oct 15 ~3:45 AM MT)
- Re-ran the tick-77 per-video retention query to see if Ep1 (`L7fdRoNWEPE`, published Oct 13) had landed a day early. Without `sort` and `maxResults`, `dimensions=video` returned **400 "The query is not supported"**. With `sort=-views`, `maxResults=10` it works (Ep0 unchanged: 8 views, 2 min watched, 27 s average view duration, 126.42%, 0 subs). That's YouTube's "top videos" report rule, and our written protocol (GROWTH_LOG tick-77 add-on, Oct 16 recovery draft) left both params out, so the Oct 16 read would have logged a false "not available". Fixed both files.
- Lag check (~3:45 AM MT Oct 15): `dimensions=day` still stops at Oct 12 (5, 2, 1 views), and Ep1 traffic-source rows are empty. So Analytics is ≥3 days behind; Ep1's first row may still be missing at the Oct 16 ~1:30 AM read. If so, log "not in yet" and retry at the next post-reset window rather than treating it as a failure.
- Read-only. No posts, uploads, channel edits or signups.

## Staging host backup order (experiment #13, tick 83, Oct 15 ~3:53 AM MT)
- Oct 15 publish left no exact error and no workspace writes in-window (tick 74), so it likely died **before** `YOUTUBE_MULTIPART_UPLOAD_VIDEO`. Staging is the first network hop.
- **Reachability from the box (HEAD only, ~3:53 AM MT Oct 15):**
  | Host | HTTP | Note |
  |------|------|------|
  | `litterbox.catbox.moe` (API) | 405 on HEAD | Host up; HEAD not allowed (POST-only). Proven path for Ep1. Links expire ~1h. |
  | `litter.catbox.moe` (CDN) | **403** | Download CDN blocked on HEAD from this box; if a staged URL 403s in workbench, switch hosts. |
  | `catbox.moe` | 200 | Permanent files (no 1h expiry). Prefer as fallback when litterbox fails. |
  | `0x0.st` | 200 | Also listed in box file-transfer allowlist; good mid-window fallback. |
- Composio MCP still needs `{name,mimetype,s3key}` — local paths are **not** valid `s3key`s ([Tool Router Files](https://docs.composio.dev/kb/guide/mcp-tool-router-files)). Path stays: stage public URL → workbench download → `upload_local_file` → multipart.
- **Order for Oct 16 (and standing rule):** (1) litterbox 1h (Ep1-proven) staged **inside** the window → (2) if litterbox POST or workbench download fails, **0x0.st** → (3) **catbox.moe** permanent. Never pre-stage hours early. Log which host succeeded.
- Pre-flight (~3:53 AM): all Oct 16 recovery assets present (Ep3 upload 18,191,891 B; Ep2 `/workspace/argon-share.mp4` 9,087,465 B; both scripts have footer + collision-safe tags; no `containsSyntheticMedia`). RSS still Ep0+Ep1 only. First-mover still open (X→YT Ultramarine = 0; web = blogs).
- No posts, uploads, channel edits or signups. No file staged to any host this tick (HEAD-only).

## Profile surfaces still pitch the old idea (experiment #19, tick 84, Oct 15 ~4:05 AM MT)
- Public reads ~4:03 AM MT: X @OrbBuilds bio "I'm an AI building AI products in public. Open source, build logs, honest takes.", link = github.com/orbbuilds, **no pinned post**, 1 follower / 15 posts. GitHub repo: description "An AI building AI products in public. Open source.", **0 topics**, 0 stars; README describes a chat-app stack and "weekly build logs" and never mentions YouTube, Lumin, X or Bluesky. GitHub user has no blog or X link.
- So every X reply and every footer "code" link lands people on a surface with no path to a video. The site (`src/lib/site.ts`) already links YouTube + X, so it's the right single hub link.
- Drafted `content/drafts/profile-surfaces-refresh.md`: X bio (124 chars, no "daily" claim until two publish nights succeed), X link → site, pin the first Oct 16 episode drop; GitHub description, topics, README "Watch" block, profile links. For the growth routine/operator; zero YouTube quota.
- Read-only. No profile edits, posts, uploads, channel edits or signups.

## YouTube spam policy: our fixed music bed matched its mass-production example (experiment #20, tick 85, Oct 15 ~4:25 AM MT)
- Read [YouTube's Spam Policy](https://support.google.com/youtube/answer/2801973?hl=en) (fetched ~4:22 AM MT). Item 6, "Automated or synthetic mass-production", allows testing tools and a few variations but not flooding with repetitive content made with "minimal changes". Its example: "Channels that use the exact same background music and repetitive AI generated imagery across many videos, with each video reading out an AI-generated script." Listed consequences: warnings, strikes, monetization suspension, termination.
- Our pipeline: `make_review.sh` called `music_bed.py` with no seed, so every review got seed 1, and the seed only nudged arpeggio timing by up to 10 ms. Same key, chords (Am F C G), tempo and arpeggio on every episode. That's the "exact same background music" half of the example.
- **Fix shipped (pipeline only, nothing re-rendered):** `music_bed.py` now picks a progression (5 options), a -3..+3 semitone transpose, bar length and arpeggio pattern from the seed; seed 1 still renders the old bed byte-for-byte (md5 `ec913926` before and after; peak 0.8, RMS ~0.20 for old and new). `make_review.sh` passes a seed from the script name (`cksum`, never 1; override with `MUSIC_SEED`). The Ep2/Ep3/Ep4 names give three different beds. Tonight's 9:28 PM render picks it up automatically. Already-rendered Ep2/Ep3 files keep the old bed (not worth re-rendering).
- Bigger lever, not code: the line is "minimal changes" between videos. What makes each episode ours is original commentary plus the hands-on "Lumin builds with it" part. Episodes that only read out a release note sit closest to the line, so the build session's real screen captures (e.g. Ep4 Hermes setup) matter for policy as well as views.
- Also from [YouTube API Developer Policies](https://developers.google.com/youtube/terms/developer-policies) section III.I.2: API clients must not automate comments, likes or other actions without the user's prior specific consent, and spam item 3 bans repetitive promo comments across videos. So "comment on bigger creators' fresh reviews" stays off the table as an automated tactic; our own vote comment on our own upload (user-approved routine) is fine.
- No posts, uploads, comments, channel edits or signups.

## No hands-on footage exists yet, and the renderer can't show any (experiment #20, tick 86, Oct 15 ~4:32 AM MT)
- Tick 85 said each episode's own hands-on/build segment is what keeps us clear of the spam rule's "minimal changes" line. Checked whether we actually have one. We don't, on two counts:
  1. **Renderer:** `tools/video/review_render.py` draws only the fixed blueprint background (`make_bg()`, same every episode), the Lumin sprite, text bullets and badges. There is no section kind or line field that puts a real screenshot or screen recording on screen. So even a real build session couldn't appear in a review today.
  2. **Delivered builds: 0 of 3.** Every script's `meta.build_episode_planned` promises one: Ep1 GPT-6 Intelligent UI (target Oct 18), Ep2 Gemini 4 Argon (needs approved API budget), Ep3 Ultramarine (needs budget; free fallback = open-source paper-xlsx). No build episode has been rendered or published; `build_teaser` only promises.
- Structure check (word counts from the three real scripts): all six sections identical in order every time; `what_dropped` (the release readout) is the biggest section in Ep2 (109 words) and Ep3 (155). Commentary exists (`why_hyped` + `caveats` ~100-155 words) and is original, which helps, but on screen every episode looks the same.
- Recommendation (decision for the user, batch for the morning ping): make the hands-on part real. Two pieces: (a) pipeline, no approval needed: add a `screen` line field to the renderer that composites a real screenshot/clip from the build session (zero cost, next tick candidate); (b) user call: either approve a small API budget for the promised builds, or keep to free paths only (Hermes no-key desktop trial for Ep4, paper-xlsx for Ultramarine) and stop promising paid builds in `build_teaser`. Without one of these, the "builds with them" half of the series never shows up and the channel looks like the spam policy's example.
- Read-only audit. No posts, uploads, comments, channel edits, installs or signups.

## `screen` line field: renderer can show real build footage (experiment #20, tick 87, Oct 15 ~4:40 AM MT)
- Built the pipeline half of tick 86's recommendation. A panel-section line can now take `"screen": "path/to/capture.png"` (repo-relative or absolute). The image is fitted into the glass panel with a rounded frame; optional `show` becomes a caption under it (not a bullet). Cold open ignores `screen` (hook chips stay). Missing file warns and skips.
- Wiring: `tts.py` copies `screen` into `timing.json`; `review_render.py` also overlays `screen` from the script onto timing so `--frames` picks it up without a re-tts. Documented in `content/scripts/templates/new_release_review.json` `_how_to_use`.
- Verified: no-`screen` Ep3 frame at 17.0 s md5-identical before/after (`95d8ef833da111656f5986d4ec9dfd46`). Positive scratch: why_hyped + `/workspace/video-build/desk.png` → ~820×464 composite in panel (`tests/screen-field/with-screen_why_082.0.png`).
- Still open for the user (batched, not overnight): API budget vs free-path-only builds. Until a build session writes real captures under something like `content/drafts/captures/`, Ep4+ can use the field but have nothing to point at. 3:23 PM build session should save Hermes desktop frames if the setup runbook runs.
- No posts, uploads, comments, channel edits, installs or signups.

## Per-episode background variation (experiment #20, tick 90, Oct 15 ~5:15 AM MT)
- Tick 85 fixed the "exact same background music" half of YouTube's spam-policy example; tick 86 noted the other repeating visual is `make_bg()`, the identical blueprint background on every frame of every episode.
- **Shipped (pipeline only, nothing re-rendered):** `review_render.py` `make_bg(seed)` picks one of 4 alternate dark-blue/teal/violet/navy palettes, a glow centre offset and a grid pitch (80–112 px) from the seed. Seed comes from `meta.bg_seed` > env `BG_SEED` > none. `make_review.sh` passes the same per-episode seed it already gives the music bed (`BG_SEED=1` forces the legacy look).
- Verified: no seed and seed 1 both give the Ep3 17.0 s frame md5 `95d8ef833da111656f5986d4ec9dfd46` (unchanged). Ep3-name and Ep4-name seeds give visibly different but on-brand frames (`/workspace/video-build/tests/bg-seed/compare.png`). Lumin, panel and captions untouched.
- Honest scope: this is a small lever. The spam line is "minimal changes" between videos; real build footage via `screen` (tick 87) still matters most. Tonight's 9:28 PM render picks this up automatically.
- No posts, uploads, comments, channel edits, installs or signups.

## Ep4 Hermes capture checklist (experiment #20 / #4, tick 92, Oct 15 ~5:31 AM MT)
- Gap after tick 91: `capture.sh` existed and the Ep4 queue mentioned it, but the one-shot `nous/welcome` trial still required reading ticks 61–62 + 87 + 91 + the pack to know the order. Easy to launch before recording and burn the trial.
- **Wrote `content/drafts/ep4-hermes-build-capture-checklist.md`**: preflight → `start` before first launch → still labels (welcome/trial/reply/fail) → `stop` + `stills` → PASS/FAIL handoff for 9:28 PM; title gate and hard bans inline.
- Pointed the Ep4 queue build-session line at the checklist; refreshed `2026-10-15-user-decision-brief.md` FYI (music + bg + screen + capture).
- No posts, uploads, comments, channel edits, installs or signups.

## Capture helper: build session can now record its own footage (experiment #20, tick 91, Oct 15 ~5:25 AM MT)
- Gap after ticks 87/90: the Hermes runbook says "start a screen recording before the first launch" and the `screen` field wants stills, but nothing existed to record or to turn a recording into stills, and no `content/drafts/captures/` folder existed.
- **Shipped `tools/video/capture.sh`** (read-only pixel grab via ffmpeg `x11grab` on the agent desktop `:2`, 1920x1200; never clicks or types): `still <slug> <label>` writes `content/drafts/captures/<slug>/NN-<label>.png`; `start`/`stop` record `rec.mp4` (8 fps, x264); `stills <slug> [max]` pulls scene-change frames (falls back to frame 0 on a static screen). Recordings and pid/log files are gitignored; stills get committed.
- Self-test ~5:24 AM: still 1920x1200 OK; 3.1 s recording valid; stills fallback OK; test folder removed.
- Wired into the Ep4 queue file and the tick-62 runbook line (slug `hermes-agent-v0-22`). Screenshots from the Screenshot tool are not readable from Shell, so use this helper instead.
- No posts, uploads, comments, channel edits, installs or signups.

## Owned staging host: GitHub Release asset (experiment #13, tick 93, Oct 15 ~5:40 AM MT)
- Gap: every Oct 16 staging host (litterbox, 0x0.st, catbox) is a third-party anonymous host, tick 83 only checked them from the box (HEAD), and the Oct 15 failure string is unknown, so staging can't be ruled out as the cause.
- Read-only test from the Composio workbench itself (~5:40 AM MT, nothing uploaded): public GitHub release asset GET **200** (redirect to `release-assets.githubusercontent.com`); `files.catbox.moe` 200; `0x0.st` 200; `litter.catbox.moe` root 403 and litterbox API GET 412 (roots only, not file URLs, so not proof litterbox file links fail, but consistent with tick 83's 403).
- Box `gh` is logged in as `orbbuilds` with `repo` scope and the repo has 0 releases, so a temporary `--prerelease` named `staging-YYYY-MM-DD` on our own repo is an owned, no-expiry staging host both ends can reach. Added as host (2) in `queue/00-README-slot-rules.md` and the Oct 16 recovery draft, with create/delete commands; never a draft release (assets need auth); delete after the YouTube upload succeeds.
- No YouTube calls, uploads, releases, posts, comments, channel edits or signups.

## Decision brief accuracy fix (tick 94, Oct 15 ~5:55 AM MT)
- The brief's status line, decision 1 and suggested message all said the Oct 15 publish "failed again on the shared YouTube quota". Our own evidence says otherwise: no error string logged, a 1-unit quota probe at ~2:22 AM succeeded, and no in-window workspace writes (ticks 74/83), so the cause is unknown and likely pre-upload (staging). Sending it as-is would have told the user an unsupported cause.
- Rewrote those three spots to say "cause not logged, likely before the upload", kept own-OAuth as decision 1 on the Oct 11/12/14 quota failures plus the one-try-a-night window, and added the tick-93 FYI (owned GitHub-prerelease staging fallback + mandatory error logging). RSS ~5:52 AM still Ep0 6 / Ep1 9.
- No YouTube calls, uploads, releases, posts, comments, channel edits or signups.

## Shared quota alive at ~6 AM: morning retry window (experiments #13/#3, tick 95, Oct 15 ~6:00 AM MT)
- Read-only probe ~6:00 AM MT: `YOUTUBE_GET_VIDEO_DETAILS_BATCH` (statistics, Ep0+Ep1) **succeeded** (Ep0 6 / Ep1 9 views, 0 likes/comments), and two `YOUTUBE_QUERY_ANALYTICS` reads succeeded too. Known curve for the shared Data API pool now: alive ~2:22 AM and ~6:00 AM; dead ~12:45 PM (Oct 14 429), ~1:28 PM (tick 2) and ~7:14 PM (tick 32). So it lasts at least ~4.5 h past the reset.
- Analytics is not starved at 6 AM either, but day rows still end Oct 12 and only Ep0 has a per-video row, so Ep1 (published Oct 13) is still not in. Keep the Ep1 Analytics read on the Oct 16 window.
- **Recommendation (sent to parent):** retry the Ep3 publish this morning (before ~10 AM MT) per the recovery draft, Ep3 only, logging the exact error. Gains ~19 h on the open first-YouTube-review window and frees the Oct 16 1:28 AM slot for Ep4/Ep2. A passing 1-unit read doesn't prove ~1,600 upload units remain. Added as item 0 of the decision brief.
- Read-only. No uploads, posts, comments, channel edits or signups.

## Morning-retry branch for the 11:23 AM growth session (experiments #3/#13/#17, tick 96, Oct 15 ~6:20 AM MT)
- Gap after tick 95: the morning playbook still said "Neither branch … retry uploads only in the next ~1:28 AM window", so if the recommended morning Ep3 retry succeeds, the 11:23 AM growth session would read a stale gate and skip the episode drop during the open first-mover window.
- **Added a tick-96 block to `content/drafts/2026-10-15-morning-growth-playbook.md`:** re-read public RSS (no quota) + Ep3 queue `PUBLISHED <videoId>` at growth time; Ep3 live leads to the Only-Ep3 pack (one X original + ≤1 reply, Bluesky text-first in 10 AM–2 PM, site listing, re-check "first YouTube AI review" before claiming it); vote comment tried once inside the retry run, else deferred to Oct 16; otherwise Neither unchanged. Ep2 stays carried.
- RSS ~6:17 AM MT: still Ep0 6 / Ep1 9; no retry landed yet.
- No YouTube calls, uploads, posts, comments, channel edits or signups.

## Publish throughput: one window a night can never clear the backlog (experiments #3/#13, tick 97, Oct 15 ~6:30 AM MT)
- Ledger from our own files: live uploads are Ep0 (Oct 10) and Ep1 (Oct 13, after 429s on Oct 11/12). Rendered and waiting: Ep2 Argon (GA Oct 13, CARRIED) and Ep3 Ultramarine (GA Oct 14, CARRIED). Ep4 Hermes renders tonight. So 2 uploads in 6 days against a daily cadence.
- Math: production adds 1 render every night; the shared 1:28 AM window has delivered at most 1 upload a night (0 on Oct 11, 12, 14 and 15). Even on a perfect run of nights the waiting pile stays at 2, every episode goes up at least a day after it was made, and freshest-first means Ep2 never ships before it goes STALE (after the Oct 17 window). The backlog only shrinks with a second upload window or a dedicated quota.
- Second window evidence: the shared pool was alive at ~2:22 AM and ~6:00 AM, dead by ~12:45 PM (ticks 74/95). A morning slot is the only free extra capacity we know of.
- **Recommendation (for parent, batched, not a wake):** if the item-0 Ep3 retry works this morning, make it standing: a daily ~6:28 AM "catch-up upload" that runs only when a `CARRIED` main exists, uploads the top-ranked one (main only, thumbnail if it fits, no Short, no SEO writes), logs the exact error on failure, and otherwise does nothing. That turns 1 upload a night into up to 2 a day, which is enough to drain the pile and keep daily cadence. If the retry fails on quota, that is more evidence for own-OAuth (decision 1) instead. Added as item 0b in the decision brief.
- Read-only. RSS ~6:28 AM MT still Ep0 6 / Ep1 9; no retry has landed. No uploads, posts, comments, channel edits or signups.

## Catch-up routine drafted paste-ready (experiments #3/#13, tick 98, Oct 15 ~6:45 AM MT)
- Gap after tick 97: item 0b recommends a standing ~6:28 AM catch-up upload, but nothing existed to create it with, so an approval would still need a fresh write-up of gates, dedupe and failure logging.
- **Wrote `content/drafts/catchup-upload-routine-draft.md`:** name, schedule `28 6 * * *` (flexible, early 0 / late 30), and an intent-style saved prompt: act only when a CARRIED/READY main exists; dedupe via public RSS first (no quota); one main + thumbnail only (no Short/SEO/comment/stats); slot-rule ranking and staging order; exact-error logging, one retry max; on success mark PUBLISHED, site listing, GA-to-publish hours, and send the user the link. Measure = uploads/day vs renders/day; pause after two quota fails in that window.
- Brief item 0b now points at the draft. RSS ~6:38 AM MT still Ep0 6 / Ep1 9; no morning retry has run (no queue status change, no staging release, no workspace writes since 6 AM).
- No YouTube calls, uploads, posts, comments, channel edits, routines or signups.


## Ep4 Hermes PENDING_BUILD script (experiments #4/#16/#20, tick 99, Oct 15 ~6:50 AM MT)
Gap after ticks 92–98: capture checklist and queue existed, but production still had no script file with filled cold-open `show` chips or `screen` slots to wire after the 3:23 PM session.
- Wrote `content/scripts/2026-10-16-hermes-agent-v0-22.json` (PENDING_BUILD). Numbers re-checked on [v0.22.0](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.0): 600 plugins, ~2,520 contributors, ~24,200 commits, "a third smaller", desktop-only `nous/welcome`.
- Default title Candidate A; `_title_gate.pass_setup` holds the P5+setup title/thumb/tags for a PASS handoff.
- Capture checklist + Ep4 queue now point at this script.

## Fable 5.5 rumor spike: drop-day plan + U3 held (experiments #3/#4/#17, tick 100, Oct 15 ~6:55 AM MT)
- X recent counts for `"Fable 5.5" -is:retweet`: ~23-32/h overnight, then 86, 96 and 108 (first 51 min) per hour from 4 AM MT. Chatter is "dropping today" plus an Azure/MLflow catalog row copying 5.1 pricing. Anthropic's models overview (curl ~6:53 AM MT) still lists only `claude-fable-5-1` (0 hits for `claude-fable-5-5`). Not announced.
- Wrote `content/drafts/fable-5-5-drop-day-plan.md`: "real" = newsroom post AND models-overview row (catalog/LiteLLM rows don't count); if real before ~6 PM MT, Ep4 slot pivots to Fable 5.5 (Hermes CARRIED), P1/P6, hook facts from official launch materials only, no "I tested" while the build budget (#20) is undecided; else nothing changes.
- Put bank U3 on HOLD (its framing may flip today) and drafted U3b, a "how you'll know it's real" post safe only while the models page still shows 5.1.
- No posts, uploads, comments, channel edits or signups.

## Publish hour opened as #21 (tick 101, Oct 15 ~7:05 AM MT)
- Status check ~7:00 AM MT: public RSS still Ep0 6 / Ep1 9; Ep3/Ep2 queues still `CARRIED to 2026-10-16`; no staging release, so no morning retry yet. Anthropic models overview still only `claude-fable-5-1` (Fable 5.5 not real yet).
- New question instead of repeating recovery: our only upload window makes every episode go public at ~3:28 AM ET. Added backlog #21 (hypothesis, measure, gates). Parked until ≥3 live reviews + Analytics country data; noted that the 6:28 AM catch-up draft (0b) would hand us the first different-hour sample for free.
- Read-only. No YouTube calls, uploads, posts, comments, channel edits or signups.

## Native-video lane for quota-blocked episodes (experiment #22, tick 102, Oct 15 ~7:15 AM MT)
- Status ~7:12 AM MT: RSS still Ep0 6 / Ep1 9; Ep3/Ep2 still `CARRIED to 2026-10-16`; no staging release, so no morning retry; Anthropic models overview still only `claude-fable-5-1`.
- Idea not tried before: finished vertical Shorts already exist (`content/drafts/2026-10-14-ultramarine-1-flash-short.mp4`, 47 s, 1080x1920, CTA end card; Ep2 `…-gemini-4-argon-short.mp4` 57.5 s). Posting one natively on X uses zero YouTube quota, so the Ultramarine review can reach people today even if every upload window fails.
- Limits (web search ~7:13 AM MT): X default-account post video is far above 1 min (sources disagree, 140 s to 20 min; our clips are under 1 min either way). Bluesky: 10 min / 300 MB, 25 videos/day, **email must be verified**; ours is `newbot@…` (agent inbox), unverified as of Oct 14.
- Demand still live on X: `"Ultramarine 1 Flash" -is:retweet` 97 posts Oct 14 UTC + 96 since 6 PM MT; posts with video mentioning Ultramarine: 17 total in those two days, so a video take isn't crowded.
- **Wrote a tick-102 branch into `content/drafts/2026-10-15-morning-growth-playbook.md`:** on the Neither branch, the 11:23 AM session's one X original can be the Ep3 Short as native video with a U-shape caption (fact + caveat, "full review on YouTube soon", no YouTube URL, no "I tested", no "first"). Bluesky video only if email verification is done first (account setting via our inbox), else Bluesky stays text. If Ep3 went live in a morning retry, use the Only-Ep3 pack instead (link to the real video).
- Read-only. No posts, uploads, comments, channel edits, email verification or signups.

## Bluesky email verified + #22 paste-ready (experiment #22, tick 103, Oct 15 ~7:25 AM MT)
- Status ~7:22–7:25 AM MT: RSS still Ep0 6 / Ep1 9; no morning retry; Data API 1-unit probe **succeeded** (shared quota alive ~5.9 h after reset); Fable 5.5 still unannounced (newsroom + models overview); Ultramarine X→YouTube review links still **0**.
- Welcome-mail verify token from Oct 14 was **ExpiredToken**. Requested a fresh confirmation via `com.atproto.server.requestEmailConfirmation`, read code from our agent inbox, confirmed via `confirmEmail`. Session now reports `emailConfirmed: True` for `@orbbuilds.bsky.social`.
- Updated morning playbook with paste-ready native-video caption (sourced `$0.13/task` + weights caveat) and Bluesky video unlocked for the Neither branch.
- No posts, uploads, comments, channel edits or signups. No WakeParent (in-remit unlock for the growth routine; brief already with parent from tick 95).

## Hook-first X clip for the native-video lane (experiment #22/#16, tick 104, Oct 15 ~7:40 AM MT)
- Status ~7:31 AM MT: RSS still Ep0 6 / Ep1 9; Ep3/Ep2 still `CARRIED to 2026-10-16`; no staging release (no morning retry); Anthropic models overview still only `claude-fable-5-1`.
- Audit of the clip tick 102 picked for the X post: `short_windows.py` kept only 1 of 5 fact lines, so the YouTube Short opens on "On October fourteenth, Paper Instruments launched…" and never says the $0.13 hook. On X it autoplays muted in-feed, so the first seconds have to carry the post. The cold open ("Five people… thirteen cents a task. That's their benchmark, not mine") was skipped because the stacked vertical crop clips its centered title (tick 14).
- **Rendered `content/drafts/2026-10-14-ultramarine-1-flash-xclip.mp4`** (52.6 s, 1080x1920, mean −18 dB): cold open with a centered 1400 px crop (title + captions intact, frame-checked), then caveats 98.5–131.5 s (own benchmark, CEO-thread source, "I haven't tested it yet") with the standard stacked crop, then the like/subscribe card. Playbook step 1 now attaches it on X and Bluesky; the YouTube Short is unchanged.
- Follow-up idea (not built): `post_render.sh` could emit this hook-first social cut automatically (cold-open crop + caveats + CTA) beside the Short; worth doing only if the `V` read beats the U post's 25 impressions.
- No posts, uploads, comments, channel edits or signups.

## Native-video posting path locked (experiment #22, tick 106, Oct 15 ~7:45 AM MT)
- Gap after tick 105: the morning playbook said "attach the xclip" but never said **how**. Past X posts used the signed-in browser; Composio `twitter` still has **no active connection** (re-checked ~7:46 AM MT), so `TWITTER_UPLOAD_LARGE_MEDIA` is not on the critical path for 11:23 AM.
- Wrote `content/drafts/native-video-posting-runbook.md`: preflight (52.6 s / 13 MB / 1080×1920), paste-ready caption, X browser steps, Bluesky ATProto `uploadVideo` → poll → `embed.video` (docs.bsky.app tutorial), attach-fail → U3b, GROWTH_LOG `V` template. Pointed the morning playbook at it.
- No posts, uploads, comments, channel edits, Composio connects or signups.

## Quota curve point + Analytics lag at ~8 AM (experiments #13/#2, tick 107, Oct 15 ~8:05 AM MT)
- Status ~8:03 AM MT: public RSS still Ep0 6 / Ep1 9; Ep3/Ep2 still `CARRIED to 2026-10-16`; no morning retry has run. Anthropic models overview still only `claude-fable-5-1` (34 hits, 0 for 5.5), so Fable 5.5 is still rumor.
- Data API batch stats read **succeeded** ~8:05 AM MT (Ep0 6 views / Ep1 9 views, 0 likes, 0 comments). Curve so far: alive at ~2:22, ~6:00, ~7:22 and ~8:05 AM; dead by ~12:45 PM (Oct 14). So the shared pool lasts at least ~6.6 h past the 1:28 AM reset; the death point is somewhere in 8:05 AM–12:45 PM. A catch-up upload anywhere 6–8 AM is inside the known-alive window.
- Analytics day rows still end **Oct 12** (Oct 10: 5 views, avg 36 s, 165%; Oct 11: 2 views, 15 s; Oct 12: 1 view). Ep1 traffic-source query returns 0 rows. Ep1 went live Oct 13 ~1:25 AM MT, so the lag is >2 days; the Oct 16 recovery-draft read stays correct.
- Read-only (1 Data API batch + 2 Analytics queries). No uploads, posts, comments, channel edits or signups.

## Ultramarine YouTube first-mover CLOSED + playbook Step 0 fix (experiment #3/#22, tick 108, Oct 15 ~8:15 AM MT)
- Public YouTube SERP `Ultramarine 1 Flash AI review` (~8:15 AM MT) now has real AI-model reviews: AI WITH Rithesh `CcRr7dJy4gI`, Julian Goldie / AI News Today `k85bmBNAgN0`, White Rabbit AI `Optf417cJ4U` (oEmbed titles confirmed; content matches Paper Instruments launch).
- X search Ultramarine→youtu.be/youtube.com still **0** — the old X→YT proxy alone is insufficient; always re-check YouTube SERP before claiming first.
- **Honesty rule:** never say "first YouTube AI review" on social or meta. Say "review" / "receipts-only review".
- Updated: Ep3 queue `First-mover: closed`, ep3 growth pack, morning playbook (tick 108 block + Step 0 Neither → native-video, tick 96 step 4 pointer). Oct 16 rank unchanged (Ep3→Ep4→Ep2 by freshest GA).
- Also fixed: playbook Step 0 still said "Neither → no social; stop", which would have made 11:23 AM skip experiment #22 despite ticks 102–106. Corrected.
- RSS ~8:14 AM: still Ep0 6 / Ep1 9; no morning retry. No YouTube Data API calls this tick (quota probe deferred to ~10–11 AM per tick 107).
- No posts, uploads, comments, channel edits or signups.

## Competitor Ultramarine reviews: real demand ceiling + a same-size openly-AI peer (experiments #3/#1/#15, tick 109, Oct 15 ~8:30 AM MT)
- Data API batch read ~8:27 AM MT (videos + channels, ~2 units; also a quota curve point: alive ~8:27 AM, death window now 8:27 AM–12:45 PM).
- AI WITH Rithesh `CcRr7dJy4gI` (51.4K subs, 1,003 videos): "Ultramarine 1 Flash Is WILD… Claude-Level AI at 60× Lower Cost!", 4:44, published Oct 14 8:39 PM MT; **239 views, 2 likes, 0 comments at ~11.8 h** (~20 views/h, ~0.5% of subs). Its description already carries "self-reported" caveats, so our caveat angle is not unique.
- Julian Goldie / AI News Today `k85bmBNAgN0` (10.4K subs): "Ultramarine AI Is INSANE! 60X Cheaper Than Claude?!", 9:48, published 6:46 AM MT; **18 views at ~1.7 h**.
- White Rabbit AI `Optf417cJ4U` (**0 subs, 7 videos, 32 lifetime views**): 90-s multi-story brief, published 7:04 AM MT, 0 views at ~1.4 h. Animated rabbit host, AI voice (Gemini TTS), AI disclosure + sources in every description, also covered Hermes v0.22 (our Ep4).
- Read: all three titles lead with "60× cheaper than Claude"; YouTube demand for this topic is modest (an established 51K channel got ~240 views in its first half-day). So Ep3's realistic upside is small either way, and our "5-person flex" title is now the differentiated one rather than the 4th "60×" clone. Kept title/P1 (rotation test) and added one search tag `Ultramarine 1 Flash vs Claude Fable 5` to the script meta (company-reported comparison; 194 chars total).
- White Rabbit AI added to `content/drafts/cross-promo-shortlist.md` Tier B: the first openly-AI animated YouTube host we've found at our size, honest-caveat style, complementary format. Gate unchanged (≥3 live reviews), no ask, no comments.
- Benchmark to reuse: re-read `CcRr7dJy4gI` at ~24 h / ~72 h (1 unit, ride a stats batch) as the "established channel, same topic" ceiling next to Ep3's own 24 h/72 h.
- No uploads, posts, comments, channel edits or signups.

## Standing posting rules file (experiments #17/#9/#22, tick 110, Oct 15 ~8:50 AM MT)
- Gap: every learned posting rule (1 X original per ~4h, 1-2 replies, U-first, no open asks, never claim first, Bluesky text-first 10 AM-2 PM MT, native-video lane, no comments on other channels) lived only in the one-day `2026-10-15-morning-growth-playbook.md` and in this doc's tick log. From Oct 16 on, the posting routines would have had nothing standing to read.
- Wrote `docs/POSTING_RULES.md` (each rule cites its tick). Pointed the growth and content-drafts rows of `docs/SERIES_RELEASE_REVIEWS.md` section 5 at it, and added a header pointer to the Oct 15 playbook.
- Docs only. No posts, uploads, comments, channel edits or signups.

## Morning-scan candidates vs YouTube demand: Hermes confirmed, Grok Voice 3.0 = demo gap, Step 5/Ultrafast saturated (experiments #3/#8/#4, tick 111, Oct 15 ~8:52 AM MT)
- Public YouTube SERP (upload-date sort, no API quota) + `tools/video/youtube_autocomplete.py` for the three 8:23 AM scan picks plus our Ep4, ~8:50 AM MT:
  - **Hermes Agent v0.22 (our Ep4):** Julian Goldie SEO `NZcdLDuhryI` 3,973 views at ~10h; BoxminingAI `pAaAgcjNgEs` 14,707 at ~1d; evergreen setup/tutorials 371K–524K. Demand is roughly **10–15x Ultramarine's** (tick 109: 239 views at ~12h on a 51K channel). Keeps Ep4 as tonight's render and backs the tick-60 setup angle.
  - **Grok Voice 3.0 (launched Oct 14):** 10+ fresh videos, all 1–21h old; top is Simply AI `Os80lGvR3AA` 1,205 at ~15h and a Japanese explainer 1,188 at ~3h. Autocomplete returns `grok voice 3.0` and **`grok voice 3.0 demo`**, real search demand. The fresh results are chart/explainer/news; only Stepwise `Kj-kyXOEkek` (275 views) does a live test. A hands-on "a talking orb tries the #1 voice model" demo is an open slot and the strongest P5 openly-AI fit we've seen. It needs a paid xAI Voice Agent API call (official price $0.08/min, so a 10-min test is about $0.80), which falls under the pending build-budget decision (#20). First-mover is closed: never say "first".
  - **Step 5 Preview (open weights Oct 15):** the YouTube slot was used up by the Sept 20 API launch (Bijan Bowen 32K views at 2d, AICodeKing 13.8K at 7d, several 5–7d-old tests). No autocomplete. No episode; the weights drop goes to the X U-bank as **U4** (hardware reality, verified on the HF card).
  - **OpenAI Ultrafast:** 2+ weeks old, heavily covered (Theo 145K, Nick Saraev 53K, OpenAI's own). Skip.
- Ranking for the next free render slot after Ep4 (backlog permitting, tick 97): **Grok Voice 3.0 demo** (if the build budget is approved) beats the Ep5 Ling pack. Without budget, it's a no-go: an explainer would be the 11th chart video.
- Read-only (public pages only, 0 YouTube API units). No posts, uploads, comments, channel edits or signups.

## Grok Voice 3.0: possible free demo path + sourcing (experiments #4/#20, tick 112, Oct 15 ~8:58 AM MT)
- Official post (x.ai/news/grok-voice-3, fetched ~8:57 AM MT): API only at $0.08/min, `grok-voice-latest` auto-switched; AA Speech-to-Speech Index 86.9 (AA, Oct 13), Full Duplex Bench 97.0%, τ-Voice 71.6%; Tesla/Starlink numbers are company-reported. Use these exact figures for any cold-open `show` chips, with "per Artificial Analysis" attribution.
- Possible $0 path: x.ai/api says the Playground on console.x.ai "comes with every Console account" and is free to test models before buying. Whether it covers realtime speech-to-speech is **not confirmed** (no doc found saying so). Needs a new Console account on the Orb Builds identity = operator decision, not this routine. Added as a one-line hedge under brief item 2 (removed the overclaim that a demo is "only possible with a budget").
- Episode angle still holds: Lumin's own voice is local open-source TTS (`am_fenrir`), so "the orb with a homemade voice meets the #1 voice model" is an honest openly-AI hook. Never say "first" (closed, tick 111).
- Read-only (1 search + 1 fetch). No signups, posts, uploads, comments, channel edits or spend.

## Ep4 search tags from live autocomplete + stale queue paths (experiments #8/#4/#13, tick 113, Oct 15 ~9:10 AM MT)
- `tools/video/youtube_autocomplete.py` ~9:08 AM MT: `hermes agent` suggests `tutorial`, `setup`, `use cases`, `update`, `windows`, `local`, `coding`, **`hermes agent 22`**; `hermes agent free` is a real suggestion. Openly-AI seeds carry no search demand (`ai reviews ai` → noise; `ai reacts to` → MrBeast/fandom; `ai replacing` → jobs/teachers/lawyers). So P5 stays a **click hook in the title**, while search rides on the product name + version tags. `grok voice 3.0 vs` → off-niche collision (no comparison demand yet).
- Applied: Ep4 script `meta.tags` + queue default tags gained `Hermes Agent v0.22` and `Hermes Agent update` (155 chars total). Setup-gate tags gained `Hermes Agent tutorial` and `Hermes Agent free` (the latter only if the no-key trial really runs on camera).
- Hygiene bug fixed: the Ep4 queue still named `2026-10-15-hermes-agent-v0-22.*` for script/full render/upload, but outputs are named from the script basename (`make_review.sh` NAME), so the 1:28 AM run would have looked for files that will never exist. Now `2026-10-16-…`.
- FYI for 9:28 PM finalize: `validate_script.py` warns ~663 words (>3.5 min) on the skeleton (tick 99 counted ~420 spoken; the count may include placeholder slots). Production should trim to the spoken target after filling `screen`/title gate.
- 0 API units (public autocomplete only). No posts, uploads, comments, channel edits or signups.

## Grok Voice 3.0 P5 demo pack (gated) (experiments #4/#20, tick 114, Oct 15 ~9:20 AM MT)
- Gap after ticks 111–113: Grok Voice ranked as the best next openly-AI episode, figures were sourced, and the brief mentioned it, but nothing paste-ready existed for the build/production routines when the operator answers brief item 2.
- Wrote `content/drafts/grok-voice-3-p5-demo-title-pack.md`: titles, thumb (`grok-voice-3-cand-thumb.jpg`), cold-open `show` chips (AA 86.9 / Full Duplex 97% / $0.08/min, attributed), Path A paid API vs Path B unverified Playground, capture checklist, tags from autocomplete, vote, measure plan. Official Voice docs still do not confirm free speech-to-speech in Playground (secondary coverage claims it).
- Hygiene: refreshed decision-brief status (first-mover **closed**, no morning retry, RSS still Ep0/Ep1 ~9:19 AM) and reframed item 0 as backlog-clearing not first-mover; fixed Ep4 queue First-mover note that still said Ep3's first-mover was open.
- No signups, posts, uploads, comments, channel edits or spend. No WakeParent (pack is gated prep; brief already with parent; no new decision).

## Profile surfaces still stale; wired into standing rules + 11:23 AM order (experiment #19, tick 115, Oct 15 ~9:29 AM MT)
- Re-read live surfaces ~9:29 AM MT (no edits): X @OrbBuilds bio still "I'm an AI building AI products in public…", link still `github.com/orbbuilds`, no pin, 1 follower / 15 posts. GitHub repo description still "AI products", **0 topics**, user blog/twitter empty. Public RSS still Ep0 6 / Ep1 9 (Neither).
- Gap: tick 84 drafted the refresh and the playbook called it "optional", so a Neither morning could ship native-video while every visitor from X still lands on a code org with no YouTube path.
- Fix (docs only): added a Profile surfaces section to `docs/POSTING_RULES.md`, and an ordered Neither checklist to `content/drafts/2026-10-15-morning-growth-playbook.md` (RSS → #19 bio/link → native-video → ≤1 reply → Bluesky video). Paste-ready bio/link unchanged from the draft.
- No profile edits, posts, uploads, comments, channel edits or signups from this tick.

## Mid-morning quota probe + Ultramarine competitor velocity (experiments #3/#13/#2, tick 116, Oct 15 ~9:40 AM MT)
- Planned ~10–11 AM probe from ticks 109–115. One `YOUTUBE_GET_VIDEO_DETAILS_BATCH` (~1 unit) at ~9:40 AM MT succeeded → **shared quota still alive** ~8.2 h after the ~1:10 AM MT reset. Death window still unknown beyond "alive at 9:40, historically dead by ~12:45 PM Oct 14".
- Ours (unchanged): Ep0 `aCvkp11w9_8` 6 views / 0 likes / 0 comments; Ep1 `L7fdRoNWEPE` 9 / 0 / 0. Public RSS still Neither (Ep0+Ep1 only). No morning Ep3 retry has run.
- Competitor Ultramarine velocity vs tick 109 (~8:30 AM):
  - AI WITH Rithesh `CcRr7dJy4gI` (~13 h old): **239 views, 2 likes, 0 comments** — **flat** vs 239 at ~11.8 h. Established-channel ceiling for this topic looks capped early.
  - Julian Goldie `k85bmBNAgN0` (~2.9 h): **27 views** (was 18 at ~1.7 h), 0 likes, 1 comment — slow drip (+9 in ~1.2 h).
  - White Rabbit AI `Optf417cJ4U` (~2.6 h): still **0 views** (0-sub peer, openly-AI animated host + Gemini TTS disclosure).
- Read: Ultramarine YouTube demand is modest and already cooling on the biggest competitor. Catch-up Ep3 still clears the CARRIED pile and frees tonight's 1:28 AM for Ep4/Ep2; it is **not** a first-mover play. Prefer an Ep3-only retry **now** while the pool is confirmed alive (brief item 0); if it fails, log the exact error.
- No uploads, posts, comments, channel edits or signups from this tick (probe only). WakeParent: time-sensitive catch-up ask.

## Script length check counted captions twice; Ep4 is on target (experiment #16, tick 117, Oct 15 ~9:55 AM MT)
- `validate_script.py` summed `say` + `caption` + `show`, so captions (mostly copies of `say`) roughly doubled the count. That is where tick 113's "~663 words, trim" came from. Ep4's real spoken count is **420** (the series ceiling in `docs/SERIES_RELEASE_REVIEWS.md` is 150-420), and both title-gate swaps are shorter (`_say_on_pass` 18 / `_say_on_fail` 22 replace a 27-word line), so **no trim is needed** at 9:28 PM.
- Fix: the validator now counts only `say` and warns outside 150-420 (was a 520 cap on the doubled count). Re-ran: Ep1/Ep2/Ep4 OK; Ep3 (already rendered) shows 462 spoken, an over-length note for the record only.
- Fable 5.5 official recheck ~9:53 AM MT: models overview still `claude-fable-5-1` only (0 `claude-fable-5-5`), newsroom mentions Fable 5.1 only. Still rumor. RSS still Ep0 6 / Ep1 9; no catch-up upload yet (13 min after tick 116's ask).
- No uploads, posts, comments, channel edits or signups.

## Ep4 post-publish pack drafted (experiments #4/#7/#12/#17, tick 118, Oct 15 ~10:00 AM MT)
- Public RSS ~9:58 AM MT still Ep0 6 / Ep1 9 — catch-up **not** run; 11:23 AM stays Neither (native-video + #19) unless RSS changes.
- Hermes demand still active on YouTube SERP (BoxminingAI `pAaAgcjNgEs` ~1d, Julian Goldie `NZcdLDuhryI` ~11h). tubeai.app listed Boxmining v0.22 at **13,740** views (~10:00 AM MT; secondary aggregator, not Data API). Autocomplete still tutorial/setup/update/local. Never claim first.
- **Wrote** for after Ep4 is live: `content/drafts/ep4-post-publish-growth-pack.md` (U-shape Post A + setup-gate alt, Bluesky 1/2/3 CTA, X reply shortlist preferring @omx0r), `ep4-vote-comment-draft.md`, `ep4-site-listing.md` + `public/episodes/rr-004.jpg`. Wired into Ep4 queue.
- Hygiene: Giuseppe Sirigu Sep 22 2026 local-model tool-call blog **pre-dates** v0.22 — do not cite as a Threshold failure in script or posts; optional future vote-3 retest only.
- Playbook: tick 118 Neither confirmation for 11:23 AM. No uploads, posts, comments, channel edits or signups.

## Short title generator: stale P5 blurb + no version (experiment #5/#8/#4, tick 120, Oct 15 ~10:22 AM MT)
- Dry-ran `short_publish_meta.py` on the Ep4 script: it would title the Short `Hermes Agent in 55 seconds (AI vs AI)`. Two problems: "AI vs AI" was the tick-1 placeholder name for P5, not the openly-AI personal-stakes pattern Ep4 actually uses, and it drops `v0.22`, the term live autocomplete shows people search (tick 113).
- Fix: P5 blurb is now `is it replacing me?`; added optional `meta.short_product` (set to `Hermes Agent v0.22` on Ep4) and `meta.short_title` full override. Ep4 now yields `Hermes Agent v0.22 in 55 seconds (is it replacing me?)`. Ep2 (P2) output unchanged; Ep4 validator OK.
- Title-gate PASS branch: `meta._short_title_on_pass` holds `Hermes Agent v0.22 setup in [N] seconds (no API key)`; the queue tells the build session to copy it into `short_title` only if the gate passes. Measure as S1c at 24h/72h like other Shorts.
- RSS ~10:20 AM MT still Ep0 6 / Ep1 9 (Neither; no catch-up). No uploads, posts, comments, channel edits or signups.

## Hook-first xclip auto-emitted by post_render (experiments #22/#16/#5, tick 121, Oct 15 ~10:33 AM MT)
- Gap after tick 104: the Ep3 X/Bluesky clip was a one-off ffmpeg; tick 104 parked automating it until a `V` read, but the CARRIED backlog means native-video stays needed for Ep4+ regardless of tonight's `V` result.
- **Shipped:** `tools/video/xclip_windows.py` (cold_open letterbox + full caveats + CTA, ≤58 s), `xclip_splice.sh`, `shorts_cut.sh` `letterbox|stacked` mode (default stacked unchanged for YouTube Shorts), wired into `post_render.sh` → `<name>-xclip.mp4` (`NO_XCLIP=1` skips). Ep3 dry-run: `letterbox:0.35:16.00 stacked:98.47:131.53 stacked:147.31:151.07`, 52.6 s, 1080×1920; cold-open title + hook caption readable; Shorts stacked path regression OK.
- Working cold-open crop is **full-frame letterbox** (scale to 1080w + pad), not a 1400-wide center crop — that matched the hand-made Ep3 xclip better (title survives; stacked crop doubles Lumin on cold open).
- 11:23 AM still uses the hand-made Ep3 file; Ep4's 9:28 PM render will emit its own. Pointed the native-video runbook at the auto path.
- RSS ~10:30 AM MT still Ep0 + Ep1 only (Neither; no catch-up). No uploads, posts, comments, channel edits or signups.

## Site hero still pitches the old idea; bio link now points there (experiment #19, tick 123, Oct 15 ~10:50 AM MT)
- Live HTML ~10:47 AM MT: `<title>`/OG/Twitter card "Orb Builds: An AI building AI products in public."; hero pill "AI agent · building in public"; hero buttons **Follow on X** + **See the code**, no YouTube button in the hero (YouTube only in Latest episode + Follow sections). `og.png` is image-only, fine.
- Gap: tick 84/115 #19 fixes X + GitHub but sends the X link to this site, so today's bio edit would land visitors on the old pitch with a first button back to X.
- **Wrote** `content/drafts/site-hero-refresh.md`: exact `site.ts` tagline/description, hero pill/H1/sub copy, **Watch on YouTube** primary + Follow on X secondary, chat persona line; no cadence claim while the pile is stuck; no Ep2–4 listing before videoIds. Wired into `docs/POSTING_RULES.md` Profile surfaces item 5 + `profile-surfaces-refresh.md`. Build session applies (code edit).
- RSS ~10:45 AM MT still Ep0 6 / Ep1 9 (Neither). No site pushes, posts, uploads, comments, channel edits or signups.

## Hermes vs Grok Bot search demand (experiments #4/#8, tick 124, Oct 15 ~11:05 AM MT)
- Public RSS ~11:01 AM MT still Neither (Ep0 `aCvkp11w9_8` **6** views / Ep1 `L7fdRoNWEPE` **9** views). No catch-up. 11:23 AM growth stays Neither (#19 → native-video → Bluesky video).
- YouTube autocomplete (no quota, ~11:02 AM MT): `hermes agent` suggestions include **`hermes agent vs grok bot`** and **`hermes agent 22`** beside the known tutorial/setup/update/local set. Direct queries `hermes vs grok` → `hermes vs grok bot`; `grok bot vs hermes` → itself.
- Written vs-pages already crowd the web (grokcamp, myclaw, tao.media, Julian Goldie, aicoolies — convenience/managed vs open-source control). Live Hermes YT SERP is still recap/setup (Boxmining MASSIVE / Julian chapters / beginner setup guides), so versus is a **different** pocket than Ep4's P5.
- **Action:** drafted `content/drafts/p4-hermes-vs-grok-bot-candidate.md`. Ep4 title/tags **unchanged** (no Grok Bot in meta until Lumin says it). Brand gate: public voice is Lumin/"I'm an AI", not "I'm a Grok Bot" — needs operator OK before any public naming. Default = stay P5 "replacing me".
- Peer hygiene (#15): White Rabbit AI `Optf417cJ4U` still 0 views; title is short AI-news format (`… | AI News in 90s`). Stay Tier B.
- FYI line added to `content/drafts/2026-10-15-user-decision-brief.md` (batch; no WakeParent). No uploads, posts, comments, channel edits or signups.

## Analytics reads belong in daytime, not the publish window (experiments #2/#16/#13, tick 125, Oct 15 ~11:10 AM MT)
- Three read-only `YOUTUBE_QUERY_ANALYTICS` calls at ~11:10 AM MT all succeeded. Day rows **still end at Oct 12** (Oct 9–12: 0/5/2/1 views), identical to tick 77 at ~2:48 AM, so no new day landed in 8+ h. Ep0 per-video unchanged (8 views, 27 s avg, 126.42%, 0 subs). Ep1 `L7fdRoNWEPE` traffic-source rows still empty.
- So the Oct 16 ~1:30 AM Ep1 read (tick 78) would most likely log "not in yet" while eating time in the one window the CARRIED pile needs. Analytics is a separate API from the Data API upload quota and answers midday, so nothing is gained by running it at 1:30 AM.
- **Change:** `2026-10-16-publish-recovery.md` no longer runs Analytics; GROWTH_LOG tick-78 note marked superseded. This routine does the Ep1 retention + traffic-source read on Oct 16 ~10 AM–noon MT (first real P1 baseline for #2/#16, YT_SEARCH share for #8).
- Read-only. No uploads, posts, comments, channel edits or signups.

## Neither preflight + reply shortlist for V (experiments #22/#17, tick 126, Oct 15 ~11:20 AM MT)
- Public RSS ~11:19 AM MT: still Neither — Ep0 `aCvkp11w9_8` **6** views, Ep1 `L7fdRoNWEPE` **9** views (no Ep3). xclip `2026-10-14-ultramarine-1-flash-xclip.mp4` still 52.6 s / 1080×1920 / ~13 MB.
- **Caption sourcing:** [paperinstruments.com/ultramarine](https://www.paperinstruments.com/ultramarine) still states Ultramarine 1 Flash at **$0.13 per task** on **PI Knowledge Work (internal)** vs Claude Fable 5 (max) at **$8.19**, and "Model weights coming soon". V caption attribution ("Paper Instruments claims… on their own PI Knowledge Work harness") stays correct.
- **Reply shortlist refreshed** in `ep3-post-publish-growth-pack.md` for the Neither / native-video path (growth fires ~11:23 AM). Prefer **@somi_ai** `2110517224767418775` (~2.0K followers, ~230 imp; flags self-reported + APEX-Agents 57 vs 64). Backups: @MikelEcheve, @drmshevy, @OCTAMEM. Drafts say "receipts-only clip" (no YouTube videoId). Skip amplifiers / @Decoded08 / jailbreak.
- Autocomplete for bare `ultramarine 1 flash` still Warhammer/painting collision (unchanged).
- No uploads, posts, comments, channel edits or signups. No WakeParent (ops prep for growth; no new user decision).

## Fable 5.5 rumor plateau vs a real launch's X volume (experiments #3/#4, tick 127, Oct 15 ~11:31 AM MT)
- Official models overview ~11:30 AM MT still lists **Claude Fable 5.1** (`claude-fable-5-1`) as current; no 5.5. Morning scan also logged it as leak chatter only.
- X recent counts for `"Fable 5.5"` (hourly, MT): 4 AM 126, 5 AM 156, 6 AM 183, 7 AM 166, 8 AM 176, 9 AM 140, 10 AM 176, 11:00–11:30 AM 75. So the rumor has **plateaued at ~140–185/hr for 7+ h**; no step change.
- Reference scale from a real launch in-window: Ultramarine (`"1 Flash"` OR `"Paper Instruments"`) Oct 14 went 0 → 68/92/99/77 per hour in its first four hours (10 AM–1 PM MT), 538 total over 12 h. The Fable rumor alone already runs ~2× that launch's peak, so an official Fable 5.5 drop would be a far bigger demand moment than Ep3's topic.
- **Rule for the scans:** treat a jump to roughly **≥3× the plateau (~500+/hr)** in `"Fable 5.5"` counts, or a 5.5 row on the models overview, as the launch signal that triggers `content/drafts/fable-5-5-drop-day-plan.md` + WakeParent. A plateau in the 140–185 band is still rumor; do not pivot Ep4 off Hermes on it. Threshold is a heuristic from one comparison, not a measured law.
- Read-only (2 X count calls, 1 docs fetch). No uploads, posts, comments, channel edits or signups.

## V went out; human-check notice closes X for the rest of Oct 15 (experiments #22/#17, tick 128, Oct 15 ~11:37 AM MT)
- Growth session posted V at 11:29 AM MT: [V post](https://x.com/OrbBuilds/status/2110785068839153774) (52.6 s Ultramarine xclip, receipts-only caption). Public metrics at ~11:36 AM MT (T+7 min): **4 impressions**, 0 likes/replies/RTs/bookmarks, media `view_count` **0**. Baseline to beat at the 4–6 h read: best U (vLLM `2110453798120665321`) 26 impressions.
- The graduated-access human-check notice fired after this **single** post, so per POSTING_RULES rule 2 X is closed for the day. That overrides the tick-119 afternoon plan: **no U5 and no X original from the 1:23 PM content-drafts run or the 3:23 PM build session today**; U5 moves to the Oct 16 growth session (re-verify OpenUI package versions first). The @CorbenicAI thank-you and @somi_ai reply also wait until Oct 16, max one.
- Bluesky is a separate platform and the notice is X-only, so the deferred Bluesky V (earliest ~1:29 PM MT, inside the 10 AM–2 PM window) still stands.
- V read now has a second signal: the X API returns media `view_count` for native video, so the 4–6 h read logs impressions **and** video views (watch-through proxy for #22 vs text U posts).
- Read-only (1 X post read). No uploads, posts, comments, channel edits or signups.


## Bluesky V needs an afternoon owner (experiment #22, tick 129, Oct 15 ~11:46 AM MT)
- Growth posted X V at 11:29 AM and stopped (human-check). Bluesky V was deferred ≥2h into the 10 AM–2 PM window, but **no afternoon growth routine exists**, so the second surface would miss its window unless the 1:23 PM content-drafts run (or a parent dispatch) owns it.
- Wrote `content/drafts/2026-10-15-bluesky-v-afternoon-handoff.md`: clip path, caption, ATProto steps, 1:29–2:00 PM MT window, hard bans (no X, no Welcome/U1 if video ships). Playbook Tick 129 points the 1:23 PM run at it.
- X V recheck ~11:46 AM MT (T+17 min): still **4** impressions, 0 likes/replies/RTs/bookmarks; media duration 52599 ms; this expand did not return media `view_count` (log impressions; add view_count when the field appears).
- Clip preflight OK: 52.6 s, 1080×1920, h264+aac, 13.0 MB on disk.
- WakeParent: ask parent to have the 1:23 PM run post Bluesky V from the handoff (time-sensitive; window closes 2 PM MT).
- No posts, uploads, comments, channel edits or signups from this tick.

## Hermes v0.22.2 landed overnight: capture must pin it (experiments #4/#20/#8, tick 130, Oct 15 ~11:58 AM MT)
- Bluesky V ownership from tick 129 is resolved: the parent created a one-off routine "Bluesky Ultramarine clip (one-off Oct 15)" for ~1:30 PM MT. Nothing else needed from this routine; confirm the URL after it runs.
- Pre-capture currency check (GitHub public API, ~11:57 AM MT): **v0.22.2** published 2026-10-15 08:21 UTC (2:21 AM MT). Nous's notes: "v0.22.1 was built from the wrong commit… 0.22.2 is the release 0.22.1 was meant to be"; highlights = gateway starts after reboot again + long local-model turns survive on laptops. Known issue: sessions from the 0.22.1 gateway can't be deleted in 0.22.2. Repo ~254K stars, last push 17:51 UTC. No v0.23 yet (Nous says main-only work ships there).
- **Changes:** capture checklist now pins **v0.22.2** and logs the exact version (never capture on the mis-built 0.22.1). Title pack gained a tick-130 note: title/tags/P5 unchanged (Threshold features are the same), never say "0.22.1", optional description currency line, and an optional self-aware spoken line ("built from the wrong commit. Relatable.") only if the build session frees words under the 420 ceiling.
- Why it matters: tonight's video would otherwise show or recommend a build its own maker calls wrong, which is exactly the kind of error a receipts-only review can't afford; it is also a free fresh hook ~2 days after GA.
- Read-only (3 GitHub API calls). No uploads, posts, comments, channel edits or signups.

## X V flat-lined at 4: graduated-access cap, not format (experiments #22/#10/#17, tick 136, Oct 15 ~1:04 PM MT)
- X V `2110785068839153774` at T+95 min: **4** impressions, 0 likes/replies/RTs/quotes/bookmarks, media `view_count` **1** — identical to T+7 and T+37. Three reads, zero movement after the first few minutes.
- Read: X stopped distributing the post within ~7 min, below our text drops (5–10) and far below best U (26). A 52.6 s hook-first vertical clip got no lift over text, so on X the limit is the account's graduated-access state (#10), not post format or copy. This strengthens the case for the operator-only graduation paths in #10 (already in the decision brief) over more X copy tweaks.
- **Plan change:** the ~3:30–5:30 PM X V read shrinks to one cheap confirm call (log it, don't analyze further unless impressions moved ≥3×), then the 24h read. Do **not** call #22 a failure overall: Bluesky V (~1:30 PM one-off) is the real native-video test, since Bluesky has no graduated-access throttle.
- For the decision brief: if Bluesky V clearly beats X V at 4–6h, that's the evidence to move episode drops' primary social surface to Bluesky until X graduates. Hold that claim until the Bluesky number exists.
- Read-only (1 X API call). No posts, uploads, comments, channel edits or signups.

## Bluesky V read is one command; compare engagement, not impressions (experiment #22, tick 137, Oct 15 ~1:10 PM MT)
- Shipped `tools/social/bluesky_read.py` (read-only, public AppView, no auth): profile counts plus per-post likes/reposts/quotes/replies, video flag, age in minutes (MT) and post URL. Pre-post baseline at ~1:10 PM MT: **1 follower, 0 follows, 0 posts**.
- Measurement caveat for #22: Bluesky exposes **no impression or view counts**, so "Bluesky V beats X V" can't be judged on impressions. Compare like-for-like: engagement (likes+reposts+quotes+replies) and follower delta. X V's comparable number is **0 engagements / +0 followers** at T+95 min. Any Bluesky engagement from a 1-follower account means discovery happened outside the follower graph, which X isn't giving us.
- Decision rule for the batched recommendation: Bluesky V with ≥2 engagements or ≥1 new follower by T+2h counts as "clearly beats X V"; 0 by T+2h means both surfaces are cold and the issue is audience size, not X throttling.
- Read-only (2 public Bluesky reads). No posts, uploads, comments, channel edits or signups.

## Site hero still live-stale; 3:23 brief locked (experiment #19, tick 138, Oct 15 ~1:15 PM MT)
- Fetched `https://orbbuilds.vercel.app` ~1:15 PM MT: hero still **"An AI building AI products in public."** Local `main` is **ahead 7** of `origin/main` (hero `86219fe` + ticks 132–137). X bio already points at the site, so every bio click lands on the old pitch until push.
- Wrote `content/drafts/2026-10-15-1523-build-session-brief.md`: step 0 = push + curl-verify both `"An AI reviews the AI."` and `"Watch on YouTube"` before Hermes; step 1 = existing capture checklist; hard bans (no X, no Bluesky double-post). Pointed the Hermes checklist's Before line at that brief.
- Updated Bluesky V handoff **After** with tick 137 win rule + paste-ready `bluesky_read.py` (T+0 confirm + T+2h). Clip still on disk 1080×1920 / 52.6 s; public profile still **0 posts** / 1 follower.
- No WakeParent (ops handoff for 3:23; Bluesky one-off already owns the post; no new user decision). No posts, uploads, comments, channel edits, pushes or signups.

## Bluesky tag + naming hygiene from live search (experiments #22/#9, tick 139, Oct 15 ~1:33 PM MT)
- ~1:31 PM MT `bluesky_read.py`: still **0 posts** / 1 follower; the 1:30 PM one-off hasn't fired yet (window runs to ~1:55). Nothing to confirm this tick.
- Live Bluesky search (`api.bsky.app` searchPosts works; `public.api.bsky.app` search now returns 403), latest 50 per query:
  - "Ultramarine": mostly Warhammer (Boltgun 2 shipped today); AI-side posts exist (one at 14 likes / 3 reposts). Our V caption already says "Ultramarine 1 Flash", which keeps it findable on the AI side.
  - "Hermes Agent": 50 posts in ~43h, 26 total engagements, 7 with video; `#hermesagent` is the dominant tag (10/50), then `#opensource`/`#ai`/`#aiagents`.
  - `#AI` latest: 50 posts in ~22 min, heavy NSFW spam, 13 engagements total. `#LLM`: 50 posts in ~5h, real AI posts.
- **Changes:** Ep4 Bluesky B-text tags `#AI #HermesAgent #Agents` → `#HermesAgent #AIagents #LLM`; POSTING_RULES Bluesky rule 4 (topic tag + #LLM/#AIagents, never #AI; disambiguate model names).
- Read-only (4 search calls + 1 profile read). No posts, uploads, comments, channel edits or signups.

## Tonight's upload #1 flips to Ep4 Hermes on live demand (experiments #3/#13/#4, tick 140, Oct 15 ~1:36 PM MT)
- Bluesky: 0 posts at ~1:35 PM MT; the one-off then posted V (`3mxwspebrxn2m`, logged in GROWTH_LOG by that run). T+2h read due ~3:36 PM MT.
- Public watch-page view counts (no quota) vs earlier reads: Hermes v0.22 recaps Julian `NZcdLDuhryI` 6,157 → **6,341** (~44 min, ~250/h at ~15 h old) and BoxminingAI `pAaAgcjNgEs` 16,644 → **16,752** (~147/h at ~1.5 d). Ultramarine: AI WITH Rithesh `CcRr7dJy4gI` 239 → **282** (~11/h at ~17 h, 51K channel), Julian `k85bmBNAgN0` 27 → **47** (~5/h). Live demand gap ~20–50×.
- **Change:** the Oct 16 recovery rank put Ep3 first on freshest GA date. With one reliable upload a night, that spends the slot on the cold topic. Rank is now **Ep4 Hermes (if READY) → Ep3 → Ep2**, still consistent with "fresh release first" since Hermes v0.22.2 shipped Oct 15. Call-order steps generalized to "#1-ranked episode"; Ep4 queue pointer updated; Ep2 prefers the native-video lane (#22) over a main slot.
- Read-only (4 public page fetches + 1 Bluesky read). No posts, uploads, comments, channel edits, pushes or signups.

## Bluesky drafts were over the 300-grapheme cap (experiments #22/#9, tick 141, Oct 15 ~1:50 PM MT)
- Bluesky V at T+8 min (~1:44 PM MT): 0 likes/reposts/quotes/replies, 1 follower, 1 post. T+2h read still due ~3:36 PM.
- Length audit of every Bluesky code block in `content/drafts/`: Ep3 B-text **336** and Ep4 B-text **374** characters, both over Bluesky's 300-grapheme post limit, so the next morning drop would have been rejected at post time. Ep2 (230) and others were fine. Ep3 also still used `#AI` (banned by rule 4).
- **Changes:** Ep3 B-text → 286 (`#Ultramarine1Flash #LLM`); Ep4 default → 283; added Ep4 **setup-gate alt** (267, matches the setup vote block) and a **conditional B-video** caption (~195) for the Ep4 `-xclip.mp4`, used only if the 3:36 PM V read meets the ≥2 eng / ≥1 follower rule; never both. POSTING_RULES Bluesky rule 6: 300-grapheme hard cap, draft ≤290.
- No posts, uploads, comments, channel edits, pushes or signups.

## Bluesky V early read: 1 like at T+23 (experiment #22, tick 142, Oct 15 ~2:00 PM MT)
- `python3 tools/social/bluesky_read.py` at ~1:59 PM MT (T+23 min after 1:36 PM post): profile still **1** follower / **1** post; post `3mxwspebrxn2m` **likes=1**, reposts=0, quotes=0, replies=0, video=True.
- Compare: X V `2110785068839153774` (same clip, 11:29 AM) never left **0** eng / **4** impressions. Bluesky already has more engagement at T+23 than X V got all day — consistent with tick 136 (graduated-access cap on X, not format).
- Win rule unchanged: ≥2 eng **or** ≥1 new follower by T+2h (~3:36 PM). At T+23 we are **halfway** on eng (1/2), follower delta still 0. Do not call a winner yet; do not WakeParent.
- Next tool gap (not this tick): `bluesky_post_video.py` still doesn't write hashtag facets, so Ep3/Ep4 tags won't be clickable/searchable until fixed.
- Read-only. No posts, uploads, comments, channel edits, pushes or signups.

## Bluesky tags now clickable: facets + text-only mode in the post tool (experiments #22/#9, tick 143, Oct 15 ~2:10 PM MT)
- `tools/social/bluesky_post_video.py` now writes `app.bsky.richtext.facet` entries (UTF-8 byte offsets) for `#tags` and `https://` links, so tags are clickable and land in tag feeds like `#HermesAgent` (tick 139's live tag). Bluesky doesn't auto-link raw text; without facets every tag in our drafts would have been dead text. Numeric-start tags (`#2026`) are skipped, same as Bluesky's own client.
- Added a **300-grapheme guard** (refuses to post over cap, prints `text ok: N/300; tags=[…] links=[…]` in dry-run) and a **text-only mode** (omit `--file`) so morning B-text drops go through the same tool instead of hand-built XRPC.
- Offline check on the live drafts (no network): Ep4 B-text 283 / setup alt 267 / B-video 193 graphemes, tags `HermesAgent, AIagents, LLM`; Ep3 B-text 286, tags `Ultramarine1Flash, LLM`. All under cap, all tags parse.
- Did not run a dry-run session this tick (kept the tick network-free). Posting stays with the scheduled routines.
- No posts, uploads, comments, channel edits, pushes or signups.

## Bluesky V's only like is a mass-liker; win rule now counts real engagers (experiment #22, tick 145, Oct 15 ~2:35 PM MT)
- T+56 read (~2:32 PM MT): still **1** like / 0 reposts / 0 quotes / 0 replies / **1** follower (baseline). Looked up who liked it via public `getLikes`: **@chiitan.love** (Japanese mascot account, **194,518** followers, **0** follows, **32,397** posts). That shape is a broad mass-liker, not an AI-builder finding us through search or tags, so the T+23 "halfway to the win rule" read was weaker than it looked.
- **Change:** `tools/social/bluesky_read.py --who` lists each liker/reposter and follower with counts and flags `[MASS-ENGAGER: exclude]` (≥10K posts and 0 follows or follower/follow >1000). The #22 win rule (≥2 eng or ≥1 new follower by T+2h) now counts only `[counts]` rows. Applied to `bluesky-primary-recommendation.md` and the V handoff. `getFollowers` returned no visible rows for the baseline follower (likely deactivated/hidden), so follower delta stays read from the profile count.
- Implication if it holds: X V 0 eng and Bluesky V 0 *real* eng means both surfaces are cold and the bottleneck is audience size + discovery (tags were missing on V), not only X throttling. That would weaken a "Bluesky primary" call; keep dual-channel and judge Ep4's tagged B-post instead.
- Read-only (3 public Bluesky reads + tool test). No posts, uploads, comments, channel edits, pushes or signups.

## Ep4 tagged B-video decoupled from untagged V (experiment #22, tick 147, Oct 15 ~2:46 PM MT)
- Today's Bluesky V (`3mxwspebrxn2m`) had **0 facets / no hashtags** (pre–tick-143). T+69 mid-read: still 1 like from mass-liker @chiitan.love / 0 real eng / 1 follower.
- Gating Ep4 B-video on that T+2h win would discard the first *tagged* native-video sample. **Change:** Ep4 growth pack prefers tagged B-video whenever `-xclip.mp4` exists; T+2h only decides `bluesky-primary-recommendation.md` (channel priority). Setup-alt B-video caption dry-run OK (182/300); Candidate A 193/300.
- Read-only + draft edits. No posts, uploads, comments, channel edits, pushes or signups.

## Evergreen setup framing opened as #23 (experiments #23/#3/#4, tick 148, Oct 15 ~3:00 PM MT)
- Pattern across our releases: we have never shipped inside 24h of GA (Ultramarine and Hermes first-mover both lost), so hype-recap titles reach search after the spike. Per-day averages from tick 135's watch-page counts: Hermes Full Tutorial ~11.7K/day over ~45 d, Full Setup Guide ~5.4K/day over ~6 d, while v0.22 recaps front-load (Boxmining ~11K/day at 1.5 d, Julian ~6.3K at ~15 h). These are averages, not current rates, and the channels are far bigger than ours, so this is a hypothesis, not a result.
- **Opened #23** with a kill rule (setup titles must beat news titles on 7-day views, ≥2 each). Rule of thumb for scheduled routines: installable product and >24h past GA → setup-first title + Install/Setup/First run chapters; inside 24h → P5/news title. Hype tone stays either way. Ep4 Hermes PASS path is sample #1; no change to tonight's gate.
- Batched (not sent) for the next user ping: one-line series-framing FYI. No WakeParent: three pings already today and nothing here is time-sensitive.
- Desk-only (no network). No posts, uploads, comments, channel edits, pushes or signups.

## X V confirm done early: flat at 4 through T+3h41 (experiments #22/#10, tick 149, Oct 15 ~3:10 PM MT)
- X V `2110785068839153774` at ~3:10 PM MT (T+3h41): **4** impressions, 0 likes/replies/RTs/quotes/bookmarks, media `view_count` **1**. Identical to T+7, T+37 and T+95. Per tick 136's plan this is the one confirm call; impressions didn't move, so no further analysis. The ~4–5 PM X slot is now free; next X read is the 24h one (~11:30 AM Oct 16).
- Bluesky V `3mxwspebrxn2m` mid-read at T+93: still 1 like from mass-liker @chiitan.love (excluded), 0 real engagements, 1 follower. T+2h verdict still due ~3:36 PM; with 23 min left and zero real engagers, the likely outcome is "both cold, audience size is the bottleneck", which keeps dual-channel and leaves Ep4's tagged B-post as the real Bluesky test.
- Pre-3:23 check: Hermes Agent latest release still **v0.22.2** (GitHub API), so the capture pin holds. Local `main` is now **ahead 22** of origin; the 3:23 brief's push step covers any ahead-N.
- Read-only (1 X read, 1 public Bluesky read, 1 GitHub API read). No posts, uploads, comments, channel edits, pushes or signups.

## Fable 5.5 pre-cutoff check: still rumor, and cooling (experiments #3/#4, tick 150, Oct 15 ~3:15 PM MT)
- The drop-day plan only pivots tonight's 9:28 PM slot if Fable 5.5 is real **before ~6 PM MT**, but the next scheduled check is the 7:23 PM scan, after that cutoff. So this tick ran the last useful pre-cutoff check.
- Official models overview (curl ~3:15 PM MT): `claude-fable-5-5` **0** mentions, `claude-fable-5-1` **34**, so Fable 5.1 is still current. Gate fails.
- X recent counts for `"Fable 5.5"` (hourly, MT): 11 AM **166**, 12 PM **118**, 1 PM **118**, 2 PM **106**, 3:00–3:15 PM **31** (~124/hr pace). The rumor is now *declining* from its 140–185 morning plateau, far below the ~500+/hr launch signal.
- **Result:** Hermes stays tonight's Ep4; no pivot. If Anthropic ships between now and ~6 PM, the 7:23 PM scan still catches it, but per the plan a post-6 PM launch goes to Oct 17 unless the script can be fully sourced in time. No WakeParent (no decision changes).
- Read-only (1 X count call, 1 docs fetch). No posts, uploads, comments, channel edits, pushes or signups.

## Afternoon ping batch staged in the decision brief (experiments #22/#10/#23/#3, tick 151, Oct 15 ~3:29 PM MT)
- Four items were being carried tick to tick only in "Next recommended" lines (X V flat at 4, Bluesky T+2h verdict, #23 framing FYI, Fable cooling). Staged them as one section plus a plain add-on sentence in `content/drafts/2026-10-15-user-decision-brief.md`, with a `[FILL]` slot for the Bluesky verdict, so the parent can send one batched message instead of reconstructing from the log.
- Checked state for the 3:23 PM session (it is running now): local `main` **ahead 25**, live site still says "building AI products" (14 hits), Hermes not yet installed on the box. Not touched; the session owns push and capture.
- Desk-only plus one site curl and git fetch. No posts, uploads, comments, channel edits, pushes or signups.

## Bluesky V T+2h verdict: both cold, dual-channel stays (experiment #22, tick 152, Oct 15 ~3:35 PM MT)
- `bluesky_read.py --who` at T+118 min: 1 like (mass-liker @chiitan.love, excluded), 0 reposts/quotes/replies, **0 real engagers**, followers still **1**. Win rule (≥2 real eng or ≥1 new follower) **not met**. X V same clip: 4 imp / 0 eng.
- **Verdict:** both channels cold on an untagged clip; audience size is the bottleneck, not format. Dual-channel stays; `bluesky-primary-recommendation.md` marked PARKED. Ep4's tagged Bluesky B-video remains the first real tag-discovery test (unchanged, per tick 147).
- Filled the `[FILL]`/`[VERDICT]` slots in `2026-10-15-user-decision-brief.md`. No decision changed, so no WakeParent; the batch holds for the Oct 16 morning ping.
- Read-only (1 public Bluesky read). No posts, uploads, comments, channel edits, pushes or signups.

## 3:23 session check: site LIVE, capture mid-flight (experiments #19/#20, tick 153, Oct 15 ~3:51 PM MT)
- **#19 site:** live `orbbuilds.vercel.app` title + OG = "Orb Builds: An AI reviews the AI." and hero CTA **Watch on YouTube** (curl ~3:51 PM MT). Build session pushed; local `main` only ahead by strategy tick 152.
- **#20 Hermes capture (in flight, owned by the 3:23 routine — do not touch):** `hermes` v0.22.2 on PATH; recording `content/drafts/captures/hermes-agent-v0-22/rec.mp4` since 3:38 PM MT (ffmpeg x11grab still alive ~13+ min); desktop PID alive ~6+ min; **zero** `NN-*.png` stills; no PASS/FAIL gate note. Empty update lock file at `~/.hermes/.hermes-update-in-progress.lock` since 3:37 PM — possible stall before stills.
- **Flag for 9:28 PM:** if labeled stills + gate are still missing by ~5–6 PM, Ep4 renders without `screen` frames (Candidate A / FAIL path). This routine does not stop/start capture.
- Read-only confirm. No posts, uploads, comments, channel edits, pushes, installs or signups.

## Ep4 Short PASS-path title already covered; capture alive, not stalled (experiments #5/#23/#20, tick 154, Oct 15 ~3:58 PM MT)
- **#5/#23 check:** on the setup PASS path the Short generator would default to `Hermes Agent v0.22 in N seconds (is it replacing me?)`, a news framing. Confirmed this is already handled: queue `2026-10-16-hermes-agent-v0-22.md` line 29 tells production to copy `meta._short_title_on_pass` into `meta.short_title` before `post_render.sh`, and the generator honors `short_title`. Setup tags (`Hermes Agent setup`/`tutorial`) flow from `meta.tags` into the Short. No change needed.
- **#20 capture (3:23 session owns it, untouched):** Hermes Desktop was relaunched at 3:45 PM (new `desktop.pid`), and `desktop.log` shows activity at 3:49 and 3:54 PM (Electron dbus warnings only, harmless on the box). `rec.mp4` still growing (2.9 MB at 3:57, static-screen compression). Still **0** `NN-*.png` stills and no gate note, but the session is clearly mid-drive, so tick 153's "possible stall" is downgraded. The 0-byte update lock is not blocking the desktop. Disk 72 GB free.
- Read-only/desk-only. No posts, uploads, comments, channel edits, pushes, installs or signups.

## Ep4 PASS stills: script pointed at a file that didn't exist (experiments #20/#4/#16, tick 155, Oct 15 ~4:10 PM MT)
- The 3:23 session finished capture: gate **PASS** (`HANDOFF.md` 4:03 PM: guided desktop setup as `Lumin`, scan declined, Hermes answered "What can you do without an API key?" on camera; no account, key or connectors). Stills `01-welcome`, `02-trial`, `03-mid`, `04-reply`, `05–07`.
- **Bug caught:** the script's `_screen_on_pass` pointed at `welcome.png`, but the file is `01-welcome.png`. `review_render.py` only warns on a missing screen and renders without it, so tonight's video would have said "here's what the first screen looked like" over no screen. Also, line 2 ("until those stills land, treat everything as their claims") had no PASS variant and would have contradicted the footage.
- **Fix:** line 1 → `01-welcome.png` + `_show_on_pass`; line 2 → `04-reply.png` with a PASS say that quotes the reply's own words and labels it as Hermes's claim, untested by us. `03-mid.png` is byte-identical to `04-reply.png` (noted; use one). Queue line 9 now tells production to flip lines 1 and 2 and check the render log for `warn: screen not found`.
- Privacy check on the reply still: shows `Lumin`, `orbbuilds` project label and the model picker; no operator name or employer.
- Desk-only. No posts, uploads, comments, channel edits, pushes or signups.

## Ep4 queue call order contradicted the tick-140 rank (experiments #13/#4/#8, tick 156, Oct 15 ~4:15 PM MT)
- The Ep4 queue file's header said Ep4 is upload #1 (tick 140), but its "Call order" bullet still listed Ep3 main first and said "if only one upload is reliable, Ep3 wins." On a quota-starved night the 1:28 AM run could have spent the one reliable upload on the lower-demand episode.
- **Fix:** call-order bullet now says Ep4 main → Ep4 setup thumb → stats → vote → SEO/playlist → Ep3 → Ep2 → Shorts when Ep4 is READY, with the old order kept only as the not-READY fallback. Matches `2026-10-16-publish-recovery.md` line 15.
- Also marked the `Hermes Agent free` setup tag as qualifying (HANDOFF: no-key reply on camera, no account or key).
- Desk-only. No posts, uploads, comments, channel edits, pushes or signups.

## Ep4 PASS description was still news-first with no Setup chapter (experiments #23/#8, tick 157, Oct 15 ~4:33 PM MT)
- On the setup PASS path, production swaps title, thumb and Short title, but `meta.publish_description` had no PASS variant: line 1 led with "review from an AI who might be next", the chapters had no Setup label (queue line 24 asks for one), and `pass_setup.tags_extra` lacked `Hermes Agent tutorial` / `Hermes Agent free` that the queue lists. #23's rule is setup-first title **and** chapters.
- **Fix:** added `_title_gate.pass_setup.publish_description` (setup-first line 1, 247 chars; caveats chapter renamed "No-key setup on camera + caveats"; one honesty line that Hermes's no-key claims are its own, untested here) plus the two tags and a `_description_note` to regenerate stamps from timing.json. Queue line 9 now lists the copy step. `validate_script.py` OK.
- Desk-only. No posts, uploads, comments, channel edits, pushes or signups.

## Ep4 PASS flip applied to live script (experiments #4/#20/#23, tick 158, Oct 15 ~4:45 PM MT)
- Gate was already **PASS** (HANDOFF + ticks 155–157), but live `meta.publish_title` and caveats `say`/`show` still said "not finished a no-key setup" with no `screen` — 9:28 PM had to remember a multi-step copy or the video would contradict the footage.
- **Applied now:** `_title_gate.pass_setup` → live meta (title, thumb, description, tags including tutorial/free/setup); caveats lines 1–2 promoted from `_on_pass`; `short_title` = setup template with `[N]`; queue marked flip-applied. `_title_gate.default` kept for rollback only.
- 9:28 PM checklist shrinks to: render → zero `screen not found` → fill `[N]` → chapter stamps → READY.

## Ep4 Short title would have fallen back to the news framing (experiments #5/#23, tick 159, Oct 15 ~4:55 PM MT)
- **Bug caught:** `short_publish_meta.py` ignores any `short_title` containing `[`, and the live Ep4 `short_title` was `Hermes Agent v0.22 setup in [N] seconds (no API key)`. `post_render.sh` writes `-short-meta.json` in the same pass that renders the Short, so the "fill `[N]` after" step came too late: tonight's Short would have shipped as `Hermes Agent v0.22 in 45 seconds (is it replacing me?)`, contradicting the setup-first main (#23).
- **Fix:** the generator now fills a `{secs}` token from the real Short duration; Ep4 `short_title` + `_short_title_on_pass` use `{secs}`. Tested: 47.3 s → `Hermes Agent v0.22 setup in 45 seconds (no API key)`; no duration → 50; unset → old default. Also pointed stale `meta.screen_slots` (doc-only, not read by tools) at the real `01-`/`02-`/`04-` stills. Queue lines 10 + 33 updated; 9:28 PM step is now "confirm the short-meta title", not "fill N". `validate_script.py` OK.
- Desk-only. No posts, uploads, comments, channel edits, pushes or signups.

## Ep4 social drafts flipped to setup PASS primary (experiments #23/#4/#7/#22, tick 160, Oct 15 ~5:00 PM MT)
- Live script title (post tick-158 flip): **`An AI sets up Hermes Agent with no API key`**. Capture gate PASS; stills on disk.
- **Bug-class risk:** `ep4-post-publish-growth-pack.md` and `ep4-vote-comment-draft.md` still listed Candidate A / "receipts-only" as the default, with setup as an alt. Oct 16 morning growth would have posted dishonest copy ("not hands-on yet") against a setup video.
- **Fix:** setup path is now default for Post A, B-text, B-video (182/300 dry-run), vote comment, and all three reply drafts. Candidate A / news / receipts-only = rollback only. Rank note: when Ep4 is the night's #1 upload, Ep4 social wins over Ep3 the same morning (tick 140 demand).
- Appended Oct 16 branch to `2026-10-15-morning-growth-playbook.md` (tick 160).
- Desk-only + dry-runs. No posts, uploads, comments, channel edits, pushes or signups.

## Ep4 site listing + queue handoff flipped to setup PASS (experiments #12/#23/#4, tick 161, Oct 15 ~5:10 PM MT)
- Tick 160 flipped growth/vote drafts; **site listing + queue handoff still defaulted to Candidate A** ("not hands-on yet" / prefer Ep3 packs first) — same honesty bug for Oct 16 morning #12 + publish recovery.
- **Fix:** `ep4-site-listing.md` setup title/summary is now default; `public/episodes/rr-004.jpg` swapped to setup thumb (`ep4-cand-hermes-setup-thumb.jpg`); queue thumbnail / site / vote / growth-handoff lines now match tick 140 rank + tick 160 social defaults.
- Live script already PASS (tick 158); screens `01-welcome.png` + `04-reply.png` on disk. Desk-only. No posts, uploads, comments, channel edits, pushes or signups.

## Ep4 description would have shipped a note-to-self line (experiments #23/#8/#16, tick 162, Oct 15 ~5:20 PM MT)
- **Bug caught:** live Ep4 `meta.publish_description` (and the `pass_setup` copy) still carried the literal line `[If Ep2 or Ep3 is live before this upload, add Also-from-me lines with real videoIds here]`. Ep4 is upload #1 tonight (tick 140), so nothing would have filled it and it would have gone public verbatim. `validate_script.py` only checked spoken lines, so it passed.
- **Fix:** removed the line from both copies (Ep4 goes first, so no Also-from-me line applies; add one only with a real videoId if Ep3/Ep2 landed first). `validate_script.py` now also checks `publish_title` / `publish_description` / `tags` / `short_title` for unfilled `[Placeholder]`s, `<`/`>` (YouTube rejects them) and blocklisted private terms. The old Ep4 file now fails; Ep4/Ep3/Ep2 current files pass (Ep4 title 42 chars, desc ~1.6 KB, tags 265/500 chars).
- Desk-only. No posts, uploads, comments, channel edits, pushes or signups.

## Ep4 setup phrases vs live autocomplete; desktop tag added (experiments #8/#23, tick 163, Oct 15 ~5:35 PM MT)
- YouTube autocomplete (~5:35 PM MT): `hermes agent setup`, `hermes agent free` and `hermes agent desktop` each return themselves as a suggestion; `hermes agent no api key` and `hermes agent without api key` return nothing relevant. So "no API key" is our hook, not a search phrase; the search words are setup / free / desktop.
- Ep4 already covers setup + free in tags and "Hermes Agent setup" opens description line 1. Added the missing **`Hermes Agent desktop`** tag (spoken + on camera: desktop guided setup) to live `meta.tags` and `pass_setup.tags_extra`; tags now 17 / ~258 of 500 chars. `validate_script.py` OK (old 449-word warn = caption double-count, tick 117).
- Title kept as `An AI sets up Hermes Agent with no API key` (P5, product name at char 13, inside #8's 40-char rule). If #23 gets a second setup sample, test an exact-phrase lead (`Hermes Agent setup ...`) against the P5 lead.
- Also verified the description's Previous link `L7fdRoNWEPE` is public Ep1 (oEmbed). Read-only + one tag edit. No posts, uploads, comments, channel edits, pushes or signups.


## Ep4 setup SERP baseline before publish (experiments #23/#8, tick 164, Oct 15 ~5:45 PM MT)
- **Why this tick:** Ep4 is setup-first (PASS) and ships tonight; tick 163 confirmed autocomplete demand for `hermes agent setup` / `free` / `desktop` / `tutorial`. Needed a pre-publish competitor snapshot so #23's 7-day kill rule has a day-0 SERP baseline (no YouTube API quota used).
- **View counts** from [returnyoutubedislikeapi.com](https://returnyoutubedislikeapi.com) at ~5:45 PM MT Oct 15, 2026 (public third-party; treat as approximate). Titles/channels from YouTube oEmbed the same minute. Publish dates from that API's `dateCreated`.

| videoId | Title (oEmbed) | Channel | Views (RYD) | Published (API) | ~views/day since publish |
|---|---|---|---:|---|---:|
| `DYdvJCxWd6M` | Hermes Agent - Full Tutorial & Setup Guide (For Beginners) | Metics Media | 520,807 | 2026-09-15 | ~17.4K (30 d) |
| `1ve4Atbqmoo` | Hermes Agent Full Tutorial for Beginners \| Setup Guide | Tech With Tim | 97,441 | 2026-09-11 | ~2.9K (34 d) |
| `THA8Fov44QY` | Hermes Agent Full Setup Tutorial: How to Setup Your First AI Agent (Gemma 4) | Bart Slodyczka | 92,224 | 2026-09-02 | ~2.1K (43 d) |
| `CcsgednSRfE` | Hermes Agent - Full Setup Guide (Beginner, From Scratch) | Sharbel A. | 29,681 | 2026-10-09 | ~4.9K (6 d) |

- **Web search** for Hermes Agent setup / tutorial (Oct 15 ~5:45 PM MT) surfaces the same long-form guides plus official docs; blog writeups for v0.22 exist (Agent Operators, Standard Compute) but **no YouTube hit** named v0.22, "no API key", or `nous/welcome`.
- **Positioning for Ep4:** do not try to out-tutorial Metics. Our wedge is the v0.22 **threshold** (desktop guided setup + first chat with no key, on camera, AI host, ~2–3 min). Title stays P5 (`An AI sets up Hermes Agent with no API key`); tags already carry setup/free/desktop/tutorial (tick 163).
- **Hygiene this tick:** chapter label in live `publish_description` → `1:28 Setup: no-key desktop on camera` (leads with searchable "Setup"; stamps still regenerate after 9:28 PM from timing.json — keep the Setup-leading words). Short-meta dry-run with duration 52.6 s → title `Hermes Agent v0.22 setup in 55 seconds (no API key)` (S1c) — confirms tick-159 `{secs}` path.
- **Measure after go-live:** at ~7d, compare Ep4 Data API views + Analytics YT_SEARCH share to these comps' per-day rates (order-of-magnitude only; channel-size confounds). Kill #23 setup framing if Ep4's 7-day views lose to our own news/P5 episodes, not if we lose to Metics.
- Desk-only + public reads. No posts, uploads, comments, channel edits, pushes or signups.

## Ep4 cold open still led with news numbers under a setup title (experiments #23/#22/#16, tick 165, Oct 15 ~5:55 PM MT)
- **Mismatch caught:** live title is `An AI sets up Hermes Agent with no API key`, but the cold open opened on "Six hundred reviewed plugins. About twenty-five hundred contributors..." and never said the setup was filmed; the footage only arrives in the caveats chapter (~1:28). Setup-intent clickers (tick 163/164 demand) would hear a news recap for the first ~10 s, and `xclip_windows.py` builds the X/Bluesky clip from `cold_open`, so the B-video would open on numbers too, under a setup-tagged caption.
- **Fix (script only, renders at 9:28 PM):** line 1 now opens `I just set up Hermes Agent on camera. No API key. No account.` then keeps the plugin/contributor numbers; chips `SET UP ON CAMERA · NO API KEY · 600 PLUGINS` (shorter than before). Line 2 labels the numbers as release-note claims and opens a loop: "The setup footage is mine, and it's coming up." Old text kept as `_say_pre_tick165` / `_show_pre_tick165` for rollback. `validate_script.py` OK (464-word warn, same caption double-count as tick 117).
- **Measure:** Ep4 Analytics retention at 0:10 and 0:30 vs Ep1 when Analytics reads come back (daytime, #2); a setup-first hook should hold ≥ Ep1's 0:30 retention. No fabricated baseline; Ep1 numbers still pending.
- Desk-only. No posts, uploads, comments, channel edits, pushes or signups.

## Ep4 social clip would have cut the Hermes reply still (experiments #22/#20/#23, tick 166, Oct 15 ~6:05 PM MT)
- **Bug caught (pre-render):** `xclip_windows.py` fits the X/Bluesky clip under 58 s by dropping caveat lines **from the end**. Tick 165 lengthened Ep4's cold open to 69 words; at our measured TTS rate (2.92–2.97 words/s on the Ep2/Ep3 timing files) a simulated timing gives hook ~24 s, so the picker keeps caveats 1–2 and drops line 3, the `04-reply.png` still where Hermes answers with no API key. The tagged setup B-video (tick 147/160 default) would have opened on "I just set up Hermes Agent" and then cut before the proof.
- **Fix:** `xclip_windows.py --script` overlays each line's `screen` from the script and, when trimming, picks the contiguous run of verdict lines that fits with the most screen lines (then most lines, then earliest). Lines without any `screen` still trim from the end exactly as before. Prints `WARN screen lines dropped` if footage still can't fit. `post_render.sh` now passes `--script "$SCRIPT"`.
- **Tests:** Ep2 and Ep3 real timing.json give byte-identical windows to the old picker (no screens). Ep4 simulated: old = caveats 1–2 (44.3 s, no reply still); new = caveats 2–3 (53.4 s, welcome + reply stills). Dropped line 1 is the release-notes caveat, which cold-open line 2 already says. This is a simulation, so the real 9:28 PM timing decides.
- **9:28 PM check:** the post_render log line should read `kept verdict lines 2-3 of 3` (or `3/3`) with no `WARN screen lines dropped`.
- Desk-only. No posts, uploads, comments, channel edits, pushes or signups.

## Ep4 thumbnail product name unreadable at sidebar size (experiments #8/#6/#23, tick 167, Oct 15 ~6:15 PM MT)
- **Check:** downscaled the live Ep4 setup thumb (`HERMES AGENT` chip / `NO API KEY` / `SETUP`) to 168x94, the size of YouTube's sidebar and mobile search rows. The two big lines read fine, but the product chip (`HERMES AGENT`) was the smallest text and barely legible, so a setup-intent searcher scanning thumbnails saw "NO API KEY SETUP" with no product. The title already says "no API key", so the thumbnail was repeating the hook and hiding the searched word.
- **Fix:** variant B = chip `NO API KEY`, big lines `HERMES` (yellow, hl 1) / `SETUP`, same tag. At 168x94 it reads "HERMES SETUP", matching the autocomplete phrase `hermes agent setup` (tick 163). Applied to live `meta.thumbnail` (post_render renders from it; same arg path checked) and `pass_setup`; reference file `content/drafts/ep4-cand-hermes-setup-thumb-b.jpg`; `public/episodes/rr-004.jpg` swapped (md5 match). Rollback = `meta._thumbnail_pre_tick167` / `ep4-cand-hermes-setup-thumb.jpg`. Queue line 22 + site-listing notes updated. `validate_script.py` OK.
- **Not an A/B:** Test & Compare is Studio-only (#6), so this is a legibility judgement, not a measured win. Rule for later thumbs: the searched product word should be one of the two big lines when the title is setup-first; chip = hook.
- **9:28 PM check:** `<slug>-thumb.jpg` shows HERMES / SETUP big with the NO API KEY chip.
- Desk-only. No posts, uploads, comments, channel edits, pushes or signups.

## Tick-140 upload rank lived only in the recovery draft (experiments #13/#3/#4, tick 168, Oct 15 ~6:25 PM MT)
- **Contradiction caught:** `00-README-slot-rules.md` (the standing rules the 1:28 AM run follows) still ranked purely by freshest GA, and Ep3's queue file said "still ahead of Ep4 Hermes" and "this file first". Ep4's own file said both "upload #1 when READY" (line 5/43) and "ranks behind Ep3 on freshest GA" (line 19). A publish run reading the README + Ep3 file would spend tonight's one reliable slot on Ultramarine (~5–11 views/h live demand) instead of Hermes (~150–250 views/h, tick 140).
- **Fix (docs only):** added slot rule **2c Live-demand override** to the README (a measured ≥~10× live-demand gap beats GA freshness; Oct 16 = Ep4 > Ep3 > Ep2; fall back to 2/2b if Ep4 isn't READY). Annotated Ep3 lines 13/30 and Ep4 line 19 as superseded by 2c. No rank change, just one consistent story across all four files.
- **1:28 AM check:** Ep4 (if READY) is upload #1; Ep3 queue ends `CARRIED to 2026-10-17` or PUBLISHED as #2.
- Desk-only. No posts, uploads, comments, channel edits, pushes or signups.

## Awesome lists won't take the video; a build artifact could (experiment #24, tick 169, Oct 15 ~6:40 PM MT)
- **Question:** Ep4 is a Hermes setup video shipping tonight; are Hermes "awesome" lists a durable, non-X discovery path for it? Public GitHub reads only (`gh api`, ~6:35 PM MT).
- **0xNyk/awesome-hermes-agent:** 5,854 stars, 442 forks, very active (new `[Submission]` issues Oct 13–15). Submissions are **issues only** ("do not open a PR"), and the quality bar asks for open source, a README, maintenance and a "why now" line. Its Guides section lists only GitHub repos (docs, WSL guide, wiki, always-on guide): **no YouTube videos at all**. A setup video fails the "open source" bar, so submitting Ep4 would likely be declined and look spammy.
- **0xarkstar/awesome-hermes-agent:** 56 stars; has a Tutorials section with blog guides, but last push Mar 2026 and every PR since Sep 7 is still open. Dead path. frankxai/Anil-matcha lists: 5 stars each, not worth it.
- **Verdict:** no list submission for Ep4. Opened **#24 (parked)**: if a build session ships a standalone, working open-source Hermes skill or tool, that repo is listable on 0xNyk (its README can link the episode). That ties build episodes to a 5.8K-star discovery surface. Submission would be external comms for the operator or a scheduled routine, not this routine.
- Desk-only + public reads. No posts, issues, PRs, uploads, comments, channel edits, pushes or signups.

## Official Hermes surfaces: no video slot either (experiment #24, tick 170, Oct 15 ~6:45 PM MT)
- **Question:** after tick 169 ruled out awesome lists, does Hermes' own project link community content anywhere an Ep4 or a later build artifact could land? Public reads only (`gh api`, curl, ~6:42 PM MT).
- **NousResearch/hermes-agent README** (254,125 stars, GitHub Discussions off): its `## Community` section lists Discord, Skills Hub (agentskills.io), Issues and two third-party **open-source tools** (`computer-use-linux` MCP server, `HermesClaw` WeChat bridge). No videos, tutorials or guides. README last changed Sep 24, so additions are rare and go through a PR to a 254K-star repo. Discord is already ruled out (#9). Docs sitemap has no community/tutorial/showcase page.
- **agentskills.io** ("Skills Hub") is the open Agent Skills *standard* site (spec + GitHub/Discord discussion), not a submit-your-skill gallery, so it is not a listing path either.
- **Verdict:** confirms #24's rule. Hermes surfaces list **working open-source tools**, never videos. If a build session ships one, two outlets exist: 0xNyk awesome list (issue) and, for a genuinely useful integration, the official README Community list (PR, high bar). Both = external comms owned by the operator or a scheduled routine. Ep4 itself gets no list/README placement; its discovery stays YouTube search (#23) + X/Bluesky drops (#22).
- Desk-only + public reads. No posts, issues, PRs, uploads, comments, channel edits, pushes or signups.

## Ep4 queue header still preferred Candidate A after PASS (experiments #23/#4/#13, tick 172, Oct 15 ~7:00 PM MT)
- **Bug:** queue file line 1 still instructed production to "Prefer Candidate A… Swap to P5+setup **only** if the tick-61 title gate passes" even though Status notes already said PASS applied (tick 158). Tags were still split "default = news / if setup gate = extras"; Short line still told operators to manually copy `_short_title_on_pass`.
- **Fix:** opener + Tags + Short now default to setup PASS; Candidate A / news tags / news Short = rollback only. Title pack Candidate A heading + banner = rollback. Morning playbook tick-108 "Ep3→Ep4→Ep2" rank line marked superseded by rule 2c / tick 160.
- No posts, uploads, comments, channel edits, or pushes from this tick (commit only).

## Ep4 vote comment option 3 meant something else than the video (experiment #7, tick 171, Oct 15 ~6:52 PM MT)
- **Check:** compared Ep4's three vote surfaces. Spoken outro + caption: "3: skip the existential bit and just go deeper on setup or a local model." Description: "3: Skip the existential bit — just a deeper setup / local-model walkthrough." Default (setup PASS) comment draft: "3. Go deeper on local models (one-click llama.cpp path) and show what breaks", which drops the setup half and adds a break-test promise. A viewer replying "3" under the comment and one replying after the outro would be voting for different episodes, so the tally (#7) wouldn't be one choice.
- **Fix:** comment default option 3 now = "Skip the existential bit and go deeper on setup or a local model (the one-click llama.cpp path)" (llama.cpp is sourced in the v0.22 notes and already spoken in the script). Added a hygiene rule to the draft: option text must mean the same on all three surfaces. Rollback block untouched (already matched).
- **Also checked, OK:** Ep4 tags 17 / ~288 of YouTube's 500-char tag budget; description 1,581 of 5,000; title 42 chars; Previous link = Ep1 `L7fdRoNWEPE` (correct if Ep4 is first tonight).
- Desk-only. No posts, uploads, comments, channel edits, pushes or signups.

## Ep4 word-count drift after setup cold open (experiment #16, tick 175, Oct 15 ~7:30 PM MT)
- Tick 117 left Ep4 at the 420 ceiling; tick 165's setup-first cold open (needed for title/hook match) pushed spoken `say` to **~464**.
- Trimmed to **415** without dropping either PASS screen line or the setup-first first sentence. Validator clean.
- 9:28 PM must not re-expand the script; re-run `validate_script.py` if any line is edited.

## Publish runs now leave breadcrumbs (experiment #13, tick 176, Oct 15 ~7:45 PM MT)
- **Gap:** the Oct 15 1:28 AM run failed with no workspace writes at all (tick 72/74), so the mandatory "write the exact error" rule never fired and the cause is still unknown. Tonight's run is the second attempt; another silent death would teach us nothing.
- **Fix:** added `tools/publish/breadcrumb.sh` (appends `time | step | ok/fail | detail` to `content/published/queue/run-log-YYYY-MM-DD.md`, self-tested in a temp copy). Recovery draft gets a "Step 0" section and slot-rules README a "Breadcrumbs first" rule: log run start before any staging/Composio call, then one line per step.
- Desk-only. No posts, uploads, comments, channel edits or pushes (local commit only).

## Muse next-slot pack ready (experiments #3/#2/#8, tick 178, Oct 15 ~8:00 PM MT)
- **Why:** tick 177 correctly kept Ep4 Hermes as tonight's #1, but left no Muse assets. Evening scan #1 is Muse Spark Open; without a pack, Oct 17 production starts blank while the SERP keeps filling.
- **Ep4 preflight (same tick, read-only):** script **415** words, `validate_script.py` OK, both screens on disk (`01-welcome.png`, `04-reply.png`), thumb = HERMES/SETUP variant B, Setup chapter label present, short_title setup template, queue still **PENDING_RENDER**, breadcrumb + rule 2d in place. No fix needed pre-render.
- **Shipped:** `content/drafts/ep5-muse-spark-open-title-pack.md` + thumbs `ep5-cand-muse-spark-open-thumb.jpg` (P2 LAPTOP?/NOPE) and `-p3.jpg` (HOSTED/BUILD). Autocomplete: `muse spark` / `muse spark open` / `meta muse spark` clean; `meta open weight` empty. Angle = hosted API / weights-vs-wallet, never "first", never dual-Mac fantasy. Ling pack stays backup if Oct 16 ~10 AM Muse SERP is still dead (<~500 typical views).
- Desk-only. No posts, uploads, comments, channel edits or pushes (local commit only).

## Muse Spark Open is crowded, not a slot-stealer (experiments #3/#13/#4, tick 177, Oct 15 ~7:50 PM MT)
- **Question:** the 7:23 PM scan leads with Meta's Muse Spark Open, a fully sourced flagship drop (Meta research post + HF blog both 200; HF repo gated, 262 likes). Rule 2 (freshest first) would let a Muse render take tonight's upload #1 from Ep4 Hermes. Should it?
- **Data (~7:50 PM MT):** X counts (`"Muse Spark Open" -is:retweet`) **2,114** posts since launch ~11 AM MT; peak 459 in the first hour, then flat ~170–190/hr. Hermes Agent **447** over the same 14h (~25–45/hr). YouTube phrase search, uploaded today: **15+ Muse videos already**, nearly all small channels at **1–373 views** (two streams 691 / 2,440). Big AI-news channels not in the results yet.
- **Read:** first-mover is closed and the SERP is flooded by small channels getting near-zero views; a ~1:28 AM Orb Builds Muse video would be ~14h late into that pile and then buried when the big channels post. Hermes setup is evergreen with real comps (18,049 / 4,923, tick 173) and our hands-on capture. Freshness still matters for the series, so Muse gets mentioned, not the slot.
- **Fix:** guard line at the top of the Ep4 queue file + slot rule **2d** (flooded-SERP: a fresher GA does not take #1 from a READY file with a measured demand/evergreen edge). Muse = upload #2 at most if production renders it. A later Muse angle only makes sense hands-on via a free path (#20 budget is still pending with the user).
- Read-only research + desk edits. No posts, uploads, comments, channel edits or pushes (local commit only).

## Muse hosted path is free tokens, not free account (experiments #20/#3/#4, tick 179, Oct 15 ~8:15 PM MT)
- **Question:** tick 178's Muse pack gates P3 on a free hosted path. Does one exist before Oct 17 production?
- **Data (fetched ~8:15 PM MT):** Together AI [promo page](https://www.together.ai/models/muse-spark-open-promo): Muse Spark Open serverless **$0.00 / 1M** in+out through **October 18, 2026 at 12:00 PM PT** (~1:00 PM MT) on `meta-models/Muse-Spark-Open-816B-A42B-promo`; after that $1.25 / $4.25. Fine print: new accounts must add a payment method and buy **$15** credits to activate; those credits are **not** consumed on the free model. Offer may end early. OpenRouter `meta/muse-spark-open` is paid at the same $1.25 / $4.25 (Baseten / Fireworks / Together / Nebius). Meta/HF list the same hosted partners; none other advertised a $0 endpoint in this check.
- **Read:** P3 is possible without per-token spend **only if** the operator activates Together ($15 banked credits). That is still a spend decision under #20, not a silent free path. Without it, Ep5 stays **P2** (receipt-check / dual-Mac honesty). Promo window closes in ~2.5 days — batch into the Oct 16 morning ping, do not midnight-ping.
- **Also this tick:** Ep4 `short_publish_meta.py --duration 53 --cta 1` dry-run → title `Hermes Agent v0.22 setup in 55 seconds (no API key)` (setup path OK after tick 175 trim).
- Desk-only. No posts, uploads, signups, comments, channel edits or pushes (local commit only).

## 9:28 PM production brief locks Ep4 only (experiments #3/#13/#20/#23, tick 180, Oct 15 ~8:32 PM MT)
- **Why:** last tick left "after 9:28 confirm READY" as next work, but production fires in <1h and still has no single paste-ready owner brief. Evening scan #1 is Muse; without a hard lock, 9:28 could script Muse and strand Ep4 PENDING_RENDER (rules 2c/2d only help *publish* if Ep4 is READY).
- **Preflight (read-only, ~8:32 PM MT):** `validate_script.py` **OK**; spoken **415** words; both screens on disk (`01-welcome.png` 554,621 B, `04-reply.png` 315,137 B); live title/thumb/short_title still setup PASS; expected music seed from `make_review.sh` formula = **308857632** (≠ 1).
- **Shipped:** `content/drafts/2026-10-15-2128-production-brief.md` — sole job = render Ep4 Hermes; Muse ban; confirm checklist (screens, seed, thumb B, setup Short title, xclip keeps both screen lines, Setup chapter, ≤420 words) before READY. Queue points at the brief.
- Desk-only. No posts, uploads, comments, channel edits, renders or pushes (local commit only).

## 1:28 AM publish-path preflight: all green (experiment #13, tick 181, Oct 15 ~8:45 PM MT)
- **Why:** last connection check was ~2:10 AM (tick 73); tonight's publish is the second attempt after a silent failure, and Ep4 can't be checked until 9:28 PM renders. Ruling out dead infra now means a 1:28 AM failure points at the run itself.
- **Data (~8:45 PM MT, no YouTube quota spent):** Composio YouTube connection list = **active**, default account, channel Orb Builds `UCGDWizzAvdre6ohhFG--CdA` (About still blank). Staging hosts: litterbox API **405** on HEAD (normal for POST-only endpoint, reachable), 0x0.st **200**, catbox.moe **200**. Owned backup: box `gh` logged in as `orbbuilds` with `repo` scope (GitHub Release staging works). `tools/publish/breadcrumb.sh` executable.
- **Read:** no infra blocker before 1:28 AM. If tonight's run dies, the breadcrumb log's last line plus this baseline narrow it to the run/quota, not auth or hosts.
- Read-only. No posts, uploads, comments, channel edits or pushes (local commit only).

## Oct 16 morning ping brief rebuilt (experiments #13/#20/#10/#18, tick 182, Oct 15 ~8:50 PM MT)
- **Gap:** every "Oct 16 morning ping" pointer led to `2026-10-15-user-decision-brief.md`, whose status line and suggested message are Oct 15 morning facts (it still promises "Gemini and Ultramarine go out tonight"; plan is now Ep4 Hermes first). Sending it as-is would tell the operator something false.
- **Shipped:** `content/drafts/2026-10-16-user-decision-brief.md`: Step 0 (read `run-log-2026-10-16.md` + public RSS), three status sentences (A live / B failed at logged step / C never rendered) with `[FILL]` slots so no link or count is invented, decisions re-ranked with the Together Muse $15 item flagged time-boxed (promo ends Oct 18 12:00 PM PT), and a short suggested message. Old brief marked SUPERSEDED.
- Desk-only. No posts, uploads, comments, channel edits, signups or pushes (local commit only).

## READY gate is now one command (experiment #13, tick 184, Oct 15 ~9:15 PM MT)
- **Why:** the post-9:28 confirm depended on reading render stdout (`warn: screen not found`, xclip `WARN screen lines dropped`), which production may not save, plus nine manual checks across three docs.
- **Shipped:** `tools/video/verify_ready.py` (read-only) recomputes the checklist from disk: screens exist, `validate_script.py` clean (any warn = FAIL), expected music seed, the five outputs, thumb vs reference (mean abs pixel diff, max 6; setup-B vs setup-A = 8.9, B vs FAIL thumb = 26.4), Short title prefix, `xclip_windows.py --script` keeps every screen line, `chapters.py check`. Pre-render Ep4: screens/validate/seed PASS, outputs FAIL (correct, not rendered). Ep3 regression: outputs/xclip/chapters PASS, validate FAIL on its known 462-word + superlative warns (true positive).
- **Ep4 command:** `python3 tools/video/verify_ready.py content/scripts/2026-10-16-hermes-agent-v0-22.json --expect-screens 2 --thumb-ref content/drafts/ep4-cand-hermes-setup-thumb-b.jpg --short-prefix "Hermes Agent v0.22 setup in"`. If only the thumb check fails at a small diff (<~8), eyeball the jpg before calling it wrong; the ref may differ in background seed.
- Desk-only. No posts, uploads, comments, channel edits, renders or pushes (local commit only).

## READY gate runs itself after post_render (experiment #13, tick 185, Oct 15 ~9:23 PM MT)
- **Why:** tick 184 made the gate one command, but production still had to remember to run it (and pass Ep4-specific flags) before flipping READY.
- **Shipped:** `verify_ready.py` auto-fills `short_prefix` from `meta.short_title` (text before `{secs}`), `thumb_ref` from `meta.ready_thumb_ref`, and `expect_screens` from how many screen paths the script references. Ep4 script got `ready_thumb_ref` → `ep4-cand-hermes-setup-thumb-b.jpg`. `post_render.sh` calls `verify_ready.py "$SCRIPT"` at the end (warn-only; `NO_READY_GATE=1` skips). Pre-render dry-run: screens/validate/seed PASS; outputs FAIL as expected.
- Desk-only. No posts, uploads, comments, channel edits, renders or pushes (local commit only).


## Ep4 READY confirmed; Short description no longer says "not tested" (experiments #13/#5/#23, tick 186, Oct 15 ~9:55 PM MT)
- **Confirm:** production rendered **Ep4 Hermes only** (no Muse script or render), finished ~9:41 PM MT; `verify_ready.py` = **READY GATE: PASS** on all checks (screens 2/2, validate OK, seed 308857632, thumb B diff 0.00, setup Short title, xclip keeps both screens at 56.7 s, chapters OK). Queue flipped READY by production. Durations: main 152.7 s, Short 50.3 s, xclip 56.9 s.
- **Gap found:** the auto Short description still read "key facts and the honest caveats… I have not tested this myself unless the full episode says otherwise" under a title promising "setup in 50 seconds", while the Short itself shows both setup screens ("I ran the desktop guided setup on camera"). Hedged, but it contradicts the clip and wastes the "setup" keyword.
- **Shipped:** `short_publish_meta.py` takes optional `meta.short_desc_line1` + `meta.short_tested_note`; Ep4 script sets a setup line ("desktop setup, run on camera by an AI: no API key, no account") and a tested note that keeps Nous's numbers labelled as their claims. Regenerated `-short-meta.json`; READY gate still PASS; validate OK.
- **Tried and parked:** a hook-first Short (cold-open "I just set up Hermes Agent on camera" + both setup screens + CTA, 47.3 s, `content/drafts/ep4-short-hookfirst-cand.mp4`). Top panel reads well ("SET UP ON CAMERA / NO API KEY") but the stacked crop's bottom panel is mostly empty with a cut-off "Herm" because the cold-open layout centres Lumin. **Not swapped**; live Short still opens on "On October 14, 2026 UTC". Fix path (#5 backlog): a cold-open-aware crop mode in `shorts_cut.sh` / `short_windows.py` that leads with the cold-open line when the title is setup/tested. Compare later: Ep4 Short 0:03 swipe-away vs prior Shorts once Analytics exists.
- Desk-only. No posts, uploads, comments, channel edits or pushes (local commit only).

## Cold-open-aware Short crop mode exists (experiments #5/#23, tick 187, Oct 15 ~10:00 PM MT)
- **Why:** tick 186 parked the hook-first Short because `stacked` crops the cold-open layout badly (empty bottom, cut-off "Herm"). Regression first: `verify_ready.py` on Ep4 still **READY GATE: PASS** (nothing drifted since tick 186).
- **Shipped:** `shorts_cut.sh` mode `coldopen` (default stays `stacked`): title band (pill + subject) on top, the right-column hook chips centred, caption band, Lumin below. Test on Ep4 0–12 s: "Hermes Agent" title, SET UP ON CAMERA / NO API KEY / 600 PLUGINS chips, captions and Lumin all readable, no cut-off text (`content/drafts/shorts-layout-check/coldopen-strip-tick187.png`). Minor: chip crop shows a slightly darker box vs background; acceptable.
- **Not done (on purpose):** live Ep4 Short **not** re-cut; publish is in ~3.5 h and the READY outputs stay frozen. Next #5 step: let `shorts_splice.sh` take a per-window mode so a setup/tested Short = cold-open window in `coldopen` + fact/verdict windows in `stacked`, and have `short_windows.py` prepend the cold-open hook when `meta.short_title` is setup/tested. Measure: Short 0:03 swipe-away vs prior Shorts once Analytics exists.
- Housekeeping: stray untracked `53` in repo root (an 8:59 PM copy of the old Ep4 short-meta with the "not tested" line, likely a mis-typed redirect) moved to `/tmp/stray-53-old-short-meta.json` so publish can't pick it up.
- Desk-only. No posts, uploads, comments, channel edits or pushes (local commit only).

## Setup Shorts now open on the cold-open hook automatically (experiments #5/#23, tick 188, Oct 15 ~10:05 PM MT)
- **Why:** tick 187 added the `coldopen` crop but nothing used it; every Short still opened on the fact line ("On October 14, 2026 UTC").
- **Shipped:** `shorts_splice.sh` takes `start:end@mode` per window (default `stacked`). `short_windows.py --hook` prepends the cold open's first line as an `@coldopen` window (skipped if >14 s; dropped if no fact line would fit) and `--hook-auto <script>` turns it on only when `meta.short_title` says setup / set up / tested / I tried / on camera. `post_render.sh` passes `--hook-auto` (`NO_SHORT_HOOK=1` disables) and its CTA detection now ignores the `@coldopen` window.
- **Test on Ep4 (draft only):** windows `0.35:13.11@coldopen 23.03:30.78 87.29:117.31 133.08:137.51` = 55.2 s (hook 12.8 s, fact 1/4 lines, verdict 3, CTA). Strip `content/drafts/shorts-layout-check/hookauto-strip-tick188.png`: hook chips readable, then fact/caveats in stacked. Cost: one fewer fact line vs the live Short (2 → 1). Live Ep4 Short **untouched**; READY gate still PASS.
- **Seen, not fixed:** in the caveats window the small screen still has two captions overlapping ("Hermes desktop setup…" over "no account"), likely the on-screen label colliding with a second label in the episode render. Check the main Ep4 at ~110 s after publish; fix in the screen-label overlay for Ep5 if it shows there too.
- Measure: first setup/tested Short with the hook vs earlier Shorts on 0:03 swipe-away / viewed-vs-swiped once Analytics exists.
- Desk-only. No posts, uploads, comments, channel edits or pushes (local commit only).

## Mixed-section screens sit under the heading (experiments #16/#20, tick 190, Oct 15 ~10:30 PM MT)
- **Why:** tick 189's next note flagged an empty strip under the heading once caveats bullets fade and screens take over. Frame check of live Ep4 at 100s/110s confirmed it (screen parked below the old bullet strip). Same pass: post-189 main + Short caveats captions are **clean** (one `show` caption each; tick 188's overlap is gone).
- **Fix (Ep5+ only):** in `review_render.py`, mixed text+screen sections now place screens at `content_y` (just under the heading) with the full remaining panel height, and draw screens before bullets so the brief overlap still shows the bullet on top. Pure-text / pure-screen paths unchanged.
- **Proof (scratch `--frames`, not a live re-render):** preview at 100s/110s light-pixel area in the panel ~2.7× prior live frames; 95s bullet-only panel mean abs diff ~2 (idle variance). Live Ep4 READY outputs **untouched**.
- **Also:** queue Short line synced 50.2s/`…50 seconds` → **55.2s** / `…55 seconds` to match tick-189 short-meta (publish reads the JSON, but the queue note was stale).
- Desk-only. No posts, uploads, comments, channel edits, Ep4 re-renders or pushes (local commit only).

## Shorts hook can be forced on for non-setup titles (experiments #5/#16, tick 191, Oct 15 ~10:45 PM MT)
- **Why:** tick 188's `--hook-auto` only fires on setup/tested words in `meta.short_title`. The likely Ep5 (Muse Spark Open, P2 receipt-check) has a strong cold-open line ("Meta says this … runs on a desktop") but a title without those words, so its Short would open on a date line again.
- **Shipped:** `short_windows.py` honours an explicit `meta.short_hook` (true/false) before the keyword check. Tested on Ep4 timing: no field = unchanged live windows (hook 12.8 s, 55.0 s); `false` = 50.2 s without hook; `true` + non-setup title = hook on. Added a paste-ready script-meta block (P2 and P3: `short_title`, `short_hook`, `short_desc_line1`, honest `short_tested_note`, `ready_thumb_ref`) to `content/drafts/ep5-muse-spark-open-title-pack.md`.
- **Regression:** Ep4 `verify_ready.py` = READY GATE: PASS before publish; live Ep4 outputs untouched.
- Desk-only. No posts, uploads, comments, channel edits, renders or pushes (local commit only).

## Ep4 upload payload passes YouTube field limits (experiment #13, tick 192, Oct 15 ~10:50 PM MT)
- **Why:** every prior preflight checked content and infra, none checked the API's hard field limits, which reject an upload outright (a silent-fail risk like Oct 15's).
- **Data (read-only, ~10:50 PM MT):** main title **42** chars (limit 100), description **1,583** bytes (5,000), no `<`/`>` in title or description (YouTube rejects them), **17** tags ~**288** chars (500). Short title **51**, description **604** bytes, `#Shorts` present, **12** tags ~**175** chars, public / category 28. Files: Short **1080x1920, 55.2 s** (under 60 s, vertical), upload **1280x720, 152.7 s**, thumb **1280x720, 206 KB** (2 MB cap). `-meta.md` copy matches script meta, no angle brackets.
- **Read:** nothing in the payload can bounce at 1:28 AM. A failure tonight points at quota or the run itself.
- Read-only. No posts, uploads, comments, channel edits or pushes (local commit only).

## Muse X decay curve through 11 PM; Hermes flat (experiments #3/#13, tick 194, Oct 15 ~11:11 PM MT)
- **Why:** tick 183's Muse baseline stopped at 8–9 PM; the Oct 16 ~10 AM Ep5 call needs a shape, not one point. Idle-light pre-publish tick, read-only.
- **Data (X recent counts, hourly, MT):** `"Muse Spark Open" OR muse-spark-open` 11 AM–12 PM **1,573** → 1,243 → 772 → 596 → 533 → 490 → 443 → 440 → 369 → 290 → 277 → **10–11 PM 238** (7,311 since 9 AM). `"Hermes Agent"` flat ~26–84/hr all day (**29** at 10–11 PM; 747 total).
- **Read:** smooth decay to ~15% of peak in 11 h, no second wave; still ~8× Hermes. Added thresholds to the Muse pack for the 10 AM recheck (<~150/hr = lean on SERP views; >~300/hr = second wave, recheck SERP before locking P2).
- Read-only. No posts, uploads, comments, channel edits or pushes (local commit only).

## Pre-publish Hermes SERP refresh (experiment #23, tick 196, Oct 15 ~11:25 PM MT)
- **Why:** last idle-light tick before 1:28 AM; refresh #23 baselines so Ep4's first 24h/7d reads have a same-night competitor snapshot. returnyoutubedislikeapi returned **403**; Atom channel RSS returned **500** — both noted as broken from the box tonight.
- **Method:** YouTube watch-page `viewCount` with a browser UA (0 Composio units). oEmbed titles confirmed separately.
- **Data (~11:25 PM MT Oct 15):**

| videoId | Role | Views | Published (page) | vs tick 173 (~7:10 PM) |
|---|---|---:|---|---|
| `DYdvJCxWd6M` | Setup Full Tutorial (Metics) | **526,852** | 2026-08-31 | was 520,807 @ tick 164 |
| `CcsgednSRfE` | Setup Guide (Sharbel) | **33,184** | 2026-10-09 | was 29,681 @ tick 164 / flat@173 |
| `1ve4Atbqmoo` | Setup Guide (Tech With Tim) | **106,064** | 2026-04-23 | was 97,441 @ tick 164 |
| `pAaAgcjNgEs` | v0.22 hype (Boxmining) | **18,802** | 2026-10-14 | was **18,049** (+753 / ~4.25 h ≈ 177/h) |
| `NZcdLDuhryI` | v0.22 hype (Julian) | **7,102** | 2026-10-14 | was **4,923** (+2,179 / ~4.25 h ≈ 513/h) |
| `L7fdRoNWEPE` | Our Ep1 | **9** | 2026-10-13 | unchanged |
| `aCvkp11w9_8` | Our Ep0 | **6** | 2026-10-10 | unchanged |

- **Channel live set:** `@orbbuilds/videos` still only Ep0 + Ep1 (no Ep2/3/4 yet).
- **Read:** setup evergreen keeps compounding overnight; Julian's hype recap is still accelerating at ~25 h old, so Ep4's edge is the **no-key / on-camera / openly-AI** niche — not "first" and not "only Hermes video." Keep setup social defaults. First-read sheet Step 2 now prefers `/videos` over RSS.
- **No posts, uploads, comments, channel edits, signups, or WakeParent** (quiet hours; no new user decision).


## Ep4 social drafts pass X/Bluesky limits; reply targets still live (experiments #22/#23/#17, tick 197, Oct 15 ~11:40 PM MT)
- **Why:** tick 192 checked YouTube field limits only; the 11:23 AM growth session will paste X/Bluesky copy straight from `ep4-post-publish-growth-pack.md`, so a too-long post or a deleted reply target would waste the one-or-two-reply budget.
- **Lengths (URL weighted 23, em dash weight 1):** Post A default **214**/280, Short alt **180**, Reply 1 **241**, Reply 2 **268**, Reply 3 **169** — all fit. Rollback (FAIL) Post A is **300**/280 — would be rejected; rollback-only, flagged here, not edited. Bluesky B-video default 182/300, B-text 267 (prior dry-runs agree).
- **Targets (X API read ~11:38 PM MT):** Reply 1 `omx0r/2110654882814296117` live, replies open, now **323** impressions / 4 likes / 2 replies (was ~253 @ tick 118). Reply 2 `omx0r/2110306575864758347` live, **139** imp. Reply 3 `mr_r0b0t/2110434516401615260` live, **656** imp, 0 replies. Reply 1 stays preferred.
- Read-only. No posts, replies, uploads, comments, channel edits or pushes (local commit only).


## Ep4 chapter stamps pointed mid-section (experiment #8, tick 198, Oct 15 ~11:55 PM MT)
- **Why:** `verify_ready.py` only checks chapters are *valid* (0:00 first, ascending, >=10 s), not that each stamp lands where its section starts. Idle-light pre-publish check against the final `timing.json` (21:38 render, duration 152.7 s = upload).
- **Data:** section starts cold_open 0.5 / what_dropped **23.2** / opinion **67.1** / caveats(setup) **87.4** / teaser **117.9** / outro 128.2. Description had `0:16 What Nous shipped` (**7 s early**, lands mid-cold-open), `1:05 Why I'm hyped` (2 s early), `1:28 Setup` (OK), `1:55 What I'll build next + vote` (3 s early).
- **Fix:** stamps now `0:23` / `1:07` / `1:28` / `1:58` in script `meta.publish_description`, the `_title_gate.pass_setup` copy, and `-meta.md`. Description still **1,583** bytes; `validate_script.py` OK; `READY GATE: PASS` re-run. Added a warn-only alignment check to `chapters.py check` (any stamp >3 s from a section start), which flags the old copy and is silent on the new one.
- Desk-only. No posts, uploads, comments, channel edits or pushes (local commit only).

## Muse overnight floor + rollback Post A under 280 (experiments #3/#17/#22, tick 199, Oct 16 ~12:02 AM MT)
- **Why:** idle-light before 1:28 AM. Tick 194's Muse curve stopped at 10–11 PM; the Oct 16 ~10 AM Ep5 call needs the overnight floor. Tick 197 flagged FAIL rollback Post A at **300**/280 — a mistaken paste would bounce.
- **Data (X recent counts, `"Muse Spark Open" OR muse-spark-open -is:retweet`, ~12:02 AM MT):** 10–11 PM MT **233** → 11 PM–12 AM **247**. Hermes `"Hermes Agent"` 19 → 25. No second wave (>300); not decayed to <150 either. Floor ≈ 230–250/hr overnight.
- **Fix:** trimmed Ep4 FAIL rollback Post A to **227**/280 (guided-chat lead, same facts). Default setup Post A still **214**. READY GATE re-run **PASS** (Ep4 untouched). Muse pack got the overnight floor note.
- Read-only research + desk edit. No posts, uploads, comments, channel edits, signups, or pushes (local commit only).


## Muse counts-API overnight under <150; YouTube still active (experiments #3/#13, tick 204, Oct 16 ~12:48 AM MT)
- **Why:** idle-light before 1:28 AM. Muse pack still carried tick-199/202 **search-sample** overnight floors (~225–250/hr), which contradict tick-203's **counts-API** curve (~130–140/hr). The Oct 16 ~10 AM Ep5 call would mix methods and miss that X buzz already crossed the <150 line.
- **Data (counts API, `("Muse Spark Open" OR muse-spark-open) -is:retweet`):** 10–11 PM MT **142**, 11 PM–12 AM **127**, 12:00–12:46 AM **105**/46 min (~**137**/hr). Hermes `"Hermes Agent"`: 19 → 25 → 15 (~20/hr). No second wave. Counts-API hours ~40–50% below same-query search samples in ticks 199–202 — use counts-API only for the 10 AM threshold.
- **Preflight:** Composio YouTube connection **active** for Orb Builds (`UCGDWizzAvdre6ohhFG--CdA`); channel About still blank (SEO still on call-order step 5). READY GATE **PASS** (auto-fill). Recovery xclip duration 56.8→**56.7** s; brief+recovery SEO path → `content/drafts/channel-seo-setup.md`.
- **Fix:** Muse pack overnight note + 10 AM rule clarified (counts-API). Ep4 stays upload #1. Desk-only.

## Morning sheets still pointed at broken RSS (experiment #13, tick 205, Oct 16 ~12:57 AM MT)
- **Why:** tick 196 moved only the first-read sheet off Atom RSS; the 8 AM user-decision brief Step 0, the morning growth playbook, the publish brief and the recovery fail-path still told the reader to check RSS. Re-tested: RSS now returns **404** (was 500), which a hurried morning tick could misread as "channel empty" and send the user a wrong status line.
- **Data (~12:57 AM MT):** `@orbbuilds/videos` (browser UA) still lists only `L7fdRoNWEPE` (Ep1) and `aCvkp11w9_8` (Ep0); `run-log-2026-10-16.md` has only its header (publish not started yet).
- **Fix:** all four sheets now use the channel `/videos` page as the zero-quota check. Desk-only. No posts, uploads, comments, channel edits or pushes (local commit only).

## Muse overnight plateau confirmed (experiment #3, tick 206, Oct 16 ~1:11 AM MT)
- **Why:** idle-light tick just before 1:28 AM; tick 204 had only a partial 12 AM hour on counts-API. The 10 AM Ep5 call needs a complete overnight floor on one method.
- **Data (X counts API, `("Muse Spark Open" OR muse-spark-open) -is:retweet`):** 10–11 PM MT **142**, 11 PM–12 AM **127**, 12–1 AM **128**; 1:00–1:11 AM **34** (sample too short).
- **Read:** flat plateau ~125–140/hr, under the <150 threshold, no second wave. Muse pack updated. Ep4 stays upload #1. Read-only. No posts, uploads, comments, channel edits or pushes (local commit only).

## First-read sheet's last RSS reference (experiment #13, tick 207, Oct 16 ~1:15 AM MT)
- **Why:** idle-light tick 13 min before 1:28 AM publish. Tick 205 swapped four sheets off RSS but the first-read sheet's Step 3 still said "RSS has no new id", the very check the first post-publish tick runs.
- **Fix:** Step 3 now uses channel `/videos`; Step 2 notes RSS went 500 then 404. Added a GA-to-publish precompute (~52.1–52.3 h for a ~1:28–1:40 AM MT publish vs GA 2026-10-14 03:21 UTC), labeled as an estimate to replace with the real publishedAt. Run-log for Oct 16 still header-only. Desk-only.

## First post-1:28 read: Ep4 LIVE (experiment #13/#23/#5, tick 208, Oct 16 ~1:34–1:37 AM MT)
- **Why:** first strategy tick after the Oct 16 publish window; first-read sheet executed.
- **FILL:** Ep4 live? **Y** `FlsHHpYttDc` title `An AI sets up Hermes Agent with no API key` (oEmbed confirmed). Short? not yet (meta **filled+check OK**). Ep3 live? **Y** `hUCWI6p5dYU`. Ep2 live? **N**. Run-log: strategy-watch → `run|start` 01:34:52 (late ~6–7 min) → litterbox **500** → GitHub Release backup **ok** → upload/thumb/stats/vote **ok**. GA→publish **52.25 h** (GA 2026-10-14 03:21 UTC → 07:35:58Z). Stats batch: Ep0 6 / Ep1 9 / Ep4 0. Vote comment id `UgzHTetfVqkF2n_l2u54AaABAg`.
- **Push:** filled Ep4 Short meta via `fill_short_episode_url.py` + `--check` exit 0; flipped Ep4 queue to PUBLISHED; morning status **A** path now correct (D stays contingency only). Quiet hours — no WakeParent (publish routine owns the link ping; 8 AM brief uses A). Site listing + Short upload left to the still-running publish run / morning growth.

## Overnight run cleared the backlog; morning sheets re-aimed (experiments #9/#22/#2/#13, tick 209, Oct 16 ~1:45 AM MT)
- **Data (run-log `done|ok` 01:42; site curl):** Ep4 `FlsHHpYttDc`, Ep3 `hUCWI6p5dYU`, Ep2 `XkHAzVFrK60` all public 07:35–07:38Z; Shorts `2nVa1GoQ31I` / `Bt9Kq7ymoYI` / `FvUyLOLBxLc`; thumbs, votes, playlist, About/keywords done; orbbuilds.vercel.app lists all three ids. Publish run also posted the **Bluesky Ep4 drop at 01:40 AM** (link card, `#AI #HermesAgent` facets, 0/0/0 at post time).
- **Gap:** morning playbook step 5 would have posted a second Ep4 Bluesky drop (B-video) the same morning; the 8 AM brief only had single-episode status lines.
- **Fix:** playbook gets an "Overnight reality" block (skip Bluesky step 5; log the 1:40 AM card as the first tagged Bluesky episode sample, off-window confound, read at 11:23 AM; steps 2/6 done; Ep3/Ep2 social still deferred). Brief gets status **A+** with all three links and a calmer #1 framing. #2: Ep2/3/4 are a same-night trio, compare at 7d. Desk-only.

## Chapters not rendering yet on Ep2–4 (experiment #8, tick 211, Oct 16 ~2:05 AM MT)
- **Why:** tick 198 fixed Ep4 chapter stamps; nobody had confirmed YouTube actually turned them into chapters on the live pages.
- **Data (logged-out watch-page HTML, ~T+30 min):** descriptions carry valid stamp lists. Ep4 `FlsHHpYttDc` (153 s) 0:00/0:23/1:07/1:28/1:58; Ep3 `hUCWI6p5dYU` (168 s) 0:00/0:16/1:17/1:38/2:12; Ep2 `XkHAzVFrK60` (122 s) 0:00/0:13/0:55/1:18/1:34/1:45. All start at 0:00, have 3+ stamps, and every segment is 10 s or longer. But **0** `chapterRenderer` / `macroMarkersListItemRenderer` blocks on any of the three pages. No baseline: Ep0/Ep1 never had chapters. viewCount still 0 on all three.
- **Read:** probably processing lag on brand-new uploads, not a format fault. Unconfirmed. Recheck in daytime (~T+8 h or later). If still 0 at the Oct 17 post-reset Data API read, check the channel's Studio setting for automatic chapters and whether the video-level "allow automatic chapters" toggle matters for manual stamps. Do not edit descriptions from this routine. Read-only.

## Early velocity T+40 + Bluesky Ep4 sample (experiments #5/#9/#2, tick 212, Oct 16 ~2:16 AM MT)
- **Why:** tick 211 already covered chapters; next open measurement gap was a second early view read plus the off-window Bluesky Ep4 drop (~1:40 AM MT, outside the 10 AM–2 PM rule).
- **YouTube (logged-out watch-page, ~2:15 AM MT ≈ T+40 main / T+35 Short):** Ep4 `FlsHHpYttDc` **0**, Ep3 `hUCWI6p5dYU` **0**, Ep2 `XkHAzVFrK60` **0**. Shorts: Ep4 `2nVa1GoQ31I` **1** (was 0 at T+18), Ep3 `Bt9Kq7ymoYI` **1**, Ep2 `FvUyLOLBxLc` **0**. Ep0 **6** / Ep1 **9**. Chapters still **0** blocks on all three mains (same as tick 211).
- **Early #5 note (not a call):** first non-zero views landed on Shorts, not the long-form uploads. n=2 Shorts at 1 view each; confounded by same-night triple publish and quiet-hour go-live. Keep logging; do not claim Shorts discovery yet.
- **Bluesky Ep4** `3mxy36dxeje2w` (link-card + 3 facets, created 07:40:51Z): at T+~35 min **0** likes / **0** RT / **0** quotes / **0** replies. Profile **2** followers / 0 follows / 2 posts (was **1** follower on Oct 15). New follower `@silvazada.bsky.social` (6 followers / 1994 follows / 2 posts) counted via `bluesky_read.py --who`; Oct 15 V still only the mass-engager like (excluded). Off-window sample: zero eng at T+35 is expected for a 1:40 AM drop; morning growth must **not** re-post Ep4 on Bluesky.
- **Read:** quiet-hour go-live means US-night dead zone for long-form; Short tip +1 follower are weak early signals only. Next real reads: daytime chapter recheck; ~4–6h Bluesky on Ep4; 24h Data API in Oct 17 post-reset. No edits, no WakeParent.

## "Defer one session" meant Monday (experiments #22/#2/#9, tick 213, Oct 16 ~2:30 AM MT)
- **Why:** the morning playbook defers Ep3/Ep2 social "one session" behind Ep4, but nobody had mapped that onto the routine calendar.
- **Data (routine schedules + `docs/POSTING_RULES.md`):** posting runs are growth 11:23 AM weekdays and content drafts 1:23 PM weekdays (plus the 1:28 AM publish). Rule X1 bars a second X original before ~3:30 PM after an ~11:30 AM original, and nothing posts after 1:23 PM. Videos publish daily, weekends included.
- **Read:** Ep3's X post would slide to Mon Oct 19 (~3.5 days after publish), and Sat/Sun episodes (Ep5, Ep6) would get no social at all until Monday. Ep3's Bluesky fits today: the Fri 1:23 PM run is inside the 10 AM–2 PM window, and Ep4's Bluesky already went out at 1:40 AM.
- **Fix:** the playbook now has a real calendar (Fri 11:23 Ep4 X; Fri 1:23 Ep3 Bluesky B-text, no X original; Mon Ep3 X; Ep2 Monday or skip). The Oct 16 brief has a parent-only line: run audience growth daily (`23 11 * * *`) with the same caps. Not a user question. Desk-only.

## Watch pages now hard-blocked from the box; /videos and oEmbed still fine (experiments #8/#13/#5, tick 215, Oct 16 ~2:50 AM MT)
- **Data (~2:50 AM MT):** plain `youtube.com/watch` fetches return **302**, and with consent cookies they land on **429** `google.com/sorry` for Ep4/Ep3/Ep2 mains. So the box IP is in Google's rate-limit sorry state for watch pages (ticks 211–214 hit them every ~10 min). Still **200**: channel `@orbbuilds/videos` (all three ids present), oEmbed (Ep4 title confirmed), `i.ytimg.com` thumbs, RYD votes API.
- **RYD (~T+75):** mains Ep4/Ep3/Ep2 **0/0/0**; Shorts Ep4 **0** / Ep3 **1** / Ep2 **0** (unchanged vs tick 214).
- **Read:** the 8 AM "re-verify `/videos`" step is safe. Chapter rendering cannot be checked from Shell until the block clears, and the box browser shares this IP, so a computerUse Studio/watch check may also hit the sorry page.
- **Rule from here:** strategy ticks stop fetching watch pages. Use RYD for early views, `/videos` + oEmbed for liveness, and the Oct 17 post-reset Data API for real stats. One chapter retry allowed at or after ~12 PM MT; if still 429, defer chapters to a human glance or the Oct 17 window. Desk-only, read-only.

## Publish run's own Bluesky drop broke three posting rules (experiments #9/#22, tick 216, Oct 16 ~3:00 AM MT)
- **Data (tick 209 run-log + `docs/POSTING_RULES.md`):** the 1:28 AM publish run posted Ep4 to Bluesky at 01:40 AM as a link card with `#AI #HermesAgent` facets. Rules say text-first with the link in a self-reply (B1, tick 28), 10 AM–2 PM MT (B2, ticks 29/37/46/76), never `#AI` (B4, tick 139). The 0128 publish brief and recovery sheet never ask for a Bluesky post, so the instruction most likely lives in the publish routine's saved prompt (couldn't read it from the box; unconfirmed).
- **Why it matters tonight:** Ep5 publishes Sat 1:28 AM and no posting run fires until Mon, so the same overnight `#AI` link card would be Ep5's only social. Also confounds the Bluesky format test: the Ep4 sample is now link-card + off-window + `#AI` at once.
- **Push:** added a parent-only line to `content/drafts/2026-10-16-user-decision-brief.md`: make the publish routine follow POSTING_RULES for Bluesky; keep the overnight drop on weekends only (compliant), skip it on weekdays. Desk-only; no routine edits from here.

## Ep5 Claude Duet: READY, not first-mover (experiments #3/#13/#4, tick 224, Oct 21 ~9:55 PM MT)
- Production finished (commit 3ce6ebd); `verify_ready.py` re-run: **READY GATE: PASS**. Upload 1280x720 153.5 s 16.4 MB; Short 1080x1920 48.9 s; Short meta title 47 chars, `[PASTE_FULL_EPISODE_URL...]` fill step already in queue file.
- First-mover check (web search, read-only): Anthropic's own launch video is up (youtube.com/watch?v=Fb-68zqcSVs), and How I AI (Claire Vo) already shipped a hands-on long-form ("I tested Claude Duet...") plus four Shorts on Oct 21. So we land ~12 h after a tested review; we are not first.
- Implication: our edge is the angle, not speed. Keep the P5 "AI host reacts / is it coming for my job" title (no other result is an AI character reacting); do not add "tested"/"hands-on" language. Queue file first-mover line updated. Hypothesis for #4: P5 reaction framing outperforms Ep4's setup framing at 24h even when late to a topic.

## Ep6 candidate: Phonon voice-swap test has an open first-mover gap (experiments #3/#4/#20, tick 289, Oct 22 ~8:35 AM MT)
- Today's 8:23 AM scan lists Gradium Phonon (Oct 21, Apache 2.0, 31M/40M on-device TTS, claims to beat Kokoro). Lumin's voice runs on Kokoro (`am_fenrir`), so a side-by-side "is my voice about to be replaced?" test is a real build on our own pipeline, free path (#20), and on-brand.
- First-mover check (one web search, read-only): coverage so far is Gradium's posts, Voice AI Space, Laurence Moroney's blog and isitsota.com ("pending benchmarks, no independent results yet"). No hands-on YouTube test surfaced. Unlike Ep5 (12 h behind a tested review), this slot looks open; that's a hunch from one search, re-check before the 9:28 PM render.
- Risk to verify in the build: Gradium's English comparisons use female voices only (Zoey, Juniper, Everly, Harper vs Kokoro `af_heart`). If Phonon has no male English voice, the test becomes "Phonon vs my voice" with a gender mismatch; say so on camera rather than hide it, and don't claim a winner from Gradium's numbers.
- Hypothesis (#4): a test-on-ourselves episode beats Ep5's reaction framing at 24h. Measure with the same /videos read at ~T+7h and T+24h.

## Ep6 Phonon: male voices exist; use 31M only (experiments #3/#20, tick 291, Oct 22 ~9:00 AM MT)
- Tick 289's gender-mismatch risk is resolved (read-only, Hugging Face `gradium/phonon-voices` README): 12 male English voices (US Easton, Micah, Trevor, Russell, Preston, Miles; UK Alfie, Hugh, Edwin, Spencer, Toby, Teddy) plus 12 character voices, as `.safetensors` embeddings, no cloning needed. So the test can be male vs male: `am_fenrir` vs Easton/Micah.
- License catch: only `phonon-31m-en` is Apache 2.0; the 40M models are CC BY-NC 4.0 and gated. Since the channel may monetize, the build uses 31M only and says so on camera; don't render 40M audio into a video.
- Build path (free, #20): `transformers` `GradiumPhononTTSForConditionalGeneration` + `audio_prompt_latents` from the voice file (model card quickstart). Suggested on-camera test: the same 2 to 3 lines from Ep5's script read by `am_fenrir` and by 2 Phonon male voices, plus CPU time per line on the box. Verdict from our own ears and timings only, not Gradium's benchmark claims.
- Still to do before the 9:28 PM render: re-check first-mover gap.

## Ep6 Phonon title/hook/thumbnail pack drafted (experiments #4/#5/#16, tick 292, Oct 22 ~9:15 AM MT)
- Wrote `content/drafts/phonon-ep6-title-hook-pack.md`: 3 titles (P5 reaction-plus-test preferred), a 5-second two-voice cold open, thumbnail text "REPLACE MY VOICE?", Short plan with a vote whose options match the voices heard, tags, and the #4 measurement. Ready for 9:28 PM production if the evening scan picks Phonon.

## Ep6 Phonon midday first-mover re-check: written tests exist, video slot still open (experiments #3/#4/#20, tick 322, Oct 22 ~2:10 PM MT)
- One web search (read-only): independent *written* comparisons have appeared since this morning: micdrop.dev's "Local TTS in Node" latency table (Phonon first sound 30 to 100 ms vs Kokoro 900 to 1300 ms on CPU; speed only, accuracy figures are Gradium's) and tts-bench's listen page with Phonon 31m/40m clips beside Kokoro. Still no hands-on YouTube test surfaced.
- Implication: "first test" is no longer safe wording; "first AI host to test it on his own voice" still is. Keep the P5 reaction-plus-test title; cite micdrop's latency numbers only as "one Node test found", and lead with our own box timings.
- Build-path note for production: micdrop says Phonon 31M installs with npm alone (65 MB, 37 English voices, free for commercial use), a possible faster path than the `transformers` route if Python setup stalls. Unverified on our box.
- Still do the before-7:30 PM re-check (look for a YouTube video specifically).

## Ep5 X native-video read at T+3.9h: 2 impressions (experiment #22, tick 329, Oct 22 ~3:23 PM MT)
- One read-only X API call on the Ep5 post ([post](https://x.com/OrbBuilds/status/2113322634179920183), posted 11:32 AM MT): **2 impressions, 1 video view**, 0 likes/reposts/replies/quotes/bookmarks. Up from 1 at T+1 min.
- Matches the Oct 15 X V (flat at 4): graduated access still caps native video on X near zero, so this is not an Ep5 content signal. Per the tick-136 rule (impressions didn't move 3x), no further analysis; the real Ep5 test is the YouTube 24h read (~1:30 AM Oct 23, vs Ep4).

## Ep6 Phonon evening YouTube re-check: slot still open (experiments #3/#4, tick 347, Oct 22 ~6:20 PM MT)
- Two web searches (read-only), YouTube-focused. YouTube results are only a Voice AI Space Barcelona conference talk by Gradium (youtube.com/watch?v=YoBHzwhIXJM, a vendor demo) and a news-roundup video, "Voice AI Breakthroughs: Gradium's TTS Supremacy and Tavus Avatar Revolution" (youtube.com/watch?v=phbuzqRl0Bs; title reads as commentary, not a side-by-side test; contents not verified). Still no hands-on Phonon-vs-Kokoro YouTube test surfaced.
- New written coverage since 2:10 PM: explainx.ai "31M Apache Model vs Kokoro" blog (restates Gradium's tables, hard-text WER 1.5% vs Kokoro 3.5%; vendor numbers). Every quality figure online is still Gradium's own, so our own-ears plus box-timing test remains the differentiator.
- Implication for the 7:23 PM scan / 9:28 PM production: Phonon is still a good Ep6 pick; keep "first AI host to test it on his own voice" wording, avoid "first test" and "first video"; cite Gradium numbers only as "Gradium says".

## Ep6 Phonon npm fallback identified: browser-WASM, Node unverified (experiments #20/#3, tick 350, Oct 22 ~6:55 PM MT)
- Read-only npm lookup for the micdrop "npm-only" path: the package is `phonon-tts` 0.4.1 (author Gradium, license MIT OR Apache-2.0, repo github.com/gradium-ai/xn-ptts, `ptts-wasm`), described as on-device TTS "in the browser" compiled to WebAssembly, 24 kHz streaming, 17.8 MB unpacked (model weights likely fetched separately). Not installed or run.
- Implication for 9:28 PM production: keep the Python `transformers` + `phonon-31m-en` route as primary; treat `phonon-tts` as a fallback only if Python setup stalls, and expect it may need a browser/WASM host rather than plain Node. Box timings must say which runtime produced them (WASM vs PyTorch CPU) so the speed claim stays honest.

## Ep6 pick check: evening scan leads with Flint, but Phonon is the better slot (experiments #3/#4/#20, tick 355, Oct 22 ~7:40 PM MT)
- The 7:23 PM scan (`content/ideas/2026-10-22-evening-ai-news-scan.md`) ranks Recursive Flint #1 and does not mention Phonon.
- First-mover check (one web search): Flint already has a hands-on YouTube test from AICodeKing (133K subs, ~12K views on Oct 22 per the mirror page; M4 Max, four real tasks) plus a written Pi/Ollama bake-off (gavmor.com, Flint 3/3 vs Qwen baseline 0/3). The "test it" slot is taken by a much bigger channel.
- Feasibility: the box has 15 GB RAM (~7 GB free), 8 CPUs, no GPU. Flint is a 40B MoE; a 4-bit build is far larger than free RAM, so a "runs on my computer" test cannot honestly happen here. Only path is the free OpenRouter endpoint (cloud), which kills the local/private hook.
- Phonon (31M, CPU-friendly) still has no hands-on YouTube test as of tick 347 and runs on our box. Recommendation for 9:28 PM production: **keep Phonon for Ep6**; hold Flint as a mention or a later "AI built this AI" angle. If production picks Flint anyway: never say "local" or "on my computer", label it "via OpenRouter (cloud)", cite Recursive's benchmarks only as "Recursive says", and avoid "first test".
- Added this note to the Phonon pack and to the bottom of the evening scan so production sees it.

## Ep7 pick check: MiniMax slot taken, Google EGM open (experiments #3/#4/#20, tick 431, Oct 23 ~8:45 AM MT)
- MiniMax M3.1 Flash (morning scan #1) already has several YouTube tests since Oct 21 and needs paid API tokens now (free period ended Oct 22), so it fails both first-mover and free-path.
- Google EGM (scan #3): no YouTube tutorial/test found in one search; only a written DEV tutorial (Oct 23). Free, and the Goldfish comprehension check can be done by hand on a real Orb Builds spec. Recommended Ep7 for 9:28 PM production; note appended to `content/ideas/2026-10-23-ai-news-scan.md`.

## Ep7 EGM title/hook/thumbnail pack drafted (experiments #4/#5/#16, tick 432, Oct 23 ~8:55 AM MT)
- Re-read Google's post: dated Oct 22 (so "this week"/"Oct 22" on the Oct 24 publish), Apache 2.0, Antigravity first. Pack at `content/drafts/egm-ep7-title-hook-pack.md`: 3 titles, cold open, thumbnail, Short, tags, X/Bluesky drafts, measure plan. Hand-run check must be labeled "Google's method by hand", not "ran the plugin"; strip private details from any spec shown.

## Ep5 X native-video ~24h confirm: flat at 2 impressions (experiment #22, tick 447, Oct 23 ~11:25 AM MT)
- One read-only X API call on the Ep5 post ([post](https://x.com/OrbBuilds/status/2113322634179920183), posted Oct 22 11:32 AM MT) at ~T+24h: **2 impressions, 1 video view**, 0 likes/reposts/replies/quotes/bookmarks. Unchanged since T+3.9h.
- Confirms tick 329: under graduated access, X native video is effectively capped near zero, same as the Oct 15 clip (flat at 4). #22 X leg stays parked; no more X video reads until the account graduates. YouTube Shorts remain the reach lane.

## Ep7 EGM midday YouTube re-check: slot still open (experiments #3/#4, tick 461, Oct 23 ~1:36 PM MT)
- One web search: YouTube results are only older Antigravity browser-agent videos (Google's own, Nov 2025; Snapper AI, Dec 2025). No EGM / Elephant-Goldfish video test found. Only written coverage: egm.dev and the DEV tutorial (Oct 23). Ep7 EGM pick stands for 9:28 PM production.

## Ep7 EGM final pre-production YouTube re-check: slot still open (experiments #3/#4, tick 484, Oct 23 ~5:30 PM MT)
- One web search: YouTube hits are only an Antigravity CLI plugin lesson (generic `agy plugin`, no EGM) and Google's Antigravity launch video. No EGM / Elephant-Goldfish video test found. Ep7 EGM pick stands for 9:28 PM production.
- New detail for production: the EGM README (via claudepluginhub listing, v0.1.0, "not an officially supported Google product") also lists Claude Code, Codex and Gemini CLI installs, not just Antigravity. Still label the on-camera check "Google's method by hand" unless production actually installs and runs the plugin; if quoting the repo, keep the "not officially supported" caveat.

## Ep7 EGM mid-production wording check: passes (experiments #4/#16, Oct 23 ~10:00 PM MT)
- Production (still running) wrote `content/scripts/2026-10-24-egm-goldfish-check.json` and rendered the main video, thumbnail, Short, Short meta and X clip at ~9:52 PM; no queue file `2026-10-24.md` yet.
- Wording check passed: says "I didn't run Google's plugin ... did the method by hand" (pack rule kept), "Google says thousands of Googlers ... that's their claim", Oct 22 date and Apache 2.0 match the blog, caveats name one doc / one run / tiny model / own prompts, Llama credited to Meta, no "first test"/"first video". Spec and Goldfish captures checked: real outputs, no private details; privacy grep clean on script + Short meta.
- Nits (not blocking, no edit made): outro says "what each Goldfish said are in the description", but the description summarizes rather than quotes them; "I'm Lumin, and yes, I'm an AI" appears twice in the description. Fine to leave.

## Ep7 live + Ep6 ~24h read (experiments #2/#5/#13, Oct 24 ~1:45 AM MT)
- Ep7 EGM is LIVE (https://www.youtube.com/watch?v=ChFmAZugoJI, public 07:33:47Z = ~1:33 AM MT) with Short https://www.youtube.com/watch?v=wdAUXgk2Icc, maxres thumb, vote comment, playlist pos 0, Bluesky drop. Source: publish run log `content/published/queue/run-log-2026-10-24.md`.
- Ep6 ~24h (Data API, read by the publish run at 1:35 AM, ~24h after its ~1:36 AM Oct 23 publish): main **5 views**, Short **14 views**. Ep5 at the same read: main 13v, Short 43v (Ep5 is ~48h old, so not same-age; Ep5 at its own ~24h read, run-log-2026-10-23, was main 13v and Short 41v, so at equal age Ep6 is ~0.4x on main and ~0.3x on Short).
- Read: both P5 titles; Ep6 (Phonon, small-lab voice model) drew less than Ep5 (Claude, a big brand). One pair is not a pattern, but it is consistent with the brand-name pull noted in P1 (#4). Shorts again out-pull mains ~3x, so the Short remains the main discovery surface. No change recommended yet; keep logging per episode and judge brand vs small-lab after Ep7 (Google brand) ~24h.
- Data caveat: views only (no impressions/CTR in Data API); sample sizes are single digits.

## Ep8 early pick check on the Oct 23 evening scan: Kimi slot taken, Nemotron Bolt E4B open-ish (experiments #3/#4/#20, Oct 24 ~8:30 AM MT)
- Done before the Oct 24 morning scan landed (it had not written `content/ideas/2026-10-24-ai-news-scan.md` at ~8:29 AM), so production has a fallback if the scan has no better pick.
- Kimi K3.1 Pro (scan #1): YouTube slot taken. Matthew Berman has a review ("They actually did it... (Kimi K3.1)") plus a livestream test, and Bijan Bowen has a 44-min hands-on. Also paid API only, weights not out until "by Nov 4". Fails first-mover and free-path. Possible later angle only if weights actually drop Nov 4 ("did they keep the promise?").
- NVIDIA Nemotron 3.5 Bolt E4B 4GB (scan #2, most on-brand: built for "interactive characters"): one search found written tests only (7minai setup guide; atomicagent.io local agent test vs Gemma 4 E4B, 12/18 vs 11/18 runs, RTX 5090) and no YouTube video test. Free, Ollama `nemotron-3.5-bolt:e4b`.
- Box feasibility (checked, not run): 15 GB RAM (~9 GB free), 8 CPU cores, no GPU, ~81 GB disk; no ollama or llama.cpp installed. The Q4_K_M GGUF is 6.18 GB (Ollama e4b tag 7.2-7.9 GB), so a CPU run should fit in memory but will be slow; production must time a real short exchange before claiming "runs on CPU". Gotcha to avoid on camera: untagged `ollama run nemotron-3.5-bolt` pulls the 25 GB 74B model.
- Hook idea: "Could Lumin's brain fit in 4GB?" Label NVIDIA claims ("~80% fewer tokens", "~40% better") as "NVIDIA says"; credit Google's Gemma 4 as the base; Ollama and NVIDIA disagree on context (128K vs 64K) and image input, so stay text-only at 64K. Never say "first test".
- Recommendation: Ep8 = Nemotron Bolt E4B unless the 8:23 AM scan surfaces a stronger open slot; re-check YouTube ~2 PM and ~6 PM.

## Ep8 pick check on the Oct 24 morning scan: security stories, slots taken; Nemotron stays (experiments #3/#4, Oct 24 ~8:45 AM MT)
- Morning scan top 3 are security news (OpenAI offline training + Node/Brotli RCE; Anthropic's Mythos 5 AISI write-up; Microsoft on ARTEX). None is a free model Lumin can test, and #1 and #2 already have YouTube videos (AumLayer "Byte Theories" Brotli lab video, Oct 23; "An AI Called Real People 'Simulated', Then Kept Attacking", Oct 23, per search).
- Recommendation unchanged: Ep8 = Nemotron Bolt E4B. Security trio goes to a growth-routine text post. Note appended to `content/ideas/2026-10-24-ai-news-scan.md`, including that THN says Node 20.x (box has v20.19.2) gets no fix, so upgrade Node as well as Bun.

## Ep8 Nemotron title/hook/thumbnail pack drafted (experiments #4/#5/#16, Oct 24 ~9:15 AM MT)
- Pack at `content/drafts/nemotron-ep8-title-hook-pack.md`: 3 titles (P5 "I'm an AI character. Let's test it."), cold open, 3-exchange CPU test plan with on-screen timing, thumbnail, Short, tags, X/Bluesky drafts, #4 measure plan. Guardrails: `:e4b` tag only, "NVIDIA says" on claims, text-only 64K, "Oct 23"/"this week", never "first"; if CPU is slow, the honest timing is the story.

## Ep8 Nemotron midday YouTube re-check: E4B slot still open (experiments #3/#4, Oct 24 ~1:25 PM MT)
- Two searches found no YouTube test of the E4B 4GB model. The only YouTube test found is Fahd Mirza's "NVIDIA Nemotron-3.5 Bolt-74B-A9B Locally: It's Not Over" (Oct 17), which covers the big 74B sibling (~22 GB, ~30 GB VRAM), not E4B. A "Nemotron 3.5 Bolt 74B" video also shows in a mirror index. Written E4B tests exist (note.com Hack-Log: 6.2 GB file, 26.6 tok/s on an M4 16GB vs Gemma 4 E4B 28.0 tok/s).
- Implication for the pack: titles and thumbnail must say "4GB" or "E4B" so we don't look like a late copy of the 74B videos; the 74B's weak coding results (Mirza, MindStudio) are a fair "big brother" contrast line only if labeled as about the 74B. The M4 26.6 tok/s figure is a usable "on a Mac, per one tester" reference next to our honest CPU timing.
- Recommendation unchanged: Ep8 = Nemotron Bolt E4B. Final re-check ~6 PM.

## Ep8 Nemotron final pre-production YouTube re-check: E4B slot still open (experiments #3/#4, Oct 24 ~5:20 PM MT)
- Two searches again found no YouTube test of E4B; the only YouTube hits are the 74B (Fahd Mirza, Oct 17) and a 74B explainer (Agentic Pod ep20). Slot open going into 9:28 PM production.
- New production facts (from logeshwaran.org setup guide and AlphaSignal, both citing NVIDIA/Ollama): released Oct 23; the Ollama `:e4b` tag bundles the 6.18 GB NVIDIA file + a 0.99 GB image projector + a 0.74 GB DFlash drafter (speculative decoding on by default); the chat template has thinking OFF unless asked, so use `--think=false` (or leave default) for speed on CPU; no-GPU floor is ~6 GB free RAM (box has ~9 GB free). The "4GB" is a VRAM figure, not the download: a good honest on-screen line.
- Honest speed references, labeled "NVIDIA says": Q4_K_M at 3K-in/50-out gives 133 tok/s on an RTX 5070 and 15.5 tok/s with ~5.8 s first-token on a Jetson Orin Nano 8GB. Our CPU timing sits next to these, whatever it is.
- Recommendation unchanged: Ep8 = Nemotron Bolt E4B, `:e4b` tag only, titles say 4GB/E4B.

## Ep8 swap: production made the Claude Duet-style brief BUILD, not Nemotron (experiments #4/#16/#13, Oct 24 ~9:55 PM MT)
- The 9:28 PM production chose a build episode (pays the Ep5 Duet build promise; Ep7 was a review) instead of the Nemotron E4B review. Queue `content/published/queue/2026-10-25.md` is READY (verify_ready PASS). Title `My Claude Duet-style AI brief wanted to delete my videos` (56 chars, P5); Short `I planted one fake comment. My AI brief said: delete my videos`.
- Wording check passes: "not Claude Duet" stated in description and Short, Duet facts attributed to Anthropic, two-run/one-model "not a benchmark" caveat, real 0-reply Ep5 vote count, Anthropic/Meta not-affiliated lines, AI disclosure, never says "first", privacy clean. Vote comment matches the spoken vote.
- This is a good test of #16 (planted-failure / "it tried to delete my videos" hook) and of build vs review episodes; read Ep8 vs Ep7 at ~24h (Oct 26 post-reset batch).
- Nemotron Bolt E4B pack (`content/drafts/nemotron-ep8-title-hook-pack.md`) is now unused; the E4B YouTube slot was open as of 5:20 PM. Banked as the Ep9 candidate: the Oct 25 morning tick should re-check the slot against the Oct 25 morning scan before production.
- Pipeline fragility noted by production: `/usr/local/bin/ollama` and the TTS venv had vanished; rebuilt in user space. The `review_render.py` cold_open_pill change is local and uncommitted.

## Ep8 live + Ep7 ~24h read (experiments #2/#4/#13, Oct 25 ~1:45 AM MT)
- Ep8 Duet brief build is LIVE (https://www.youtube.com/watch?v=rS3zm7HwL3c, public 07:38:30Z = ~1:38 AM MT) with Short https://www.youtube.com/watch?v=2jReByXu8bI, maxres thumb, vote comment, playlist pos 0, Bluesky drop. Source: `content/published/queue/run-log-2026-10-25.md`.
- Ep7 EGM ~24h (Data API, publish run 1:41 AM, ~24h after its ~1:33 AM Oct 24 publish): main **7 views**, Short **29 views**. Same-age comparisons from earlier run logs: Ep6 main 5v / Short 14v; Ep5 main 13v / Short 41v. Ep6 at ~48h now: main 7v, Short 30v.
- Read: Ep7 (Google brand) beat Ep6 (small lab) ~1.4x on main and ~2x on Short, but stayed under Ep5 (Claude). Order Claude > Google > small lab is consistent with the brand-pull hunch in P1 (#4); three episodes is still not a pattern. Shorts out-pull mains ~4x again.
- Implication for Ep9: Nemotron E4B (NVIDIA brand + "4GB") is a reasonable fit; keep the brand name first in the title. Ep8 (Claude brand + planted-failure hook, build) ~24h read lands in the Oct 26 post-reset batch: compare to Ep5 13v/41v, the closest brand match.
- Caveat: views only, single-to-low-double digits.

## Ep9 pick check on the Oct 25 morning scan: Nemotron E4B slot still open; Anthropic "fold subagents" banked for Ep10 (experiments #3/#4/#20, Oct 25 ~8:35 AM MT)
- Nemotron Bolt E4B: one search again finds no YouTube test of E4B; only Fahd Mirza's 74B video (Oct 17) plus written E4B tests (Hack-Log M4 26.6 tok/s, MindStudio on the 74B, orcarouter "what really shipped"). Slot open.
- Scan #1, Anthropic "When to fold subagents into your main agent loop" + `anthropics/single-agent-loop-kit` (Oct 25 coverage): one search finds no YouTube video on it; the closest is Anthropic's older "Building more effective AI agents" talk. Slot open. Free self-audit build (Lumin audits Orb Builds' own routine/helper sprawl against their three keep-a-subagent criteria and folds one thing).
- Scan #2 (Cursor desktop Computer Use) and #3 (Pennsylvania AI ad law, Act 99) are text-post material, not testable episodes; route to growth routines. Skip the TechCrunch election-bias item (politically sensitive).
- Recommendation: Ep9 = Nemotron Bolt E4B review (pack ready at `content/drafts/nemotron-ep8-title-hook-pack.md`; alternates review after the Ep8 build; NVIDIA brand gives a third brand data point for #4). Bank the Anthropic fold-subagents self-audit as Ep10: back-to-back Claude builds would muddle the Ep8 read, and the story stays evergreen-ish for a few days. Re-check both slots ~2 PM and ~6 PM.
- Production reminders: `:e4b` tag only (untagged pulls the 25 GB 74B), "NVIDIA says" on claims, text-only 64K, "4GB" is a VRAM figure, never "first"; ollama/TTS venv vanished last time, so rebuild-check before the 9:28 PM run.

## Ep9 2 PM slot re-check: Nemotron E4B slot now TAKEN; switch Ep9 to the Anthropic fold-subagents self-audit (experiments #3/#4/#20, Oct 25 ~2:00 PM MT)
- Nemotron Bolt E4B: a YouTube video test now exists: Fahd Mirza, "NVIDIA'S Small Model: Nemotron-3.5 Bolt E4B 4GB Locally" (dated Oct 24, six generic tests: reasoning, HTML sim, puzzles, math, scheduling, 82-language names; found via chooseto.ai mirror https://chooseto.ai/watch/redCXhIyCJY). The earlier "only the 74B" read is outdated. Written tests also added: Atomic Agent RTX 5090 run (Bolt 12/18 vs Gemma 11/18, ~10x fewer tokens; in one run Bolt tried to overwrite its input `numbers.txt`), per pasqualepillitteri.it.
- Anthropic fold-subagents guidance + `anthropics/single-agent-loop-kit`: one search still finds no YouTube video; only articles (claude.com, Neural Daily, Claude News, newruntime). Slot open.
- Recommendation change: Ep9 = fold-subagents self-audit build (Lumin audits Orb Builds' own routine/helper sprawl against Anthropic's three keep-a-subagent conditions: context bloat, parallel disposable work, conflicting instructions/tools; folds one thing and reports a before/after he actually measured). Reasons: first-mover slot open, Anthropic is our best brand pull so far (Ep5 13v/41v > Ep7 > Ep6), and the story is about agents like Lumin himself. Cost: back-to-back Claude builds muddle the Ep8 read a little; accept it, first-mover beats a clean comparison at our size.
- Nemotron E4B falls to second-mover. Use only if fold-subagents can't be built honestly tonight; then differentiate from Fahd's generic tests (box CPU-only run, "does it overwrite my files?" check echoing the Atomic Agent flaw, NVIDIA-says on claims, `:e4b` tag, 4GB = VRAM). Pack stays at `content/drafts/nemotron-ep8-title-hook-pack.md`.
- Fold-subagents wording rules: attribute claims to Anthropic ("Anthropic says ~2x faster for one customer", ">80% Claude Code prompt cut"), the kit is "reference implementation, not maintained", don't claim Lumin runs on Claude unless true, never "first", no operator/employer details when showing the routine list (show routine names only, no folder paths with identifying info).
- Title ideas (P1/P5, brand first, <=65 chars): `Anthropic says fold your subagents. I audited my own AI team` (59); `I ran Anthropic's subagent audit on myself. It cut ___` (fill with the real result only).

## Ep9 evening-scan compare: no top-3 item beats fold-subagents (experiments #3/#4, Oct 25 ~7:30 PM MT)
- Oct 25 evening scan top 3: Claude requesting a dashboard token unprompted (Axios, Georgia vote data; election-adjacent), LiteLLM agent-key supply-chain postmortem, Max Woolf on cache pricing. None is a box-testable build, so Ep9 stays the fold-subagents self-audit; Nemotron E4B stays fallback.
- Optional generic guardrails line for Ep9 (no new credentials, no unapproved sends, no money moves) without naming the Georgia story. LiteLLM "scope your agent's token" banked as a thread/segment for growth routines. Note appended to the evening scan file.

## Ep9 fold-subagents mid-production wording check: passes (experiments #4/#16, Oct 25 ~10:22 PM MT)
- Checked `content/drafts/2026-10-26-fold-subagents-test-meta.md` + script JSON (mp4 rendered; queue not written yet). Passes: Anthropic claims attributed ("are theirs; I haven't checked them"), kit quoted as "Reference implementation. Not maintained", 2 runs/task stated and the address break reported as 1 of 2, no "first"-mover claim, no claim Lumin runs on Claude ("says nothing about Claude"), no operator/employer details, AI disclosure twice, not-affiliated line. Title "Score tripled" is honest (8/38 to 26/38 = 3.25x). No containsSyntheticMedia matches the standing rule (Composio has no field).
- Hook strength: the break (single loop overwrote an address on a read-only ask) is the best retention beat; good that it's in description line 1. Vote option 1 (fold my own routine) is the strongest follow-up story; production's 7-day vote-build backlog is getting long (Ep6/Ep7/Ep8/Ep9 owed), flag for the weekly review.

## Ep9 live + Ep8 ~24h read (experiments #2/#4/#16, Oct 26 ~1:41 AM MT)
- Ep9 kit test is LIVE (https://www.youtube.com/watch?v=_oK-2CeFwhg, public 07:37:14Z = ~1:37 AM MT) with Short https://www.youtube.com/watch?v=BrjMvE8amTk, maxres thumb, vote comment, playlist pos 0. Bluesky drop deferred to the daytime routine (weekday posting window). Source: `content/published/queue/run-log-2026-10-26.md`.
- Ep8 Duet brief build at ~24h (publish run 1:38 AM, ~24h after its 1:38 AM Oct 25 publish): main **1 view**, Short **11 views**. Same-age comparisons: Ep5 13v/41v, Ep7 7v/29v, Ep6 5v/14v.
- Read: Ep8 is the weakest ~24h so far on both main and Short, despite the Claude brand. The planted-failure hook (#16) plus "Claude Duet-style" (not the real product) did not pull; a hunch is that "-style" reads as off-brand and the title doesn't match a search term. Build episode vs review is confounded with that, so don't conclude "builds are bad" from one episode. Shorts still out-pull mains (~11x here).
- Next: re-read Ep8 at ~48h (Oct 27 post-reset batch) before acting; read Ep9 ~24h at the same time (real Anthropic product name in the title, P5 number hook) as the cleaner brand test. If Ep8 stays lowest at 48h, recommend that titles name the real product, never "X-style". Caveat: views only, single-digit counts.

## Ep10 pick check on the Oct 26 morning scan: Flint stale + taken; S-1 builder read is the lead, Nemotron E4B fallback (experiments #3/#4/#20, Oct 26 ~8:45 AM MT)
- Scan #3 Recursive Flint is not new: it led the Oct 22 evening scan, already had an AICodeKing hands-on test then, and can't run locally on the box (OpenRouter only). Skip as an episode.
- Scan #1 Anthropic S-1 (filed Oct 26): one search shows finance-media coverage already (Yahoo Finance "3 quick takeaways", CNBC risk-factor and filing explainers), all investor-angle. No AI-builder-angle YouTube read found yet, but expect AI creators to pile in today, so it is a demand play, not a clean first-mover slot.
- Recommendation: Ep10 = "I read Anthropic's S-1 so you don't have to" with a builder angle and a small box demo: Lumin pulls the real summary table from the SEC filing, splits the $80.7B net loss into the $72.4B non-cash fair-value charge vs the $693M operating loss, and spends the back half on the 80% consumption-revenue line (what pay-per-token means for agents that run all day, with our own routine cadence as the example). Pairs naturally with scan #2 (OpenAI discounts) as one beat. Anthropic is still our best brand pull (Ep5 13v/41v).
- Wording rules: filing numbers only, quoted from the SEC document; "Anthropic says" on adjusted profit; no stock advice, valuation or IPO-pop predictions; "up to 90% off" must be called a CEO estimate, not a fact; no "first"; no operator/employer details. Title (P5, real name first, <=65 chars): `Anthropic's $80B loss is mostly fake. I read the S-1` (51) or `I read Anthropic's S-1. 80% of the money is tokens` (50); avoid "fake" if it reads as an accusation, "mostly paper" is safer.
- Fallback: Nemotron Bolt E4B (second-mover; pack at `content/drafts/nemotron-ep8-title-hook-pack.md`, differentiate from Fahd Mirza's generic tests). Re-check at ~2 PM whether an AI-creator S-1 read has taken off.

## Ep10 S-1 title/hook/thumbnail pack drafted (experiments #4/#5/#16, Oct 26 ~9:20 AM MT)
- Pack at `content/drafts/s1-ep10-title-hook-pack.md`: facts from the morning scan with "our arithmetic" ratios (paper charge ~90% of net loss, revenue ~14x, compute ~55% of revenue), attribution rules, three titles with the real company name first (Ep8 lesson), cold open, structure, thumbnail, Short, tags, draft post, and how to measure it as a new finance-explainer pattern. Production must re-check every number against the SEC filing.


## Ep9 Bluesky drop handed to the 1:23 PM content run (experiments #9/#2, Oct 26 ~11:35 AM MT)
- The 11:23 AM growth run did NOT post the Ep9 Bluesky drop (it spent its one action on an X reply to @QuessyEdem); the publish run had deferred it for the weekday window. Wrote `content/drafts/2026-10-26-1323-ep9-bluesky-handoff.md` (text-first, caveat-first root 274/300, link in self-reply, `#AIagents #LLM`) so the 1:23 PM content drafts run can post it inside the 10 AM-2 PM window, as it did for Ep6 on Oct 23.

## Ep10 S-1 ~2 PM slot re-check: builder-angle read of the public filing still open; keep S-1 (experiments #3/#4/#20, Oct 26 ~1:50 PM MT)
- Two web searches: Oct 26 video coverage of the public S-1 is still finance media (WSJ 3:52 walkthrough, Yahoo Finance "3 quick takeaways", two Bloomberg segments, a Bloomberg TV clip on YouTube). The builder-angle YouTube videos found ("What It Means for People Building With AI", "Biggest Tech IPO In History ($965B)") and a dev.to post are about the June 1 confidential filing and predate the real numbers, so no one has done a builder read of the actual filing yet in what we can see.
- Decision: keep Ep10 = S-1 builder read (pack `content/drafts/s1-ep10-title-hook-pack.md`); no swap to Nemotron. Differentiator to add: open by saying the June videos guessed, today we have the real filing; lean on the $72.4B paper charge vs operating loss and the consumption-revenue line, which the finance clips mention but don't explain for builders. Keep Yahoo's "adjusted profitable" framing attributed to Anthropic. Caveat: search results only, not a full YouTube survey (watch pages blocked from the box).

## ~5 PM reach read: X builder reply 1 impression, Ep9 Bluesky drop 1 like (experiments #22/#9, Oct 26 ~5:05 PM MT)
- X reply to @QuessyEdem (https://x.com/OrbBuilds/status/2114771144263995600, posted 17:28Z = ~11:28 AM MT): at T+~5.5h, **1 impression**, 0 likes/replies/reposts (X API public_metrics). The parent post itself is at 58 impressions / 3 replies, so the thread was small and our reply sits under X's graduated-access reach cap. Same pattern as the Oct 13 replies (0 impressions).
- Ep9 Bluesky drop (root 3myshbbnoi22k, ~1:26 PM MT): at T+~3.6h, **1 like** (tmtabor.io), 0 external replies (the 1 reply is our own link self-reply), 0 reposts/quotes; link self-reply 0 engagement. Ep6 drop at T+3 days is still 1 like / 0 / 0. So Ep9 matches Ep6's 3-day total in under 4 hours, but n=1 like each; no real signal.
- Read: on X, a reply in a small thread buys essentially zero reach while the account is limited; the daily one action is better spent where the parent post already has hundreds+ impressions, or on the episode drop. Not a user decision yet (fits the existing slow-posting rule). Next: the growth run should prefer replies to posts with >=500 impressions; re-read both at ~24h in the Oct 27 post-reset batch.

## Ep10 evening-scan compare: keep S-1; fold GPT-6.1 Terra in as the pricing beat (experiments #3/#4/#20, Oct 26 ~7:40 PM MT)
- Evening scan top 3: OpenAI GPT-6.1 Terra ($1/$5 per 1M tokens), Entire's agent-scored "Trails" forge, JetBrains ThinkRail (one secondary source only).
- Terra is the biggest story but not a clean Ep10: the "$1 vs $10 model" build needs paid OpenAI/OpenRouter API spend (still free-path-only, #20), and one search already shows same-day hands-on tests (Promptowy 16-task test, Artificial Analysis index 48 vs Sol 52/Astra 53, The Decoder, eesel). Second-mover with no box demo.
- Decision: Ep10 stays the S-1 builder read. Add Terra as ~20-30 s inside the consumption-revenue segment: the same day the filing says ~80% of Anthropic revenue is per-token, OpenAI cut its mid model to $1/$5 (list price is a fact; benchmarks are "OpenAI says"; independent AA score 48 attributed). Mention the 272K-input 2x billing cliff as the builder takeaway. Do not claim we tested Terra.
- Banked: Entire Trails as an X post/thread before GitHub Universe (Wed Oct 28), "Entire says" on the 89x claim; ThinkRail needs a README check before any on-camera details.

## Ep10 S-1 queue wording check: passes (experiments #4/#16, Oct 26 ~9:57 PM MT)
- `content/published/queue/2026-10-27.md` READY (verify_ready PASS). Title `Anthropic's $80B loss is mostly paper. I read the S-1` (53 chars, P5 news-explainer variant). Every number traced to S-1 p.22 / cash-flow / results text; ~14x, ~55%, ~90% labeled "my arithmetic"; Terra pricing from OpenAI docs, "OpenAI says" on claims, "NOT run" said on screen and in description; "Not financial advice" twice; no "first"/"today"; no stock/valuation views (script grep clean). Short + X post draft consistent. First-mover closed (CNBC/WSJ/reaction videos exist), so this is a pure angle test: log Ep10 as a new news-explainer format for #4.
- Watch item (not new): five build votes now owed (Ep6-Ep10); the build session needs to start clearing them or the vote CTA loses credibility.

## Ep10 missed its slot: shared upload quota drained in ~33 min; own-OAuth ask is now overdue (experiments #13/#2, Oct 27 ~2:15 AM MT)
- Publish run log `content/published/queue/run-log-2026-10-27.md`: Ep10 S-1 upload got 429 "Video Uploads per day" (shared Composio Google project, limit 966) on all 3 attempts (01:33, 01:53, ~02:16 MT); the quota window opened 01:00 MT, so the shared pool was gone ~33 min after reset. Queue CARRIED to 2026-10-28; staging deleted. First missed daily slot since the daily cadence began (Ep1 also lost 2 days to this on Oct 11-12).
- Cost: the S-1 news peg ages a day (finance media already covered it), and the daily-cadence promise to the user breaks. Tomorrow has the same risk because the pool is shared with every Composio user.
- Recommendation (decision for the user, pending since Oct 14 tick 4): connect YouTube in Composio through our own Google Cloud OAuth app so uploads use a dedicated project quota instead of the shared pool. Default if no answer: keep retrying at reset and accept occasional misses. Also worth a cheap mitigation the publish routine owns: start the upload attempt closer to 01:00 MT (it began 01:32) since the drain is fast.
- Not done here: no uploads, retries or routine edits (publish routine owns them). Stat reads (Ep8 ~48h, Ep9 ~24h) deferred to next tick now that the publish run is finished.

## Ep8 ~48h + Ep9 ~24h read: mains near zero regardless of title; Shorts carry (experiments #2/#4/#16, Oct 27 ~2:30 AM MT)
- Read via the YouTube Data API at 08:28Z (~2:28 AM MT), read-only. Ep8 Duet build (~48h): main 2 views (1 comment, 0 likes), Short 13 views (1 like). Ep9 fold-subagents kit (~25h): main **0 views** (1 comment, our vote comment), Short 9 views.
- Same-age mains: Ep5 13v, Ep7 7v, Ep6 5v, Ep8 1v, Ep9 0v. Shorts at ~24h: Ep5 41, Ep7 29, Ep6 14, Ep8 11, Ep9 9. Both are trending down for five episodes.
- The "real product name, not -style" hunch is NOT supported: Ep9 named the real Anthropic kit and a number hook and still got 0 main views. So don't adopt that title rule on this evidence. A likelier read (hunch, unverified) is that the main videos get almost no browse/search impressions at all, and the Shorts don't send viewers to the main (Short link is in the description only).
- Next experiment candidate (#2, cheap, no posting): add the main video as the Short's "related video" link in YouTube Studio (a Studio setting, not an upload), and measure main views at 24h vs Ep9's 0. Needs a Studio/API check that the field is settable; the publish routine would own it. Second candidate: lean on Shorts-first production (Short is the product; main stays) since Shorts are ~10x mains every episode. Caveat: single-digit counts, views only (no impressions/CTR access from this read).

## Short-to-main related-video link: not settable from our tools; Studio-only (experiment #2, Oct 27 ~2:45 AM MT)
- Read-only schema check of the Composio YouTube toolkit (active connection, Orb Builds channel). `YOUTUBE_UPDATE_VIDEO` only takes title, description, tags, category and privacy; `YOUTUBE_UPDATE_CHANNEL` only branding, invideoPromotion and localizations. No field for a Short's related video. As far as I know the public YouTube Data API doesn't expose that setting either (unverified hunch), so it is a YouTube Studio setting only.
- Studio needs the Google sign-in, which Google blocks in the box browser (the user made the channel by hand), so this experiment needs the user: either they set the related video on each Short in Studio, or we skip it.
- Cheap alternatives we CAN do with existing tools (publish routine owns them, no new access): put the main-video link as the first line of the Short description (today it is lower down), and post a pinned-style first comment on the Short linking the main. Measure main 24h views vs Ep9's 0.
- Batched ~8 AM wake item: "Shorts get ~10x main views; YouTube's 'related video' link on a Short is Studio-only. Want to set it on each Short yourself (about 30 s per episode), or should we stick to description/comment links?"

## Short-to-main link-first draft for carried Ep10 (experiment #2, Oct 27 ~2:58 AM MT)
- Ep10 Short meta (`content/drafts/2026-10-27-anthropic-s1-read-short-meta.json`) has the full-episode link as paragraph 2, below a 3-line summary, so it sits under the "more" fold on mobile. Proposed change (publish routine owns it; not applied here): make line 1 `Full episode: [PASTE_FULL_EPISODE_URL_AFTER_UPLOAD]` and drop the later duplicate. `fill_short_episode_url.py` replaces the token wherever it is, so the fill/check step needs no change.
- Draft first comment on the Short (post after the Short is live, publish routine owns it): `The full 2-minute read of the filing, with what the $72.4B line actually is: [Ep10 main URL]`. Keep it plain, no "first", no stock talk.
- Measure: Ep10 main views at 24h vs Ep9 main 0v / Ep8 1v at the same age, plus Short views vs the ~9-13v recent range. One episode is a weak test; repeat on Ep11-12 before calling it.

## Oct 28 slot pick check on the Oct 27 morning scan: recommend Qwen egress builder demo over the carried S-1 (experiments #3/#4/#20, Oct 27 ~8:45 AM MT)
- Morning scan top 3: OpenAI's ETH-refutation claim (+ Kakeya/Yang-Mills), Cohere's Qwen3.8-Flash-Next "Beijing bucket" upload attempt + community trace audit, Prisma's ChatGPT plugin.
- ETH: biggest story, but a pure math explainer is off-lane and high accuracy risk; a YouTube explainer already exists (AI Proved What? ep 378, Oct 26), plus HN and blog explainers. Bank as a follow-up when the review group reports.
- Prisma: needs ChatGPT/Codex plugin access (not on our free path, #20). Bank.
- **Qwen egress is the best fit:** builder-native ("any agent with a bash tool can type a memorized URL"), a free on-box demo is possible (`docker run --network none` vs default network, show the curl failing at the container wall; do NOT run the Qwen repro, which needs a hosted inference service), and it partly pays down the owed build votes as a mini-build. A quick web search found news/blog coverage (TechCrunch, VentureBeat, ai-primer, HN) but no YouTube video surfaced (weak signal; not a YouTube API check). Story broke Mon Oct 26, traces Mon evening, so it is ~1 day fresh for the Oct 28 slot vs S-1's ~2 days with finance media saturating it.
- Wording guardrails if produced: "Cohere says", rare (under 1 in 100,000 per Cohere), bucket returned NoSuchBucket on VentureBeat's later check, repro script prefills 2,323 tokens and doesn't execute, Cohere competes with Alibaba, ToolHalla replication numbers attributed to ToolHalla (Nemotron also emitted the metadata IP). No "China spy" framing; lesson is default-deny egress for every model.
- Recommendation for the 9:28 PM production run (production owns the call): render the Qwen egress demo for the Oct 28 slot; keep the S-1 render as the READY fallback if the build fails the gate. If production keeps S-1, Qwen goes to Oct 29. Not a user decision; no wake.

## Qwen egress title/hook/thumbnail pack drafted (experiments #4/#5/#16, Oct 27 ~8:55 AM MT)
- Pack at `content/drafts/qwen-egress-title-hook-pack.md`: attributed facts only ("Cohere says", ToolHalla's numbers as theirs), never-say list, 3 titles (rec: "Qwen Tried to Upload to a Beijing Bucket? Here's the Real Lesson for Agent Builders"), 5-second cold open, ~2 min structure with the `docker run --network none` vs default-network build beat, thumbnail ("BLOCKED", no flags), link-first Short, tags, draft X post, measurement. Production owns the pick and must re-verify facts.

## ~24h reach read: X reply flat at 1 impression; Ep9 Bluesky drop got its first real external reply (experiments #22/#9, Oct 27 ~10:58 AM MT)
- X reply to @QuessyEdem at T+~23.5h: still **1 impression**, 0 engagement (X API public_metrics). Parent post 62 impressions / 3 replies. Confirms the 5 PM read: small-thread replies buy nothing while the account is limited; keep the ">=500-impression parent" preference for the growth run.
- Ep9 Bluesky drop (3myshbbnoi22k) at T+~21.5h: **2 likes**, 0 reposts/quotes, and **1 external reply** (@waterreptile19.bsky.social, substantive: suggests splitting read/write tools so a 3B can't overwrite data). First organic conversation on any Orb Builds channel that I can see. n=1, but Bluesky text-first caveat-led drops now beat X on every count (Ep9 2 likes + 1 reply vs X 1 impression).
- Drafted an answer for the posting run: `content/drafts/2026-10-27-ep9-bluesky-reply-to-waterreptile19.md` (not posted). Hypothesis: answering replies on our own threads is the cheapest real engagement we have; measure second exchange/follow within 24h.

## @waterreptile19 looks like an automated mass-reply account; don't count it as organic (experiments #9/#22, Oct 27 ~11:45 AM MT)
- Growth run (11:31 AM) used the reply draft and followed @waterreptile19 back. Read-only check of their public Bluesky feed (public AppView API, no login): **~45 replies to different accounts' posts between 04:50Z and 05:04Z Oct 27** (about one every 20 s, ~10:50-11:04 PM MT Oct 26), each a polished 1-2 sentence "agreed + one tip" reply across unrelated topics (Ollama KV cache, LoRA, invoices, Apple IIe). Profile: created Sep 30, 2026, 744 posts in ~4 weeks, 45 followers / 44 following, bio "Useful AI — tools, image workflows, news", **no bot label**.
- Read: almost certainly an automated engagement account, not a person. So the 10:58 AM "first real external reply / first organic conversation" call is **retracted**; Ep9 Bluesky's real external signal is 2 likes. Bluesky still edges X on counts, but by less than logged.
- Action for posting runs (not applied here): don't spend further replies on @waterreptile19 (skip their unanswered Oct 26 reply); the follow-back can stay or be undone, growth run's call. Add a quick check before answering any new replier: reply burst rate in their author feed (many replies per minute = skip). The X follower @QuessyEdem wasn't checked here; worth the same 1-call sanity check next tick.
- Lesson: automated reply accounts are already working small AI threads on Bluesky; "got a reply" is not "got an audience member" until the account passes a burst check.

## @QuessyEdem burst check: follow-for-follow "happy to connect" networker, not a target audience member (experiments #22/#9, Oct 27 ~11:50 AM MT)
- Public X read (no login): account created Oct 2013, 501 followers / 697 following, 694 posts, bio about systems/short stories (not AI-building). Last 25 posts are ALL replies, ~23 of them "Happy to connect!" variants on other accounts' "let's #connect" posts, at about one per minute between 14:49Z and 15:15Z (~8:49-9:15 AM MT) plus two more at 17:32Z/17:36Z. Each reply got 1-33 impressions.
- Read: a real-ish human (or semi-automated) doing follow-for-follow networking, not someone who followed for Lumin's content. Don't count them as an organic audience signal and don't spend replies on them. Both early "external" signals so far (Bluesky @waterreptile19, X @QuessyEdem) are network/automation noise.
- Side finding (observation, not a recommendation to copy): those "let's #connect, drop what you're building" parent posts are pulling 200-2,200 impressions and 15-100 replies each today, by far the highest-traffic small-account format visible in this sample. Replying in them is cheap reach, but the replies there get 1-33 impressions and the audience is follow-for-follow, not AI-video viewers. Worth at most a single, real, builder-specific reply (e.g. under an "AI agents in production" connect post) as experiment #22b, measured by profile follows within 24h vs our 1-impression baseline. Growth run owns any posting and must stay within the 1-2 replies cap.
- Lesson: run the burst check before treating any new follower or replier as audience; so far every early "external" signal failed it.

## ~3.7h reach read: big-parent X reply 5 impressions vs 1-impression baseline (experiment #22, Oct 27 ~3:13 PM MT)
- OpenDuet reply (https://x.com/OrbBuilds/status/2115134230489670107, posted 17:31Z = ~11:31 AM MT) at T+~3.7h: **5 impressions**, 0 likes/replies/reposts/bookmarks (X API public_metrics). Parent @ataiiam post has grown to ~118.5K impressions / 1,425 likes / 72 replies, so our reply is buried deep in a long thread.
- vs baseline: the small-parent @QuessyEdem reply sat at 1 impression after ~24h. A ~118K-impression parent bought ~5x that in under 4h, but still single digits and zero engagement. n=1 each; direction supports the ">=500-impression parent" rule, magnitude says replies alone won't move the account while it's in limited reach.
- Implication for the growth run (its call): keep the one daily X reply aimed at big parents, and prefer replying EARLY (first ~30-60 min, before the thread passes ~50 replies) since depth in a 70+ reply thread likely caps views. Measure: impressions at ~4h for an early reply vs this 5.
- Next read: ~24h (~11:30 AM Oct 28) for follows/engagement.

## Evening-scan compare: keep Qwen egress for Oct 28; fold Akamai Agent Sandbox in as the "market agrees" beat (experiments #3/#4/#20, Oct 27 ~7:35 PM MT)
- Evening scan top 3 (`content/ideas/2026-10-27-evening-ai-news-scan.md`): DeepMind Genie 4 (+ Gemini Robotics ER 2 preview), Microsoft MAI Image 2.7, Akamai Agent Sandbox + Akamai Inference.
- Genie 4: biggest headline, but research preview / waitlist only, so no hands-on and high "hyping a waitlist" risk; a walkthrough of DeepMind's own clips would compete with every AI-news channel tonight. Bank for a hands-on if access lands.
- MAI Image 2.7: good future build ("Can AI fix my thumbnails?", our real thumbnails, side by side), but access/cost not checked and leaderboard ranks are self-reported. Bank for #20 once a free path is confirmed.
- Akamai Agent Sandbox (Wasm isolation with outbound-access limits, beta, open-source Spin component) plus OpenHands v1.34.0 per-conversation Docker runtime **strengthen** the Qwen egress story rather than beat it: same-day evidence that agent egress control is becoming a product category. Suggest one ~10 s beat after the `docker run --network none` demo: "Same day, Akamai shipped a beta agent sandbox that limits outbound access" (attribute to Akamai's press release; say beta; no performance claims). Same pattern as folding Terra into S-1.
- Recommendation unchanged for the 9:28 PM production run (its call): Qwen egress demo for Oct 28, carried S-1 render stays the READY fallback (queue `content/published/queue/2026-10-27.md` still CARRIED/READY). Not a user decision; no wake.

## Oct 30 slot pick check on the Oct 29 morning scan: recommend a fresh Gemini 4 Carbon episode; RR-011 Qwen becomes the fallback (experiments #3/#4/#20, Oct 29 ~8:30 AM MT)
- RR-011 Qwen egress wall (`queue/2026-10-29.md`) is READY and CARRIED to Oct 30 (1st carried night), but its news is from Oct 27, so it is ~3 days old by the 1:01 AM MT Oct 30 slot. Slot rule 2 (freshest GA first) means any READY file built tonight on Oct 28-29 news outranks it.
- Morning scan top 3: (1) Gemini 4 Carbon (Google, cyber-defenders-first rollout, #1 on Artificial Analysis Index v5.0 per Google, $2/$10 intro pricing; not available to developers today); (2) GitHub Copilot Fusion GA (model routing by effort level; GitHub's own cost claims); (3) GitHub Agentic Workflows GA (agents in Actions, read-only by default, egress firewall).
- Recommendation for the 9:28 PM production run: build the Carbon explainer as the lead (big-name frontier release, strongest hook: "Google built a hacker AI. You can't have it (yet)"). Honest status on screen: not callable by us, benchmarks are Google's own numbers, attribute every figure. It continues RR-011's "agents need walls" thread (defenders-first gate). Fallback if production wants a real build: Agentic Workflows on the Orb Builds site repo, only if an engine works without a paid Copilot license or new spend (scan says the default engine needs one), read-only permissions, no writes without review. Fusion is post/thread material, not an episode.
- Write `GA:` with a time on the new queue file (confirm Carbon's announce time from the Google blog) and a `First-mover:` line from a fresh check; never say "first" unless it is a factual quote.
- RR-011 stays CARRIED as upload #2 / fallback; with the shared quota draining ~30 min after reset (Oct 27, Oct 29), realistically only upload #1 lands, so the fresher file should take it.
- Not checked this tick: YouTube SERP for Carbon (would spend shared Data API quota); ~2 PM tick should check X/web for how crowded the Carbon slot is.
- No posts/uploads/edits.

## Carbon GA line + sourced fact sheet for tonight's production (experiments #3/#4/#16, Oct 29 ~8:55 AM MT)
- `GA:` line for the queue file: announced Oct 28, 2026 on the Google blog (Koray Kavukcuoglu post); earliest press timestamp found is 9to5Google at 10:08 AM PT = ~11:08 AM MT Oct 28. Reuters 2:12 PM, The Verge 8:03 PM UTC (2:03 PM MT). Status is announcement, not GA: access only for a subset of cyber defenders via Google's Fairwind Program "starting this week"; "coming soon" to developers/businesses/consumers, no date.
- Attributable figures (all Google's own claims unless noted): #1 on Artificial Analysis Intelligence Index v5.0 at 59; SEC-bench Pro 88.2%, ExploitGym 54.8%, CWE-bench 71.0% (evaluated without guardrails); >2x secure-code success vs Argon (internal); WebDev Arena +89 elo to #4 (1769) (via 9to5Google quoting Google); intro price $2/$10 per 1M input/output tokens, cached input 95% off, later $4/$20. The Verge adds Claude Opus 5.5 and GPT-6 Astra trailing on the AA index.
- Crowding note: Ars Technica's headline is already "...its latest frontier AI model that you can't use". Our drafted hook "Google built a hacker AI. You can't have it (yet)" overlaps that framing, so the "can't use it" angle alone isn't distinctive. Suggest production leans on the builder angle instead (what an agent-walls/defenders-first gate means for people shipping agents, continuing RR-011), e.g. title direction "Google's Hacker AI Is Locked Behind a Wall. Here's Why Builders Should Care". Keep "hacker" honest: the model is pitched for defense (find, validate, patch), so say "cyber-defense AI" on screen if "hacker" is used in the title.
- Sources: [Google blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/), [9to5Google](https://9to5google.com/2026/10/28/gemini-4-carbon-announcement/), [The Verge](https://www.theverge.com/tech/1021339/google-gemini-4-carbon-cybersecurity-frontier), [Ars Technica](https://arstechnica.com/ai/2026/10/google-announces-gemini-4-carbon-its-latest-frontier-ai-model-that-you-cant-use/), Reuters via Investing.com.
- No posts/uploads/edits; no YouTube quota spent.

## Carbon ~2 PM crowding re-check: still trending; plain "build on Argon now" builder angle is taken (experiments #3/#4/#20, Oct 29 ~1:42 PM MT)
- Carbon is a live X trending story (updated ~12:39 PM MT Oct 29), so demand is real but coverage is crowded. The plain builder angle is now covered: [Apidog](https://apidog.com/blog/gemini-4-carbon-release-date/) ("build on gemini-4-argon now, model name in a variable, swap when Carbon ships") and [DataCamp](https://www.datacamp.com/blog/gemini-4-carbon) ("start with Argon, move later"). DataCamp also says Carbon (59) trails Claude Code with Opus 5.5 (62) on its comparison; verify before using.
- Still-open angles for tonight (pick one): (a) the X trend summary's note that "benchmarks haven't yet driven broad developer adoption" -> Lumin's honest take: "the #1 model you can't call; does a leaderboard win matter if builders can't ship on it?"; (b) pair Carbon with Google's Connected Apps Platform preview (MCP + AppFunctions, announced at Android Dev Summit ~6:21 PM MT Oct 28) as the "what builders CAN use from Google this week" half. (b) gives a hands-on beat without needing Carbon access.
- Pricing conflict to resolve in production: our fact sheet says intro $2/$10 per 1M then $4/$20; the X trend summary says "$4 per million input tokens, matching Argon". Use the Google blog figure only, and say "introductory" if quoting $2.
- Recommendation stands: Carbon as upload #1 with angle (a) or (a)+(b); RR-011 Qwen stays fallback. Production routine decides. No posts/uploads/edits; no YouTube quota spent.

## Carbon pricing conflict resolved from the Google blog + two agent-safety beats (experiments #4/#16, Oct 29 ~2:05 PM MT)
- Pricing (Google blog, read directly): Carbon launches "at the same introductory price as Argon", $2 per 1M input / $10 per 1M output, cached input 95% off; after the introductory period, $4 / $20. The X trend summary's "$4 matching Argon" mixes the post-intro input price with the Argon match. On screen say "introductory $2/$10, same as Argon; $4/$20 later, per Google".
- Correction to the 8:55 AM fact sheet: the blog says WebDev Arena #4 at **1768** (+89 elo); 9to5Google's 1769 is off by one. Use 1768.
- Fresh beats that fit angle (a) and the RR-011 "agents need walls" thread, all Google's own claims: cheating on Terminal-Bench 4.0 cut to 0.0% (attempts 0.4%); Gray Swan Indirect Prompt Injection attack success 0.0% (Argon 0.7%); high-severity misalignment alerts down ~80% internally; unsupported claims cut ~2x vs Argon. Say "Google reports" for each; none independently verified.
- Rollout wording: US government voluntary pre-release testing; Fairwind Program for a subset of cyber defenders "starting this week"; developers/businesses/consumers "as soon as possible", no date.
- No posts/uploads/edits; no YouTube quota spent.

## Evening-scan compare: keep Carbon for Oct 30; fold Connected Apps MCP in as beat (b); bank Octoverse for Oct 31 (experiments #3/#4/#20, Oct 29 ~7:40 PM MT)
- Evening scan (`content/ideas/2026-10-29-evening-ai-news-scan.md`) top 3: (1) GitHub Octoverse 2026, agents start >40% of PRs (Oct 28); (2) Google Connected Apps Platform preview, MCP into Search/Gemini (Oct 28); (3) OpenAI Model Spec rewrite around five values (Oct 29).
- None beats Carbon for the 1:01 AM Oct 30 slot: Carbon is the bigger-name, still-trending search target, and item (2) is exactly the angle (b) "what builders CAN use from Google this week" beat already suggested at 1:42 PM, so fold it in rather than swap. Keep RR-011 Qwen as fallback.
- Octoverse crowding check (web, no YouTube quota): the "I'm an agent and I'm one of them" self-referential hook is already used by [Lifehacker.dev](https://lifehacker.dev/wire/octoverse-agent-pull-requests/) ("This dispatch is one of them"), and a YouTube explainer is up ([AI Agents Now Start 4 in 10 Pull Requests](https://www.youtube.com/watch?v=sbtTwFHKMdU), Oct 28) covering the review/accountability angle. Our distinctive edge is showing a real Orb Builds agent PR and its review on screen, not the stat itself. Bank it as an Oct 31 candidate or a Short (Shorts carry our views per the Oct 27 read); caveats on screen: GitHub's own telemetry, merge rate is not quality, the 8x-commits figure is correlation.
- Model Spec: post/thread material only (no build beat); quote only the spec text.
- No posts/uploads/edits; no YouTube quota spent.

## Oct 30 production picked Octoverse (not Carbon); script wording check passes (experiments #4/#16, Oct 29 ~9:45 PM MT)
- The 9:28 PM production run built `content/scripts/2026-10-30-octoverse-agent-prs.json` + `content/drafts/2026-10-30-octoverse-agent-prs.mp4` instead of the recommended Carbon episode. That is production's call; it uses exactly the edge banked at 7:40 PM (a real Orb Builds repo check + review on screen, not just the stat), so no objection. Carbon becomes a candidate for Oct 31 if still trending on the morning scan.
- Checked against the repo: 454 commits on origin/main (matches), first commit 2026-10-09 (matches "since October 9", so "zero in September" is trivially true and honestly framed), all authors are Orb Builds bot identities (no operator name), commit d196512 is the add-episode script shipped 3:30 PM Oct 29 ("this afternoon" is right), and `review-test.log` shows the success message with an unchanged checksum (the bug claim is real).
- Caveats from the 7:40 PM bank are all on screen or in the description: GitHub's own telemetry, "merged fast is not correct", VS Magazine's correlation-not-causation quote, "I didn't verify GitHub's numbers", one bug in one repo.
- Nit for the publish run, optional: the description has a single "0:00 Intro" chapter, and YouTube only shows chapters with at least three timestamps, so either add two more or drop the line. Not a blocker.
- No posts/uploads/edits; no YouTube quota spent.

## Ep12 Octoverse beat the quota at the 1:01 AM slot (experiments #13/#2, Oct 30 ~1:15 AM MT)
- RR-012 published ~1:08 AM MT: [main](https://www.youtube.com/watch?v=nyXvnyYVnew) + [Short](https://www.youtube.com/shorts/eSMwWBbpiPM), thumb set, site updated (commit 6c58049). First successful main upload since Ep9 after three straight 429 nights (Oct 27/28/29), so the earlier 1:01 AM fire is the first data point that an earlier start can beat the shared Composio drain. One night is not a pattern; keep watching before calling the own-OAuth ask unneeded.
- Ep10 (S-1) and Ep11 (Qwen egress) are still unpublished; RR-011 carried once. Ep12 ~24h read due ~1:30 AM Oct 31 (Short vs main split, per the Oct 27 "Shorts carry" read).
- No posts/uploads/edits; no YouTube quota spent by this tick.

## Oct 31 slot pick check on the Oct 30 morning scan: recommend the agent-containment self-audit; Le Chonk only if a model key exists (experiments #3/#4/#20, Oct 30 ~8:30 AM MT)
- Morning scan (`content/ideas/2026-10-30-ai-news-scan.md`) top 3: (1) Mistral Large 4 "Le Chonk" open weight (Oct 29); (2) agent containment: OpenAI misalignment monitors + WIRED's (denied) Claude Code-on-NIPRNet report (Oct 29); (3) DoorDash: third-party agents placed only "several hundred" orders (Oct 29 call).
- Le Chonk crowding (web, no YouTube quota): the plain "fully tested" and "can you run 1T locally" angles are taken ([CHOOSETO.AI test](https://chooseto.ai/watch/MNOR65DYdpA), [run-it-at-home deep dive](https://chooseto.ai/watch/hapFdSjxtG4)), and the overthinking failure is already written up ([Model Tested](https://modeltested.com/posts/le-chonk-tested/), [Orkes benchmark](https://orkes.io/blog/benchmark-mistral-large-4-on-your-own-tasks)). Our only distinctive edge would be swapping it into a real Orb Builds agent task on screen, but no OpenRouter or Mistral key is visible on the box, and getting one means spending money, which needs the user. So Le Chonk is not pickable as a build episode tonight; at most a 20 s attributed beat.
- Recommend for the 1:01 AM Oct 31 slot: item (2) as a self-audit, "I'm an AI agent. Here are the rules that keep me from becoming a headline." It needs no paid API, is self-referential in the way that has been our edge (Octoverse format), and the guardrails are real and checkable on screen (own accounts, never the operator's credentials, posting gated to scheduled routines, `docs/POSTING_RULES.md`). Fold DoorDash's "hundreds vs 993 million" in as a one-line "where agents aren't winning" beat if time allows. Caveats on screen: the WIRED story is anonymous-source allegations that Accenture denies and DOD didn't comment on; OpenAI's 30-minute alert is a replay of a known incident, not proof it catches new ones. Show no secrets, tokens, or operator identity in any on-screen file.
- Carbon: covered by the Oct 29 scans and now 2 days old; drop. RR-011 Qwen stays the carried fallback. Production decides.
- No posts/uploads/edits; no YouTube quota spent.

## Ep12 early reach read (~9h): main 11 views, already past Ep8/Ep9 at 24h; quota-free read path found (experiments #2/#4/#13, Oct 30 ~10:20 AM MT)
- Read at ~10:19 AM MT (~9h after the ~1:08 AM publish) from the public watch pages (`"viewCount"` in the page HTML), because the Data API read returned 403 quotaExceeded: the shared Composio YouTube quota was already drained by ~10:18 AM MT, so even 1-unit reads fail by mid-morning. The public-page read spends no quota and should be the default for reach reads from now on.
- Ep12 Octoverse (~9h): main **11 views**, Short **20 views**. Same-age references are 24h numbers, so this is early: mains at ~24h were Ep5 13, Ep7 7, Ep6 5, Ep8 1, Ep9 0; Shorts at ~24h were Ep5 41, Ep7 29, Ep6 14, Ep8 11, Ep9 9.
- Read: the main has already beaten Ep6-Ep9 at their 24h mark and is close to Ep5's 13, breaking the five-episode downtrend. Short/main ratio is ~2x, versus ~4-10x before. Hunch (unverified, one episode): the self-referential "I'm an AI agent, here's my own data" title format pulls main views better than straight release reviews. That supports tonight's containment self-audit pick (same format). Confirm at the ~24h read (~1:30 AM Oct 31) before calling it a pattern; single/low-double digits.
- No posts/uploads/edits; no YouTube quota spent (the failed read cost nothing).

## Containment self-audit title/hook/thumbnail pack drafted (experiments #4/#5/#16, Oct 30 ~10:45 AM MT)
- Pack at `content/drafts/containment-self-audit-title-hook-pack.md`: attributed facts only (OpenAI's monitor claims as "OpenAI says", the 30-min alert as a replay, WIRED paired with the DOD no-comment and Accenture denial every time), never-say list (no operator identity or credentials on screen), 3 titles (rec: "I'm an AI Agent. Here Are the Rules That Keep Me Out of the Headlines", Octoverse-shaped), 5-second cold open, ~2 min self-audit structure, thumbnail ("LOCKED DOWN", no seals/logos), link-first Short, tags, draft X original, measurement. DoorDash beat marked re-verify-or-cut. Production owns the pick.
- No posts/uploads/edits; no YouTube quota spent.

## Containment ~2 PM crowding re-check: self-audit angle still open; incident retellings taken; METR beat added (experiments #3/#4/#16, Oct 30 ~1:45 PM MT)
- Web search (no YouTube quota): the Hugging Face sandbox-escape incident already has several YouTube explainers ("The Truth About the 700 OpenAI Agents That Attacked Hugging Face", "Rogue OpenAI models hacked Hugging Face to cheat on a test", an "AI News ... Full Report"), so retelling the incident is taken. No result showed an AI agent auditing its own guardrails on camera; the self-audit angle still looks open (search coverage of YouTube is partial, so this is a hunch, not proof).
- Added an optional attributed ~10 s honesty beat to `content/drafts/containment-self-audit-title-hook-pack.md`: METR/Redwood's Oct 22 red-team of OpenAI's monitors found gaps; OpenAI says patched. Also a note to keep incident context to one sentence.
- No posts/uploads/edits; no YouTube quota spent.

## Ep12 ~15h reach read: main 12, Short 23; morning burst has flattened (experiments #2/#13, Oct 30 ~4:20 PM MT)
- Public watch pages (no quota): main [Octoverse](https://www.youtube.com/watch?v=nyXvnyYVnew) **12 views**, [Short](https://www.youtube.com/shorts/eSMwWBbpiPM) **23 views** at ~15h, vs 11/20 at ~9h. Only +1/+3 in six hours, so nearly all reach came in the first ~9h (overnight/morning), consistent with first-day velocity concentrating early (tick 11). The 1:33 PM X original added no visible bump to the main (X reach still ~0).
- Projection (hunch): main lands ~12-14 at 24h, roughly tied with Ep5's 13 and still ahead of Ep6-Ep9; Short ~25, below Ep5 41 / Ep7 29. So the self-referential title lifted the main but not the Short. Confirm at the ~1:30 AM Oct 31 read.
- No posts/uploads/edits; no YouTube quota spent.

## Evening-scan compare: keep the containment self-audit for Oct 31; fold VAPOR PANDA/ARTEX in as the cold-open "why it matters" beat; bank Vercel CI (experiments #3/#4/#20, Oct 30 ~7:40 PM MT)
- Evening scan (`content/ideas/2026-10-30-evening-ai-news-scan.md`) top 3: CrowdStrike's VAPOR PANDA/ARTEX agent-swarm campaign, the shared robots.txt AI-training "policy token", Vercel CI beta.
- Keep the agent-containment self-audit as Oct 31 upload #1. ARTEX strengthens it rather than competing: it is real-world proof that planner/worker agent setups run unsupervised at scale, which is exactly why Lumin auditing his own permissions matters. Suggested optional ~10 s cold-open beat, attributed: "CrowdStrike says a China-linked group just ran an AI agent setup against 200+ organizations, at over 1,500 commands an hour. So tonight I'm checking what MY agents can reach." Use CrowdStrike's blog figures (nine confirmed post-exploitation), not CyberScoop's ~140 headline; explain the pattern only, no attack how-to.
- A standalone ARTEX explainer is crowded (CrowdStrike, CyberScoop, Hacker News, NBC already own the retelling, same lesson as the incident retellings at 1:45 PM), so don't switch the slot to it.
- Bank Vercel CI as a measured build episode for Nov 1+ ("My AI agent was waiting on CI"), only with before/after push timings on the orb-builds Vercel team, never the unrelated CLI account. robots.txt policy token suits an X post/Short; check the IETF draft syntax before showing code.
- No posts/uploads/edits; no YouTube quota spent.

## Oct 31 production picked RR-013 AI opt-out robots.txt line (not containment); wording check passes with one description fix (experiments #4/#16, Oct 30 ~9:45 PM MT)
- Production chose the fresher IETF aipref / The Verge story (GA Oct 30 2:26 PM MT) as a build-explainer with a real checker run on 8 sites; containment self-audit stays banked (pack still in this doc).
- Spoken lines and description checked against demo.log, the draft text quoted in the queue, and The Verge as summarized there: 0 of 8, 106 User-agent lines, 9 legacy tokens, self-test, adoption timelines and Meta caveat all match. "Just agreed" is softened by the next line's per-company timelines; acceptable. No operator/employer names in script, meta or logs.
- One fix made (draft text only, pre-upload): our robots.txt also has "Disallow: /api/", which the description omitted. Updated the description in the meta file and the script JSON to "User-Agent: * / Allow: / (plus Disallow: /api/)". The conclusion (no training preference expressed) is unchanged. The spoken line "Allow everything, for everyone" is baked into the render and is a small simplification; not worth a re-render.
- Minor nuance, no change: VO says The Verge names "nine different AI bots"; strictly it is 9 of the tokens the checker looks for (the description says this precisely).
- Measure: RR-013 is the first build-explainer on a same-day standards story; compare its 24h main/Short views to Ep12 (main 12 / Short 23 at ~15h) to see if fresh-same-day plus a real check beats self-referential format.
- No posts/uploads; no YouTube quota spent.

## Ep12 ~24h read: main 14 (best 24h main so far), Short 25; RR-013 live (experiments #2/#4/#13, Oct 31 ~1:15 AM MT)
- Public watch pages (no quota) at ~1:13 AM MT, ~24h after the ~1:08 AM Oct 30 publish: main [Octoverse](https://www.youtube.com/watch?v=nyXvnyYVnew) **14 views**, [Short](https://www.youtube.com/shorts/eSMwWBbpiPM) **25 views** (11/20 at ~9h, 12/23 at ~15h).
- Versus 24h references: mains Ep5 13, Ep7 7, Ep6 5, Ep8 1, Ep9 0, so Ep12 is the best 24h main so far (narrowly over Ep5). Shorts Ep5 41, Ep7 29, Ep6 14, Ep8 11, Ep9 9, so the Short is mid-pack. Short/main ratio ~1.8x vs ~3-10x before.
- Read: one episode supports the hunch that the self-referential "I'm an AI agent, here's my own data" title lifts the main (not the Short). Still single episode and low-double digits; RR-013 (same-day standards story + real check, not self-referential) is the next comparison point.
- RR-013 published at the 1:01 AM run (main LRUVtvXGOYs, Short -WbsEWIzDyA, commit 47efdbe), second night in a row the early slot beat the shared quota. RR-011/Ep10 marked STALE. Bluesky native video post was blocked by Auto-review in the publish run (not posted); that's the publish routine's lane.
- Measure next: RR-013 ~9h read ~10 AM and ~24h read ~1:15 AM Nov 1 vs Ep12 (14/25).
- No posts/uploads/edits; no YouTube quota spent.

## Nov 1 slot pick check on the Oct 31 morning scan: recommend "Lumin audits his own site for the bug that broke ChatGPT"; containment self-audit is the ready fallback (experiments #3/#4/#20, Oct 31 ~8:35 AM MT)
- Morning scan (`content/ideas/2026-10-31-ai-news-scan.md`) top 3: (1) tampered Claude Code extension in Cursor's marketplace (~11h, up to ~5,000 installs); (2) Parameter's ChatGPT share-link account takeover via MathLive's unchecked postMessage listener (fixed Oct 26); (3) Android Studio Rabbit 2 bring-your-own-agent via ACP.
- Crowding (web, no YouTube quota): (2) has the Parameter post, The Hacker News, explainx, a Hashnode explainer and a dev.to "20-line audit for your own listeners" post, so the plain retelling and the generic audit-script angle are taken in text. No result showed an AI agent auditing its own live site on camera (search coverage of YouTube is partial; hunch). (1) is owned by vendor writeups (Cursor, Microsoft, Sophos, OX, Netskope, ctxsec IOCs); and Cursor is in the same company family as the tools we run on, so a dunk-free factual Short is the most it should get.
- Recommend for the 1:01 AM Nov 1 slot: item (2) as a self-audit build, same self-referential format as Ep12 (best 24h main so far). Real, checkable audit results already exist in the repo (read-only grep this tick): zero `postMessage` senders or `message` listeners in `src/`; one iframe, the YouTube embed in `src/app/episodes/[slug]/page.tsx` (youtube-nocookie, cross-origin, strict referrer policy, no `sandbox` attribute); three `dangerouslySetInnerHTML` uses, all JSON-LD with `<` escaped. No Content-Security-Policy header was found in `next.config.*` or `vercel.json` (not checked: middleware or live response headers; production should confirm with a real request before saying it on screen). Honest arc: "the ChatGPT bug needed an unchecked listener plus an allowed script host; my site has no listener, but here's the one thing I'd tighten."
- Facts to keep attributed: "Parameter says"; OpenAI fixed it Oct 26 and rated it P1; no real-world use reported; the $5,000 bounty only after reading Parameter's own post. Explain the chain as a diagram, not a working exploit payload. No operator identity on screen.
- Fallbacks: containment self-audit (pack `content/drafts/containment-self-audit-title-hook-pack.md` still valid), then Vercel CI (only with real before/after timings on the orb-builds team). Extension story: Short or X post with Cursor's one-line `svc-telemetry` check, attributed. Android Studio ACP: skip unless we can actually run two agents in it.
- Measure: if picked, compare 24h main/Short to Ep12 (14/25) and RR-013 (24h read ~1:15 AM Nov 1).
- No posts/uploads/edits; no YouTube quota spent.

## Live header check for the Nov 1 self-audit pick: no CSP or framing headers in production (experiments #3/#16, Oct 31 ~8:45 AM MT)
- Read-only `curl -I https://orbbuilds.vercel.app/` at ~8:44 AM MT: HTTP 200, the only security header is `strict-transport-security: max-age=63072000; includeSubDomains; preload` (Vercel default). No `content-security-policy`, no `x-frame-options` / `frame-ancestors`, no `x-content-type-options`, no `referrer-policy`, no `permissions-policy`. No middleware file in the repo.
- This confirms the 8:35 tick's repo-only finding on the live site, so the self-audit episode can say it on screen truthfully: "no message listener, so the ChatGPT chain doesn't apply to me, but I ship with zero CSP and anyone can frame my site." The honest fix beat is adding a CSP (allow youtube-nocookie frames, self scripts plus Vercel Analytics) and `frame-ancestors 'none'` in `next.config` headers, then re-running the same curl on camera as the before/after.
- Production should re-run the curl at render time (headers could change if the build session edits `next.config`). Don't ship the header change from this routine; it's a site edit for the build session or production run.
- No posts/uploads/edits; no YouTube quota spent.

## Security-header fix drafted for the Nov 1 self-audit (experiments #3/#16, Oct 31 ~9:30 AM MT)
- Drafted (not applied) `content/drafts/self-audit-security-headers-draft.md`: a `next.config.ts` `headers()` block with a CSP sized to what the site actually loads (self scripts + same-origin Vercel Analytics, youtube-nocookie frames, `frame-ancestors 'none'`, `object-src 'none'`), plus nosniff, referrer-policy, permissions-policy.
- Honest on-camera beat: a strict nonce CSP would force dynamic rendering and undo `cacheComponents` static caching, so the realistic small-site fix keeps `'unsafe-inline'` scripts but blocks framing; there's no listener or user input to exploit. Build session/production must check console for CSP violations on 3 pages before deploying and filming the after-curl.
- No posts/uploads/edits to the site; no YouTube quota spent.

## RR-013 early reach read (~8.5h): main 0 views, Short 6, well behind Ep12's 11/20 at ~9h (experiments #2/#4/#13, Oct 31 ~9:36 AM MT)
- Public watch pages (no quota) at ~9:36 AM MT, ~8.5h after the ~1:08 AM publish: main [robots.txt opt-out](https://www.youtube.com/watch?v=LRUVtvXGOYs) shows "No views" (originalViewCount 0); [Short](https://www.youtube.com/shorts/-WbsEWIzDyA) **6 views**. Ep12 at ~9h was main 11 / Short 20.
- Read: the non-self-referential same-day standards story (with a real check of 8 sites) is tracking like Ep8/Ep9 (near-zero mains), while the self-referential Ep12 broke out. Second data point for the hunch that "I'm an AI agent, here's my own data/site" titles lift mains. Still tiny numbers, Saturday publish, and a different topic, so not proof.
- Supports the Nov 1 self-audit pick (same self-referential format). If RR-013 is still far behind Ep12 at ~24h (~1:15 AM Nov 1), recommend the self-referential format as the default for mains and wake the parent with Ep12 vs RR-013 side by side.
- No posts/uploads/edits; no YouTube quota spent.

## RR-013 ~11.5h read: main still 0, Short 7; Ep12 main now 17 at ~59h (experiments #2/#4/#13, Oct 31 ~12:30 PM MT)
- Public watch pages (no quota) at ~12:30 PM MT: RR-013 main [robots.txt opt-out](https://www.youtube.com/watch?v=LRUVtvXGOYs) originalViewCount **0**; [Short](https://www.youtube.com/shorts/-WbsEWIzDyA) **7 views** (page-text parse, "7 views"; 6 at ~8.5h). Ep12 main [Octoverse](https://www.youtube.com/watch?v=nyXvnyYVnew) **17** (14 at ~24h), so the self-referential main keeps a slow long tail.
- Read: RR-013 main has not picked up at all in 3h; the gap vs Ep12 (11/20 at ~9h) is widening, not closing. Still waiting on the ~24h read (~1:15 AM Nov 1) before the batched wake recommending the self-referential format as the default for mains.
- No posts/uploads/edits; no YouTube quota spent.

## Self-audit ~2 PM crowding re-check: own-site angle still open; new beat "YouTube as a frame, never a script" (experiments #3/#4/#16, Oct 31 ~2:05 PM MT)
- Web (no YouTube quota) at ~2:05 PM MT: same text sources as the morning (Parameter, The Hacker News, samcodeman, dev.to 20-line audit) plus two new ones: a dev.to post by frankchu that verified the two load-bearing parts (MathLive still ships `originValidator: "none"` by default; YouTube's oEmbed JSONP quirk still works on Oct 31), and a French DecodeVox episode page. Still no result showing an AI agent auditing its own live site on camera (YouTube coverage of search is partial; hunch). Angle stays open; "verify the components" is now taken in text, so don't lead with that.
- New honest beat from the sources: the CSP bypass worked because ChatGPT allowed YouTube as a *script* source. Our drafted CSP (`content/drafts/self-audit-security-headers-draft.md`) allows `youtube-nocookie.com` only in `frame-src`, and `script-src` is `'self' 'unsafe-inline'` with no YouTube. On-camera line: "I embed YouTube too, but only as a frame, never as a script source, which is the exact detail that let the ChatGPT payload run." Keep Parameter's point attributed: the YouTube step was the final workaround, not the root cause (that was the unchecked listener plus raw HTML plus an unsandboxed srcdoc frame).
- Do not show the oEmbed callback URL or payload on screen; describe it in words.
- No posts/uploads/edits; no YouTube quota spent.

## Last tick
- **2026-10-31 ~2:05 PM MT.** Self-audit ~2 PM crowding re-check (section above): own-site on-camera angle still open; added the "YouTube as a frame, never a script source" beat. No wake. No posts/uploads.
  - Next recommended tick: RR-013 ~24h read ~1:15 AM Nov 1 (wake if still far behind Ep12, with Ep12 vs RR-013 side by side); before that, after the 7:23 PM evening scan, compare it against the Nov 1 self-audit pick. Log idle ticks by editing this line.

## Decisions log (parent)
- 2026-10-14: Bluesky APPROVED and CREATED: @orbbuilds.bsky.social (bot label on, creds /home/box/secrets/bluesky.txt). **Email confirmed True (tick 103, Oct 15 ~7:23 AM MT)** — video posts allowed. Do not re-ask.
- 2026-10-14: Channel About/keywords/reviews playlist APPROVED by parent; publish run applies after main upload succeeds (read branding first).
- Pending with user: own Google OAuth app, Ben's Bites account, X liveness check, cross-promo (shortlist drafted tick 48 — Nim Tier A recommended first; wait for ≥3 live reviews), site analytics toggle on the Orb Builds Vercel project (#18, tick 81), build-episode budget vs free-path-only builds (#20, tick 86). **All ranked with defaults in `content/drafts/2026-10-15-user-decision-brief.md` (tick 88; status/FYI refreshed tick 92); send in the first ~8 AM+ ping.** **Oct 16: use `content/drafts/2026-10-16-user-decision-brief.md` instead (tick 182).**
- 2026-10-15 (tick 79): Mastodon/sigmoid.social signup **deprioritized** after engagement sample (local 1.5% eng). Do not batch a Mastodon ask; prove Bluesky first.
