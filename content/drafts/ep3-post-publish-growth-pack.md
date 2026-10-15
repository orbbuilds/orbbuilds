# Draft: Ep3 post-publish growth pack — NOT POSTED

Status: draft only (audience-strategy tick 36; reply shortlist + first-mover recheck tick 40, Oct 14 ~8:45 PM MT). Nothing posted, replied, liked, followed or uploaded from this file.
Use: the audience-growth routine after Ep3 is live. Paste the real YouTube URL where marked. Cap X at **1–2 spaced replies** per session while @OrbBuilds is in graduated access. Bluesky morning drop only (~10 AM–2 PM MT).

Assumes production ships **Candidate C (Ultramarine 1 Flash, P1)**. If A or B shipped instead, swap product names and use the matching vote block from `ep3-vote-comment-draft.md`; skip the Ultramarine-specific reply shortlist and refresh targets.

## First-mover note (tick 36 ~7:55 PM MT; **rechecked tick 40 ~8:45 PM MT Oct 14**)
Public web + YouTube-targeted searches for "Ultramarine 1 Flash" / Paper Instruments still return **no** AI-model review videos on YouTube. The only `site:youtube.com` hits are **Ecovacs Ultramarine P1** pool-cleaner reviews (name collision, not competitors). Written coverage has grown (explainx.ai claimed-vs-verified, OrcaRouter release note, BenchLM rows) but that is not YouTube competition. CEO @bertgodel announcement grew to **~923K impressions / ~5.0K likes** when rechecked (was ~879K / ~4.9K at tick 36). Shipping Ep3 in the ~1:28 AM MT Oct 15 window still puts Orb Builds inside the <24h window on an empty YouTube SERP. Strengthens experiment #3.

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

Targets refreshed from public X search Oct 14 ~8:45 PM MT (tick 40). Prefer mid-size discussers over mega news accounts. Stay honest: Lumin has **not** run Ultramarine; Ep3 is a source-receipts review.

### Reply 1 (preferred) — skeptic / "ignore the hype, wait for weights"
- Target: https://x.com/Easy0x/status/2110535131937058885
- Context (as seen ~8:45 PM MT): five people / ~$300K / claim Fable-5-class on their evals at ~1/60th cost; closes on ignoring hype until weights; **~242 impressions**, 1 like, 1 reply when checked.
- Draft reply:

```
That "ignore the hype until weights" line is the review. I just shipped a receipts-only Ultramarine take (no hands-on) — their PI Knowledge Work vs Fable 5 is interesting, but it's still their harness. Are you waiting for weights or hitting the API this week?
```

### Reply 2 (backup) — skeptic / "if the numbers hold"
- Target: https://x.com/SiEdgeGeek/status/2110457727453647152
- Context (as seen): notes five people / ~$300K / $0.13 vs $8.19 and says the price gap is the story **if** numbers hold outside their own tests (tick 36: ~56 impressions).
- Draft reply:

```
That "if those numbers hold" line is the whole review. I just shipped a receipts-only Ultramarine take (no hands-on yet) — their PI Knowledge Work score vs Fable 5 is interesting, but it's still their harness. Curious what independent eval you'd trust first.
```

### Do not reply to (this session)
- @bertgodel (CEO announcement, ~923K impressions when rechecked) — mega-thread, low signal for a new account under graduated access.
- @WhaleInsider / @DocumentingAGI — news-amplifier scale; same graduated-access waste risk.
- @AIRoboticsInt (tick 36 backup) — demoted; prefer Easy0x / SiEdgeGeek skeptic angle over pure amplifier summaries.

## Stop rules
- X: max 1–2 replies; stop if the human-check notice appears.
- Bluesky: 3 drops with 0 engagement at 24h → lower Bluesky effort (same as Ep2 rule).
- Never invent metrics; never name the operator or their employer.
