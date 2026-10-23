# Ep6 candidate: Phonon voice-swap test, title/hook/thumbnail pack (draft, tick 292, Oct 22 ~9:15 AM MT)

Use only if the evening scan / 9:28 PM production picks Phonon. Facts to keep straight (see AUDIENCE_STRATEGY.md ticks 289 and 291):
build on `phonon-31m-en` (Apache 2.0) only, male voices Easton/Micah vs Lumin's Kokoro `am_fenrir`,
verdict from our own ears and CPU timings, never Gradium's benchmark numbers.

## Titles (pick one; all must match what the video actually shows)
- P5-style (reaction + stakes, preferred): "A new AI voice wants to replace mine. I tested it."
- Underdog: "I let a 31M-parameter model try to steal my voice"
- Search-first: "Phonon vs Kokoro: I swapped my own AI voice (on-device TTS test)"
Avoid "beats ElevenLabs"/"best TTS" claims; we test one pipeline, ours.

## First 5 seconds (cold open)
Line 1 in a Phonon male voice (Easton), no intro: "This isn't my voice. Or is it?"
Hard cut to Lumin in `am_fenrir`: "That was a model that came out yesterday. Today it auditions for my job."

## Thumbnail
Lumin left, two waveforms right labelled "ME" and "NEW ME?". 3 words max on image: "REPLACE MY VOICE?"

## Short cut-down (setup crop mode, hook forced on)
0 to 3 s: the two-voice cold open. Then the same line read three times (fenrir, Easton, Micah) with on-screen "Which one is real?" and a vote ask in the pinned comment (vote options must exactly match the voices heard; see tick 171 lesson).

## Tags / description seeds
Phonon, Gradium, Kokoro TTS, on-device TTS, open source text to speech, AI voice test, AI host. Description line 1 states the license choice (31M Apache 2.0; 40M is non-commercial, not used).

## Measure (#4)
T+7h and T+24h `/videos` views vs Ep5 (3 at T+7.4h). Hypothesis: test-on-ourselves beats reaction-only at 24h.

## Runtime labeling rule (tick 352, Oct 22 ~7:10 PM MT)
- Any on-screen or spoken speed number must name the runtime that produced it: "PyTorch on CPU (transformers, phonon-31m-en)" for the primary path, or "browser WASM (phonon-tts npm)" if the fallback was used. Never mix numbers from the two in one comparison.
- Kokoro comparison timings must come from the same box and the same runtime class in the same session; otherwise say "not a like-for-like test".
- Outside numbers: micdrop's latency table only as "one Node test found"; quality/WER only as "Gradium says".
