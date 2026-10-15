# Queue: Ep4 Hermes Agent v0.22 for 2026-10-16 slot (PENDING_RENDER)

> Drafted by audience-strategy tick 89 (Oct 15 ~5:05 AM MT) so the 3:23 PM build + 9:28 PM production inherit every standing hygiene step. **Do not upload from this file until Status is READY** and the render paths below are filled. Prefer Candidate A from `content/drafts/ep4-p5-openly-ai-title-pack.md` (P5). Swap to P5+setup title/thumb **only** if the tick-61 title gate passes (desktop `nous/welcome` trial or local model answering, no account). Do not overwrite Ep2 (`2026-10-15.md`) or Ep3 (`2026-10-15-ultramarine-1-flash.md`).
- Standing rules: `00-README-slot-rules.md` in this folder.
- Oct 16 recovery / three-way rank: `content/drafts/2026-10-16-publish-recovery.md` (Ep3 first-mover open → Ep4 Hermes closed → Ep2 Argon).

- Status: **PENDING_RENDER** (no script/mp4 yet as of tick 89). Production fills paths → flips READY. If it cannot render tonight, leave PENDING; do not invent READY.
- Episode: RR-004 / Episode 4 (daily)
- Script: content/scripts/2026-10-15-hermes-agent-v0-22.json (create at render; title/description/tags in meta)
- Title (default until setup gate): `I asked Hermes Agent if it's replacing me` (42 chars; alts in pack)
- Title (if setup gate passes): `An AI sets up Hermes Agent with no API key` (47 chars) — note `P5+setup` in GROWTH_LOG
- title_pattern: **P5** (keep after upload; log 24h/72h views in GROWTH_LOG under #4; if setup path, still P5 but mark `P5+setup`)
- GA: 2026-10-14 03:21 UTC (GitHub v0.22.0) = **Oct 13 9:21 PM MT** (tick 75 slot rule 2b — do not read date-only as newer than Ep3)
- First-mover: **closed** (BoxminingAI Hermes v0.22 recap already up, tick 60). Tier (b) under slot rule 2b → ranks behind Ep3 while Ep3 First-mover stays open.
- Upload file: (fill after render) content/drafts/2026-10-15-hermes-agent-v0-22-upload.mp4
- Full render: (fill) content/drafts/2026-10-15-hermes-agent-v0-22.mp4
- Thumbnail default: **content/drafts/ep4-cand-hermes-agent-thumb.jpg** (`REPLACING` / `ME?`, hl 2, tag `AI host · not tested yet`)
- Thumbnail if setup gate: **content/drafts/ep4-cand-hermes-setup-thumb.jpg** (`NO API KEY` / `SETUP`, hl 1, tag `AI host · tested on camera`) — already rendered tick 64
- categoryId 28, privacyStatus public
- Tags (default): `Hermes Agent review`, `Hermes Agent`, `Nous Research`, `AI agent desktop`, `local AI agent`. Hashtags: `#AI #Agents #OpenSource`.
- Tags if setup gate: also `Hermes Agent setup`, `Hermes Agent local LLM` + a `Setup` chapter ≥10 s.
- Description: product-first line 1 from pack + chapters from timing.json + honesty lines + **footer** from `content/drafts/description-footer.md` (Previous = newest live review that night: Ep3 if up, else Ep1 `L7fdRoNWEPE`; skip playlist line on first night if playlist not created yet). Do **NOT** pass `containsSyntheticMedia` (tick 49).
- Cold open (#16): fill sourced `show` chips — preferred `600 PLUGINS · ~2,520 CONTRIBUTORS · NO API KEY` (tick 56); frame-check 1/3/5/8 s; fallback `600 PLUGINS · NO API KEY` if chip collides.
- Build captures (#20 / tick 87): if the 3:23 PM session records Hermes desktop frames, wire them via the script `screen` line field (repo-relative path). No-`screen` frames stay unchanged. Do not invent screenshots.
- Music (#20 / tick 85): confirm `video-build/<slug>/music.wav` came from a **non-1** seed (seed from script name in `make_review.sh`). Log seed in episode notes.
- Facts from Nous GitHub v0.22.0 release notes only. Allowed: "a third smaller" (Nous claim). Forbidden: AICoder 34%/LOC. Not affiliated.

- Short file: (fill after post_render) `…-hermes-agent-v0-22-short.mp4` + `…-short-meta.json` (CTA end card via `post_render.sh`). Paste full-episode URL. Never burn Short before older CARRIED mains (Ep3, then Ep2).

- Channel SEO (#11, APPROVED): after main succeeds, apply once per night if not already done. Add this videoId to "AI Release Reviews" playlist. ~50 units — never before main.

- Site listing (#12): draft after videoId exists (mirror `ep3-site-listing.md`). Do not list before public.

- Vote (#7): outro + `YOUTUBE_POST_COMMENT` from pack Candidate A vote block (or setup-gate rewrite if used). Pin needs a person.

- Growth handoff (not this routine): morning playbook stays **Neither** until a videoId exists; after Ep3/Ep2 land, prefer their packs first. Ep4 social only after Ep3 U-drop budget is spent (X graduated-access cap).

- **Call order in the post-reset window (#13 / #7):** same as slot rules. On a three-way night: (1) Ep3 main → (2) Ep3 thumb → (3) stats batch → (4) Ep3 vote → (5) SEO/playlist if units → (6) Ep4 main only if quota remains after Ep3 (+ Ep2 preferred before Shorts per recovery draft: Ep3 → Ep4 → Ep2) → Shorts last. **Prefer Ep2 main before Ep4 Short.** If only one upload is reliable, Ep3 wins; Ep4 and Ep2 carry.

- Build-session runbook (ticks 61–62, not this routine): Linux = from-source Electron via `hermes desktop`; trial once per OS user — record first launch; no `setup --portal` / `auth upgrade` / `/login` / connectors without parent OK. Free-path-only until operator picks a build budget (#20).
