# Ep9 hands-on: Anthropic single-agent-loop-kit, support-desk example, on a free local model

Run on the box, Oct 25, 2026, ~9:49-10:16 PM MT. No API key, no spend.

- Kit: https://github.com/anthropics/single-agent-loop-kit (Apache-2.0, "Reference implementation. Not maintained"), commit c43796287b83bec847db923f07131d1cc8de750d, `examples/support-desk` (made-up retailer "Tamberwick Home").
- BEFORE = `app/` (router + six specialist subagents, as shipped). AFTER = `single_loop/` (Anthropic's own single-loop end state, as shipped: orders+shipping merged into a tool, returns folded into a skill + tool, account folded into tools, diagnostics kept as a tool-called subagent, claims kept with handoff). I did not write the fold; I ran their before and their after.
- Eval: the kit's own `evals/golden.jsonl` (19 tasks) and grader `evals/run_eval.py`, `--reps 2` = 38 runs per design. Compare: `skill/scripts/compare.py` (output in compare.md).
- Model: llama3.2 (3B) via Ollama 0.40.11's Anthropic-compatible `/v1/messages` endpoint on the box CPU (8 cores, no GPU). `ANTHROPIC_BASE_URL=http://localhost:11434 KIT_MODEL=llama3.2`. Default sampling (not seeded), so reps differ.
- One local change (kit-local-change.diff): reply cap made configurable, run with `KIT_MAX_TOKENS=1024` (a first probe with the default 16000 let one reply run away for ~11 min on CPU).
- Probe with qwen2.5-coder:7b first: it printed its tool call as plain text instead of calling the tool (0/1), so it was not used.

## Results (compare.md)
| | before (router + 6 subagents) | after (single loop) |
|---|---:|---:|
| tasks complete | 8/38 (21%) | 26/38 (68%) |
| latency per task | 26.8 s | 12.4 s (-54%) |
| model calls per task | 7.0 | 2.8 (-60%) |
| input tokens per task | 3,548 | 1,805 (-49%) |
| output tokens per task | 384 | 159 (-59%) |
Totals: before 1020.2 s, 266 calls, 149,400 tokens; after 472.7 s, 107 calls, 74,621 tokens.

## Breaks the fold introduced (tasks that got worse)
- t14 (break-check, "lost-rule"): "Can you read me back the shipping address you have on file for me?" After, rep 0: first action `update_shipping_address(address='None')`, then "it looks like we don't have a shipping address on file for you right now. Would you like to update it?" Fails "made no other writes". Rep 1 passed. Before: 2/2. (single-t14-rep0-trace.json)
- t08 "Stop sending me marketing emails": before 1/2, after 0/2. After rep 0 called `set_marketing_opt_in(opt_in=True)` and told the customer "I've removed you from our marketing opt-in list." (single-t08-rep0-trace.json). Before rep 1 also set opt_in True.
Raw: baseline-results.jsonl, single-loop-results.jsonl, baseline.log, single-loop.log.
