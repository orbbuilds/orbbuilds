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
| 3 | Speed-to-publish: ship reviews of big releases within ~24h of general availability | Search and Browse demand peaks in the first day; most top results for "Gemini 4 Argon" were under 24h old when checked | Hours from GA to our publish, compared with 72h views | **In progress (tick 11):** bottleneck mapped (tick 4); first-day velocity data (tick 11) shows <5h-old videos growing 79–156% in ~2h vs 2–12% for 9h+; dedicated-quota decision still pending with user |
| 4 | Lean into the openly-AI angle ("an AI reviews the AI…") | Being an AI is our only edge over human reviewers. Neuro-sama's titles that make the AI itself the hook get above-median views | Compare views and CTR of AI-angle titles with plain titles inside #2 | Queued |
| 5 | Vertical Shorts cut from each episode (30–45 s hook + verdict) | Shorts are the discovery surface for small channels. About 70% of Neuro-sama's uploads are Shorts | Shorts views, and subscribers gained from Shorts. Watch the upload quota cost first | **In progress (tick 5):** vertical cut tool + splice tool + auto window picker built (tick 13); Ep2 Short rendered at `content/drafts/2026-10-14-gemini-4-argon-short.mp4` (57.5 s); first upload waits on quota headroom after the main episode |
| 6 | Thumbnail A/B with YouTube Test & Compare (reaction face + logo vs scoreboard/versus) | A versus or scoreboard layout reads faster in a crowded feed | Test & Compare winner and watch-time share | Queued |
| 7 | Audience vote loop ("pick what Lumin builds with it next") in the video and pinned comment | A return reason plus a low-effort comment prompt raises comments and returning viewers | Comments per video at 24h/72h vs Ep1's 0 (returning viewers not available via Composio) | **In progress (tick 10):** Ep2 vote comment drafted (`content/drafts/ep2-vote-comment-draft.md`); needs a poster (user or a routine that covers commenting) |
| 8 | Search-first metadata: exact product name in the first ~40 characters, chapters in the description | Small channels get found through search before Browse | Traffic-source share isn't available via Composio; proxy = 72h views vs Ep1 baseline, plus a manual Studio spot-check if ever available | **In progress (tick 3):** applied to Ep2 meta; rule written for the video routine |
| 9 | Community map: places beyond X where an openly-AI show is allowed and wanted | X is throttled (graduated access), so a second outside channel matters more than more X replies. Some communities ban AI-written posts outright; picking ones that allow them avoids bans and wasted effort | A table of communities with size, self-promo rule and AI-content rule, each quoted from the community's own rules page; later, referral views per channel (proxy: views in 24h after a share) | **In progress (tick 9):** HN out; Discord user-account automation out; Bluesky drafts ready; Ben's Bites News submit draft ready (`content/drafts/bens-bites-submit-draft.md`); Reddit still needs a browser pass |

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

**Measure:** Shorts views at 24h/72h and channel subscriber delta (`YOUTUBE_GET_CHANNEL_STATISTICS`) after reset. Log as pattern `S1` rows in GROWTH_LOG.

## Community map (experiment #9, tick 6, Oct 14 ~2:15 PM MT)
Goal: find one or two places beyond X where Lumin can share episodes honestly, as an openly-AI host, without breaking the community's rules.

**Hacker News: ruled out for anything Lumin writes.** The HN guidelines (news.ycombinator.com/newsguidelines.html, fetched Oct 14) say "Please don't put generated text in HN posts" and "Don't post generated text or AI-edited text." Every Orb Builds post or comment would be AI-generated, so HN is off-limits for this project, including a Show HN of the pipeline. The Show HN rules (news.ycombinator.com/showhn.html, fetched Oct 14) also require something people can try, made by someone who is "around to discuss" it. Don't revisit this unless the operator decides to post there themselves, which would conflict with keeping them incognito.

**Reddit: rules not read yet.** reddit.com JSON and old.reddit.com both refuse the box (old Reddit now requires login; the JSON endpoints return no data to curl; WebFetch timed out). Reading each subreddit's sidebar rules needs the box browser (a computerUse subagent, read-only, no login needed on new Reddit). Candidates to check, no sizes or rules recorded yet because none were read: r/singularity, r/artificial, r/ArtificialInteligence, r/OpenAI, r/GoogleGeminiAI, r/LocalLLaMA, r/aivideo, r/NewTubers (feedback threads for small channels), r/SideProject. Record for each: subscriber count, self-promotion rule, AI-generated-content rule, and whether a weekly self-promo thread exists. Posting from Reddit would also need an account, which we don't have; that is a user decision.

**Bluesky: allowed, and a good fit for broadcast-only posting (tick 7, Oct 14 ~2:25 PM MT).** Sources fetched Oct 14: the [Bluesky Community Guidelines](https://bsky.social/about/support/community-guidelines) (updated Sep 19, 2025) have no rule against AI-generated content, and explicitly allow "clearly labeled fictional character accounts" as long as they don't mislead. The [Bluesky bot docs](https://docs.bsky.app/docs/starter-templates/bots) say automated accounts that post on a regular schedule "are welcome", should self-label as `bot` (now a visible robot badge, Settings, Account, Automation label, per Bluesky's v1.119 announcement), and should only like, repost or reply when a user has tagged the bot first. The [Developer Guidelines](https://docs.bsky.app/docs/support/developer-guidelines) define spam as automated or bulk interactions that notify users (follows, likes, replies, DMs). Write limits (1,666 records/hour, 11,666/day per the [rate-limit docs](https://docs.bsky.app/docs/advanced-guides/rate-limits)) are far above anything we'd do.
- Fit: Lumin is openly AI and a named character, so the bot label is honest and on-brand, not a penalty. Posting is a plain API call with an app password, no browser sign-in fight and no new-account throttle mentioned in these docs (not verified in practice).
- Rules for us if adopted: label the account `bot`; post only our own episode drops and build updates (1–2 per day); reply only when someone tags @Lumin or replies to us; never auto-follow or auto-like. Bio says it's an AI host; no operator name or employer.
- Not yet known: how much AI-news audience is on Bluesky, and how users treat bot-labeled accounts. Measure with post likes/reposts and the episode's views in the 24h after a Bluesky post.
- **Needs a user decision:** creating the account (a signup under the Orb Builds identity, email from our own inbox). Pending, batched for the next recommendation to the user.
- **Drafts ready (tick 8):** `content/drafts/bluesky-account-draft.md` — handle `orbbuilds.bsky.social` (fallback `lumin.bsky.social`), display name, bot label, 185-char bio matching channel copy, welcome + episode-drop + build-update post templates, posting rules, and how to measure. Nothing created or posted.

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

## Last tick
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
