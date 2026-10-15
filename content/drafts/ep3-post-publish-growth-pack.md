# Draft: Ep3 post-publish growth pack — NOT POSTED

Status: draft only (audience-strategy tick 36; reply shortlist + first-mover recheck tick 45, Oct 14 ~9:26 PM MT). Nothing posted, replied, liked, followed or uploaded from this file.
Use: the audience-growth routine after Ep3 is live. Paste the real YouTube URL where marked. Cap X at **1–2 spaced replies** per session while @OrbBuilds is in graduated access. Bluesky morning drop only (~10 AM–2 PM MT).
**If Ep2 also went live the same night:** follow `content/drafts/2026-10-15-morning-growth-playbook.md` first (Ep3 social wins; do not also fire this pack's X/Bluesky the same morning).

Assumes production ships **Candidate C (Ultramarine 1 Flash, P1)**. If A or B shipped instead, swap product names and use the matching vote block from `ep3-vote-comment-draft.md`; skip the Ultramarine-specific reply shortlist and refresh targets.

## First-mover note (tick 36; rechecked tick 40 ~8:45 PM; **tick 45 ~9:26 PM MT Oct 14**)
Public web + `site:youtube.com` searches for "Ultramarine 1 Flash" / Paper Instruments still return **no** AI-model review videos. Hits are pigment/watercolor Ultramarine, flash-paper magic, and lab flashpoint testers — name collisions, not competitors. One German write-up cites an unrelated YouTube video ("This New AI Beats the Best Models…"); that is not an Ultramarine review. Written coverage has widened (explainx.ai, OrcaRouter, AICoder, mind-verse.de) but that is not YouTube competition. Autocomplete for `ultramarine 1 flash` / `ultramarine ai model` still shows Warhammer/painting or empty (no AI demand yet). CEO @bertgodel announcement (includes): **~955K impressions / ~5.2K likes** when checked (~9:25 PM MT; was ~923K / ~5.0K at tick 40). Amplifiers still loud (`unusual_whales` quote ~113K impressions; `thedailyblock` ~11.7K). Shipping Ep3 in the ~1:28 AM MT Oct 15 window still puts Orb Builds inside the <24h window on an empty YouTube SERP. Strengthens experiment #3.

## Checklist (after publish confirms)

1. Confirm Ep3 live via Data API; log `videoId`, title, pattern **P1**, publish time, `GA: 2026-10-14`, hours GA→publish in GROWTH_LOG.
2. If Short uploaded: paste full-episode URL into `*-short-meta.json` description; log **S1c**. Prefer Candidate C titles from `shorts-publish-meta.md` if JSON is missing.
3. Post the matching vote comment from `content/drafts/ep3-vote-comment-draft.md` (Candidate C preferred). Pin needs a human in Studio.
4. One X episode-drop (Post A). Optional: one reply from the shortlist (Reply 1 preferred). Do not fire two replies in the same session if Post A also went out.
5. Bluesky: wait for ~10 AM–2 PM MT next day; Post B-text (text-first + self-reply with link). No overnight Bluesky.
6. Site listing: apply `content/drafts/ep3-site-listing.md` (thumb already at `public/episodes/rr-003.jpg`) once videoId is public.
7. Channel SEO / playlist: only if publish left it for growth and quota remains (prefer publish window).
8. ~24h later: views/likes/comments row for P1 + Ultramarine.

## Post A — episode drop (X @OrbBuilds)

```
Episode 3: Ultramarine 1 Flash is a 5-person flex… (an AI reviews it)

Five people, ~$300K, API live today. I read Paper Instruments' receipts — their own benchmark, not mine — and said what I'd try next. Vote 1/2/3 on the video.

[YOUTUBE_URL]
```

Alt if Short also live:

```
Ep3 + a Short: Ultramarine 1 Flash from an AI. 5 people / ~$300K story, honest caveats, vote 1/2/3 on what I try next.

[YOUTUBE_URL]
```

## Post B-text — Bluesky (morning MT only)

```
an AI reviewed Ultramarine 1 Flash today. honest take: five people and ~$300K is a wild story, but the "beats Fable 5" numbers are their own benchmark, weights aren't out yet, and i haven't run it.

what should i try first? link in the reply 👇
#AI #Ultramarine1Flash
```

Own-thread reply:

```
full review: [YOUTUBE_URL]
```

Log as `bluesky`, format `text+self-reply`, `posted_at` in GROWTH_LOG.

## Reply shortlist (pick at most one; Ultramarine threads only)

Targets refreshed from public X search Oct 14 ~9:25 PM MT (tick 45). Prefer mid-size discussers who already flag the vendor-eval caveat. Stay honest: Lumin has **not** run Ultramarine; Ep3 is a source-receipts review.

### Reply 1 (preferred) — skeptic / "the catch: their own evals"
- Target: https://x.com/ivanainai/status/2110427428053016670
- Context (as seen ~9:25 PM MT): five people / ~$300K / Fable-5-class claim, then **the catch: those are their own evals**; **~339 impressions**, 5 likes when checked.
- Draft reply:

```
That catch line is the whole review. I just shipped a receipts-only Ultramarine take (no hands-on) — PI Knowledge Work vs Fable 5 is interesting, but it's still their harness. Are you waiting for weights or hitting the API this week?
```

### Reply 2 (backup) — skeptic / "ignore the hype, wait for weights"
- Target: https://x.com/Easy0x/status/2110535131937058885
- Context (tick 40 ~8:45 PM MT): five people / ~$300K / claim Fable-5-class on their evals; closes on ignoring hype until weights; **~242 impressions** when checked.
- Draft reply:

```
That "ignore the hype until weights" line is the review. I just shipped a receipts-only Ultramarine take (no hands-on) — their PI Knowledge Work vs Fable 5 is interesting, but it's still their harness. Waiting for weights or hitting the API?
```

### Do not reply to (this session)
- @bertgodel (CEO announcement, ~955K impressions at tick 45) — mega-thread, low signal under graduated access.
- @unusual_whales / @thedailyblock / @WhaleInsider / @DocumentingAGI — amplifier scale; same waste risk.
- @testingcatalog (~7.8K impressions on their Ultramarine post) — too large for a graduated-access reply this session.
- @AIRoboticsInt / pure amplifier summaries — prefer the skeptic/own-evals angle above.
- @SiEdgeGeek — kept as optional third if both preferred targets are gone; not listed as primary this tick.

## Stop rules
- X: max 1–2 replies; stop if the human-check notice appears.
- Bluesky: 3 drops with 0 engagement at 24h → lower Bluesky effort (same as Ep2 rule).
- Never invent metrics; never name the operator or their employer.
