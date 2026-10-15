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
- YouTube: Ep0 6 views, Ep1 6 views / 0 likes / 0 comments. Ep2 (Gemini 4 Argon) rendered and queued.
- X: 0 followers, recent posts 3–9 impressions.
- GitHub: 0 stars.

## Ranked experiment backlog
| # | Experiment | Hypothesis | How to measure | Status |
|---|-----------|-----------|----------------|--------|
| 1 | Competitive study of titles, thumbnails and hooks on similar channels | Proven patterns from AI-news and AI-character channels can be borrowed honestly and get more clicks than our current generic titles | Patterns library below; then rotate patterns via #2 | **Done (tick 1, Oct 14)** |
| 2 | Rotate one title pattern per daily episode (patterns P1–P5 below) | Some patterns get much better click-through at our size than others | **Proxy (confirmed):** views / likes / comments at ~24h and ~72h via Data API (`YOUTUBE_GET_VIDEO_DETAILS_BATCH`). CTR/impressions/traffic source are **not** available through Composio (no Analytics API tools). Log each row with pattern ID in GROWTH_LOG | **In progress (tick 44):** measurement locked; rotation assigned; packs ready for Ep3 (P1), Ep4 (P5), **Ep5 (P3/P2, Ling-3.1-flash candidate)** |
| 3 | Speed-to-publish: ship reviews of big releases within ~24h of general availability | Search and Browse demand peaks in the first day; most top results for "Gemini 4 Argon" were under 24h old when checked | Hours from GA to our publish, compared with 72h views | **In progress (tick 45):** Ep3 Ultramarine queue PENDING_RENDER; YouTube SERP still empty of AI reviews at ~9:26 PM MT; CEO ~955K impressions; growth-pack replies refreshed (@ivanainai preferred); dedicated-quota decision still pending |
| 4 | Lean into the openly-AI angle ("an AI reviews the AI…") | Being an AI is our only edge over human reviewers. Neuro-sama's titles that make the AI itself the hook get above-median views | Compare 24h/72h views (Data API) of P5 primary-hook titles vs P1 titles that only use a secondary AI tag; CTR still unavailable | **In progress (tick 35):** Hermes Agent v0.22 filled into Ep4 P5 pack (gate 1); thumb `content/drafts/ep4-cand-hermes-agent-thumb.jpg`. Production fills `[Product]` only if Ep4 topic stays Hermes; else swap pattern |
| 5 | Vertical Shorts cut from each episode (30–45 s hook + verdict) | Shorts are the discovery surface for small channels. About 70% of Neuro-sama's uploads are Shorts | Shorts views, and subscribers gained from Shorts. Watch the upload quota cost first | **In progress (tick 22):** tools + Ep2 CTA Short ready; **short-meta auto-fill** (`tools/video/short_publish_meta.py` → `<slug>-short-meta.json` via `post_render.sh`). Ep2 JSON ready. Upload still waits on quota after main episode |
| 6 | Thumbnail A/B with YouTube Test & Compare (reaction face + logo vs scoreboard/versus) | A versus or scoreboard layout reads faster in a crowded feed | Test & Compare winner and watch-time share | **Prepped (tick 15):** P6 thumbnail tool built; Ep2 v2 swapped in (v1 kept as B). Test & Compare is Studio-only (no Composio tool), so measuring it needs a person |
| 7 | Audience vote loop ("pick what Lumin builds with it next") in the video and pinned comment | A return reason plus a low-effort comment prompt raises comments and returning viewers | Comments per video at 24h/72h vs Ep1's 0 (returning viewers not available via Composio) | **In progress (tick 30):** Ep2 comment draft ready; **template + series rule wired** (outro = reply 1/2/3 from Ep3 on); Ep3 comment drafts in `content/drafts/ep3-vote-comment-draft.md` (Candidate C Ultramarine added tick 34). Still needs a poster after upload |
| 8 | Search-first metadata: exact product name in the first ~40 characters, chapters in the description | Small channels get found through search before Browse | Traffic-source share isn't available via Composio; proxy = 72h views vs Ep1 baseline, plus a manual Studio spot-check if ever available | **In progress (tick 47):** chapters checker `tools/video/chapters.py` in post_render (Ep3 had a 9 s chapter, fixed); Ep2 meta (tick 3); autocomplete tool + series checklist (tick 39); Ep3 Candidate C tags/hashtags now collision-safe in the pack copy production will paste |
| 9 | Community map: places beyond X where an openly-AI show is allowed and wanted | X is throttled (graduated access), so a second outside channel matters more than more X replies. Some communities ban AI-written posts outright; picking ones that allow them avoids bans and wasted effort | A table of communities with size, self-promo rule and AI-content rule, each quoted from the community's own rules page; later, referral views per channel (proxy: views in 24h after a share) | **In progress (tick 46):** HN/Discord out; Bluesky live; text-first + **morning ~10 AM–2 PM MT** drop; hours 16–18 weaker than 10–15 on `#AI` (hour 18 matured); Critical AI allowlist-only; Ben's Bites pending; Reddit parked |
| 10 | Get @OrbBuilds out of X graduated access the sanctioned way | Reach on X is capped by the account's limited state, not by post quality (replies 0 impressions, posts 3–9). Lifting it is worth more than any X copy tweak | Logged-out handle search shows the account; reply impressions above 0; no human-check notice after posting | **Researched (tick 23):** two operator-only paths found (liveness check, automated-account label); needs a user decision, batched |
| 11 | Channel-level discovery: fill the blank channel About, keywords, and a public "AI Release Reviews" playlist | A blank About and no playlists waste search surface and session time; filling them costs no upload slot | Hygiene, not an A/B test: log the go-live date so later view changes aren't credited to the wrong experiment; channel views/subs via Data API | **Ready for publish (tick 26):** APPROVED. Steps wired into `content/published/queue/2026-10-15.md`. Draft in `content/drafts/channel-seo-setup.md`. Apply after tonight's main upload (+ Short) succeed |
| 12 | Site landing page lists each live episode the same day (`src/lib/episodes.ts` + `public/episodes/`) | orbbuilds.vercel.app is a second discovery surface; Ep1 is listed but Ep2 was missing from the publish checklist, so a successful YouTube upload would still leave the site stale | Hygiene: site shows the new episode within ~1 day of YouTube publish (auto-deploy on push to main). No site analytics yet, so no referral claim | **Ready for publish:** Ep2 draft + `rr-002.jpg` (tick 31); **Ep3** draft `content/drafts/ep3-site-listing.md` + `rr-003.jpg` (tick 40). Apply each only after that videoId is public |
| 13 | Treat the ~1 AM MT post-reset window as the only YouTube API window, and order calls inside it | On shared quota, any YouTube call after the window (stats, private-to-public flip, playlist, SEO) can fail, so the publish run has to do everything YouTube in one ordered pass | Hygiene: each publish run logs which steps succeeded; 24h/72h stats rows actually get filled | **Wired (tick 32–33):** evening probe failed, no scheduled-publish field exists, order + stats pull added to the Oct 15 queue; standing queue rules in `queue/00-README-slot-rules.md` (tick 33) |
| 14 | Standard description footer that cross-links the previous live review, site, code, X and Bluesky (and the reviews playlist once it exists) | Ep1 ends with only Code + X, so a finished viewer gets no next click from us; links ride in the upload call and cost no extra quota | Hygiene + weak proxy: Ep1 views at first-footer upload, then +24h/+72h (Data API). No traffic-source data via Composio | **Ready for publish (tick 42):** Ep2 queued `publish_description` now has Previous/site/code/X/Bluesky (script + queue note); Ep3 pack still points at `description-footer.md`. Playlist line still skipped on first night. No back-fill of Ep1 on shared quota |

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

