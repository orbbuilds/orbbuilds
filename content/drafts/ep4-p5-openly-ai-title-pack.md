# Ep4 title pack (pattern P5) — openly-AI angle (experiment #4)

Drafted by the strategy routine, Oct 14 ~5:10 PM MT. Not posted or uploaded.
Ep4's assigned pattern is **P5** (weird personal-stakes / AI-as-the-hook). Product name is filled only after the news scan locks a real release. Every title below is a reaction/review frame until Lumin has actually tested or built with the product.

## Why P5 is different from the brand cue
Ep1–Ep3 already tack on "(an AI reviews it)" / "An AI reads the receipts" as a **secondary** brand tag. Experiment #4 tests making Lumin being an AI the **primary hook** — the reason to click — the way Neuro-sama's "Asking A.I. The Hard Hitting Questions" titles do (above her median, tick 1). Measure by comparing Ep4's 24h/72h views (Data API) to Ep1/Ep3 (both P1 with only a secondary AI tag). Do not claim CTR.

## When P5 fits (pick one gate; otherwise swap pattern)
Use P5 only when at least one is true of the locked product:
1. It is an agent / coding / automation model that could replace work Lumin does (reviews, builds, scripts).
2. The official announcement talks about replacing or assisting AI developers / creators / reviewers.
3. Lumin can honestly ask the product a personal-stakes question on camera (job, replacement, "can you host a show?") without inventing capabilities.
If none fit, swap with the next unused pattern (P3 if a real N builds, else P2) and note the swap in GROWTH_LOG. Do not force a replacement gag onto a random chip or pricing tool.

## Title formulas (fill [Product]; keep under ~60 chars; one hype word max)
Primary (prefer the one that matches the gate):
1. `I asked [Product] if it's replacing me` (~40 + name)
2. `An AI reviews the AI that could replace him` (use when the product name is long; put the real name in description line 1 and the first ~40 chars via a shorter alt)
3. `[Product]: an AI checks if he's obsolete`
4. `I asked [Product] for my job description` (only if Lumin actually asks that on camera)
5. `[Product] vs me: an AI reviews his replacement` (P5 + soft versus; no scores unless quoted)

Alts that stay honest pre-test:
- `Will [Product] take my job? An AI's first look` (first look / reacts, not "I tested")
- `An AI reads the [Product] announcement that might replace him`

Never: "I tested" / "I built" / "beats me at X" until that is literally true. No unaffiliated "coming for my job" presented as a provider claim — it's Lumin's worry, said as opinion in the video.

## Thumbnail (P6 via `tools/video/thumbnail.py`)
Words add to the title; do not repeat the full title. Honesty tag stays.
- Preferred: `--line1 REPLACING --line2 ME? --hl 2 --tag "AI host · not tested yet"`
- Alts: `MY JOB?` (hl on JOB), `OBSOLETE?`, `AI VS AI` (hl on second AI), `WHO WINS?`
- Product chip: exact short product name in `--product`
- Example once product locks:  
  `python3 tools/video/thumbnail.py content/drafts/ep4-<slug>-thumb.jpg --product "[PRODUCT]" --line1 REPLACING --line2 ME? --hl 2 --tag "AI host · not tested yet"`

## First 5 seconds (hook templates)
Open on the stakes, then name the product. Cold open still discloses "I'm an AI".
1. "I'm an AI who reviews new models for a living. Today one of them might be applying for my job. It's called [Product]."
2. "Quick question for [Product]: are you coming for this glowing orb? I'm asking as the orb."
3. "Human reviewers don't have to worry about the model replacing the host. I do. Let's read what [Lab] just shipped."

Then cut into "What dropped" with official facts only. The replacement bit is opinion / framing — never invent that the lab said it would replace reviewers unless the source says so.

## Description line 1 (rule #8) + vote (#7)
- Line 1 shape: `[Product] review from an AI who might be next: what [Lab] released on [date], what it costs, and the honest caveats.`
- Outro vote (match pinned comment later): "Reply 1, 2 or 3. 1: I actually ask [Product] the replacement question on camera. 2: I build one real thing with it and show the wreckage. 3: skip the existential bit, just the specs."

