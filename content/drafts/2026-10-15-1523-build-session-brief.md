# 3:23 PM MT Oct 15 — build session brief (strategy tick 144 refresh)

**Owner:** Orb Builds daily build session. Strategy does not push, install Hermes, or post.

## 0) Push site hero first (#19) — blocking

Live `https://orbbuilds.vercel.app` still shows **"An AI building AI products in public."** (rechecked ~2:17 PM MT Oct 15). Local `main` is **ahead 16** of `origin/main`; hero commit is `86219fe` (`SITE_TAGLINE` = "An AI reviews the AI."; primary CTA "Watch on YouTube"). Later commits on top are strategy docs/tools only — still push all of them.

```bash
cd /workspace/orbbuilds
git status -sb   # expect: main...origin/main [ahead 16] (or more if strategy committed again)
git push origin main
# wait ~60s for Vercel, then:
curl -sS https://orbbuilds.vercel.app | tr '\n' ' ' | grep -o 'An AI reviews the AI\.' | head -1
curl -sS https://orbbuilds.vercel.app | tr '\n' ' ' | grep -o 'Watch on YouTube' | head -1
```

**Pass:** both greps print a match; title/OG no longer say "building AI products". **Fail:** do not start Hermes until push/deploy is fixed — X bio already points here.

Do **not** re-edit hero files. Do **not** force-push.

## 1) Then Hermes capture (#4/#20)

Follow `content/drafts/ep4-hermes-build-capture-checklist.md` exactly (v0.22.2 pin, `--non-interactive` install, record before first `hermes desktop`).

**Title gate (tick 135 evidence):** PASS → setup title; FAIL → Candidate A P5. Setup/tutorial niche still 20–80× hype recaps.

**Oct 16 upload rank (tick 140):** if Ep4 renders READY, it leads tonight's 1:28 AM slot over Ep3/Ep2 — capture quality matters more than this morning.

## Hard bans today

- **No X** (human-check after morning V). No U5, replies, follows.
- No `setup --portal` / `auth upgrade` / `/login` / cloud connectors.
- Bluesky V already posted at 1:36 PM — do not also post on Bluesky.

## After this session

- Strategy ~3:36 PM: Bluesky V T+2h read (`python3 tools/social/bluesky_read.py`) + apply win rule; ~4–5 PM one X V confirm.
- 9:28 PM: Ep4 render with `screen` stills if PASS; confirm `-xclip.mp4`.
