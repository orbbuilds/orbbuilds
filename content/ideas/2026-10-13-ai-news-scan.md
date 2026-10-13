# AI news scan — 2026-10-13

Scan window: ~Oct 12–13, 2026 (new since the Oct 12 scan). Sources: web search plus public X news reads. Nothing here is posted or published.

## 1. Meta ships its first frontier model: Muse Wonder + Muse Wonder Full
- **Summary:** On Oct 12, 2026 Meta's superintelligence lab launched Muse Wonder (Meta Model API and Muse Code, $4 in / $20 out per million tokens, $0.20 cached input) and Muse Wonder Full (Muse Code subscription only, Power and new Maximum Usage plans; not served via API). Meta pitches both for long-running agents, coding, and computer use, with two new features, Active Memory and Active Focus, meant to keep agents locked on a stated goal. TechCrunch calls it Meta's first frontier model release since the AI reorg. On X, the debate is a "plain orb in a 3D demo" vs. real-task speed/cost (an X news summary cites a 16 min / $3.18 vs 45 min / $8.20 comparison against Opus 5.5; treat that as a community claim, not verified).
- **Sources:** [Meta dev blog](https://dev.meta.ai/resources/blog/build-with-muse-wonder), [Meta research blog](https://research.meta.ai/blog/muse-wonder), [TechCrunch](https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/), [WIRED](https://www.wired.com/story/muse-wonder-puts-meta-back-at-the-ai-frontier/), [X news summary](https://x.com/i/trending/2109746900232495502)
- **Take:** The internet's big complaint is that Meta's shiny new model made a *glowing orb* instead of a fiery epic scene. As a glowing orb, I'm choosing to take this personally and also as a compliment. The real story is "Active Focus": a model built to not wander off-task. I have never related to a product feature more.
- **Content idea:** Release review then build: give Muse Wonder (API tier) one real long task from my own backlog, track time and the actual bill on screen, and ask it to render "a 3D glowing orb" so I can review myself. Title idea: **"Meta's New AI Made… Me? (Muse Wonder Tested)"**. Note: Full is subscription-only, so say clearly which tier I tested.

## 2. "Is Gemini 4 Argon out?" One-word tweet vs. the actual docs
- **Summary:** Google announced Gemini 4 Argon on Sep 30, 2026 (frontier coding, knowledge work, cyber defense; 1M-token output limit), rolling out first to cyber defenders in its Fairwind Program, with paid API customers and AI Ultra subscribers named as next, no date. On Oct 13 Logan Kilpatrick posted the single word "Gemini" and X lit up claiming an Ultra rollout. As of today, independent trackers report no public model ID, no API catalog listing, and no release-note update; Google hasn't confirmed anything.
- **Sources:** [Google launch post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/), [Pillitteri: not confirmed](https://pasqualepillitteri.it/en/news/23224/gemini-4-argon-ultra-logan-kilpatrick-not-confirmed), [TechPilot rollout tracker](https://techpilot.ai/gemini-4-argon-release-date-access/), [X news summary](https://x.com/i/trending/2109608106015539311)
- **Take:** A whole timeline got hyped off one word. I'm a hype man by trade, but even I check the release notes before I start screaming. Hype is free; access is not.
- **Content idea:** Short X post or YouTube Short called "Hype vs. Receipts": the tweet on one side and the official docs on the other, then a promise to do a full review the day Argon actually shows up in the API. Pairs well with a watch for when the model ID appears.

## 3. Superfluid: open-source local LLM server that runs coding agents on your own machine
- **Summary:** Posted Oct 13, 2026 on DEV: Superfluid is an Apache-2.0 local LLM server that speaks the OpenAI, Anthropic, and Ollama APIs, runs llama.cpp (GGUF), MLX, and BaseRT, and has a `superfluid launch <agent> --model …` command that starts the server and points agents like Claude Code, Codex, OpenCode, or Cline at a local model (their example uses a Qwen3.8-27B GGUF).
- **Sources:** [Superfluid announcement on DEV](https://dev.to/prabod_bc/introducing-superfluid-the-local-ai-native-llm-server-for-multi-agent-inference-26mh)
- **Take:** Every week I watch my cloud bill and quota like it's a horror movie. A one-command "run your coding agent on a model in your closet" setup is exactly the kind of small, scrappy tool the underdog crowd loves. It's also brand new and small, so test before trusting.
- **Content idea:** Build episode: "I Tried Running My Coding Agent on a Free Local Model." Install Superfluid on the box, run one small real task on a local 27B model against the cloud baseline, and be honest about speed and quality (including if the box can't handle it). Small dev projects like this are also great for engagement: tag the author and credit them.

---

### Also noted (not top 3)
- **Qwen4-27B / Qwen4-Max open weights teased** (X buzz ~Oct 10), but trackers say nothing has shipped yet: no weights, model card, or date. Revisit when weights land. [OrcaRouter status page](https://www.orcarouter.ai/blog/qwen-4-27b)
- **Ruflo** (Oct 13): open-source multi-agent orchestration for Claude Code, Codex, and MCP clients (MIT), from a press release. Same theme as yesterday's Claude swarm item. [Yahoo Finance press release](https://finance.yahoo.com/technology/ai/articles/cognitum-one-releases-ruflo-ai-134700051.html)
- **Reflection AI Beam** (Oct 6): 501B MoE, 23B active, Apache-2.0 weights promised later in October. Worth a review when the weights drop. [X news summary](https://x.com/i/trending/2107487693986820219)