**Also noticed:** `videos.insert` has a `status.containsSyntheticMedia` field. Lumin is openly AI, so the publish routine should set it to `true` on every upload (consistent with the honesty rules).

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
- **Account live (tick 26):** @orbbuilds.bsky.social created (bot label on; email still unverified per decisions log). Do not re-ask.
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
- **Ep2 preferred file:** `2026-10-14-gemini-4-argon-short-cta.mp4` (S1c). Title: `Gemini 4 Argon in 50 seconds (AI hype check)`. Description opens with a one-line summary, then `Full episode: [URL]` once the main upload returns an ID. Tags + `#Shorts`; `containsSyntheticMedia: true`.
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
  - Title: `[Product] in [N] seconds ([blurb])` where N is the Short duration rounded to the nearest 5 s, and blurb comes from the parent title pattern (P2 → "AI hype check", P1 → "AI review", P5 → "AI vs AI", …).
  - Description: one-line summary, `Full episode: [PASTE_…]` placeholder, source URL, honesty lines, `#Product #Shorts #AInews`.
  - Tags from script meta + product / AI Shorts; `containsSyntheticMedia: true`; `short_pattern` = `S1c` (CTA end card) or `S1`.
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

## Last tick
- **2026-10-14 ~9:58 PM MT (tick 47).** Ep3 flipped READY (~9:50 PM). Pre-publish audit found chapters that YouTube would reject (8.4 s teaser chapter) and an inaccurate `#OpenSource` hashtag; fixed both in the script meta + queue. Built `tools/video/chapters.py` and a warn-only check in `post_render.sh`. No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which file(s) went up, status lines, first stats rows (Ep1 views as #14 baseline); morning Bluesky drop ~10 AM–2 PM MT (refreshed Ep3 pack); optionally run `chapters.py check` on any new render. Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~9:38 PM MT (tick 46).** Pushed #9: matured Bluesky hour 18. `#AI` hour 18 still weak vs 10–15 MT (34% vs 41%); AI News holds; text>link confirmed; morning drop rule unchanged. Ep3 queue still PENDING_RENDER (production running). No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which file(s) went up, status lines, first stats rows (Ep1 views as #14 baseline); confirm Ep3 flipped PENDING→READY with collision-safe tags + footer; morning Bluesky drop ~10 AM–2 PM MT (use refreshed Ep3 pack). Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~9:26 PM MT (tick 45).** Pushed #3 (first-mover recheck) right before the 9:28 PM render: YouTube SERP still empty of Ultramarine AI reviews; CEO ~955K impressions; refreshed Ep3 growth-pack reply shortlist (@ivanainai preferred for own-evals catch). No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which file(s) went up, status lines, first stats rows (Ep1 views as #14 baseline); confirm Ep3 flipped PENDING→READY with collision-safe tags + footer; morning Bluesky drop ~10 AM–2 PM MT (use refreshed Ep3 pack); mature Bluesky hour 18 (after ~10 PM or morning). Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~9:25 PM MT (tick 44).** Drafted the missing Ep5 pack (P3/P2) with Ling-3.1-flash as a candidate, ran autocomplete, rendered thumb. No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which file(s) went up, status lines, first stats rows (Ep1 views as #14 baseline); confirm Ep3 flipped PENDING→READY with collision-safe tags + footer; morning Bluesky drop ~10 AM–2 PM MT; mature Bluesky hour 18. Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~9:08 PM MT (tick 43).** Pushed #3/#13 hygiene before the 9:28 PM render: wrote `queue/2026-10-15-ultramarine-1-flash.md` (PENDING_RENDER) with GA, P1, collision-safe tags, #11/#12/#14, Short, growth/vote handoff, and call order so production only fills paths and flips READY. No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which file(s) went up, status lines, first stats rows (log Ep1 views as the #14 baseline at first footer upload); confirm Ep3 flipped PENDING→READY and used collision-safe tags + footer; morning Bluesky drop ~10 AM–2 PM MT; mature Bluesky hour 18 (morning pull ok). Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~8:56 PM MT (tick 42).** Pushed #14 onto the queued Ep2: applied Previous/site/code/X/Bluesky footer into `content/scripts/2026-10-14-gemini-4-argon.json` `publish_description` and noted it on `queue/2026-10-15.md` so tonight's upload ships the footer (tick 41 had only drafted it for Ep3/template). No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which file(s) went up, status lines, first stats rows (log Ep1 views as the #14 baseline at first footer upload); confirm Ep3 used collision-safe tags, P1 and the footer if it rendered; morning Bluesky drop ~10 AM–2 PM MT; mature Bluesky hour 18 (after ~10 PM or morning pull). Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~8:55 PM MT (tick 41).** Opened #14: standard description footer (previous live review, site, code, X, Bluesky; playlist once it exists). Wired into the §4 checklist, script template and Ep3 pack before the 9:28 PM render. No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which file(s) went up, status lines, first stats rows (log Ep1 views as the #14 baseline); confirm Ep3 used collision-safe tags, P1 and the footer; morning Bluesky drop ~10 AM–2 PM MT; mature Bluesky hour 18 (should be mature after ~10 PM). Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~8:45 PM MT (tick 40).** Pushed #3 (first-mover recheck) + #12 hygiene for Ep3: YouTube SERP still empty of Ultramarine AI reviews (~8:45 PM MT); CEO post ~923K impressions; refreshed Ep3 growth-pack reply shortlist (@Easy0x preferred); drafted `ep3-site-listing.md` + `public/episodes/rr-003.jpg`. No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which file(s) went up, status lines, first stats rows; confirm Ep3 used collision-safe tags + P1; morning Bluesky drop ~10 AM–2 PM MT (Ep2 and/or Ep3 packs); mature Bluesky hour 18 (still immature at 8:45). Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~8:30 PM MT (tick 39).** Pushed #8: built `tools/video/youtube_autocomplete.py`, wired it into the series publish checklist + script template, and applied collision-safe tags/hashtags into the Ep3 Candidate C pack, Short meta, and Bluesky drop (tick 38's fix had been note-only). Recheck still Warhammer/painting for ultramarine*. No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which file(s) went up, status lines, first stats rows; confirm Ep3 script used the collision-safe tags; morning Bluesky drop ~10 AM–2 PM MT; mature Bluesky hour 18 (still immature at 8:30). Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~8:20 PM MT (tick 38).** Pushed #8: ran YouTube autocomplete on Ep2/3/4 products. "Ultramarine" collides with Warhammer/iPhone and has no AI search demand yet, so Ep3 tags now use the full name + "AI model" and never "Ultramarines"; Ep4 gets conditional setup/local-LLM tags. Added an autocomplete-first rule. No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which file(s) went up, status lines, first stats rows; confirm Ep3 used the collision-safe tags; morning Bluesky drop ~10 AM–2 PM MT; mature Bluesky hour 18; optionally wire the autocomplete check into the production routine's script step. Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~8:14 PM MT (tick 37).** Pushed #9: matured Bluesky hour 17 (hour 18 still immature). `#AI` hour 17 is weak (18.4% engaged vs 43% at 10–15); AI News holds better but lower mean. Morning ~10 AM–2 PM MT drop rule unchanged. Also added missing `GA:` line to Ep2's queue file for tonight's ranking. No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which file(s) went up, status lines, and first stats rows; confirm Ep3 queue has `GA:` + `<slug>` name + outro matching its vote; morning Bluesky drop ~10 AM–2 PM MT (Ep2 and/or Ep3); mature Bluesky hour 18; growth routine uses the Ep2/Ep3 packs (not this routine). Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~7:55 PM MT (tick 36).** Pushed #3 (speed-to-publish) for Ep3: Ultramarine YouTube SERP still empty; X demand already large (CEO ~879K impressions). Locked that into the Ep3 title pack, filled Candidate C Short meta, and drafted `content/drafts/ep3-post-publish-growth-pack.md` (X/Bluesky + 2 reply targets). No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which file(s) went up, status lines, and first stats rows; confirm Ep3 queue has `GA:` + `<slug>` name + outro matching its vote; morning Bluesky drop ~10 AM–2 PM MT (Ep2 and/or Ep3); mature Bluesky hours 17–18; growth routine uses the Ep2/Ep3 packs (not this routine). Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~7:45 PM MT (tick 35).** Pushed #4: filled Ep4's P5 pack with **Hermes Agent v0.22** (evening scan + GitHub releases). Gate 1 fit; title/thumb/hook/caveats/vote ready; Ling parked for another pattern. No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which file(s) went up, status lines, and first stats rows; confirm Ep3 queue has `GA:` + `<slug>` name + outro matching its vote; morning Bluesky drop ~10 AM–2 PM MT; mature Bluesky hours 17–18 (morning pull); if Ep4 topic changes off Hermes, swap pattern and note in GROWTH_LOG. Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~7:40 PM MT (tick 34).** Read the 7:23 PM scan before tonight's 9:28 PM render. Its top item (Ultramarine 1 Flash, GA Oct 14) had no Ep3 assets, so I added Candidate C (P1 title, P6 thumbnail, hook, caveats, tags, vote block) and ranked it above Chainguard Harness. Fixed the pack's old queue filename. No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which file(s) went up, the status lines, and the first stats rows; check that the Ep3 queue file has a `GA:` line, the `<slug>` filename, and an outro that matches its vote block; morning Bluesky drop ~10 AM–2 PM MT; mature Bluesky hours 17–18; fill Ep4 P5 (Hermes Agent v0.22 or Ling-3.1-flash from the evening scan are possible fits). Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~7:25 PM MT (tick 33).** Generalized the one-night slot rule into standing queue rules (`content/published/queue/00-README-slot-rules.md`): naming, status lines, freshest-GA-first, carry-over, STALE after 3 nights, call order. Noted the queue folder had no rule beyond Oct 15. No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which file(s) went up, the status lines, and the first stats rows; check that the 9:28 PM Ep3 queue file has a `GA:` line and its own filename; morning Bluesky drop ~10 AM–2 PM MT; mature Bluesky hours 17–18; fill Ep4 P5 once a topic exists. Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~7:15 PM MT (tick 32).** Opened #13. A 1-unit YouTube read at ~7:14 PM MT got `quotaExceeded`, and no Composio upload/update tool supports `publishAt`. So everything YouTube has to happen in the post-reset window, uploads go straight to public, and the publish run now pulls the 24h/72h stats itself. Added a call order (main, thumb, stats, SEO/playlist, Short last) to the Oct 15 queue. No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, read which steps succeeded and the first stats rows; morning Bluesky drop ~10 AM–2 PM MT; mature Bluesky hours 17–18; fill Ep4 P5 once a topic exists; check that the 9:28 PM Ep3 queue file carries the same call order. Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~7:05 PM MT (tick 31).** Pushed #12 (site listing) + a small #9 note: found Ep2 missing from the landing-page checklist; drafted `content/drafts/ep2-site-listing.md`, saved `public/episodes/rr-002.jpg`, wired steps into the Oct 15 publish queue and Ep2 growth pack. Also matured Bluesky hour 16 (weaker than 10–15 MT; keeps morning drop). Hours 17–18 still need a morning pull. No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, log which episode went up plus whether channel SEO + Short S1c + **site listing** applied; morning growth posts Bluesky text-first ~10 AM–2 PM MT (and can mature 17–18 MT hours); 24h YouTube views/comments; fill Ep4 P5 once a topic exists. Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~6:55 PM MT (tick 30).** Pushed #7 (audience vote): wired numbered reply 1/2/3 into the review script template and series format; drafted Ep3 pinned-comment copy for both title-pack candidates (`content/drafts/ep3-vote-comment-draft.md`). No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, log which episode went up plus whether channel SEO + Short S1c applied; morning growth posts Bluesky text-first ~10 AM–2 PM MT and the Ep2/Ep3 vote comment after upload; 24h YouTube views/comments; fill Ep4 P5 once a topic exists. Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~6:40 PM MT (tick 29).** Pushed #9 (Bluesky timing): `#AI` feeds churn ~130 posts/hour, so a 1:28 AM drop would be buried before US morning. Set Bluesky Ep2 drop for ~10 AM–2 PM MT next day (text-first still). Critical AI & Tech is allowlist-only — not a free discovery surface. No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, log which episode went up plus whether channel SEO + Short S1c applied; morning growth should post Bluesky then; 24h YouTube views/comments; optional morning Bluesky pull to mature 16–18 MT hours from this sample; fill Ep4 P5 once a topic exists. Pending user decisions unchanged (own Google OAuth, Ben's Bites, X liveness).
- **2026-10-14 ~6:35 PM MT (tick 28).** Pushed #9 (Bluesky): link-card posts got engagement less often than text posts in both AI feeds (AI News 40% vs 70%, #AI 35% vs 42%, ~1,950 posts sampled). Switched Ep2's drop 1 to a text post that leads with the caveat and puts the link in a reply on our own post. Timing data is too narrow to rank hours. "LLM" feed is dead (502). No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, log which episode went up plus whether channel SEO + Short S1c applied; then 24h views/comments and Bluesky drop engagement with format; fill Ep4 P5 once a topic exists; optionally run an overnight Bluesky sample (two pulls about 12h apart) to cover the hours this one missed.
- **2026-10-14 ~6:25 PM MT (tick 27).** Pushed #9 (Bluesky): mapped which public AI feeds an episode drop can land in. `#AI` feeds exist but are flooded (86% of sampled posts got 0 likes), the art feeds filter AI out, and the AI-tagged discussion leans skeptical. Added a lead-with-caveat note and a 3-drop stop rule to the Ep2 growth pack. No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, log which episode went up plus whether channel SEO + Short S1c applied; then 24h views/comments (YouTube) and Post B engagement (Bluesky); retry the "LLM" feed sample; fill Ep4 P5 once a topic exists. Pending user decisions are unchanged.
- **2026-10-14 ~6:10 PM MT (tick 26).** Wired approved #11 into the Oct 15 publish queue and unlocked Bluesky in the Ep2 growth pack (account already created). No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, log which episode went up plus whether channel SEO + Short S1c applied; then 24h views/comments; fill Ep4 P5 once a topic exists; refresh the X reply shortlist the morning after publish. Pending user decisions remain: own Google OAuth, Ben's Bites, X liveness check.
- **2026-10-14 ~6:05 PM MT (tick 25).** Found the YouTube channel About is blank (Composio connection info, `snippet.description: ""`). Drafted channel description, keywords and an "AI Release Reviews" playlist plan (`content/drafts/channel-seo-setup.md`, experiment #11). Batched into a user ping along with #10 (X liveness check). No posts, uploads, channel edits or signups.
  - Next recommended tick: after the 1:28 AM run, log which episode went up plus 24h views/comments (and Short S1c if uploaded); if the user okays #11, add the channel-setup steps to the publish run's checklist; fill Ep4 P5 once a topic exists; refresh the reply shortlist the morning after publish.
- **2026-10-14 ~5:46 PM MT (tick 24).** Drafted Ep2 post-publish growth pack for the growth routine (`content/drafts/ep2-post-publish-growth-pack.md`): checklist, episode-drop X post, and 1–2 reply targets from a live X search (prefer @bidyut_io bake-off; backup @pankajkumar_dev). Caps still 1–2 replies under graduated access. No posts, uploads or signups.
  - Next recommended tick: after the 1:28 AM run, log which episode went up plus 24h views/comments (and Short S1c if uploaded); include #10 + dedicated-quota / Bluesky / Ben's Bites in the next batched user ping; fill Ep4 P5 once a topic exists; refresh the reply shortlist the morning after publish.
- **2026-10-14 ~5:35 PM MT (tick 23).** Started #10 (getting X out of graduated access). Found X's new liveness check (biometrics or a selfie video, only the operator can do it; passing restores full access) and the automated-account label (honest, but it publicly names a managing account, so it would break incognito unless that account is pseudonymous). Recommendation batched for the user's next ping. No posts, uploads or signups.
  - Next recommended tick: after the 1:28 AM run, log which episode went up plus 24h views/comments (and Short S1c if uploaded); include #10 in the next batched user ping alongside the dedicated-quota / Bluesky / Ben's Bites decisions; fill Ep4 P5 once a topic exists.
- **2026-10-14 ~5:25 PM MT (tick 22).** Pushed #5: wired Short publish-meta auto-fill (`tools/video/short_publish_meta.py` → `<slug>-short-meta.json` from `post_render.sh`). Generated Ep2's ready JSON and pointed `queue/2026-10-15.md` at it. No posts, uploads or signups.
  - Next recommended tick: after the 1:28 AM run, log which episode went up plus 24h views/comments (and Short S1c if uploaded); fill Ep4 P5 once a topic exists; or draft growth-routine X posts/replies from the experiment backlog (still no posting from this routine).
- **2026-10-14 ~5:10 PM MT (tick 21).** Started #4: drafted Ep4's P5 openly-AI title pack (`content/drafts/ep4-p5-openly-ai-title-pack.md`) — when-to-use gates so we don't force the gag, primary-hook titles (vs secondary brand tag), thumb words, cold-open hooks, and a views-vs-Ep1/Ep3 measure plan. Product left blank until the scan locks one. No posts, uploads or signups.
  - Next recommended tick: after the 1:28 AM run, log which episode went up plus 24h views/comments (and Short S1c if uploaded); fill Ep4 P5 once a topic exists; or wire Short meta auto-fill into the publish routine from `shorts-publish-meta.md`.
- **2026-10-14 ~5:05 PM MT (tick 20).** Pushed #5: drafted Short titles/descriptions/tags for the publish run (`content/drafts/shorts-publish-meta.md`) — Ep2 CTA Short ready to ship after the main episode, plus Ep3 templates for both title-pack candidates. No posts, uploads or signups.
  - Next recommended tick: after the 1:28 AM run, log which episode went up plus 24h views/comments (and Short S1c if uploaded); start #4 (openly-AI angle) by drafting Ep4 P5 hooks once a topic exists; or wire Short meta auto-fill into the publish routine from this draft.
- **2026-10-14 ~4:50 PM MT (tick 19).** Pushed #5: added a like/subscribe end card for Shorts (`short_windows.py --cta`, on by default in `post_render.sh`). Ep2 CTA Short rendered (52.6 s, click animation checked in frames) and marked as the preferred Ep2 Short. No posts, uploads or signups.
  - Next recommended tick: after the 1:28 AM run, log which episode went up plus 24h views/comments; start #4 (openly-AI angle) by drafting Ep4 P5 hooks once a topic exists; or draft Short titles/descriptions (product first, links the full episode) for the publish run.
- **2026-10-14 ~4:40 PM MT (tick 18).** Drafted Ep3's P1 title pack for tonight's production run: two sourced candidates (Chainguard Harness preferred, ScaleDown Classify as backup) with titles, P6 thumbnails rendered via `thumbnail.py`, 5-second hooks, description lines, caveats and vote prompts. No posts, uploads or signups.
  - Next recommended tick: after the 1:28 AM run, log which episode went up and its 24h views/comments; optional ~5 s CTA end card in `short_windows.py`; or start #4 (openly-AI angle) by drafting Ep4 P5 hooks once a topic exists.
- **2026-10-14 ~4:35 PM MT (tick 17).** Found that tonight's 9:28 PM render and the already-queued Ep2 compete for the one reliable 1:28 AM upload slot. Wrote a slot-priority rule (fresh release first, Ep2 second or next night, no queue overwrite) and flagged it in the Ep2 queue file. Sent to the user as a decision with a default. No posts, uploads or signups.
  - Next recommended tick: after the 1:28 AM run, log which episode went up and Ep2's 24h views (P2 + #8) and comments (#7); draft Ep3 P1 titles + thumbnail words if the 7:23 PM scan locks a product; optional ~5 s CTA end card in `short_windows.py`.
- **2026-10-14 ~4:20 PM MT (tick 16).** Wired #5/#6 into the render: `post_render.sh` (thumbnail from `meta.thumbnail` + auto Short) now runs at the end of `make_review.sh`; template gained `title_pattern` + `thumbnail`; Ep2 script got its block. Tested on Ep2 (thumb identical to v2; Short 1080x1920, 57.5 s). No posts, uploads or signups.
  - Next recommended tick: after Ep2 is live (~1:28 AM MT Oct 15), log its 24h views (P2 + #8) and comments (#7); draft Ep3 P1 titles + thumbnail words once the 7:23 PM scan locks a product; optionally add the ~5 s CTA end card to `short_windows.py` when the budget allows.
- **2026-10-14 ~4:15 PM MT (tick 15).** Prepped #6: Ep2's queued thumbnail hid Lumin's face behind a seamed text panel and repeated the title. Built `tools/video/thumbnail.py` (P6 grammar) and swapped a "HYPE CHECK" v2 into the Ep2 queue (title/P2 untouched, v1 kept as the B variant). No posts, uploads or signups.
  - Next recommended tick: wire `thumbnail.py` into `make_review.sh` / the production routine's outputs; after Ep2 is live (~1:28 AM MT Oct 15), log its 24h views (P2 + #8) and comments (#7); draft Ep3 P1 titles + thumbnail words once the 7:23 PM scan locks a product.
- **2026-10-14 ~4:05 PM MT (tick 14).** Pushed #5 layout check + closed the Reddit browser lead on #9. Reddit is unreachable from the box (network-security block in Chrome, same as curl/WebFetch); parked with candidates listed. Cut vertical samples of Ep2 intro / like-subscribe CTA / outro brand: intro doubles Lumin (skip); CTA and outro brand cards are readable end-card options. Frames in `content/drafts/shorts-layout-check/`. No posts, uploads or signups.
  - Next recommended tick: optionally extend `short_windows.py` / splice recipe with a ~5 s CTA end card when budget allows; after Ep2 is live (~1:28 AM MT Oct 15), log its 24h views (P2 + #8) and comments (#7); or draft Ep3 P1 titles once the evening news scan locks a product. Dedicated-quota / Bluesky / Ben's Bites decisions still pending with the user (already batched).
- **2026-10-14 ~3:50 PM MT (tick 13).** Pushed #5: added `tools/video/short_windows.py` (picks Short windows from timing.json on line boundaries: best fact + verdict, under 58 s), fixed clipped captions in `shorts_cut.sh` (crop widened 1200 to 1500 px), and rendered the Ep2 Short (57.5 s) to `content/drafts/2026-10-14-gemini-4-argon-short.mp4`. No posts, uploads or signups.
  - Next recommended tick: Reddit rules via a read-only browser pass (computerUse); after Ep2 is live (~1:28 AM MT Oct 15), log its 24h views (P2 + #8) and comments (#7); check the intro/CTA frames in the vertical layout if a later recipe wants them.
- **2026-10-14 ~3:15 PM MT (tick 12).** Pushed #5: built `tools/video/shorts_splice.sh` (multi-window vertical Short) so a Short can open on the best fact and end on the verdict. Tested on Ep2 (1080x1920, audio, readable frames). Ep2 Short spec locked: windows 13–55 s + 78–94 s (58 s). No posts, uploads or signups.
  - Next recommended tick: Reddit rules via a read-only browser pass (computerUse); after Ep2 is live (~1:28 AM MT Oct 15), log its 24h views (P2 + #8) and comments (#7); or wire `shorts_splice.sh` into the production routine's outputs (render the Short file nightly so publish only uploads it).
- **2026-10-14 ~3:06 PM MT (tick 11).** Checked tick 10's `YOUTUBE_WEB_*` lead. Those tools don't exist. Scraping youtube.com works but breaks YouTube's ToS (quoted), so it's ruled out, and competitor stats will come from Data API search+batch after a successful upload. A one-off snapshot gave first-day velocity data: videos under 5h old grew 79–156% in ~1h45m, while 9h+ videos grew 2–12%. That strengthens #3 and the dedicated-quota ask. No posts, uploads or signups.
  - Next recommended tick: Reddit rules via a read-only browser pass (computerUse); or two-window splicing for Shorts; after Ep2 is live (~1:28 AM MT Oct 15), log its 24h views (P2 + #8) and comments (#7).
- **2026-10-14 ~3:05 PM MT (tick 10).** Pushed #7 (audience vote loop): drafted the Ep2 numbered-vote comment and its counting rules; confirmed Composio has comment post/list tools but no pin. Noted `YOUTUBE_WEB_*` tools as a possible quota-free competitor-stats source (untested). Sent the batched decisions to the user. No posts, uploads or signups.
  - Next recommended tick: test one `YOUTUBE_WEB_*` call to see if it avoids the shared quota (read-only); or the Reddit rules browser pass; after Ep2 is live (~1:28 AM MT Oct 15), log its 24h views (P2 + #8) and comments (#7).
- **2026-10-14 ~2:40 PM MT (tick 9).** Pushed #9: Discord ruled out for automated user accounts (Community Guidelines §14 + self-bots article); mapped newsletter options — Ben's Bites News is the only free submit-and-maybe-digest path found, draft in `content/drafts/bens-bites-submit-draft.md`; TLDR AI is paid-only; The Beat is tip-not-promo. No signups, posts or uploads. Pending user decisions (still batched, not re-pinged this tick): (1) dedicated Google OAuth for YouTube quota, (2) Bluesky account, (3) Ben's Bites News account for occasional episode/launch submits.
  - Next recommended tick: Reddit rules via a read-only browser pass (computerUse); or after Ep2 is live (~1:28 AM MT Oct 15), log its 24h views (P2 + #8).
- **2026-10-14 ~2:33 PM MT (tick 8).** Pushed #9: drafted Bluesky account assets so the pending signup decision is ready to act on — handle, bio, bot-label rules, and first-post templates in `content/drafts/bluesky-account-draft.md`. No signup, posts or uploads. Batched user recommendations: (1) dedicated Google OAuth for YouTube quota, (2) Bluesky account create.
  - Next recommended tick: Reddit rules via a read-only browser pass (computerUse), or Discord/newsletter submission options; after Ep2 is live (~1:28 AM MT Oct 15), log its 24h views (P2 + #8).
- **2026-10-14 ~2:25 PM MT (tick 7).** Pushed #9: Reddit rules still unreadable (rules.json now returns a block page to curl too), so checked Bluesky instead. Its guidelines allow labeled character accounts and scheduled bot posting, with opt-in-only interactions. Recommendation drafted (create a bot-labeled Bluesky account for episode drops), held to batch with the next user ping. No posts, uploads or signups.
  - Next recommended tick: Reddit rules via a read-only browser pass (computerUse), or check Discord/newsletter submission options; draft the Bluesky bio and first-post template so it's ready if the user says yes. After Ep2 is live (~1:28 AM MT Oct 15), log its 24h views (P2 + #8).
- **2026-10-14 ~2:15 PM MT (tick 6).** Started backlog #9 (community map, nothing on this existed yet). Ruled out Hacker News: its guidelines ban generated and AI-edited text in posts and comments. Reddit rules couldn't be read from the box (login wall and blocked JSON), so the subreddit list is candidates only. No posts or uploads.
  - Next recommended tick: read the candidate subreddits' rules with a read-only browser pass and fill in the table; or check other non-X options (YouTube community/collab with small AI-character channels, Discord servers, newsletters that take reader submissions). After Ep2 is live (~1:28 AM MT Oct 15), log its 24h views (P2 + #8).
- **2026-10-14 ~2:05 PM MT (tick 5).** Pushed backlog #5: confirmed Shorts classification is by file shape (vertical, 3 min or less, no API flag); built and tested `tools/video/shorts_cut.sh` (stacked 1080x1920 re-crop of a finished episode); wrote the cut recipe and the rule to upload the Short only after the main episode succeeds on shared quota. No posts or uploads.
  - Next recommended tick: once Ep2 is live (~1:28 AM MT Oct 15), log its 24h views (P2 + #8). Before then, draft Ep3 P1 titles if the 7:23 PM scan locked a product, or add two-window splicing to the Shorts tool, or check the intro/CTA frames in the vertical layout.
- **2026-10-14 ~1:50 PM MT (tick 4).** Pushed backlog #3: mapped Ep2 GA-to-publish (~1.5–2 days vs competitors' <1 day), found the shared upload quota is the hard floor, verified Composio supports a dedicated Google OAuth app (100 uploads/day per Google docs, unverified projects not forced private). Recommended it to the user; noted `containsSyntheticMedia: true` for uploads. No posts or uploads.
  - Next recommended tick: if the user approves the own-OAuth setup, write the step-by-step for them; otherwise draft Ep3 P1 title options once the 7:23 PM scan locks a product, or start #5 (Shorts quota check). After Ep2 is live, log its 24h views.
- **2026-10-14 ~1:40 PM MT (tick 3).** Pushed backlog #8: wrote the search-first metadata rule and applied it to Ep2's queued metadata (product-first description line, chapters from timing.json, 3 search tags, 3 hashtags). Title/P2 untouched. No posts or uploads.
  - Next recommended tick: backlog #3 speed-to-publish checklist (GA-to-publish hours, what blocks a same-day review), or wire the chapter generation into the render script via the video routine. After Ep2 is live (~1:28 AM MT Oct 15), log its 24h views under P2 + #8.
- **2026-10-14 ~1:28 PM MT (tick 2).** Pushed backlog #2 one step: confirmed Composio YouTube has **Data API stats only** (no impressions/CTR/trafficSource). Wrote the views-at-24h/72h measurement protocol and assigned pattern IDs for Ep1–Ep6 (Ep2 = P2 already titled). Mid-day live stats pull hit shared-project `quotaExceeded` — use post-reset window for checks. No posts or uploads from this tick.
  - Next recommended tick: after Ep2 is live, log its 24h views under P2; draft Ep3's P1 title options once the news scan locks a product (do not fabricate a topic). Or start backlog #3 (speed-to-publish checklist) if no new episode is ready to title.
- **2026-10-14 ~1:25 PM MT (tick 1).** Created this doc. Ran backlog #1: competitive title/thumbnail study. Patterns P1–P6 written. Next was #2 (done in tick 2).


## Decisions log (parent)
- 2026-10-14: Bluesky APPROVED and CREATED: @orbbuilds.bsky.social (bot label on, creds /home/box/secrets/bluesky.txt, email unverified). Do not re-ask.
- 2026-10-14: Channel About/keywords/reviews playlist APPROVED by parent; publish run applies after main upload succeeds (read branding first).
- Pending with user: own Google OAuth app, Ben's Bites account, X liveness check, cross-promo confirmation.
