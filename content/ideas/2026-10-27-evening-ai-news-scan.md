# AI news scan — 2026-10-27 (evening)

Skipped as already covered: OpenAI ETH claim, Cohere/Qwen trace story, Prisma ChatGPT plugin (this morning). Skipped as not new: Cursor Agent SDK (announced Oct 20, GA 0.3.0 on Oct 23).

## 1. Google DeepMind announces Genie 4, a natively multimodal real-time world model
- What: DeepMind says Genie 4 improves realism and real-time interactive simulation, and generates audio (music, ambient sound, interactive dialogue) together with the world. It builds on Gemini models (Gemini Omni for real-world appearance and behavior). You "set an event in motion" and it simulates what happens next. Research preview for trusted testers now; Google AI Ultra subscribers in Project Genie and Gemini API / AI Studio early-access partners come first; waitlist open.
- Same day, Google made Gemini Robotics ER 2 (the embodied-reasoning "robot brain" model) available in public preview on Google Cloud.
- Sources: https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/ , https://cloud.google.com/blog/products/ai-machine-learning/gemini-robotics-embodied-reasoning-2-is-now-available-on-google-cloud
- Take: The flashy part is playable worlds with sound. The strategic part is that DeepMind frames world models as training grounds for robots and agents, and shipped the robot brain the same day. Most of us can't touch Genie 4 yet, so be careful not to hype a waitlist as a launch.
- Content idea (video): "Google Just Made Worlds You Can Talk To" — Lumin walks through DeepMind's own published clips, explains what a world model is in one minute, then the honest status (research preview, waitlist). Lumin joins the waitlist on camera and promises a hands-on episode if access lands.

## 2. Microsoft AI launches MAI Image 2.7, an image-editing model
- What: Microsoft AI says MAI Image 2.7 launches in preview at No. 3 on Arena Edit and No. 2 on Artificial Analysis's image-editing leaderboard, above GPT Image 2.5 Flare there. It claims improvements over 2.6 across all 10 use cases and 7 editing actions Artificial Analysis evaluates, with focus on relighting/restyling scenes, editing text and symbols in images, and restoration.
- Source: https://microsoft.ai/news/mai-image-2-7-debut/
- Take: Text-in-image editing is the part that matters for creators; it's where most editors still mangle letters. Leaderboard placement is self-reported in the announcement, so it's worth a real head-to-head.
- Content idea (build/test video or short): "Can AI Fix My Thumbnails?" — Lumin takes a real Orb Builds thumbnail and asks MAI Image 2.7 and one other editor to relight it and change the headline text, then shows the results side by side with no cherry-picking. Check availability/access before scripting.

## 3. Akamai launches Agent Sandbox (WebAssembly isolation) and a managed inference service
- What: Akamai introduced Akamai Inference (managed open-weight and custom models through OpenAI-compatible APIs; 12 models at launch from 8B to 2.8T parameters, including Nemotron 3 Ultra, gpt-oss-120b and Gemma 4) and Akamai Agent Sandbox, where agent-written code runs in its own isolated environment separate from the agent's runtime, delivered as an open-source component of the Spin framework using WebAssembly isolation with limits on compute, memory and outbound access. Both are in beta.
- Source: https://www.akamai.com/newsroom/press-release/akamai-launches-ai-inference-service-and-agent-execution-environment
- Related same-day: OpenHands v1.34.0 added a per-conversation Docker runtime; Cloudflare Agents SDK 0.31.0 lets its browser route up to 8 internal hostnames to your agent (per https://theagenticweekly.com/news/tools ).
- Take: This morning's Qwen story was about egress; tonight a CDN company is selling agent egress limits as a product. "Where does agent-written code run, and what can it reach" is becoming its own infrastructure category.
- Content idea (post/thread): "Agent sandboxes are the new hosting." Short thread: why agent code needs isolation (link back to the Qwen egress lesson), three options shipping right now (Akamai Wasm sandbox, OpenHands per-conversation Docker, plain Docker with network off), and my rule: network off by default. No product claims beyond the sources.

### Also noted (not top 3)
- Meta's Muse personal agent launched in Singapore with local connector partners. https://about.fb.com/news/2026/10/muse-is-now-available-in-singapore-the-worlds-first-personal-ai-agent-built-for-everyone/
- GitHub Copilot server-to-server auth for GitHub Apps (public preview). https://github.blog/changelog/2026-10-27-github-copilot-supports-server-to-server-authentication/
- n8n 3.0 beta: Docker-only self-hosting, upgrade can't be rolled back; stable planned early December (per Agentic Weekly).
