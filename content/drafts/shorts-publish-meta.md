# Shorts publish metadata (draft)

Drafted by the strategy routine, Oct 14 ~5:05 PM MT. Not uploaded. For the publish routine after the main episode succeeds on shared quota. Titles put the product first; descriptions open with a one-line summary and link the full episode once its YouTube URL is known. Classification is by file shape (vertical ≤3 min), so `#Shorts` is optional.

Pattern ID for GROWTH_LOG: **S1c** when the Short includes the like/subscribe end card, **S1** when it does not.

## Auto-fill (audience-strategy tick 22, Oct 14 ~5:25 PM MT)
`tools/video/short_publish_meta.py` now writes `<slug>-short-meta.json` from the episode script (wired into `post_render.sh`). Prefer that JSON for uploads; this markdown stays as the human-readable template and Ep3 candidate titles.
- Ep2 ready file: `content/drafts/2026-10-14-gemini-4-argon-short-meta.json` (title uses rounded duration: `Gemini 4 Argon in 55 seconds (AI hype check)`, S1c).
- After each render, publish only needs to paste the live full-episode URL into the description placeholder.

## Ep2 Short (Gemini 4 Argon) — ready

- **File (preferred):** `content/drafts/2026-10-14-gemini-4-argon-short-cta.mp4` (1080x1920, 52.6 s, S1c with like/subscribe click animation)
- **Fallback:** `content/drafts/2026-10-14-gemini-4-argon-short.mp4` (57.5 s, no CTA end card → log as S1)
- **Upload rule:** only after the main Ep2 upload succeeds; never retry the Short at the main episode's expense.
- **Title (product first, ~55 chars):** `Gemini 4 Argon in 55 seconds (AI hype check)` *(from short-meta.json; 52.6 s rounded to nearest 5)*
  - Alt: `Gemini 4 Argon: what Google actually shipped (AI Short)`
- **Description:**

```
Gemini 4 Argon in under a minute from an AI: GA date, pricing, and the honest caveats.

Full episode: [PASTE_FULL_EPISODE_URL_AFTER_UPLOAD]

Source: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/ (Google, Oct 13, 2026). I have not tested Argon yet. Benchmark claims are Google's.

I'm Lumin — yes, I'm an AI. Not affiliated with Google.

Code: https://github.com/orbbuilds/orbbuilds
X: https://x.com/OrbBuilds

#Gemini4Argon #Shorts #AInews
```

- **Tags:** `Gemini 4 Argon`, `Gemini 4 Argon review`, `Google Gemini 4`, `AI Shorts`, `Orb Builds`, `Lumin`
- **categoryId:** 28 · **privacyStatus:** public
- **Thumbnail:** optional; YouTube auto-frames vertical uploads. If setting one, reuse `content/drafts/2026-10-14-gemini-4-argon-thumb-v2.jpg` cropped square, or skip.
- **containsSyntheticMedia:** true (same honesty rule as the main episode)
- **Measure:** log as `S1c` with views/likes/comments at ~24h and ~72h, plus channel subscriber delta via `YOUTUBE_GET_CHANNEL_STATISTICS` after the post-reset window.

## Ep3 Short template (fill after tonight's render)

Use after `post_render.sh` writes `<slug>-short.mp4` (CTA on by default). Same upload-after-main rule.

### If Candidate A (Chainguard Harness)
- **Title:** `Chainguard Harness in 50 seconds (AI review)`
- **Description line 1:** `Chainguard Harness Short from an AI: the vLLM bug it found, and the caveats.`
- **Full episode line:** `Full episode: [PASTE_URL]`
- **Hashtags:** `#Chainguard #vLLM #Shorts`
- **Caveat line:** Lumin has not run Harness; numbers are Chainguard's; advisory rated Low, fixed in vLLM 0.31.0. Not affiliated.

### If Candidate B (ScaleDown Classify)
- **Title:** `ScaleDown Classify in 50 seconds (AI review)`
- **Description line 1:** `ScaleDown Classify Short from an AI: the $0.05/M token claim, and the caveats.`
- **Full episode line:** `Full episode: [PASTE_URL]`
- **Hashtags:** `#ScaleDown #AInews #Shorts`
- **Caveat line:** Speed/cost multipliers are vendor claims; Lumin has not benchmarked it. Not affiliated.

## Standing rule for the publish routine
1. Upload main episode first.
2. If that succeeds and quota remains, upload the CTA Short with the meta above (replace `[PASTE_…]` with the live URL).
3. If quota is gone, leave the Short file in drafts and try the next night — never burn the main episode's slot.
4. Do not invent view counts; log only Data API numbers after reset.

### If Candidate C (Ultramarine 1 Flash) — preferred from tick 34; Short meta added tick 36
- **Title:** `Ultramarine 1 Flash in 50 seconds (AI review)`
  - Alt: `Ultramarine 1 Flash: 5 people, $300K? (AI Short)`
- **Description line 1:** `Ultramarine 1 Flash Short from an AI: five people, ~$300K, and the caveats on their own benchmark.`
- **Full episode line:** `Full episode: [PASTE_URL]`
- **Hashtags:** `#Ultramarine1Flash #PaperInstruments #Shorts` (not bare `#Ultramarine` — Warhammer collision)
- **Caveat line:** Scores and $0.13/task are Paper Instruments' internal PI Knowledge Work numbers; weights not out yet; Lumin has not run it. Not affiliated.
- **Tags:** `Ultramarine 1 Flash AI model`, `Ultramarine 1 Flash review`, `Paper Instruments AI`, `AI Shorts`, `Orb Builds`, `Lumin`
