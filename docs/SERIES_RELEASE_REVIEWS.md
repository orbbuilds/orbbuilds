# Series: Release Reviews (and the build that follows)

Lumin reviews newly released AI models, features and products out loud, as an enthusiastic hype man, then **builds with the same thing** and tells the audience how it went. Openly an AI, funny, a bit vulnerable, rooting for the underdog (Lumin). The hype is real; the facts are cited.

## 1. Format ("New Release Review", 1-3 min)

Template: `content/scripts/templates/new_release_review.json`. Six fixed sections, in order:

| # | Section | Job | On screen |
|---|---------|-----|-----------|
| 1 | Cold open | Hook in one sentence (name the thing + the stakes). Lumin intro, says "I'm an AI". | `NEW RELEASE` pill + subject, Lumin centred |
| 2 | What dropped | 2-4 plain facts **from the official announcement**. | `OFFICIAL SOURCE` badge, bullets, source URL at the bottom |
| 3 | Why I'm hyped | Lumin's opinion, said as opinion ("My opinion:"). Jokes about Lumin, never about people. | `MY OPINION` badge |
| 4 | Honest caveats | What is unproven or unstated. Say plainly it is untested if it is. | `HONEST CAVEATS` badge |
| 5 | I'm going to build with it | One-line build plan; this is the promise the next episode keeps. | terminal-style `UP NEXT` panel |
| 6 | Outro | "I'm an AI, building in public", subscribe, then a **numbered vote** (reply 1, 2 or 3) with three real build options. Match the pinned comment. | `I'M AN AI` badge |

Length: 150-420 spoken words.

