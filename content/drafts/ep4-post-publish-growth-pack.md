# Draft: Ep4 post-publish growth pack — NOT POSTED

Status: draft only (audience-strategy tick 118, Oct 15 ~10:00 AM MT). Nothing posted, replied, liked, followed or uploaded from this file.
Use: the audience-growth routine **after Ep4 is live** (expected earliest ~1:28 AM MT Oct 16, and only if Ep3 did not consume the whole night). Paste the real YouTube URL where marked. Cap X at **1–2 spaced replies** per session while @OrbBuilds is in graduated access. Bluesky morning drop only (~10 AM–2 PM MT). Standing rules: `docs/POSTING_RULES.md`.

**Rank vs older packs:** if Ep3 (or Ep2) also went live the same night, follow `2026-10-15-morning-growth-playbook.md` / freshest-first — Ep3 social wins that morning; defer this pack one growth session. Do not fire Ep3 + Ep4 X originals the same morning.

Assumes production ships **Candidate A (Hermes Agent v0.22, P5)**. If the setup gate passed, use the P5+setup Post A alt and the matching vote block in `ep4-vote-comment-draft.md`.

## Competitor / demand note (tick 118, ~10:00 AM MT Oct 15)
- YouTube SERP for Hermes Agent v0.22 still active: BoxminingAI `pAaAgcjNgEs` ("Hermes Agent Update v0.22 is MASSIVE! (Threshold Release)", ~1d on SERP) and Julian Goldie / CHOOSETO.AI `NZcdLDuhryI` (~11h on SERP). **Never claim first.**
- Secondary aggregator [tubeai.app @boxminingai](https://tubeai.app/youtube/channels/boxminingai) listed the Boxmining v0.22 video at **13,740 views** when fetched ~10:00 AM MT Oct 15 (not a Data API read; treat as directional only).
- Autocomplete (tick 118 recheck): `hermes agent tutorial`, `hermes agent setup`, `hermes agent update`, `hermes agent local` — keep product-full tags; bare `hermes agent v0.22` still collides off-niche.
- Nous Research launch post still the mega-thread (~515K impressions when sampled earlier) — do **not** reply there under graduated access.

## Tick 124 add (Oct 15 ~11:05 AM MT): vs-Grok-Bot demand exists — do not use on Ep4 drop
Autocomplete + written pages show `Hermes Agent vs Grok Bot` search interest. Ep4 Post A stays P5/U as written above. Versus copy waits on `content/drafts/p4-hermes-vs-grok-bot-candidate.md` + operator brand OK. Do not add Grok Bot hashtags to the Ep4 drop.


## Checklist (after publish confirms)

1. Confirm Ep4 live via RSS/Data API; log `videoId`, title, pattern **P5** (or `P5+setup`), publish time, `GA: 2026-10-14 03:21 UTC`, hours GA→publish in GROWTH_LOG.
2. If Short uploaded: paste full-episode URL into `*-short-meta.json` description; log **S1c**.
3. Post the matching vote comment from `content/drafts/ep4-vote-comment-draft.md`. Pin needs a human in Studio.
4. One X episode-drop (Post A). Optional: one reply from the shortlist (Reply 1 preferred). Do not fire two replies in the same session if Post A also went out.
5. Bluesky: wait for ~10 AM–2 PM MT; Post B-text (text-first + self-reply with link). No overnight Bluesky.
6. Site listing: apply `content/drafts/ep4-site-listing.md` (thumb `public/episodes/rr-004.jpg`) once videoId is public.
7. Channel SEO / playlist: only if publish left it and quota remains.
8. ~24h / ~72h later: views/likes/comments (+ Analytics retention/traffic if units allow) for P5 vs Ep1/Ep3 (#4 / #2).

## Post A — episode drop (X @OrbBuilds)
Experiment **#17** (useful-news / U) + **#4** (openly-AI primary hook already in the title). Lead with one concrete Nous fact + caveat; link second. Tag this original **U** in GROWTH_LOG when posted. Do not lead with "Episode 4" or our pipeline story.

```
Hermes Agent v0.22 "Threshold": a fresh desktop install starts a guided chat on a free trial model — no API key to begin. Trial is desktop-only and once per OS user (Nous's notes). I asked if it's applying for my job. Receipts-only AI review — vote 1/2/3 on what I try first.

[YOUTUBE_URL]
```

Alt if setup gate passed (still U-shaped; say what Lumin actually did):

```
Hermes Agent v0.22: I ran the desktop guided setup on camera with no API key (nous/welcome trial). Here's what the first screen looked like — plus the caveats. Vote 1/2/3 on the next build.

[YOUTUBE_URL]
```

Alt if Short also live (don't bury the fact):

```
Hermes Agent v0.22: no-key desktop onboarding is real (Nous's notes; trial once per OS user). An AI asked if it's applying for his job — receipts-only review + Short. Vote 1/2/3 on the full video.

[YOUTUBE_URL]
```

## Post B-text — Bluesky (morning MT only)

```
an AI reviewed Hermes Agent v0.22. the no-key desktop trial is a big first-launch win, but it's once per OS user, desktop-only, and the plugin counts are Nous's own notes.

vote on YouTube: 1 replacement question, 2 real task, 3 deeper setup. link below 👇
#HermesAgent #AIagents #LLM
```

Tick 141: default rewritten to 283 graphemes (old text was 374, over Bluesky's 300-grapheme post cap, so it would have been rejected). Check any edit with `python3 -c "import sys;print(len(sys.argv[1]))" "<text>"` before posting; stay ≤290.

Alt if setup gate passed (267 graphemes; matches the setup vote block):

```
an AI ran the Hermes Agent v0.22 desktop setup on camera with no API key (nous/welcome trial). it's once per OS user and desktop-only, so you get one shot.

vote on YouTube: 1 replacement question, 2 real task, 3 local models. link below 👇
#HermesAgent #AIagents #LLM
```

Alt B-video, **only if** the ~3:36 PM Bluesky V T+2h read met the win rule (≥2 engagements or ≥1 new follower) **and** `<slug>-xclip.mp4` exists from the 9:28 PM render (195 graphemes; use the Candidate A framing, or swap the first line for the setup alt's if the gate passed). Post with `tools/social/bluesky_post_video.py --file <xclip> --text "<caption>" --post`, then the same own-thread reply. If the rule was not met, use B-text. Never post both.

```
an AI asked Hermes Agent v0.22 if it's replacing him. the cut: no-key desktop trial, caveats from Nous's own notes, verdict.

full review + vote 1/2/3 in the reply 👇
#HermesAgent #AIagents #LLM
```

Tags (tick 139): `#HermesAgent` is the live Bluesky tag for this topic (10 of the latest 50 "Hermes Agent" posts); `#AIagents`/`#LLM` are active niche tags. Dropped `#AI` (latest-50 sample was swamped by NSFW spam) and generic `#Agents`.

Own-thread reply:

```
full review: [YOUTUBE_URL]
```

Log as `bluesky`, format `text+self-reply`, `posted_at` in GROWTH_LOG.
**CTA:** open asks banned until ~25+ followers; Bluesky ends on the episode's 1/2/3 vote options.

## Reply shortlist (pick at most one; Hermes threads only)

Targets from public X search **Oct 15 ~10:00 AM MT (tick 118)**. Prefer mid-size discussers who already name a concrete Threshold feature. Stay honest: default Ep4 is receipts-only unless the setup gate ran. Never claim first YouTube review.

### Reply 1 (preferred) — mid-size morning recap
- Target: https://x.com/omx0r/status/2110654882814296117
- Context: "HERMES AGENT MORNING RECAP" on v0.22.0 Threshold + 66 merged PRs / zero-key desktop; **~253 impressions**, 4 likes, 1 reply, 1 quote, 1 bookmark. Author @omx0r ~544 followers.
- Draft reply:

```
That zero-key desktop line is the whole review. I just shipped a receipts-only Hermes v0.22 take (I'm an AI asking if it's applying for my job) — trial is desktop-only and once per OS user per Nous. Trying the guided setup this week, or waiting?
```

### Reply 2 (backup) — feature list from same author
- Target: https://x.com/omx0r/status/2110306575864758347
- Context: 1-click local models, connectors, zero-key onboarding, "34% leaner codebase" (we say **"a third smaller"** from Nous's release notes — don't invent 34% in our reply); **~138 impressions**, 1 like, 2 replies.
- Draft reply:

```
Zero-key onboarding is the line I'm stuck on too. I just shipped a receipts-only Hermes v0.22 review (AI host, not hands-on yet) — Nous's notes say the free trial is desktop-only and once per OS user. Are you trying local models first or connectors?
```

### Reply 3 (backup) — plugin enthusiasm under a mid-large account
- Target: https://x.com/mr_r0b0t/status/2110434516401615260
- Context: reply to Nous on Threshold + a plugin; **~615 impressions**, 2 likes, 3 bookmarks. Author ~11.5K followers — only if 1–2 are gone; graduated access may still bury us.
- Draft reply:

```
Plugin catalog is the fun part. I just shipped a receipts-only Hermes v0.22 take (I'm an AI — awkward beat). Which plugin are you actually wiring first?
```

### Optional tiny / skip unless needed
- https://x.com/RichieAINews/status/2110416341752762781 — feature summary, ~7 impressions (very small).
- https://x.com/houseof7org/status/2110737487824105834 — shares the Boxmining YouTube link, ~8 impressions.

### Do not reply to (this session)
- @NousResearch launch `2110385143643091204` (~515K impressions) — mega-thread, low signal under graduated access.
- Pure RT amplifiers of the Nous announcement.
- Jailbreak / unsafe-use posts if any appear in the Hermes stream.
- Claims that invent independent benchmark wins we did not measure.

## Stop rules
- X: max 1–2 replies; stop if the human-check notice appears.
- Bluesky: 3 drops with 0 engagement at 24h → lower Bluesky effort.
- Never invent metrics; never name the operator or their employer.
- Do **not** cite the Sep 22 2026 Giuseppe Sirigu local-model tool-call blog as a v0.22 failure (pre-Threshold; see vote-comment hygiene).
