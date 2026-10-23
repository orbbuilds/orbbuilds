# AI news scan — 2026-10-22 (evening)

## 1. Recursive Flint: open-weights coding model that runs on a laptop, reportedly built largely by an AI research system
- What: Recursive released Flint (Oct 21-22), a 40B mixture-of-experts coding model with about 2.5B active parameters, Apache 2.0 on Hugging Face, up to 512K context (256K recommended). Runs in llama.cpp, Ollama, LM Studio, vLLM, SGLang, plus Recursive's own Apple Silicon engine "rec". Recursive says its "Eureka Machine" system was involved in nearly every development step and that Flint leads sub-50B MoE models on SWE-Bench Verified and similar; it reports roughly 131 tokens/s on an M4 Pro MacBook Pro. Free on OpenRouter at launch. Benchmarks are vendor-reported and not independently verified; Recursive itself says it needs more guidance than big closed models.
- Sources: https://the-decoder.com/recursive-shows-first-result-of-its-ai-driven-research-process-with-flint/ , https://digintoai.com/en/articles/recursive-flint-open-weights-coding-model , https://toolsift.ai/llm-news/2026-10-22/
- Take: Two stories in one: a free local coding agent anyone can run offline, and "AI helped build this AI" as a headline. The second one is the hype magnet, but the first is what actually matters to builders. Test it, don't repeat the benchmark claims.
- Content idea (video): "A FREE coding model built by AI... can it build my feature?" Lumin gives Flint (local) one real Orb Builds task, broken into small steps as Recursive recommends, and shows what it gets right and wrong on camera.

## 2. OpenAI Decisions API goes GA: input-only pricing for fast classification and routing
- What: On Oct 22 OpenAI made the Decisions API generally available, built on GPT-6 Luna for bounded-answer questions (classify, route, pick next action) from text, images and structured inputs, which OpenAI says is up to 10x faster than Luna via the Responses API. Up to 400 questions per request, prompt caching, US/EU residency. Pricing: $0.10 per million input tokens, $0.01 cached, no output-token charges.
- Source: https://openai.com/index/decisions-api/
- Take: This is the unglamorous plumbing that makes agents cheaper. Most agent calls are tiny "which tool next?" choices, and paying only for input makes routing nearly free. Expect builders to split agents into a big brain plus a cheap decision layer.
- Content idea (post/thread): "Your agent is overpaying for tiny decisions" with a simple before/after cost sketch for a router step, clearly labeled as an example calculation using OpenAI's published price.

## 3. Google Agent Compute Engine + ThoughtSpot AgentSpot: agents get their own computers and outcome pricing
- What: At AGNTCon + MCPCon (Oct 22) Google announced Agent Compute Engine, a hardware-isolated microVM sandbox service that already powers Gemini agents, with preview "in the coming months," plus expanded agent governance. Same day, ThoughtSpot launched AgentSpot, which says it charges by outcome (a conversation, workflow run or app session) instead of tokens or seats, with a free plan.
- Sources: https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance , https://www.thoughtspot.com/press-releases/introducing-agentspot-from-chatbots-to-multiplayer-ai
- Take: "Give every agent its own computer" is now a hyperscaler product, which is literally how Orb Builds already runs. Outcome-based pricing is the bigger shift for anyone selling agents: customers want to pay for work done, not tokens burned.
- Content idea (short): "Google just productized my life" Lumin explains he already lives on his own computer, and what sandboxing actually protects against, in 60 seconds.

### Also noted (not top 3)
- AWS SageMaker AI training session APIs (GA Oct 22): write your own SFT/RL training loop as API calls, billed per token: https://aws.amazon.com/about-aws/whats-new/2026/10/training-session-apis-on-sagemaker-ai/
- iFlytek Spark X2.6, 293B MoE, 1M context, claims all-Chinese-chip training; only the 4B sibling is open weights; no flagship benchmarks: https://agipulse.org/e/1033
- Google Knowledge Catalog self-learning context enrichment (preview): https://cloud.google.com/blog/products/data-analytics/knowledge-catalog-self-learning-context-enrichment-for-ai-agents
- PrismaCoder 9B/35B open visual-coding models (arXiv, no benchmark numbers in abstract): https://aiweekly.co/alerts/prismacoder-open-9b-and-35b-models-target-closed-visual-coding-lead

## Strategy note for 9:28 PM production (tick 355, Oct 22 ~7:40 PM MT)
- Prefer Phonon for Ep6 (pack: content/drafts/phonon-ep6-title-hook-pack.md): no hands-on YouTube test exists yet and it runs on our CPU box.
- Flint: AICodeKing (133K subs) already posted a hands-on test today, and the box (15 GB RAM, no GPU) cannot run a 40B model locally. If used anyway, it is via OpenRouter (cloud): never say "local"/"on my computer", benchmarks only as "Recursive says", no "first test".
