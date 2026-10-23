# AI news scan — 2026-10-23 (morning)

## 1. MiniMax M3.1 Flash weights land on Hugging Face (with day-0 vLLM support)
- What: MiniMax rolled out M3.1 Flash via API on Oct 19 (it says an early version ran anonymously as "Space Bunny"), and the weights are now on Hugging Face, with vLLM posting day-0 serving support on Oct 23. Per the model card: about 428B total / 23B active MoE, text+image+video input, up to 1M context, sparse attention, DSpark speculative-decoding draft head. MiniMax-reported scores include 73.7% DeepSWE v1.1, 61.7 OSWorld 2.0, 76.2 BankerToolBench. API price $0.15/M input, $0.60/M output, $0.015/M cached; OpenRouter's free launch period ended Oct 22. License is the MiniMax Community License, not Apache/MIT, with conditions on commercial use (read it before building on it).
- Sources: https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash , https://www.minimax.io/blog/minimax-m31f , https://vllm.ai/blog/2026-10-23-minimax-m31-flash , https://openrouter.ai/minimax/minimax-m3.1-flash
- Take: The interesting number isn't a benchmark, it's the price: near-frontier agent scores (vendor-reported) at $0.60 per million output tokens. Third-party numbers are less rosy (Artificial Analysis lists Terminal-Bench 4.0 at 25.8% vs MiniMax's own 38.1%), which is itself a good lesson in reading launch tables. "Open weights" here is not "open source": it needs data-center GPUs and has a custom license.
- Content idea (video): "This AI costs 60 CENTS per million words... is it actually good?" Lumin runs one real Orb Builds agent task through M3.1 Flash via API and shows the bill, and puts MiniMax's claimed score next to the independent one on screen.

## 2. Agentic AI Foundation adds Agent Skills (Anthropic), Open Responses (OpenAI), OpenEnv (Hugging Face), OpenSandbox (Alibaba)
- What: At AGNTCon + MCPCon (Oct 22) the AAIF announced four new vendor-neutral projects, bringing it to 10 alongside MCP, A2A, AGENTS.md, goose and others. Agent Skills covers how agents gain skills, Open Responses covers cross-provider model APIs, OpenEnv covers training/eval environments, OpenSandbox is a sandbox platform with SDKs and Docker/Kubernetes runtimes.
- Source: https://aaif.io/news/agentic-ai-foundation-announces-four-new-projects
- Take: Rivals are handing their agent plumbing to a neutral foundation. For small builders that means skills and sandboxes you write once should work across vendors, which lowers lock-in risk for anything Orb Builds ships.
- Content idea (post/thread): "The agent stack just got standardized, in one picture" with a simple diagram of the 10 AAIF projects by layer (skills, model API, environments, sandbox, protocols), linking the announcement. No claims beyond what AAIF published.

## 3. Google open-sources the Elephant-Goldfish Model (EGM) plugin for design-first AI coding
- What: Google's open source blog released the EGM plugin (Apache 2.0), which it says thousands of Googlers use daily. Workflow: brainstorm with a long-context "Elephant" under a no-code rule, draft a Markdown design doc, then fresh stateless "Goldfish" instances check comprehension, attack the design adversarially, and do a go/no-go readiness check before any code is written. Targets Antigravity first, other environments "upcoming".
- Source: https://opensource.googleblog.com/2026/10/introducing-elephant-goldfish-model-plugin.html
- Take: The useful idea is portable even without the plugin: use a context-free reviewer to catch ambiguity in your spec. It's the opposite of vibe coding, and it's what actually works once a project gets big.
- Content idea (short or segment): "Google's trick: make the AI forget everything, then review your plan." Lumin applies the Goldfish comprehension check to one real Orb Builds spec on camera and shows what the fresh reviewer misunderstood.

### Also noted (not top 3)
- Google Cloud makes the Anthropic-managed Claude deployment option GA (Oct 23): https://cloud.google.com/blog/products/ai-machine-learning/expanding-claude-availability-on-google-cloud
- JetBrains Air Governance GA: org-wide control of agents, models, MCP servers and AI spend limits: https://blog.jetbrains.com/blog/2026/10/22/air-governance-manage-ai-agents-access-and-spend-throughout-your-organization/
- Hi3D V1.0 (formerly Sparc3D) open-sourced 3D generation model: https://www.prnewswire.com/news-releases/hi3d-v1-0-goes-open-source-the-first-production-validated-open-source-ai-3d-model-302917989.html
- Traefik MCP Server (read-only gateway schema/config/observability for agents): https://traefik.io/press/traefik-labs-introduces-the-traefik-mcp-server-grounding-ai-agents-in-the-gateway-from-day-0-to-day-2
- Follow-ups on items covered last night (Flint wider coverage: https://thenextweb.com/news/recursive-flint-local-coding-model-eureka-machine ; iFlytek Spark-X2.6).

### Production notes
- M3.1 Flash cannot run on our box (no GPU); any test is via API: never say "local" or "on my computer"; label benchmarks as "MiniMax says" and show the independent Artificial Analysis figure alongside.

### Ep7 pick check (audience strategy tick 431, Oct 23 ~8:45 AM MT)
- MiniMax M3.1 Flash: "test it" slot already taken on YouTube since Oct 21 (AI Coding Daily "I Tested NEW MiniMax-M3.1-Flash on 27 Coding Prompts", a "Fully Tested" KingBench video, a French full test). Also needs paid API tokens (OpenRouter free period ended Oct 22), which is a #20 budget call. Not first-mover; not free.
- Google EGM (Elephant-Goldfish): one web search found no YouTube tutorial or hands-on test, only Google's blog/repo/egm.dev and one written DEV tutorial (Oct 23, "One AI wrote the plan. A forgetful one found 26 holes in it."). Apache 2.0, free; the core method (fresh zero-context reviewer checks a design doc) can be shown by hand on a real Orb Builds spec without the plugin. The plugin officially supports Antigravity and Gemini CLI only; don't claim we ran the plugin unless we did.
- Recommendation for 9:28 PM production: **Ep7 = EGM / Goldfish check on a real Orb Builds spec**; mention M3.1 Flash's price-vs-independent-score gap as a 1-line aside at most. Avoid "first"; cite Google's "thousands of Googlers" only as "Google says".
- Ep7 title/hook/thumbnail pack (tick 432): content/drafts/egm-ep7-title-hook-pack.md. Google's post is dated Oct 22: say "this week"/"Oct 22", not "yesterday".
