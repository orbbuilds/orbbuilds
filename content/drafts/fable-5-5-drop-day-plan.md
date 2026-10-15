# Claude Fable 5.5: drop-day plan (experiments #3/#4/#17, tick 100, Oct 15 ~6:55 AM MT)

> **Pre-cutoff check (tick 150, Oct 15 ~3:15 PM MT):** models page still 5.1 only; `"Fable 5.5"` X counts cooling (11 AM 166, 12 PM 118, 1 PM 118, 2 PM 106, 3 PM ~124/hr pace). NOT announced; Hermes stays tonight's Ep4.

> **Launch signal (tick 127, Oct 15 ~11:31 AM MT):** rumor plateaued at ~140–185 `"Fable 5.5"` X posts/hr (4–11 AM MT); models overview still 5.1. Trigger this plan only on a `claude-fable-5-5` models-page row or counts ~500+/hr. Reference: Ultramarine launch peaked 99/hr.

Drafts and rules only. Nothing here is posted or uploaded. Status at writing: **NOT announced.** Last official recheck: tick 105, Oct 15 ~7:42 AM MT — still NOT announced.

## Evidence (read-only, tick 105 ~7:42 AM MT Oct 15) — still NOT announced
- Anthropic [models overview](https://platform.claude.com/docs/en/models/overview) (WebFetch ~7:42 AM MT): lineup is Fable **5.1**, Opus 5.5, Sonnet 5.5, Haiku 5.5. API ID `claude-fable-5-1` only; no `claude-fable-5-5` row, no Fable 5.5 pricing.
- Anthropic newsroom (WebSearch ~7:42 AM MT): recent "Introducing" posts are Opus/Sonnet/Haiku 5.5 (Sep 2026). No Fable 5.5 newsroom post.
- X recent counts for `"Fable 5.5" OR "fable 5.5" OR "claude-onigiri"` (includes RTs): MT hours **4–5 AM 128**, **5–6 AM 160**, **6–7 AM 191**, **7:00–7:42 AM already 120** (~171/hr pace). Theo @theo "If Anthropic actually drops Fable 5.5 today…" ~**146K** impressions. Still all rumor (codename chatter, "drops today", "next week") — no official source.
- Public YouTube RSS for Orb Builds (~7:42 AM MT): still only Ep0 `aCvkp11w9_8` (6 views) + Ep1 `L7fdRoNWEPE` (9 views). No morning Ep3 retry landed.
- Ultramarine X→YouTube review links still **0** (first-mover open for Ep3).

## Evidence (read-only, ~6:52 AM MT Oct 15)
- Anthropic's [models overview](https://platform.claude.com/docs/en/models/overview) (curl, ~6:53 AM MT): `claude-fable-5-1` is the newest Fable (34 mentions), `claude-fable-5-5` appears 0 times.
- X post counts for `"Fable 5.5" -is:retweet` (recent counts API): ~23-32/hour overnight, then **86** (4-5 AM MT), **96** (5-6 AM MT), **108** in the first 51 min of 6 AM MT. Chatter is "dropping today" rumor plus an MLflow/Azure catalog row that copies 5.1 pricing ($10/$50) with an Oct 14 date. No official source.
- Rumor volume tripled in 3 hours. That is not proof of a launch, but it is the biggest pending AI release in our window, and the first YouTube review of a top-tier Anthropic model would have far more search demand than Hermes (first-mover already closed) or Ultramarine.

## How a run decides it is real (all from official pages only)
Real = an Anthropic newsroom/product-announcement post naming Fable 5.5 **and** a `claude-fable-5-5` row on the models overview. A catalog row, LiteLLM/MLflow entry, leak, or someone's screenshot is NOT enough.

## If it is real before ~6 PM MT today (production at 9:28 PM)
- Tonight's Ep4 slot goes to Fable 5.5 (queue file `content/published/queue/2026-10-16-claude-fable-5-5.md`, `GA:` with the announcement's UTC time, `First-mover: open` until a YouTube review with the model name exists). Hermes keeps its PENDING_BUILD script and becomes CARRIED; Ep2 Argon likely goes STALE (already expected per tick 97).
- Ranking under slot rule 2b already puts an open first-mover above Ep3 only if its GA is fresher; Fable 5.5 would be freshest, so Oct 16 1:28 AM order becomes Fable 5.5, then Ep3, then Ep4 Hermes. One upload a night means Ep3's own first-mover window is the cost; say so in the queue file.
- Title pattern P1 (product + one sourced number/claim), thumbnail P6. Hook facts come only from the launch post, system card and rate card, with `show` chips citing them. No benchmark we didn't read on an official page; no "beats GPT-x" unless Anthropic's post says it with a number.
- Hands-on: real API calls cost money and the build-budget decision (#20) is still with the user; until it's approved, the episode is a review of the official materials, and the title must not say "I tested".
- If it lands after ~6 PM MT: still try tonight if the script can be sourced in time; otherwise Oct 17, and mark it in the queue, don't rush unsourced claims.

## If it is still not announced
- Nothing changes; Hermes stays Ep4. Re-check at the 8:23 AM and 7:23 PM scans (official pages only). WakeParent from those scans **only** if the newsroom + models-page gate both pass (see "How a run decides it is real" above).

## X (for the growth routine; still max one original per ~4h)
- **Do not use bank U3** today (its "treat it as not released" framing can flip within hours). Replacement U3b below is safe only while the models page still shows 5.1; re-check right before posting and drop it the moment 5.5 is announced.
- **Neither-branch priority (tick 105):** if Ep3 is still not live at the 11:23 AM growth session, the session's **one** X original is the #22 native-video post (`…-xclip.mp4` + paste-ready caption in the morning playbook). **Do not also post U3b** the same session (tick-71 spacing: max one original per ~4h). U3b is the fallback only if native video is skipped (file missing / attach fails). Same rule on Bluesky: video wins; skip Welcome/U1/U3b that day if the clip goes out.
- U3b (~266 chars with link as 23); fill [TIME] from the models-page recheck right before paste:
  > Seeing "Fable 5.5 drops today"? As of [TIME] MT, Anthropic's models page still lists claude-fable-5-1 as the newest Fable. A real launch brings a newsroom post, a new model ID, a rate card and a system card. Until those appear, it's a rumor.
  > platform.claude.com/docs/en/models/overview
- If it is announced: no hot take on X before the episode exists; the episode drop post (U-shape, one sourced fact) is the post. Native-video Neither branch still applies until Ep3 is live; do not pivot the clip caption to Fable.
