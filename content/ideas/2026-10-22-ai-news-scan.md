# AI news scan — 2026-10-22 (morning)

## 1. Gradium Phonon: open-source on-device TTS that claims to beat Kokoro
- What: Gradium (founded by Kyutai cofounders) released Phonon on Oct 21, 2026: a 31M-parameter (and 40M variant) text-to-speech model, Apache 2.0, runs fully on-device (phones, laptops, browser) in as little as 64.5 MB. Gradium says it wins blind preference tests against Kokoro (82M), Magpie and Pocket TTS. Launch partners include Hugging Face, LM Studio, Ollama, MLX Audio.
- Source: https://gradium.ai/blog/gradium-releases-phonon (weights: https://huggingface.co/gradium/phonon-31m-en)
- Take: This one is personal. Lumin's voice runs on Kokoro today. A model less than half the size claiming to beat it is exactly the kind of claim we should test on camera rather than repeat. Note the preference results are Gradium's own evaluation.
- Content idea (video): "Is my voice about to be replaced?" Lumin reads the same script in his current Kokoro voice and in Phonon, side by side, and lets viewers vote in the comments. Real build, real stakes, very on-brand underdog.

## 2. Claude API ships its first new version since 2023, and it breaks things
- What: Anthropic released API version 2026-10-21 on Oct 21. Sending temperature, top_p or top_k now returns HTTP 400 on every model; document blocks in assistant messages and citations in user messages also 400. New SDK majors: Python 2.0.0, TypeScript 1.0.0 (plus Go, Java, C#, PHP, Ruby, ant CLI), now Apache 2.0 instead of MIT. Claude Code v2.1.307 added a command to migrate code to the new version.
- Sources: https://platform.claude.com/docs/en/api/migration-2026-10-21 , https://platform.claude.com/docs/en/release-notes/overview
- Take: Killing temperature is a statement that newer models should be steered with prompts, not knobs, but anyone who pinned temperature 0 for "consistent" output on older models just lost that lever with no replacement. Upgrading blindly will break builds.
- Content idea (post or short): "I bumped my Anthropic SDK and my app broke in 3 ways" checklist thread with the three 400 errors and the fix for each, framed as a builder PSA.

## 3. OpenAI's frontier models land on Google Cloud
- What: On Oct 21, OpenAI and Google Cloud announced GPT-6 Astra, GPT-6.1 Sol and GPT-6 Luna (plus Codex agentic workflows) in Google Cloud's Model Garden, private preview now, GA "in the coming weeks." Google says it's now the only hyperscaler offering all three leading closed LLM families. OpenAI notes Microsoft remains its primary cloud partner.
- Sources: https://openai.com/index/openai-models-google-cloud/ , https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers
- Take: The model wars are turning into a distribution game. For builders, the lock-in story is fading: the same frontier models are showing up everywhere, so the moat is what you build on top.
- Content idea (video segment): "Frenemies" news hit: Google selling OpenAI's models, explained in 60 seconds, ending with what it means for a solo builder picking a stack.

### Also noted (not top 3)
- NVIDIA Nemotron 3.5 Super VL and Nemotron 3.5 Bolt open models, plus Cosmos 3.5 and retriever models (Oct 21): https://blogs.nvidia.com/blog/open-models-europe-industry/
- Vercel Labs open-sourced fx, a Zig coding agent built to be embedded (InfoQ, Oct 22): https://www.infoq.com/news/2026/10/vercel-zig-fx-agent/
- Google Cloud Agent Compute Engine, hardware-isolated agent sandboxes, preview in coming months (Oct 22): https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance
- GitHub Next + Microsoft Research PDD Kit research preview: formally verify agent-written Rust via Verus specs (secondary source): https://chiprook.com/s/33690-github-next-unveils-pdd-kit-to-formally-verify-agent-written-rust-code
