# Queue: Ep4 Hermes Agent v0.22 for 2026-10-16 slot (PENDING_RENDER)

> Drafted by audience-strategy tick 89 (Oct 15 ~5:05 AM MT); **PASS flip applied tick 158 / header honesty tick 172**. **Do not upload from this file until Status is READY** and the render paths below are filled. **Default = setup PASS** (`An AI sets up Hermes Agent with no API key`, setup thumb B, setup tags, setup Short title). Candidate A / news P5 from `content/drafts/ep4-p5-openly-ai-title-pack.md` is **rollback only** if Status somehow reverts to FAIL. Do not overwrite Ep2 (`2026-10-15.md`) or Ep3 (`2026-10-15-ultramarine-1-flash.md`).
- Standing rules: `00-README-slot-rules.md` in this folder.
- Oct 16 recovery / three-way rank: `content/drafts/2026-10-16-publish-recovery.md` (**tick 140: Ep4 Hermes is upload #1 when READY** on live demand ~20–50× Ultramarine; then Ep3, then Ep2).

- Status: **PENDING_RENDER** (script PASS-flipped tick 158; no mp4 yet). Production renders → fills paths → flips READY. If it cannot render tonight, leave PENDING; do not invent READY.

- **Title gate (3:23 PM MT Oct 15 build):** **PASS** — see `content/drafts/captures/hermes-agent-v0-22/HANDOFF.md`. Use setup title/thumb/tags. Status remains PENDING_RENDER until mp4s exist.
- **PASS flip APPLIED (strategy tick 158, ~4:45 PM MT):** live script already has setup `publish_title` / thumb / `publish_description` / setup tags / caveats `say`+`show`+`screen` (`01-welcome.png`, `04-reply.png`) / `short_title` with `{secs}` (auto-filled by `short_publish_meta.py` from the real Short duration, tick 159). 9:28 PM: **do not re-copy** `_on_pass` fields. Render → confirm zero `warn: screen not found` → confirm `-short-meta.json` title starts `Hermes Agent v0.22 setup in` → regenerate chapter stamps → flip READY.

- Script (PASS-flipped tick 158): `content/scripts/2026-10-16-hermes-agent-v0-22.json` — setup title/screens live in meta; still PENDING_RENDER until mp4 exists. Do not treat as READY.
- Episode: RR-004 / Episode 4 (daily)
- Script: content/scripts/2026-10-16-hermes-agent-v0-22.json (title/description/tags in meta; tick 113 fixed stale 2026-10-15 path — outputs are named from the script basename)
- Title (**PASS / setup, applied tick 158**): `An AI sets up Hermes Agent with no API key` (P5+setup). Default Candidate A kept only under `_title_gate.default`.
- Title (if setup gate passes): `An AI sets up Hermes Agent with no API key` (47 chars) — note `P5+setup` in GROWTH_LOG
- title_pattern: **P5** (keep after upload; log 24h/72h views in GROWTH_LOG under #4; if setup path, still P5 but mark `P5+setup`)
- GA: 2026-10-14 03:21 UTC (GitHub v0.22.0) = **Oct 13 9:21 PM MT** (tick 75 slot rule 2b — do not read date-only as newer than Ep3)
- First-mover: **closed** (BoxminingAI Hermes v0.22 recap already up, tick 60). Tier (b) under slot rule 2b → ranks behind Ep3 on freshest GA (Ep3 first-mover also **closed** tick 108; Ep3 still #1 by GA date Oct 14). **Overridden by slot rule 2c (tick 140/168): when this file is READY it is upload #1 on live demand; the GA-only rank above applies only as a tie-break if demand data is ever missing.**
- Upload file: (fill after render) content/drafts/2026-10-16-hermes-agent-v0-22-upload.mp4
- Full render: (fill) content/drafts/2026-10-16-hermes-agent-v0-22.mp4
- Thumbnail (**PASS / setup B, tick 167**; was setup A tick 158/161): post_render renders it from `meta.thumbnail` (`NO API KEY` chip / `HERMES` / `SETUP`, hl 1, tag `AI host · tested on camera`); reference file **content/drafts/ep4-cand-hermes-setup-thumb-b.jpg**, also copied to `public/episodes/rr-004.jpg`. Setup A (`HERMES AGENT` chip / `NO API KEY` / `SETUP`) = rollback in `meta._thumbnail_pre_tick167`. Reason: A's product chip was unreadable at 168x94.
- Thumbnail FAIL/rollback only: **content/drafts/ep4-cand-hermes-agent-thumb.jpg** (`REPLACING` / `ME?`, hl 2, tag `AI host · not tested yet`)
- categoryId 28, privacyStatus public
- Tags (**PASS / setup default, live in script meta**, ticks 158/163/172): `Hermes Agent review`, `Hermes Agent`, `Hermes Agent v0.22`, `Hermes Agent update`, `Nous Research`, `AI agent desktop`, `local AI agent`, `Hermes Agent setup`, `Hermes Agent desktop`, `Hermes Agent tutorial`, `Hermes Agent free` (tick 156 qualifies), `Hermes Agent local LLM` + a `Setup`-leading chapter ≥10 s. Hashtags: `#AI #Agents #OpenSource`.
- Tags FAIL/rollback only: drop the setup/tutorial/free/desktop/local-LLM extras; keep the news set above without claiming on-camera setup.
- Description: product-first line 1 from pack + chapters from timing.json + honesty lines + **footer** from `content/drafts/description-footer.md` (Previous = newest live review that night: Ep3 if up, else Ep1 `L7fdRoNWEPE`; skip playlist line on first night if playlist not created yet). Do **NOT** pass `containsSyntheticMedia` (tick 49).
- Cold open (#16): fill sourced `show` chips — preferred `600 PLUGINS · ~2,520 CONTRIBUTORS · NO API KEY` (tick 56); frame-check 1/3/5/8 s; fallback `600 PLUGINS · NO API KEY` if chip collides.
- Build captures (#20 / tick 87): if the 3:23 PM session records Hermes desktop frames, wire them via the script `screen` line field (repo-relative path). No-`screen` frames stay unchanged. Do not invent screenshots. Capture with `tools/video/capture.sh` (tick 91): `start hermes-agent-v0-22` before the first `hermes desktop` launch, `still hermes-agent-v0-22 <label>` at key moments, `stop` + `stills` after; files land in `content/drafts/captures/hermes-agent-v0-22/NN-<label>.png`.
- Music (#20 / tick 85): confirm `video-build/<slug>/music.wav` came from a **non-1** seed (seed from script name in `make_review.sh`). Log seed in episode notes.
- Facts from Nous GitHub v0.22.0 release notes only. Allowed: "a third smaller" (Nous claim). Forbidden: AICoder 34%/LOC. Not affiliated.

- Short file: (fill after post_render) `…-hermes-agent-v0-22-short.mp4` + `…-short-meta.json` (CTA end card via `post_render.sh`). Paste full-episode URL. Never burn Short before older CARRIED mains (Ep3, then Ep2). Short title (**PASS default**, ticks 159/172): live `meta.short_title` = `Hermes Agent v0.22 setup in {secs} seconds (no API key)` — `{secs}` auto-fills from the real Short duration. Confirm `-short-meta.json` starts with `Hermes Agent v0.22 setup in`. FAIL/rollback only: unset `short_title` so the generator falls back to news via `short_product`.

- Channel SEO (#11, APPROVED): after main succeeds, apply once per night if not already done. Add this videoId to "AI Release Reviews" playlist. ~50 units — never before main.

- Site listing (#12): `content/drafts/ep4-site-listing.md` + `public/episodes/rr-004.jpg` (**setup thumb + setup title default**, tick 161). Do not list before public.

- Vote (#7): outro + `YOUTUBE_POST_COMMENT` from `content/drafts/ep4-vote-comment-draft.md` (**setup PASS block is default**, tick 160; Candidate A = rollback only). Pin needs a person.

- Growth handoff (not this routine): `content/drafts/ep4-post-publish-growth-pack.md` (**setup PASS defaults**, ticks 160–161). Oct 16 morning playbook: **`content/drafts/2026-10-16-morning-growth-playbook.md`** (tick 173; Ep4 setup primary). Legacy note in `2026-10-15-morning-growth-playbook.md` tick-160. Site listing: `ep4-site-listing.md` setup-primary (tick 161). Neither until a videoId exists.

- **Call order in the post-reset window (#13 / #7) — tick 156 fix:** the old three-way order below is **superseded** by tick 140 (`content/drafts/2026-10-16-publish-recovery.md` line 15). When this file is READY: (1) **Ep4 main** → (2) Ep4 setup thumb → (3) stats batch → (4) Ep4 vote → (5) SEO/playlist if units → (6) Ep3 main only if quota remains → Ep2 → Shorts last. If only one upload is reliable, **Ep4 wins**. Use the old order only if this file is NOT READY at run start.
  - (Superseded, pre-tick-140:) On a three-way night: (1) Ep3 main → (2) Ep3 thumb → (3) stats batch → (4) Ep3 vote → (5) SEO/playlist if units → (6) Ep4 main only if quota remains after Ep3 (+ Ep2 preferred before Shorts per recovery draft: Ep3 → Ep4 → Ep2) → Shorts last. **Prefer Ep2 main before Ep4 Short.** If only one upload is reliable, Ep3 wins; Ep4 and Ep2 carry.

- Build-session runbook (ticks 61–62 + **tick 92 checklist**, not this routine): follow `content/drafts/ep4-hermes-build-capture-checklist.md` (record first with `capture.sh`, stills, gate PASS/FAIL note). Linux = from-source Electron via `hermes desktop`; trial once per OS user; no `setup --portal` / `auth upgrade` / `/login` / connectors without parent OK. Free-path-only until operator picks a build budget (#20).
- Length (tick 117, Oct 15): 420 spoken words, on the 150-420 series limit. Title-gate swaps are shorter, so no trim needed; if the build session adds lines, keep `validate_script.py` free of the >420 warning.
