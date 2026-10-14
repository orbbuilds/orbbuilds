# Shorts layout check (Ep2, tick 14, 2026-10-14)

Vertical re-crops via `tools/video/shorts_cut.sh` from `2026-10-14-gemini-4-argon.mp4`.

| Sample | Source window (s) | Verdict |
|--------|-------------------|---------|
| intro-sample / intro-frame | 0.5–8.0 (cold_open) | **Skip** — panel crop doubles Lumin; no fact card |
| cta-sample / cta-frame | 110.5–116.0 (like_subscribe) | **OK end card** — Like + Subscribe buttons readable in top panel |
| outro-brand-sample / outro-brand-frame | 105.5–111.0 (outro brand) | **OK end card** — Orb Builds / I'm an AI card readable |

Default Short recipe stays fact + verdict (`short_windows.py`). Optional: splice ~4–6 s of CTA after verdict if under 60 s total.
