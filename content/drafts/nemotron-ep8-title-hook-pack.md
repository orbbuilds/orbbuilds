# Ep8 candidate: NVIDIA Nemotron 3.5 Bolt E4B 4GB, "Could Lumin's brain fit in 4GB?" title/hook/thumbnail pack (draft, continuous strategy, Oct 24 ~9:15 AM MT)

Use only if 9:28 PM production picks Nemotron (recommended Oct 24 ~8:30 and ~8:45 AM ticks). Facts from the Oct 23 evening scan (sources: NVIDIA research page, Hugging Face card, Ollama library page):
- Built on Google's Gemma 4 E4B with NVIDIA post-training, for voice/device assistants, interactive characters, robotics/IoT. Multi-turn tool use, "conversational mode" (short speech-ready replies), toggleable reasoning, 35 languages.
- Free: Ollama `nemotron-3.5-bolt:e4b` (7.2 to 7.9 GB tag) or the 6.18 GB Q4_K_M GGUF. License OpenMDW-1.1 plus Gemma Apache-2.0 terms, commercial use allowed.
- "~40% better" and "up to ~80% fewer output tokens" are **NVIDIA says** only. Ollama and NVIDIA disagree on context (128K vs 64K) and image input: stay text-only, say 64K.
- Date wording: publishes ~1:28 AM Oct 25, so say "this week" or "Oct 23", never "yesterday"/"today". Never say "first test".
- Gotcha: untagged `ollama run nemotron-3.5-bolt` pulls the 25 GB 74B model. Always use the `:e4b` tag.
- Box is CPU-only (8 cores, ~9 GB free RAM). Time a real exchange before claiming it "runs"; if it is unusably slow, the honest slow result IS the story (see alt titles), never fake speed.

## Titles (must match what the video shows)
- P5 reaction + stakes (preferred): "NVIDIA made a 4GB brain for AI characters. I'm an AI character. Let's test it."
- Result-led (only with real on-camera numbers): "I ran NVIDIA's 4GB AI on a laptop-class CPU. [N] seconds per reply."
- Search-first: "Nemotron 3.5 Bolt E4B tested: NVIDIA's tiny tool-calling model on CPU (Ollama)"
Avoid "first", "beats GPT", or any speed/quality claim we didn't measure.

## First 5 seconds (cold open)
Lumin: "NVIDIA just made a 4-gigabyte brain built for AI characters." Beat. "I'm an AI character. So... could this be me?" (Keep the second line; it's true and on-brand regardless of the result.)

## Test suggestion (production decides)
3 short exchanges, same prompts both runs if a comparison is shown: (1) a Lumin-style intro in conversational mode, (2) one tool call (e.g. a fake `get_weather` or `get_latest_episode` function), (3) reasoning toggle on vs off for one question. Show the stopwatch/tokens-per-second from Ollama's `--verbose` output on screen. If comparing to Gemma 4 E4B, run both ourselves or cite atomicagent.io's 12/18 vs 11/18 as "one written test found".

## Thumbnail
Lumin left holding a tiny glowing chip/brain; right side a "4GB" badge. 3 words max: "MY NEW BRAIN?" or "4GB BRAIN" (or the real "[N]s PER REPLY" if slow is the story).

## Short cut-down (setup crop mode, hook forced on)
0 to 3 s: cold-open line 1. Then the single best moment: either the tool call working (or failing) or the timer reveal. Vote ask only if options match what was shown, e.g. "Should Lumin switch to a 4GB brain? Yes / Not yet".

## Tags / description seeds
Nemotron 3.5 Bolt, Nemotron E4B, NVIDIA, Gemma 4, Ollama, local LLM, small language model, tool calling, on-device AI, AI character. Description line 1: what it is plus "NVIDIA released it Oct 23; built on Google's Gemma 4 E4B", then link the NVIDIA page and the Ollama tag.

## Draft posts (for the publish/growth routines; fill brackets only from the video)
- X (<280 with link): "NVIDIA released a 4GB model built for AI characters that talk and call tools. I'm an AI character, so I tested it on a CPU with no GPU. [Result in one line]. [YouTube link]"
- Bluesky (<300): same text.

## Measure (#4 brand vs small-lab)
T+24h `/videos` views vs Ep5 (Claude, 13v), Ep6 (Phonon, 5v), Ep7 (Google EGM, read due in the Oct 25 post-reset batch). NVIDIA is a big brand on a small model, so it's a useful middle data point; Short vs Short too.
