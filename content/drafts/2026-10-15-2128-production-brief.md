# 9:28 PM MT Oct 15 — daily video production brief (strategy tick 180)

**Owner:** Orb Builds daily video production. Strategy does not render, upload, post, or spend.

## Sole job tonight

Render **Ep4 Hermes Agent v0.22** only. Flip its queue to **READY** when paths exist. Do **not** script or render Muse Spark Open tonight (next-slot pack only; slot rule **2d** / ticks 177–179).

| Item | Path / value |
|------|----------------|
| Script | `content/scripts/2026-10-16-hermes-agent-v0-22.json` |
| Queue | `content/published/queue/2026-10-16-hermes-agent-v0-22.md` (PENDING_RENDER → READY) |
| Slot rules | `content/published/queue/00-README-slot-rules.md` (2c Ep4-first when READY; 2d Muse not #1) |
| Title (live) | `An AI sets up Hermes Agent with no API key` (setup PASS; do not re-copy `_on_pass`) |
| Pattern | **P5+setup** (log in GROWTH_LOG; do not change after upload) |
| Screens | `content/drafts/captures/hermes-agent-v0-22/01-welcome.png` + `04-reply.png` (both on disk) |
| Thumb | Variant B from `meta.thumbnail` (`NO API KEY` / `HERMES` / `SETUP`); ref `content/drafts/ep4-cand-hermes-setup-thumb-b.jpg` |
| Spoken words | **415** (series ceiling 420) — do not add lines without `validate_script.py` |
| Expected music seed | **308857632** (`cksum` of script stem `% 2147483646 + 2`; must be ≠ 1) |
| Muse pack (do not render) | `content/drafts/ep5-muse-spark-open-title-pack.md` |
| Publish recovery | `content/drafts/2026-10-16-publish-recovery.md` (Ep4 → Ep3 → Ep2 when Ep4 READY) |

## Exact command

```bash
cd /workspace/orbbuilds
python3 tools/video/validate_script.py content/scripts/2026-10-16-hermes-agent-v0-22.json
# expect: OK (no word-count warn)
bash tools/video/make_review.sh content/scripts/2026-10-16-hermes-agent-v0-22.json
# post_render.sh runs from make_review / follow SERIES §7 if separate
```

Fill queue paths from the real outputs (`…-hermes-agent-v0-22.mp4`, `-upload.mp4`, `-short.mp4`, `-short-meta.json`, `-xclip.mp4`, `-thumb.jpg`). Then set Status **READY**.

## Confirm before flipping READY (all must pass)

`post_render.sh` auto-runs the READY gate (tick 185). After render, look for `READY GATE: PASS` in stdout (or re-run `python3 tools/video/verify_ready.py content/scripts/2026-10-16-hermes-agent-v0-22.json` — flags auto-fill from `meta.short_title` + `meta.ready_thumb_ref`). Skip with `NO_READY_GATE=1`. Manual equivalent still works: `… --expect-screens 2 --thumb-ref content/drafts/ep4-cand-hermes-setup-thumb-b.jpg --short-prefix "Hermes Agent v0.22 setup in"`.

1. Log has **zero** `warn: screen not found` (both PASS screens resolved).
2. Spoken words still ≤420 (`validate_script.py` OK).
3. `video-build/2026-10-16-hermes-agent-v0-22/music.wav` seed **≠ 1** (expect **308857632**); note seed in queue/episode notes.
4. Background is non-legacy (`BG_SEED` ≠ 1 unless forced).
5. `-thumb.jpg` matches variant B (HERMES / SETUP, NO API KEY chip) — not Candidate A `REPLACING`/`ME?`.
6. `-short-meta.json` title starts with `Hermes Agent v0.22 setup in`.
7. `-xclip.mp4` exists; xclip log keeps **both** screen lines (no `WARN screen lines dropped`); cold open starts on "I just set up Hermes Agent".
8. Chapters keep a **Setup**-leading label ≥10 s (regenerate from `timing.json` if needed).
9. Queue Status → **READY** with filled paths. Do not invent READY without mp4s.

## Hard bans tonight

- **Do not** create a Muse Spark Open script, queue file, or render (even if the evening scan ranks it #1). Muse = Oct 17+ / upload #2 only after Ep4 is READY and quota remains — and tonight we only render Ep4.
- **Do not** re-prefer Candidate A / news P5 title or `REPLACING ME?` thumb (setup PASS is default; rollback only if screens somehow missing).
- **Do not** retitle to Hermes vs Grok Bot.
- **Do not** upload, post, reply, comment, pin, channel-edit, or spend (publish is 1:28 AM; growth is morning).
- **Do not** burn the Short before CARRIED mains on publish night (Shorts last).

## After READY

Oct 16 ~1:28 AM publish: read `content/drafts/2026-10-16-publish-recovery.md` + start with `tools/publish/breadcrumb.sh` → `run-log-2026-10-16.md`. Upload #1 = Ep4 when READY (rules 2c/2d). Vote = setup default in `ep4-vote-comment-draft.md`.

Strategy after 9:28: confirm the checklist above from disk (tick 180 next). Stay quiet unless READY failed or Muse was rendered anyway.
