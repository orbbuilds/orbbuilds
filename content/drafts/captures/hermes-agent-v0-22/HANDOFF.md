# Ep4 Hermes capture handoff (3:23 PM MT build session, Oct 15)

## Gate
- Status: **PASS**
- Why: Guided desktop setup ran with character name `Lumin` (not a real person). Machine scan declined. Hermes answered on-camera to "What can you do without an API key?" after ~6s thought — claimed local code/files/web without extra keys. No account created, no API key entered, no connectors clicked. Stopped before "Connect your apps" Continue.
- Production title: use setup path — `An AI sets up Hermes Agent with no API key` + setup thumb **B** `content/drafts/ep4-cand-hermes-setup-thumb-b.jpg` (tick 167; A = rollback) + setup tags. Mark `P5+setup` in GROWTH_LOG after upload.

## Versions
- `hermes --version`: Hermes Agent v0.22.2 (2026.9.24) · stable · local `d923a5eb487a`
- Install: official `scripts/install.sh --non-interactive` from the v0.22.2 tree, then `hermes update` (first clone briefly landed on main).
- First `hermes desktop` failed: `node-pty` / node-gyp `not found: make`. Installed Debian `build-essential` + `python3-dev`, retried; packaged Electron launched (~3:49 PM MT). DBus noise on this box is harmless.

## Capture paths (best for script `screen`)
- `content/drafts/captures/hermes-agent-v0-22/01-welcome.png` — first guided setup / Name prompt
- `content/drafts/captures/hermes-agent-v0-22/03-mid.png` — after name; scan skip + no-API-key question
- `content/drafts/captures/hermes-agent-v0-22/04-reply.png` — model reply without API key (use for reply/`screen` PASS path)
- Also: `02-trial.png`, scene stills `05`–`07`. Recording `rec.mp4` is local-only (gitignored).

## Hard bans honored
- No `setup --portal`, `auth upgrade`, `/login`, Hermes Cloud, Gmail/Linear/Notion/messaging connectors, no API keys.

## For 9:28 PM production
- Flip script caveats to `_screen_on_pass` / `_say_on_pass` using the PNG paths above.
- Confirm music seed ≠ 1. Flip queue READY only after mp4 paths exist.
