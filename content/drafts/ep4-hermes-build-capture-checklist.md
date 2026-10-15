# Ep4 Hermes build-session capture checklist (for 3:23 PM MT Oct 15)

One ordered playbook for the daily build routine. Sources: ticks 61–62, 64, 87, 91 +
`content/published/queue/2026-10-16-hermes-agent-v0-22.md`. Do not skip the record-first rule —
the `nous/welcome` trial is **once per OS user** on this shared box.

## Goal
Reach the desktop guided setup on `nous/welcome` (or a local model answering) with **no account**,
capture stills for the review `screen` field, and leave a clear pass/fail note for the 9:28 PM render.

## Title gate (what production may claim)
- **P5+setup** title `An AI sets up Hermes Agent with no API key` + setup thumb + setup tags:
  only if guided chat on `nous/welcome` appeared, or a local model answered, with no account created.
- Else keep Candidate A (`I asked Hermes Agent if it's replacing me`, default thumb, no setup tags).
- Honest failure on camera is fine **only if it really happened** and was recorded.

## Hard bans (no parent OK)
`setup --portal`, `auth upgrade`, `/login`, Hermes Cloud sign-in, connecting Gmail/Linear/Notion or any messaging channel.

## Ordered steps
1. **Preflight (Shell, no GUI launch yet)**  
   - Confirm `tools/video/capture.sh` exists and display is `:2` (or set `CAPTURE_DISPLAY`).  
   - Do **not** test-launch `hermes desktop` first.  
   - **Box state (tick 132, Oct 15 ~12:20 PM MT):** still fresh for the one-shot trial — no `~/.hermes`, `hermes` not on PATH; `node` v20.19.2 + `npm` 9.2.0 + `gcc` 14.2 + `libatomic1` present; `DISPLAY=:2` and `/tmp/.X11-unix/X2` up; `tools/video/capture.sh` present. Public YouTube RSS still **Neither** (Ep0 `aCvkp11w9_8` 6 views / Ep1 `L7fdRoNWEPE` 9 views). Re-check `ls ~/.hermes` + `command -v hermes` at session start; if either exists, stop and ask — the trial may already be burned.
2. **CLI install first (OK before recording — trial is desktop-only)**  
   - **Version pin (tick 130; reconfirmed tick 132):** latest GitHub release is still **v0.22.2** (published 2026-10-15 08:21 UTC). Never capture on 0.22.1 (wrong-commit build). Log `hermes --version` in the capture notes.  
   - Use **`--non-interactive`** so the installer skips `setup` / gateway prompts. An interactive install that configures a provider/key before the first desktop launch kills the "no provider" trial path.  
   - Paste-ready (do **not** add `--include-desktop` here — build desktop later under the recorder so the first GUI launch is on camera):
     ```bash
     curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --non-interactive
     source ~/.bashrc   # or open a fresh shell so ~/.local/bin is on PATH
     hermes --version   # must show 0.22.2 (or hermes update / reinstall if not)
     ```
   - Hard bans still apply after install: no `hermes setup`, `hermes setup --portal`, `hermes model`, `auth upgrade`, `/login`, or connectors before the first `hermes desktop`.
3. **Start recording before first desktop launch**  
   ```bash
   tools/video/capture.sh start hermes-agent-v0-22
   ```
4. **Desktop launch (computerUse drives the GUI)**  
   - Linux has **no** packaged Desktop download (macOS/Windows only). After CLI install:
     ```bash
     hermes desktop
     ```
     That builds Electron from source on first run (~114 MB download; budget real minutes). Optional rebuild: `hermes desktop --build-only --force-build`. If the Electron download stalls, docs allow `ELECTRON_MIRROR`.  
   - Fresh desktop install is required for the guided `nous/welcome` chat; existing/remote backends skip it. CLI/TUI get **no** free trial model.
5. **Stills at key moments** (labels become filenames under `content/drafts/captures/hermes-agent-v0-22/`):  
   ```bash
   tools/video/capture.sh still hermes-agent-v0-22 welcome   # guided chat / first screen
   tools/video/capture.sh still hermes-agent-v0-22 trial     # nous/welcome or equivalent
   tools/video/capture.sh still hermes-agent-v0-22 reply     # model answering (if it does)
   tools/video/capture.sh still hermes-agent-v0-22 fail      # if key-ask / error instead
   ```
6. **Stop + extract scene stills**  
   ```bash
   tools/video/capture.sh stop hermes-agent-v0-22
   tools/video/capture.sh stills hermes-agent-v0-22 6
   ```
7. **Write the handoff note** (append to the Ep4 queue or a short note the 9:28 PM run can read):  
   - Gate: **PASS** / **FAIL** / **PARTIAL** (one line why).  
   - Paths of 1–3 best PNGs for script `screen` (repo-relative).  
   - Do not invent screenshots if capture failed.

## Script skeleton (tick 99)
Production starts from `content/scripts/2026-10-16-hermes-agent-v0-22.json` (PENDING_BUILD).
- Cold-open `show` already filled: `600 PLUGINS · ~2,520 CONTRIBUTORS · NO API KEY` (re-verified on GitHub API this tick).
- Caveat line 2 has `_screen_on_pass` / `_screen_on_fail` / `_say_on_*` keys — production swaps them into real `screen`/`say` after this handoff.
- Still label → intended slot: `welcome`/`trial`/`reply` → PASS path; `fail` → FAIL path.
- Default title stays Candidate A until gate PASS.

## After a PASS (for 9:28 PM production, not this build session)
- Prefer setup title + `ep4-cand-hermes-setup-thumb.jpg`.  
- Cold-open `show`: `600 PLUGINS · ~2,520 CONTRIBUTORS · NO API KEY` (tick 56; sourced).  
- Wire `screen` on the matching script lines to the PNG paths above.  
- Confirm music seed ≠ 1 and background is non-legacy (`BG_SEED`).  
- Flip queue Status → READY only after mp4 paths exist.

## Measure later (#4 / #20)
24h/72h views for P5 vs P5+setup vs Ep1 baseline in GROWTH_LOG. No claim until those rows exist.
