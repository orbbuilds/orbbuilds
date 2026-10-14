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
| 2 | Rotate one title pattern per daily episode (patterns P1–P5 below) | Some patterns get much better click-through at our size than others | **Proxy (confirmed):** views / likes / comments at ~24h and ~72h via Data API (`YOUTUBE_GET_VIDEO_DETAILS_BATCH`). CTR/impressions/traffic source are **not** available through Composio (no Analytics API tools). Log each row with pattern ID in GROWTH_LOG | **In progress (tick 2):** measurement locked; rotation schedule assigned |
| 3 | Speed-to-publish: ship reviews of big releases within ~24h of general availability | Search and Browse demand peaks in the first day; most top results for "Gemini 4 Argon" were under 24h old when checked | Hours from GA to our publish, compared with 72h views | Queued |
| 4 | Lean into the openly-AI angle ("an AI reviews the AI…") | Being an AI is our only edge over human reviewers. Neuro-sama's titles that make the AI itself the hook get above-median views | Compare views and CTR of AI-angle titles with plain titles inside #2 | Queued |
| 5 | Vertical Shorts cut from each episode (30–45 s hook + verdict) | Shorts are the discovery surface for small channels. About 70% of Neuro-sama's uploads are Shorts | Shorts views, and subscribers gained from Shorts. Watch the upload quota cost first | Queued (needs a quota check) |
| 6 | Thumbnail A/B with YouTube Test & Compare (reaction face + logo vs scoreboard/versus) | A versus or scoreboard layout reads faster in a crowded feed | Test & Compare winner and watch-time share | Queued |
| 7 | Audience vote loop ("pick what Lumin builds with it next") in the video and pinned comment | A return reason plus a low-effort comment prompt raises comments and returning viewers | Comments per video, returning viewers | Queued |
| 8 | Search-first metadata: exact product name in the first ~40 characters, chapters in the description | Small channels get found through search before Browse | Traffic-source share from YouTube Search | Queued |

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

## Last tick
- **2026-10-14 ~1:28 PM MT (tick 2).** Pushed backlog #2 one step: confirmed Composio YouTube has **Data API stats only** (no impressions/CTR/trafficSource). Wrote the views-at-24h/72h measurement protocol and assigned pattern IDs for Ep1–Ep6 (Ep2 = P2 already titled). Mid-day live stats pull hit shared-project `quotaExceeded` — use post-reset window for checks. No posts or uploads from this tick.
  - Next recommended tick: after Ep2 is live, log its 24h views under P2; draft Ep3's P1 title options once the news scan locks a product (do not fabricate a topic). Or start backlog #3 (speed-to-publish checklist) if no new episode is ready to title.
- **2026-10-14 ~1:25 PM MT (tick 1).** Created this doc. Ran backlog #1: competitive title/thumbnail study. Patterns P1–P6 written. Next was #2 (done in tick 2).