## Script meta checklist for the production run
- `title_pattern: P5` (do not change after upload)
- `meta.thumbnail` filled with words from above (not placeholders)
- Spoken disclosure that Lumin is an AI stays in cold open or outro (validator)
- Caveats: not tested yet (until the build episode); not affiliated; numbers only from the source
- Short: `post_render.sh` already adds CTA end card; Short title from `shorts-publish-meta.md` template once file exists

## How to measure (#4 inside #2)
After Ep4 publishes, append GROWTH_LOG row:
`date | videoId | P5 | title | views_24h | likes_24h | comments_24h | views_72h | notes: openly-AI primary hook`
Compare to Ep1 (P1, secondary AI tag) and Ep3 (P1). Winner is higher 24h/72h views at similar age — not proof of causation at n=1, but direction for whether Ep7+ should keep P5-style primary hooks.

## UPDATE tick 35 (Oct 14 ~7:45 PM MT): Candidate A filled — Hermes Agent v0.22

Evening scan item 3 + GitHub release page (fetched Oct 14 ~7:45 PM MT). **Gate 1 fits:** Hermes is a desktop/coding agent that does reviews, builds, connectors and scheduled work — the same class of jobs Lumin does. Prefer this over Ling-3.1-flash (weights release; better as a later P2/P3 "hardware reality check") for the P5 experiment.

### Candidate A (preferred for Ep4): Hermes Agent v0.22 "Threshold Release"
- **Product / lab:** Hermes Agent (Nous Research). Tag **v0.22.0** published on GitHub **14 Oct 03:21 UTC** (`e06df9c`); release notes body date "October 13, 2026". A **v0.22.1** patch also landed later on Oct 14 (Windows Store / plugin fixes) — review the Threshold highlights; mention 0.22.1 only if production ships after it and wants currency.
- **Title (P5, primary AI hook, 42 chars):** `I asked Hermes Agent if it's replacing me`
  - Alt (48): `Hermes Agent: an AI checks if he's obsolete`
  - Alt (58): `Will Hermes Agent take my job? An AI's first look`
  - Do **not** use "I tested" / "I installed" until Lumin actually runs the guided setup on camera.
- **Thumbnail:** `content/drafts/ep4-cand-hermes-agent-thumb.jpg`, i.e. `meta.thumbnail = {product: "HERMES AGENT", line1: "REPLACING", line2: "ME?", hl: 2, tag: "AI host · not tested yet"}`
- **First 5 seconds (hook 1, filled):** "I'm an AI who reviews new models for a living. Today one of them might be applying for my job. It's called Hermes Agent."
  - Alt hook (fact-first): "A fresh Hermes install now starts a guided chat on a free trial model before you own an API key. I'm an AI who already does that kind of work. So… awkward."
