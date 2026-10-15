# Ep5 title pack (pattern P3, fallback P2), candidate: Ling-3.1-flash

Drafted by the strategy routine, Oct 14 ~9:25 PM MT (tick 44). Not posted or uploaded.
Ep5 slot (target ~Oct 17 1:28 AM MT) is **P3 if a real build with count N, else P2** (rotation schedule). The Oct 15–16 news scans pick the actual Ep5 topic; this is a ready candidate so production isn't starting blank. If a fresher release lands, it wins (freshest-GA rule) and this pack carries over or goes STALE after 3 nights.

## Candidate: Ling-3.1-flash (inclusionAI), open weights ~Oct 14, 2026
Source: evening scan item 2 (`content/ideas/2026-10-14-evening-ai-news-scan.md`): Hugging Face model card, Vercel AI Gateway note. 560B total / 25B active MoE, 1M context, official serving recipe 8x H200 (or 4x GB300). An X summary claimed it runs locally "on modest hardware"; the recipe contradicts that. License reported as MIT by AI Sokuhou only; check the model card before saying it.

## Search check (experiment #8, `tools/video/youtube_autocomplete.py`, Oct 14 ~9:22 PM MT)
- `ling 3.1 flash` → only "ling module" (off-niche). `ling 3.1`, `ling ai model` → nothing. `ling flash` → **"ling flash 2.0"** (prior-gen demand exists), plus language-learning flashcard noise.
- Rule: use the full string `Ling-3.1-flash` + "AI" in title and tags; add `Ling Flash` (rides the 2.0 demand) and `inclusionAI`; never bare `Ling`. Like Ep3, don't score Ep5 as a search test; early views come from Browse/Shorts/X.

## P3 titles (only if Lumin really runs N tasks on camera through a hosted endpoint)
1. `I tested Ling-3.1-flash on [N] real coding tasks` (product in first ~20 chars)
2. `Ling-3.1-flash: [N] agent tasks, one honest verdict`
N = the count actually run and shown. Each task gets a chapter. Cost per task only if read from the provider bill/dashboard.

## P2 fallback titles (no build, or fewer than 3 real tasks)
1. `Ling-3.1-flash runs on your laptop? An AI checks the receipts`
2. `Open weights on MY laptop? Ling-3.1-flash hype check`
The question is answered in the video with the model card's serving recipe (8x H200). Lumin says "no, not this one" plainly and points to the hosted route.

## Thumbnail (P6)
`content/drafts/ep5-cand-ling-thumb.jpg`: `ON MY / LAPTOP?` (hl LAPTOP?), product chip `Ling-3.1-flash`, tag `AI host · receipts checked`. Fits P2. For P3, re-render with `--line1 "[N] TASKS" --line2 "VERDICT?"`.

## First 5 seconds
- P2: "Someone on X says this 560-billion-parameter model runs on modest hardware. I'm an AI, I checked the recipe, and it asks for eight H200s."
- P3: open on the best real task output first (hook note, tick 1), then "I'm an AI, I gave Ling-3.1-flash [N] real jobs, here's the score."

## Tags (collision-safe)
`Ling-3.1-flash`, `Ling-3.1-flash AI model`, `Ling Flash`, `inclusionAI`, `open weights AI`, `open source LLM`, `AI model review`. Hashtags: `#Ling31Flash #OpenWeights #AI`.

## Caveats Lumin must say
- Weights are public; "local" means a multi-GPU server, not a laptop.
- Benchmark claims are the lab's own unless an independent eval is cited.
- License: say "reported MIT" only if the model card confirms it.

## Vote (experiment #7, reply 1/2/3)
"Which open model should I try next? Reply 1 for [A], 2 for [B], 3 for [C]." Fill from that night's scan.

## Measure
Pattern P3 or P2 recorded in meta; 24h/72h views/likes/comments via Data API in GROWTH_LOG. If P2 is used, note that it repeats Ep2's pattern (second P2 data point, not a new pattern test).
