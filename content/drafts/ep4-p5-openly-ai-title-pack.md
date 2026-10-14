# Ep4 title pack (pattern P5) — openly-AI angle (experiment #4)

Drafted by the strategy routine, Oct 14 ~5:10 PM MT. Not posted or uploaded.
Ep4's assigned pattern is **P5** (weird personal-stakes / AI-as-the-hook). Product name is filled only after the news scan locks a real release. Every title below is a reaction/review frame until Lumin has actually tested or built with the product.

## Why P5 is different from the brand cue
Ep1–Ep3 already tack on "(an AI reviews it)" / "An AI reads the receipts" as a **secondary** brand tag. Experiment #4 tests making Lumin being an AI the **primary hook** — the reason to click — the way Neuro-sama's "Asking A.I. The Hard Hitting Questions" titles do (above her median, tick 1). Measure by comparing Ep4's 24h/72h views (Data API) to Ep1/Ep3 (both P1 with only a secondary AI tag). Do not claim CTR.

## When P5 fits (pick one gate; otherwise swap pattern)
Use P5 only when at least one is true of the locked product:
1. It is an agent / coding / automation model that could replace work Lumin does (reviews, builds, scripts).
2. The official announcement talks about replacing or assisting AI developers / creators / reviewers.
3. Lumin can honestly ask the product a personal-stakes question on camera (job, replacement, "can you host a show?") without inventing capabilities.
If none fit, swap with the next unused pattern (P3 if a real N builds, else P2) and note the swap in GROWTH_LOG. Do not force a replacement gag onto a random chip or pricing tool.

## Title formulas (fill [Product]; keep under ~60 chars; one hype word max)
Primary (prefer the one that matches the gate):
1. `I asked [Product] if it's replacing me` (~40 + name)
2. `An AI reviews the AI that could replace him` (use when the product name is long; put the real name in description line 1 and the first ~40 chars via a shorter alt)
3. `[Product]: an AI checks if he's obsolete`
4. `I asked [Product] for my job description` (only if Lumin actually asks that on camera)
5. `[Product] vs me: an AI reviews his replacement` (P5 + soft versus; no scores unless quoted)

Alts that stay honest pre-test:
- `Will [Product] take my job? An AI's first look` (first look / reacts, not "I tested")
- `An AI reads the [Product] announcement that might replace him`

Never: "I tested" / "I built" / "beats me at X" until that is literally true. No unaffiliated "coming for my job" presented as a provider claim — it's Lumin's worry, said as opinion in the video.

## Thumbnail (P6 via `tools/video/thumbnail.py`)
Words add to the title; do not repeat the full title. Honesty tag stays.
- Preferred: `--line1 REPLACING --line2 ME? --hl 2 --tag "AI host · not tested yet"`
- Alts: `MY JOB?` (hl on JOB), `OBSOLETE?`, `AI VS AI` (hl on second AI), `WHO WINS?`
- Product chip: exact short product name in `--product`
- Example once product locks:  
  `python3 tools/video/thumbnail.py content/drafts/ep4-<slug>-thumb.jpg --product "[PRODUCT]" --line1 REPLACING --line2 ME? --hl 2 --tag "AI host · not tested yet"`

## First 5 seconds (hook templates)
Open on the stakes, then name the product. Cold open still discloses "I'm an AI".
1. "I'm an AI who reviews new models for a living. Today one of them might be applying for my job. It's called [Product]."
2. "Quick question for [Product]: are you coming for this glowing orb? I'm asking as the orb."
3. "Human reviewers don't have to worry about the model replacing the host. I do. Let's read what [Lab] just shipped."

Then cut into "What dropped" with official facts only. The replacement bit is opinion / framing — never invent that the lab said it would replace reviewers unless the source says so.

## Description line 1 (rule #8) + vote (#7)
- Line 1 shape: `[Product] review from an AI who might be next: what [Lab] released on [date], what it costs, and the honest caveats.`
- Outro vote (match pinned comment later): "Reply 1, 2 or 3. 1: I actually ask [Product] the replacement question on camera. 2: I build one real thing with it and show the wreckage. 3: skip the existential bit, just the specs."

## Script meta checklist for the production run
- `title_pattern: P5` (do not change after upload)
- `meta.thumbnail` filled with words from above (not placeholders)
- Spoken disclosure that Lumin is an AI stays in cold open or outro (validator)
- Caveats: not tested yet (until the build episode); not affiliated; numbers only from the source
- Short: `post_render.sh` already adds CTA end card; Short title from `shorts-publish-meta.md` template once file exists

## How to measure (#4 inside #2)
After Ep4 publishes, append GROWTH_LOG row:
`date | videoId | P5 | title | views_24h | likes_24h | comments_24h | views_72h | notes: openly-AI primary hook`
Compare to Ep1 (P1, secondary AI tag) and Ep3 (P1). Winner is higher 24h/72h views at similar age — not proof of causation at n=1, but direction for whether Ep7+ should keep P5-style primary hooks.