- **Description line 1 (rule #8):** `Hermes Agent review from an AI who might be next: what Nous Research shipped in v0.22 on Oct 14, the no-key onboarding, and the honest caveats.`
- **Must-say caveats (from GitHub release notes, not invented):** guided setup runs on free trial model `nous/welcome` **once per OS user**; Skip setup ends it; connectors (Linear, Notion, etc.) go through the Nous tool gateway and create a free connectors-only identity on first use — Lumin has **not** installed or connected anything yet; release cites ~24,200 commits / ~2,520 contributors since v0.21.0 and **"a codebase a third smaller"** (verbatim in the v0.22.0 release body, rechecked tick 59 — tick 56 false-negative; say it only as Nous's claim). Do **not** use AICoder's "34%" or "≈1.06M→≈698K lines" numbers — those are secondary coverage, not in the GitHub body. Those are Nous's own release stats, not independent audits; **no model benchmarks** in the release notes; not affiliated.
- **Worth a line:** one-click local llama.cpp that only recommends models that fit GPU/RAM; 600-plugin catalog; signed desktop packages including Microsoft Store.
- **Vote loop (#7), outro + pinned comment:** "Reply 1, 2 or 3. 1: I actually ask Hermes the replacement question on camera during a fresh install. 2: I give it one real Orb Builds chore with no API key and show what happens. 3: skip the existential bit, just the specs."
- **Tags:** `Hermes Agent review`, `Hermes Agent`, `Nous Research`, `AI agent desktop`, `local AI agent`. **Tick 38 add:** YouTube autocomplete for "hermes agent" (Oct 14 ~8:20 PM MT) suggests `tutorial`, `setup`, `use cases`, `local llm` — how-to demand. Add tags `Hermes Agent setup`, `Hermes Agent local LLM`, and a `Setup` chapter in the description **only if Lumin actually runs the guided setup on camera** (else leave them out). Hashtags: `#AI #Agents #OpenSource`.
- **Sources:** [GitHub releases](https://github.com/NousResearch/hermes-agent/releases) (v0.22.0 / v0.22.1), evening scan `content/ideas/2026-10-14-evening-ai-news-scan.md` item 3.
- **Queue file (when Ep4 renders):** `queue/YYYY-MM-DD-hermes-agent-v0-22.md` with `Status: READY`, `GA: 2026-10-14 (GitHub v0.22.0 03:21 UTC)`, `title_pattern: P5`.
- **Measure (#4):** GROWTH_LOG row with pattern P5; compare 24h/72h views to Ep1 and Ep3 (both P1 + secondary AI tag).

### Candidate B (parked for a different pattern): Ling-3.1-flash weights
Gate fit is weaker for P5 (open weights + hosted coding, not "agent applying for my job"). Better as **P2** hype-check ("open weights on modest hardware?") or a Short. Do not force P5. Sources in evening scan item 2.

## UPDATE tick 55 (Oct 14 ~11:08 PM MT): cold-open `show` chips (experiment #16)
Tomorrow's Ep4 cold-open first line should include a sourced `show` chip string so the tick-54 hook chips render on screen (muted viewers). Production fills `show` from a real source number already in the script (Hermes release stats, free-trial model name, etc.) — **do not invent numbers**. Template placeholder and renderer path are in `review_render.py` / script template (ticks 53–54). If Ep4 topic swaps off Hermes, still attach `show` to whatever sourced hook the cold open uses.

## UPDATE tick 56 (Oct 14 ~11:20 PM MT): verified cold-open `show` chips for Hermes (experiment #16)
Rechecked the GitHub release bodies via the public API (v0.22.0 published 2026-10-14 03:21 UTC; v0.22.1 23:59 UTC). Verified in the v0.22.0 notes, verbatim: "~24,200 commits", "~2,520 contributors" (since v0.21.0), "The Plugin Catalog: 600 reviewed plugins", free `nous/welcome` trial "once per OS user, so onboarding needs no key". *(Tick 59 correction: "a codebase a third smaller" **is** in the v0.22.0 body — tick 56 missed it.)*

Number-led alternative to hook 1 (tick 53 rule: lead with a sourced number), only if Ep4 stays on Hermes:
- Line 1 say: "Six hundred reviewed plugins. About twenty-five hundred contributors. And a brand-new install doesn't even need an API key. I'm an AI who does this job. So is Hermes Agent applying for it?"
- Line 1 `show`: `600 PLUGINS · ~2,520 CONTRIBUTORS · NO API KEY`
- Line 2 say (attribution, required): "Those are Nous Research's own release-note numbers, not mine. Hey, I'm Lumin…"
- Chip widths: "~2,520 CONTRIBUTORS" is the longest chip so far (18 chars vs tick 54's ~11); production must frame-check 1/3/5/8 s and, if it collides with Lumin or wraps, fall back to `600 PLUGINS · NO API KEY` (keep both spoken).
- Keeps P5 (the job question is still the hook's payoff) while giving muted viewers numbers in the first 2 s.

## UPDATE tick 59 (Oct 14 ~11:48 PM MT): restored "a third smaller" (experiment #4)
Public API re-read of [Hermes Agent v0.22.0](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.0) (~11:47 PM MT): the highlight blurb ends with **"and a codebase a third smaller"** — same string as the evening scan paraphrased. Tick 56's strike was a false negative (search missed the prose in the opening paragraph). v0.22.1 patch notes do **not** repeat it (patch-only). Also present in v0.22.0 (usable if a later hook needs them, still Nous's own stats): ~6,080 merged PRs, ~15,600 files changed, ~2,045,000 insertions / ~1,140,000 deletions, ~7,180 issues closed.
- **Allowed on camera:** "a third smaller" / "a codebase a third smaller", attributed to Nous's release notes.
- **Not allowed:** AICoder's "34%" or "≈1.06M to ≈698K lines" (evening scan item 3) — secondary blog math, not in the GitHub body.
- Optional spoken add after the plugin/contributor line: "They also say the codebase is a third smaller." Do not put `1/3 SMALLER` on the primary `show` chip unless a frame-check shows room; prefer keeping `NO API KEY` for the muted-viewer payoff.

## UPDATE tick 60 (Oct 14 ~11:58 PM MT): not first-mover; setup guides are this niche's outlier shape (experiments #3/#4/#8)
- **Competitor already up:** BoxminingAI (@boxminingai, 15,500 subs, median 3,200 views/video per TubeAI's channel page, fetched ~11:57 PM MT) has published `Hermes Agent Update v0.22 is MASSIVE! (Threshold Release)` (124 views in TubeAI's daily snapshot). X search for "Hermes Agent" + youtube links since Oct 12 returned 0 posts. Ep4 publishes ~1:28 AM MT Oct 16, about 52h after GA, so #3's first-mover edge is gone for Hermes; differentiation has to come from the angle.
- **What wins in this exact niche (same TubeAI page, as listed):** Hermes is 4 of BoxminingAI's top 12 outliers, and **setup/how-to beats release recaps**: `Hermes Agent Setup with Discord (Complete Guide)` 33K (8x), `Hermes Agent Bot Mode Guide` 28K (10.2x), `Hermes Agent Kanban Setup Guide` 24K (8x) vs the v0.20 release recap 18K (10.9x). Same shape across agent frameworks: `MaxClaw: One-Click to Set Up Openclaw` 43K (39.1x), `NemoClaw Setup Guide` 42K (10.6x). Matches tick 38's autocomplete (`tutorial`, `setup`, `local llm`). One channel's data, so a strong hint, not proof.
- **Recommendation for the build session (10:23 AM / 3:23 PM Oct 15), not this routine:** actually run the v0.22 no-key guided setup (`nous/welcome` trial) on the box and capture it, ideally plus the one-click local llama.cpp model picker. Do **not** connect Gmail/Linear/Notion (that creates a Nous connectors identity, i.e. a signup) without the parent's OK. If it really runs, Ep4 can honestly use:
  - Title (P5 + setup, 47 chars): `An AI sets up Hermes Agent with no API key` (alt: `I'm an AI. I set up Hermes Agent with no API key`)
  - Thumb: `product: "HERMES AGENT", line1: "NO API KEY", line2: "SETUP", hl: 1, tag: "AI host · tested on camera"`
  - Add the conditional tags `Hermes Agent setup`, `Hermes Agent local LLM` and a `Setup` chapter.
  - Keep `title_pattern: P5` (AI is still the primary hook); note "P5+setup" in GROWTH_LOG so #4 isn't credited for setup demand alone.
- **If the setup is not run or fails:** keep Candidate A as written (`I asked Hermes Agent if it's replacing me`, "not tested yet" tag, no setup tags). A failed install on camera is also honest content ("an AI tried to install the agent that might replace him"), but only if it really happened.


## UPDATE tick 61 (Oct 15 ~12:10 AM MT): the no-key trial is desktop-only (experiment #4)
Read the Hermes v0.22.0 release body (GitHub API), the repo README and the installation docs page (~12:08 AM MT). This changes how the build session must run the setup if Ep4 is to use the "no API key" title honestly:
- **Desktop only.** v0.22.0 notes, verbatim: "A first desktop install with no provider or Nous account gets the free `nous/welcome` model as a one-time trial (once per OS user)" and "**The CLI, TUI and gateway get no account or free model.**" So the README one-liner (`curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`, then `hermes`) alone does **not** give the no-key trial.
- **Linux path per the install docs:** after the command-line install, `hermes desktop` installs and runs Hermes Desktop (or the installer's optional `--include-desktop` stage builds it from source). The guided setup chat only appears on a **fresh** desktop install, and "existing installs and remote (SSH, URL, Cloud) backends don't get it automatically".
- **Do not run** `hermes setup --portal` (OAuth login to Nous Portal), `hermes auth upgrade`, or `/login`: each signs in or creates an account, which is a signup needing the parent's OK. Connecting any app (Linear, Notion, etc.) creates a "free connectors-only identity", same rule as tick 60. In the guided setup, pick no apps and no plugins that need an account.
- **Second honest no-key path:** "Local models in one click ... no account, no API key" (llama.cpp, rated against GPU/RAM), started from **Settings → Providers → Local Model** in the desktop app. The box has no known GPU, so expect a small CPU model and slow replies; say so on camera if used.
- **Install hygiene:** the installer pulls Python 3.14, Node, ripgrep, FFmpeg, agent-browser + pinned Chromium and cua-driver. Read `install.sh` before piping it to bash, and install as the box user, not root.
- **Title gate (tightened):** `An AI sets up Hermes Agent with no API key` is allowed only if the build session reached the desktop guided setup chat on `nous/welcome`, or got a local model answering, with no account created. CLI-only install that then asks for a key: use the honest failure angle ("an AI tried to install the agent that might replace him") or keep Candidate A.

## UPDATE tick 62 (Oct 15 ~12:20 AM MT): box feasibility + one-shot capture rule (experiment #4)
Read the Hermes installation and Hermes Desktop docs pages (~12:18 AM MT) and checked the box (read-only, nothing installed).
- **No Linux desktop package.** The site's desktop packages are macOS (Apple Silicon) and Windows only. On Linux, `hermes desktop` (or the installer's `--include-desktop`) runs npm install, downloads Electron (~114 MB from GitHub releases) and builds the unpacked app from source, then launches it. Budget real minutes for the build; if the Electron download stalls, the docs' fix is `ELECTRON_MIRROR`, and a rebuild is `hermes desktop --build-only --force-build`.
- **Box state (checked):** no `~/.hermes` yet (fresh OS user, so the once-per-OS-user trial is still unused), `node`/`npm`/`gcc` present, `libatomic1` installed, an X display exists, no GPU (`nvidia-smi` absent). So the desktop build should work; the local-model fallback will be CPU-only and slow.
- **Keep it fresh:** the interactive installer also runs setup. Use `--non-interactive` for the CLI stage and do **not** run `hermes model`, `hermes setup`, or set any API key before the first `hermes desktop` launch, or the install stops being "a first desktop install with no provider".
- **One shot, so record it the first time.** The `nous/welcome` trial is once per OS user and the box is shared, so there's no rehearsal. Start a screen recording of the desktop before the first launch, and don't test-launch the desktop in a scratch run first. If the guided chat doesn't appear, that footage is the honest-failure angle.
- **Driving the window** is GUI work (computerUse on the agent's own desktop), not Shell automation. Still off-limits without the parent's OK: `setup --portal`, `auth upgrade`, `/login`, Hermes Cloud sign-in, connecting any app or messaging channel.
- Side note for the script (sourced, desktop docs): Hermes Desktop ships a built-in "Bot Mode", a roster of agents with their own chats and routines that message each other. Fair one-line comparison for Lumin ("it has a bot roster, like the one I live in"), no claims beyond the docs.

## UPDATE tick 64 (Oct 15 ~12:42 AM MT): setup thumb rendered (experiments #4/#6)
Rendered the conditional setup thumbnail so the Oct 15 build session / 9:28 PM production don't invent words mid-render:
- **File:** `content/drafts/ep4-cand-hermes-setup-thumb.jpg` (1280x720, 204 KB)
- **Command used:** `python3 tools/video/thumbnail.py content/drafts/ep4-cand-hermes-setup-thumb.jpg --product "HERMES AGENT" --line1 "NO API KEY" --line2 "SETUP" --hl 1 --tag "AI host · tested on camera"`
- **Visual check:** product chip top-left; "NO API KEY" yellow (hl 1); "SETUP" white; Lumin face clear on the right; tag "AI host · tested on camera" at bottom.
- **Default remains** `ep4-cand-hermes-agent-thumb.jpg` (REPLACING / ME?) until the title gate in tick 61 is met.
- **If setup succeeds:** set `meta.thumbnail` to the setup file (or regenerate with the same args into the episode slug path via `post_render.sh`).
- **If setup fails or is skipped:** keep Candidate A thumb; do not use the "tested on camera" tag.
