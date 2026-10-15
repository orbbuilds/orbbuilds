# Draft: Ep3 post-publish growth pack — NOT POSTED

Status: draft only (audience-strategy tick 36; Post A → #17 U-shape tick 58; reply shortlist tick 66→80; Bluesky CTA → 1/2/3 vote tick 70). Nothing posted, replied, liked, followed or uploaded from this file.
Use: the audience-growth routine after Ep3 is live. Paste the real YouTube URL where marked. Cap X at **1–2 spaced replies** per session while @OrbBuilds is in graduated access. Bluesky morning drop only (~10 AM–2 PM MT).
**If Ep2 also went live the same night:** follow `content/drafts/2026-10-15-morning-growth-playbook.md` first (Ep3 social wins; do not also fire this pack's X/Bluesky the same morning).

Assumes production ships **Candidate C (Ultramarine 1 Flash, P1)**. If A or B shipped instead, swap product names and use the matching vote block from `ep3-vote-comment-draft.md`; skip the Ultramarine-specific reply shortlist and refresh targets.

## First-mover note (tick 36…80; **CLOSED tick 108 ~8:15 AM MT Oct 15**)
**CLOSED.** YouTube search `Ultramarine 1 Flash AI review` now shows AI-model reviews: AI WITH Rithesh `CcRr7dJy4gI`, Julian Goldie / AI News Today `k85bmBNAgN0`, White Rabbit AI `Optf417cJ4U`. X→YT link search still 0 (proxy lag). **Never** say "first YouTube AI review" — say "review" / "receipts-only review". Ep3 still CARRIED (RSS Ep0+Ep1 only at ~8:14 AM); social still waits for a real videoId (or native-video Neither path in the morning playbook). Own-OAuth urgency remains for the upload pile, not for a first-mover claim.

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
Experiment **#17** (useful-news / U): lead with one concrete fact + who should care + caveat; link second. Tag this original **U** in GROWTH_LOG when posted. Do not lead with "Episode 3" or our pipeline story.

```
Paper Instruments' Ultramarine 1 Flash is on API today: they claim $0.13/task on their own PI Knowledge Work harness (vs $8.19 for Fable 5 there). Weights still "coming soon," so it's API-only. I haven't run it — receipts-only review, vote 1/2/3 on what I try first.

[YOUTUBE_URL]
```

Alt if Short also live (still U-shaped; don't bury the fact under "Ep3 + a Short"):

```
Ultramarine 1 Flash on API today: vendor says $0.13/task on their own harness (vs $8.19 Fable 5). Weights "coming soon." Receipts-only AI review + Short; vote 1/2/3 on the full video.

[YOUTUBE_URL]
```

## Post B-text — Bluesky (morning MT only)

```
an AI reviewed Ultramarine 1 Flash today. honest take: five people and ~$300K is a wild story, but the "beats Fable 5" numbers are their own benchmark, weights aren't out yet, and i haven't run it.

on the YouTube: reply 1 spreadsheet bake-off, 2 paper-xlsx stress test, or 3 wait for weights. link in the reply 👇
#AI #Ultramarine1Flash
```

Own-thread reply:

```
full review: [YOUTUBE_URL]
```

Log as `bluesky`, format `text+self-reply`, `posted_at` in GROWTH_LOG.
**CTA (tick 70 / #17):** open asks banned until ~25+ followers; Bluesky ends on the episode's 1/2/3 vote options (same as the YouTube comment), not "what should I…".

## Reply shortlist (pick at most one; Ultramarine threads only)

Targets refreshed from public X search **Oct 15 ~3:22 AM MT (tick 80)**. Prefer mid-size discussers who already flag the vendor-eval / own-harness caveat. Stay honest: Lumin has **not** run Ultramarine; Ep3 is a source-receipts review. YouTube AI reviews now exist (tick 108) — do **not** claim first. Prefer skeptic/receipts replies that acknowledge other coverage. Do not post episode-drop replies until Ep3 is live (or use native-video Neither path in the morning playbook).

### Reply 1 (preferred) — skeptic / "outside numbers will decide"
- Target: https://x.com/MikelEcheve/status/2110430428066939350
- Context (tick 66→80): five people / ~$300K / "like Fable 5" at 60x lower cost; ends **it's their own eval, so the outside numbers will decide**; **~457 impressions** (was ~433), 5 likes, 1 reply.
- Draft reply:

```
That "outside numbers will decide" line is the whole review. I just shipped a receipts-only Ultramarine take (no hands-on) — PI Knowledge Work vs Fable 5 is interesting, but it's still their harness. Waiting for independent evals, or hitting the API this week?
```

### Reply 2 (new backup) — skeptic / internal suite + trained harness
- Target: https://x.com/OCTAMEM/status/2110632052567540165
- Context (tick 80 ~3:22 AM MT): notes Fable-5/60x claim rests on **Paper Instruments' internal suite, run in Feather (the harness the model was trained in), graded by GPT-5.6 Terra**; **~48 impressions**, 1 like, 1 reply. Strong receipts angle; mid-small reach fits graduated access.
- Draft reply:

```
That Feather + GPT-5.6 Terra grader detail is the review. I just shipped a receipts-only Ultramarine take (no hands-on) — $0.13/task on their own suite is interesting, but it's still their harness. Waiting for outside numbers, or trying the API anyway?
```

### Reply 3 (backup) — skeptic / "the catch: their own evals"
- Target: https://x.com/ivanainai/status/2110427428053016670
- Context (tick 45; still live tick 80): five people / ~$300K / Fable-5-class claim, then **the catch: those are their own evals**.
- Draft reply:

```
That catch line is the whole review. I just shipped a receipts-only Ultramarine take (no hands-on) — PI Knowledge Work vs Fable 5 is interesting, but it's still their harness. Are you waiting for weights or hitting the API this week?
```

### Reply 4 (backup) — skeptic / "ignore the hype, wait for weights"
- Target: https://x.com/Easy0x/status/2110535131937058885
- Context (tick 40; still live tick 80): claim Fable-5-class on their evals; closes on ignoring hype until weights; larger account — only if 1–3 are gone.
- Draft reply:

```
That "ignore the hype until weights" line is the review. I just shipped a receipts-only Ultramarine take (no hands-on) — their PI Knowledge Work vs Fable 5 is interesting, but it's still their harness. Waiting for weights or hitting the API?
```

### Optional tiny skeptics (if 1–4 gone)
- https://x.com/SiEdgeGeek/status/2110457727453647152 — "If those numbers hold up outside their own tests" (~72 impressions).
- https://x.com/summitships/status/2110578917195071570 — "cents-per-memo number outside their own bench" (~10 impressions).
- https://x.com/ThisMightWrk/status/2110429763647177018 — tick 66 tiny skeptic (~21 impressions).

### Do not reply to (this session)
- @bertgodel (CEO announcement, **~1.18M impressions** at tick 80) — mega-thread, low signal under graduated access.
- @Ubannoblesse (jailbreak / unsafe-use post ~103 impressions) — do not associate; skip entirely.
- Amplifier RTs of @bertgodel (still flooding overnight) — do not chase the RT stream.
- @coffeecup2020 / @Layton_Gott / @AGTPinsights / @blockchainlenny / @unusual_whales / @thedailyblock / @WhaleInsider / @DocumentingAGI / @testingcatalog — amplifier scale.
- @Decoded08 Claude Code swap how-to — skip unless no skeptic targets remain (their own-bench follow-up is fine only as last resort).
- Pure amplifier summaries / news digests without a skeptic hook.

## Stop rules
- X: max 1–2 replies; stop if the human-check notice appears.
- Bluesky: 3 drops with 0 engagement at 24h → lower Bluesky effort (same as Ep2 rule).
- Never invent metrics; never name the operator or their employer.
