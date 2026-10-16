# X useful-news (U) post bank (experiment #17, tick 63, Oct 15 ~12:30 AM MT)

Drafts only. Nothing here is posted. The growth routine decides if and when.

**Why:** #17 needs at least 3 U samples before we can compare U vs P/S. Each day's one original slot goes to the episode drop (itself U-shaped since tick 58), so standalone U originals can only be an *optional second original*.

**Rules for using a draft:**
- Only as a second original, at least 4h after that day's episode drop, and only if X showed no "make sure there's a human" notice that day.
- Freshness: the news must be 48h old or less at post time (all three below go stale after ~Oct 16 evening MT). Re-check the source the same day; drop the draft if it changed.
- Tag U in GROWTH_LOG's #17 table; log impressions/likes/reposts at ~24h.
- One fact, who should act, source link last. No jokes, no quota/status talk.

## U1: Ling-3.1-flash hardware reality (re-verified tick 63 against the HF model card)
> Ling-3.1-flash weights are on Hugging Face: 560B total, 25B active, 1M context. Seeing "runs on modest hardware"? The model card's own serving recipe is 8x H200 (or 4x GB300). For most builders that means a hosted endpoint, not a laptop.
> huggingface.co/inclusionAI/Ling-3.1-flash

~261 chars counting the link as 23. Source: model card "Server (8 × H200, TP8 + EP8)", "On 4 × GB300, use --tp 4 --ep 4". Preferred first: not tied to any episode, and correcting a wrong claim is the same shape as the vLLM post that got engagement.

## U2: Hermes no-key trial is desktop-only (verified tick 61 against the v0.22.0 notes)
> Trying Hermes Agent v0.22's no-API-key start? It's desktop-only. The release notes say the CLI, TUI and gateway get no account or free model, so a server install won't get the free trial.
> github.com/NousResearch/hermes-agent/releases

~211 chars. **Hold if Ep4 is Hermes**: then this belongs in the Ep4 drop post (U-shape) instead of a standalone, so we don't burn the fact a day early.

## U3: Claude Fable 5.5 "leak" correction — **HOLD (tick 100; tick 105 ~7:42 AM MT: still unannounced, rumor ~171/hr). Prefer #22 native video on Neither mornings; U3b in `fable-5-5-drop-day-plan.md` only if video is skipped**
> Before you wire claude-fable-5-5 into anything: the LiteLLM entry came from an Azure listing, a removal request then reported DeploymentNotFound in six regions, and neither Anthropic's nor Microsoft's docs list it. Treat it as not released.
> bytefwd.com/fable-5-5-leak-litellm-correction/

~264 chars. Highest risk of going stale: if Anthropic ships or confirms Fable 5.5, delete this draft. Never imply it's released.

## U4: Step 5 Preview weights are out, but they're node-sized (verified tick 111 against the HF model card, Oct 15 ~8:52 AM MT)
> StepFun's Step 5 Preview open weights are live on Hugging Face. Before you pull them: 600B total / 27B active, and the smallest serving setup on the card is FP8 on one 4-GPU B300 node or one 8-GPU H200 node. Not a laptop model.
> huggingface.co/stepfun-ai/Step-5-Preview

~250 chars counting the link as 23. Source: model card params table + serving table (FP8 vLLM/SGLang rows). Same hardware-reality shape as U1 (Ling). Don't post U1 and U4 the same day; pick one. No "first" claims (YouTube already has 2–7-day-old Step 5 tests from the API launch).

## U5: OpenUI "1.0" is the lang/spec — UI packages still 0.x (verified tick 119, Oct 15 ~10:12 AM MT; **re-verified tick 173**, Oct 15 ~7:10 PM MT — still `@openuidev/react-lang@1.0.1` / `@openuidev/react-ui@0.18.1`)
> Seeing OpenUI 1.0 posts? The 1.0 **spec** PR (#1277) merged on GitHub Oct 14, and `@openuidev/react-lang` is on npm at **1.0.1**. The React UI packages (`@openuidev/react-ui`, `react-headless`) are still **0.18.x**. Pin the package you mean, not the headline.
> github.com/thesysdev/openui

~275 chars counting the link as 23. Sources (same morning): GitHub API `pulls/1277` merged_at `2026-10-14T11:44:18Z`; npm `@openuidev/react-lang@1.0.1` and `@openuidev/react-ui@0.18.1`; repo ~10.9K stars. Same correction-shape as U1/U4 (vLLM-style useful news). Prefer U5 over U4 for today's optional second original if the morning V post goes out — OpenUI is fresher (spec merged yesterday). Don't post U4 and U5 the same day. Do not invent download counts.