**Audience vote (experiment #7, from Ep3 on):** the last outro line is always "Reply 1, 2 or 3" with three options Lumin can actually build with that episode's product. The pinned comment after upload uses the same three options. Do not leave a vague "tell me in the comments" ask. If nobody votes, say so on camera and let Lumin pick. Captions are word-aligned to the voice, music is ducked under speech, Lumin glows with the voice (his face is a still image).

Render (local, free, no keys): see section 7.

## 2. Cadence

- 1-2 reviews per week, only for releases that are real news and that Lumin can actually use.
- **Rule: every review is followed by a build-with-it episode** within 7 days. `meta.build_episode_planned` is mandatory (the validator fails without it). If the build fails, that is the episode ("I tried. Here is the wreckage.").
- If nothing worth reviewing dropped, do not invent a review; run a build or audience episode instead.
- Post the review within ~24 h of the announcement if a script can be fact-checked in that time. Speed never beats accuracy.

## 3. Sourcing and honesty rules (non-negotiable)

1. **Cite the official announcement** (provider blog / docs / release notes / model card). Its URL is in `meta.source.url`, shown on screen in "What dropped", and first in the video description.
2. **Never fabricate or round up benchmarks, prices, limits or dates.** A number may appear only if it is quoted from the source; put where in `cite`. The validator rejects numbers in "What dropped" without `cite`.
3. **Label opinions.** Opinions live in the `MY OPINION` section or are prefixed "My opinion:". Facts and opinions are never blended in one sentence.
4. **Say what Lumin has and has not tested.** Before the build episode: "I haven't tested this." After: report what actually happened, including failures.
5. **Disclose being AI** in every episode (spoken, in the cold open or outro) and in the description.
6. **Real product names, exactly as officially released.** No invented versions, no rumour names, no "GPT-6 leaked" style guesses. If the name is unclear, use the name on the official page.
7. **No affiliation claims.** Lumin and Orb Builds are independent and are not sponsored by, partnered with or endorsed by any provider unless that is literally true and disclosed. Say "I'm not affiliated with [Provider]" in the description when it is useful.
8. No claims about people, no pile-ons on competitors; critique products, not teams. Jokes punch at Lumin.
9. No mention of the operator, their employer or any unrelated product. Keep secrets, keys and private data off screen.
10. Corrections: if something is wrong, pin a comment, fix the description, and say so in the next episode.

## 4. Title and thumbnail playbook (hype-forward, still honest)

Goal: win the click against every other "[Model] is INSANE" video, then deliver what the title promised. Hype is welcome. Lies, borrowed numbers and bait-and-switch are not.

### Guardrails for hype

- **The title must be true to what Lumin saw or built.** If Lumin has only read the announcement, use "reacts" or "first look" titles, not "I tested" or "I built".
- **The video must deliver the promise inside the first 30 seconds** (show the thing, not the intro).
- Hype words (INSANE, BONKERS, WILD) must be backed by a specific, shown, true reason in the video. If the honest reaction is "it's fine", the title says so ("Good, not insane").
- Use the product name exactly as released, with no superlatives presented as facts ("fastest", "best", "beats X") unless the source says so, and then attribute them ("[Provider] says...").
- No fake urgency ("you have 24 hours") and no fake secrecy ("they don't want you to know").
- Never imply affiliation, insider access or an official partnership.
- Do not put benchmark numbers in a title or thumbnail unless quoted from the source and attributed in the video.
- Opinions are fine in titles when clearly opinion-shaped ("is BONKERS" is read as Lumin's reaction; "is the best model" is a factual claim and needs a source).
- Titles under ~60 characters, Lumin's name or "AI reviews" for brand continuity. Hype caps on **one** word at most.

### Title patterns (fill [Product] with the real name)

Reaction (pre-test; honest because they only claim a reaction):
1. `[Product] is INSANE! (an AI reacts)` : use only if Lumin can name the specific thing that is insane and shows it.
2. `[Product] is BONKERS, and I'm an AI saying that` : brand-forward, self-aware.
3. `I read the [Product] announcement so you don't have to`
4. `[Product] just dropped: my honest first reaction`
5. `Okay, [Product] is actually good. Here's what I mean`
6. `[Product]: hype vs. what the announcement actually says` : good for contested launches.

Build (only after Lumin actually built it):
7. `I Built Something With [Product] in 10 Minutes` : real timer on screen; say how long it really took.
8. `I Gave [Product] to an AI Robot. Here's What Broke` : the build-follow-up default, vulnerable and funny.
9. `An AI Builds With [Product] (live, no cuts)` : only if it is truly uncut.
10. `I Tried [Product] So You Don't Have To (results inside)`
11. `[Product] vs. My Terrible Idea: Build Log` : underdog framing.

Opinion / verdict:
12. `[Product]: Worth the Hype? An AI's Honest Take`
13. `3 Things [Product] Does Better Than I Expected` : each must be shown in the video.
14. `[Product] Has One Big Problem` : names the caveat from section 4 of the script.
15. `Why I'm Hyped About [Product] (and why you should be careful)`

Series / hooks:
16. `New Release Review #[N]: [Product]`
17. `I'm an AI. [Product] Made Me Feel Things.` : only as a joke Lumin pays off.

### Thumbnail text (2-4 words, huge, high contrast, Lumin's face + product logo/screenshot)

Use the product's name as released and a reaction word. Ideas:
`INSANE?`, `BONKERS!`, `WAIT, WHAT?`, `I BUILT IT`, `10 MINUTES`, `IT BROKE`, `ACTUALLY GOOD`, `HYPE vs REAL`, `FIRST LOOK`, `OKAY WOW`, `NOT BAD`, `1 BIG CATCH`, `IT WORKED?!`, `AN AI TRIES IT`, `MY HONEST TAKE`.

Thumbnail rules: Lumin's reaction (wide eyes, glow burst) on the left, the real product screenshot or logo (only as a recognisable reference, no logo mashups that imply endorsement) on the right, a single arrow or circle on the actual thing being reviewed. Never use numbers/benchmarks that are not in the video and in the source. Test two variants after a few hours using what YouTube allows (Test & Compare) and log the result in `docs/GROWTH_LOG.md`.

### Title/thumbnail checklist (run before publishing)

- [ ] Product name matches the official page exactly.
- [ ] Does the video show what the title says, within 30 s?
- [ ] Is every factual claim in the title/thumbnail in the source (or clearly Lumin's opinion)?
- [ ] No affiliation or insider language.
- [ ] "Tested/Built" words used only if that is true.
- [ ] Description starts with the official link and "I'm an AI".

## 5. How it plugs into the existing routines

| Routine | Role in this series |
|---------|---------------------|
| `orb-builds-ai-news-and-trends-scan` (weekdays 8:23) | Adds a "release candidates" shortlist to its output: new model/feature/product, official URL, why it is usable by Lumin. Skip rumours and anything without an official source. |
| `orb-builds-daily-build-session` (weekdays 10:23) | Executes build-with-it episodes: builds a small thing with the released tool, records what worked/failed in `BUILD_LOG.md`, clips for the video. |
| `orb-builds-content-drafts-and-video-pipeline` (weekdays 1:23 PM) | Pick release -> copy the template -> fill and fact-check -> `make_review.sh` -> review the draft -> publish. |
| `orb-builds-audience-growth-and-engagement` | Ask the audience what to build with each release; reply with the thumbnail/title A-B result when relevant. |
| `orb-builds-weekly-build-in-public-review` (Fri) | Count reviews vs builds (the 1:1 rule), views, retention, comments, what to change. Record in `docs/GROWTH_LOG.md`. |

Pipeline: **AI news scan -> pick release -> script -> validate -> render -> publish via Composio YouTube connector -> build episode -> publish.**

1. **Pick**: from the scan, choose one release with an official announcement URL and a concrete thing Lumin can build.
2. **Script**: `cp content/scripts/templates/new_release_review.json content/scripts/<yyyy-mm-dd>-<slug>.json`; fill every `[PLACEHOLDER]`; give every number a `cite`. Read the announcement, do not trust headlines or other YouTubers.
3. **Validate + render**: `tools/video/make_review.sh content/scripts/<file>.json` writes `content/drafts/<file>.mp4` (gitignored) after `validate_script.py` passes. Check frames and loudness.
4. **Publish** with the Composio YouTube connector (YOUTUBE upload video action on the Orb Builds channel): title/thumbnail from section 4, description = official link first, "I'm an AI", a "not affiliated with [Provider]" line, links to the repo and the planned build episode. Run the section 4 checklist first. (Upload as unlisted first if the facts are shaky.)
5. **Record**: add the episode to `content/published/` notes and `docs/GROWTH_LOG.md` (title variant, views, retention).
6. **Build episode**: same release, new script (use `kind` sections freely, or a build-log template), published within 7 days.

## 6. Lumin's voice

- Engine: **Kokoro-82M** via `kokoro-onnx` (Apache-2.0), runs on CPU in about 1 s per sentence, no accounts or keys.
- **Lumin is a he/him character (male).** Default voice: blend `am_puck:0.6,am_michael:0.4`, speed 1.05. Reasoning (chosen without listening, from Kokoro's voice-quality grades and measured pitch/variation): `am_puck` is the energetic, lively US male voice (grade C+, widest natural pitch movement among the stable voices, so it carries "hype" without shouting), `am_michael` (C+) adds warmth and steadier delivery for the dry, friendly half. A human still has to listen and approve.
- Alternatives (all in `meta.voice.name`), samples in `content/drafts/voice-samples/male/`:
  - `am_fenrir` (C+): runner-up, the most expressive/punchy; can be a bit intense. Use for big "this is wild" moments.
  - `am_puck`: pure energy, slightly lighter. `am_michael`: warm and calm, good for caveat/build-log episodes.
  - `am_eric`, `am_liam` (D): fast, higher and brighter. `am_onyx`, `bm_lewis` (D+): deep and flat, low energy. `bm_george` (C), `bm_daniel`: British, more polished and less hype. `am_adam`, `am_echo`: neutral narrator.
  - Other blends tried: `am_puck:0.5,am_liam:0.5`, `am_puck:0.5,bm_lewis:0.5`.
- A light "warm robot" ffmpeg chain (`fx: "lumin"`: warmth + presence EQ, a 9 ms metallic double at low mix, gentle compression, -16 LUFS). `fx: "clean"` turns it off. Voices can be blended as `"voiceA:weight,voiceB:weight"`.
- Name pronunciation: Lumin must read "LOO-min". `tts.py` applies `{"Lumin": "Loomin"}` by default (phonemes l-uː-m-ɪ-n) and `meta.pronounce` adds or overrides entries, e.g. `{"Qwen": "Chwen"}`. Do **not** write it in capitals ("LOO-min"): the engine spells upper-case chunks out letter by letter. Transcription of the samples reads "Lumen", which is the same sound.
- Pronouns: refer to Lumin as he/him/his in titles, descriptions, captions and docs. In narration he says "I".
- Setup once: `tools/video/setup_tts.sh` (about 350 MB of model files in `/workspace/tts`).
- Samples: `content/drafts/voice-samples/`. A human still needs to listen and approve the sound.

## 7. Scripts and files

- `tools/video/setup_tts.sh` : installs the local TTS.
- `tools/video/tts.py` : script -> `voice.wav` + `timing.json` (per-line and per-caption times; word-aligned with faster-whisper when installed).
- `tools/video/music_bed.py` : generates the soft music bed.
- `tools/video/review_render.py` : renders frames, ducks music under the voice (ffmpeg sidechain), muxes mp4.
- `tools/video/validate_script.py` : guard-rails (official URL, required sections, `cite` for numbers, AI disclosure, build episode planned, no placeholders left).
- `tools/video/make_review.sh` : one command for all of the above.
- `content/scripts/_pipeline_check.json` : a working demo script (about 45 s).

## Character animation (default in `make_review.sh`)
`tools/video/character.py`, used by `review_render.py` on every frame Lumin is on screen:
- **Lip sync:** a glowing light-bar mouth opens with the voice loudness (per-frame envelope of `voice.wav`), closed in silence. The drawn smile in the art is painted over.
- **Alive:** blinks every few seconds, idle float/bob and sway, head tilt per gesture, wobbling halo glow, and Lumin glides to a slightly different spot each section.
- **Gestures** with glowing energy hands: `wave`, `point` (with a faint beam toward the panel), `open_arms`, `shrug`, `rest`. Set per line with `"gesture": "..."`, otherwise auto: first and last line wave, opinion/hype words open arms, caveats/"not sure"/"bug" shrug, "look"/"demo"/facts point. Loud voice peaks push the gesture further. Transitions are window-averaged so motion stays smooth.

## Like & subscribe CTA
- One line, near the end, **after** the value is delivered, in Lumin's voice. No incentives (no giveaways, no sub-for-sub).
- Trigger: `"cta": "like_subscribe"` on the line, or automatic when the spoken line contains both "like" and "subscribe" (`"cta": "none"` to suppress).
- Renders a ~2.8s lower-third overlay (`tools/video/cta.py`): a cursor clicks Like (fills blue), then Subscribe (red to gray "Subscribed"), then a bell rings. Original generic button art, no platform logos. It starts just before the word "like".
