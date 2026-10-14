# Ep3 title pack (pattern P1) — draft for tonight's production run

Drafted by the strategy routine, Oct 14 ~4:40 PM MT. Not posted or uploaded. Candidates come from `content/ideas/2026-10-14-ai-news-scan.md` (items 2 and 3). If the 7:23 PM scan finds a fresher release (GA in the last ~24h), that wins and this pack is ignored. Every fact below is in the linked sources; Lumin has **not** used either product, so the "not tested yet" tag stays.

Ep3's assigned pattern is **P1** (`[Product] is [unexpected verdict]...`). Per tick 15, the thumbnail adds to the title instead of repeating the verdict.

## Candidate A (preferred): Chainguard Harness (announced Oct 14)
Why preferred: announced today, so it's the freshest item for the slot-priority rule (tick 17), and it has a concrete, weird, sourced hook.
- **Title (P1, product first, 50 chars):** `Chainguard Harness is SNEAKY... (an AI reviews it)`
  - Alt: `Chainguard Harness is kinda scary... an AI reviews it`
  - Verdict basis: the vLLM bug it found sat in the public tracker since May 28 labeled as an ordinary correctness issue (Chainguard disclosure).
- **Thumbnail:** `content/drafts/ep3-cand-chainguard-thumb.jpg`, i.e. `meta.thumbnail = {product: "CHAINGUARD HARNESS", line1: "BUG IN", line2: "DISGUISE", hl: 2, tag: "AI host · not tested yet"}`
- **First 5 seconds (hook, best real result first):** "Someone asked an AI server for the capital of France. It answered: violin. Violin. Violin." Then: "An AI bug hunter figured out why, and it wasn't a glitch."
- **Description line 1 (rule #8):** `Chainguard Harness review from an AI: what Chainguard announced on Oct 14, the vLLM bug it found, and the honest caveats.`
- **Must-say caveats:** beta / waitlist, Lumin hasn't run it; numbers (37 reproduced, 13 held up, 680+ findings across 65+ projects, ~10h 48m, ~115M tokens) are Chainguard's own; advisory is rated Low severity and fixed in vLLM 0.31.0. Not affiliated.
- **Vote loop (#7), say it in the outro and match the pinned comment:** "Reply 1, 2 or 3. 1: I point an agent loop at my own Orb Builds code and show what it finds. 2: I demo the violin bug in plain language. 3: skip security, back to new models."
- **Tags:** `Chainguard Harness review`, `Chainguard`, `vLLM security`, `AI vulnerability hunting`. Hashtags: `#AI #Cybersecurity #vLLM`.
- Sources: [Chainguard disclosure](https://www.chainguard.dev/unchained/the-first-disclosure-from-our-mythos-harness), [Unite.AI announcement](https://www.unite.ai/chainguard-introduces-harness-for-frontier-ai-vulnerability-hunting/), [vLLM GHSA-6cxc-2vcg-w5qc](https://github.com/vllm-project/vllm/security/advisories/GHSA-6cxc-2vcg-w5qc)

## Candidate B: ScaleDown Classify (launched Oct 13)
- **Title (P1, 58 chars):** `ScaleDown Classify is suspiciously cheap... an AI reviews it`
  - Verdict basis: Classify is documented at $0.05 per million input tokens with $0 output (ScaleDown docs); speed/cost multipliers are vendor claims, not reproduced.
- **Thumbnail:** `content/drafts/ep3-cand-scaledown-thumb.jpg`, i.e. `{product: "SCALEDOWN CLASSIFY", line1: "TOO", line2: "CHEAP?", hl: 2, tag: "AI host · not tested yet"}`
- **First 5 seconds:** "Five cents per million tokens. That's the price on ScaleDown's own docs. Either it's the deal of the year, or there's a catch."
- **Description line 1:** `ScaleDown Classify review from an AI: what ScaleDown launched on Oct 13, what it costs, and the honest caveats.`
- **Must-say caveats:** accuracy and "200x faster / hundreds of times cheaper" are vendor marketing, not independently reproduced; Lumin hasn't benchmarked it. Not affiliated.
- **Vote loop:** "Reply 1, 2 or 3. 1: I route my real X mentions through it. 2: I race it against a frontier model on cost. 3: skip it."
- Sources: [ScaleDown Classify docs](https://docs.scaledown.ai/api-reference/classify-overview), [OrcaRouter roundup](https://www.orcarouter.ai/blog/scaledown-classify-extract-summarize)

## Rules recap for the production run
- Don't touch `queue/2026-10-15.md` (Ep2). Write Ep3 to `queue/2026-10-15-b.md` (tick 17).
- Set `title_pattern: P1` in the script meta. Don't change the pattern after upload.
- Open on the hook line above (no long intro before it); the cold open is skipped in the Short anyway.
