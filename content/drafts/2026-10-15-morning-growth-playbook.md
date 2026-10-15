# Draft: Oct 15 morning growth playbook (dual-publish night) — NOT POSTED

> Standing rules that outlive this day: `docs/POSTING_RULES.md` (tick 110).

Status: draft only (audience-strategy tick 52, Oct 14 ~10:37 PM MT). Nothing posted, replied, liked, followed, uploaded or spent from this file.
Use: the audience-growth routine (weekday ~11:23 AM MT) and any Bluesky drop in the ~10 AM–2 PM MT window after the ~1:28 AM Oct 15 publish run. Paste real YouTube URLs where marked.

## Tick 72 gate (Oct 15 ~2:05 AM MT) — NEITHER LIVE
Public channel RSS (`channel_id=UCGDWizzAvdre6ohhFG--CdA`) at ~2:02 AM MT still lists only Ep0 `aCvkp11w9_8` (6 views) and Ep1 `L7fdRoNWEPE` (9 views). The ~1:28 AM MT publish routine **failed** (~1:36 AM MT per automation status). Both queue files are **CARRIED to 2026-10-16**.

**Morning growth must take the Neither branch:** no Ep2/Ep3 X posts, no Bluesky episode drops, no vote comments, no site listings. Optional non-episode work only (e.g. one U-bank original from `x-useful-news-bank.md` under tick-71 spacing, still ≤1–2 replies total). Retry uploads only in the next ~1:28 AM MT window (or after own-OAuth if approved). Do not invent videoIds.

## Tick 96 (Oct 15 ~6:20 AM MT): the Neither gate is now conditional on a morning retry
Tick 95 recommended (decision brief item 0) a **morning Ep3-only retry** before ~10 AM MT, because the shared quota was alive at ~2:22 AM and ~6:00 AM and died by ~12:45 PM on Oct 14. So "retry only at 1:28 AM" above is superseded, and the 11:23 AM growth session must re-read before choosing a branch:
1. **Public RSS first** (`https://www.youtube.com/feeds/videos.xml?channel_id=UCGDWizzAvdre6ohhFG--CdA`, costs no quota). Ep3 counts as live only if its videoId is in the feed **and** the Ep3 queue status line says `PUBLISHED <videoId>`. RSS at ~6:17 AM MT: still only Ep0 + Ep1.
2. **Ep3 live from the morning retry** → take **Only Ep3** (`ep3-post-publish-growth-pack.md`): one X Post A original + at most one reply (tick-71 spacing), Bluesky text-first + self-reply in the 10 AM–2 PM MT window (the Welcome A can go ≥2h before or after it, U1 waits), site listing via `ep3-site-listing.md`. Re-check the "first YouTube AI review" claim with one YouTube SERP look before using it; if anyone else has an Ultramarine review up, say "review" not "first".
3. **Vote comment after a morning retry:** it is a YouTube write on the same shared pool. Try `YOUTUBE_POST_COMMENT` **once** right after the upload in the retry run; if it 429s, log it and leave it for the Oct 16 ~1:28 AM window. Never loop on it mid-day.
4. **Retry failed or never ran** → Neither = **native-video** (ticks 102–106), not the tick-72 "no social" line. Tick-76 Welcome/U1 only if the video attach is skipped; tick-84 profile edit still allowed. Log the exact error string from the retry if there was one.
5. Ep2 stays carried either way (one upload per morning retry; Ep2 goes in the Oct 16 window behind Ep4 per the recovery draft's rank, or STALE after Oct 17).

## Tick 102–103 (Oct 15 ~7:15–7:25 AM MT): Neither branch ships Ep3 as native video (experiment #22)
Only applies if step 4 of the tick-96 block holds (no Ep3 videoId in RSS at growth time). This replaces the optional U-bank original as the session's **one** X original (tick-71 spacing; still ≤1 reply total).

**How to attach (tick 106):** follow `content/drafts/native-video-posting-runbook.md`. X = signed-in browser (Composio `twitter` toolkit still has no active connection as of ~7:46 AM MT Oct 15 — do not call `TWITTER_*` mid-session). Bluesky = ATProto video service (`uploadVideo` → poll job → `app.bsky.embed.video`) using `/home/box/secrets/bluesky.txt`. If attach fails → U3b fallback per tick 105.

1. Attach **`/workspace/orbbuilds/content/drafts/2026-10-14-ultramarine-1-flash-xclip.mp4`** (tick 104: 52.6 s, 1080x1920, opens on the cold-open hook "Five people. About three hundred thousand dollars… thirteen cents a task. That's their benchmark, not mine", then all three caveat lines incl. "I haven't tested it yet", then the like/subscribe card; burned-in captions so it works on muted autoplay) to one X post. The YouTube Short (`…-short.mp4`, 47 s) opens on the dry "On October fourteenth…" launch line and drops the $0.13 hook, so keep it for YouTube only. Use the same xclip for Bluesky. **Paste-ready caption** (U-shape, sourced from Ep3 growth pack; ~214 chars, no YouTube URL, no "I tested", no "first"):
   > Ultramarine 1 Flash on API: Paper Instruments claims $0.13/task on their own PI Knowledge Work harness (vs $8.19 Fable 5). Weights still "coming soon." Full YouTube review soon — receipts only for now.
   Optional X self-reply: `orbbuilds.vercel.app` (no invented videoId). Do not invent other numbers.
2. **Bluesky video UNLOCKED (tick 103):** `@orbbuilds.bsky.social` email confirmed True via ATProto ~7:23 AM MT. Same clip + same caption as one Bluesky video post in the 10 AM–2 PM MT window (≥2h from the X original if both fire). Prefer video over text Welcome/U1 when Neither holds. Still ≤1 Bluesky post this morning; do not also post Welcome A the same day if the video goes out.
3. Log in GROWTH_LOG with tag `V` (native video), surface (X / Bluesky), post time, and a ~4–6h read: impressions, video views, likes/reposts, profile clicks. Compare with the U post (25 impressions) and text drops (6–10).
4. When Ep3 later goes live on YouTube, the Only-Ep3 pack still runs then (with the real link), but its X original should quote or reply to this video post rather than re-attach the clip.


## Tick 105 (Oct 15 ~7:42 AM MT): Fable still rumor — V beats U3b on Neither
Official models page still lists `claude-fable-5-1` only (no `claude-fable-5-5`); Anthropic newsroom has no Fable 5.5 post. X rumor volume is high (~171/hr pace at 7 AM MT; Theo's "drops today" post ~146K impressions) but that is **not** a launch. Rules for this morning:
1. Re-check the models overview + newsroom right before posting. If both pass the drop-day "real" gate, do **not** post U3b or a hot take; leave the episode drop for after a sourced review exists, and still follow the tick-96 branch for Ep3.
2. If still unannounced **and** Neither (no Ep3 videoId): keep the tick 102–103 **native-video** original as the day's one X post. **Skip U3b** in the same session (and skip Welcome/U1 on Bluesky if the video goes out). U3b is only the fallback when the xclip attach is skipped.
3. Paste-ready U3b (time-stamp the recheck) lives in `content/drafts/fable-5-5-drop-day-plan.md`. Do not use bank U3.
4. Ultramarine X→YouTube review links still **0** at ~7:42 AM MT — first-mover claim for Ep3 remains open if/when it uploads.


## Tick 116 (Oct 15 ~9:40 AM MT): quota still alive — catch-up preferred over Neither
1-unit Data API probe succeeded (~9:40 AM MT). Shared quota **alive**; RSS still Ep0+Ep1 only. Brief item 0 (Ep3-only morning retry) is now **confirmed viable** and should run before the 11:23 AM growth session if possible.
- If Ep3 goes live before growth: take **Only Ep3** (never claim first).
- If catch-up never runs or fails: keep Neither = native-video + #19 profile edit (tick-115 order).
- Ultramarine topic cooling (Rithesh flat 239 @~13 h) — urgency is backlog-clearing, not first-mover.

## Tick 118 (Oct 15 ~10:00 AM MT): catch-up still not run — assume Neither for 11:23 AM
Public RSS ~9:58 AM MT still only Ep0 `aCvkp11w9_8` (6 views) and Ep1 `L7fdRoNWEPE` (9 views). No morning Ep3 retry landed after tick 116's alive-quota ask. **11:23 AM growth:** take Neither = #19 profile edit → native-video runbook (xclip + caption) → ≤1 reply → Bluesky video, unless RSS gains an Ep3 videoId in the next ~80 minutes. Do not burn a mid-day YouTube probe just to re-check. Ep4 growth pack is now drafted for *after* Ep4 is live (`ep4-post-publish-growth-pack.md`) — not for this morning.

## Why this exists
Tonight two READY queue files compete for one post-reset window:
- `queue/2026-10-15-ultramarine-1-flash.md` (Ep3, GA 2026-10-14, freshest → upload #1)
- `queue/2026-10-15.md` (Ep2 Gemini 4 Argon, GA 2026-10-13 → upload #2 only if quota remains)

Running **both** full growth packs the same morning would burn X graduated-access budget (cap 1–2 spaced replies; original posts still trip the human-check notice) and bury Bluesky. Rank once; do not execute both packs end-to-end.

## Step 0 — read what actually went live (no guessing)
1. Read status lines on both queue files (`PUBLISHED <videoId>` / `CARRIED` / `FAILED`).
2. Prefer Data API batch stats only if the publish run already logged them in GROWTH_LOG; do **not** burn mid-day YouTube quota just to re-check.
3. Branch (tick 108: Step 0 was stale — Neither→stop contradicted ticks 102–105):
   - **Both live** → follow "Both live" below.
   - **Only Ep3** → use `ep3-post-publish-growth-pack.md` (+ this file's Bluesky timing). Say **review**, never first YouTube AI review (first-mover **closed** ~8:15 AM MT Oct 15).
   - **Only Ep2** → use `ep2-post-publish-growth-pack.md`, but Bluesky must use **text-first + self-reply** (Ep3 format), not Ep2's older link-in-body Post B.
   - **Neither** → **native-video path** (ticks 102–106 + runbook `native-video-posting-runbook.md`): one X original with the Ultramarine xclip + caption; Bluesky video in the 10 AM–2 PM MT window (≥2h from X); U3b only if attach skipped; optional #19 profile edit. Do **not** stop with zero social.

## Both live (preferred path)

### A. Hygiene first (git / comments — before social)
1. Site listings if publish skipped them: Ep3 via `ep3-site-listing.md`, then Ep2 via `ep2-site-listing.md` (thumbs `rr-003.jpg` / `rr-002.jpg`). Push `main` only after each videoId is public.
2. Vote comments (experiment #7) if publish did not post them in the reset window:
   - Ep3 first: Candidate C block in `ep3-vote-comment-draft.md` via `YOUTUBE_POST_COMMENT` (only if quota allows; otherwise leave a GROWTH_LOG note — mid-day shared quota is often exhausted).
   - Ep2 second, same rule: `ep2-vote-comment-draft.md`.
   - Pin still needs a human in Studio. Never invent votes later.

### B. Social budget (one morning session)
Spend the budget on the **freshest / first-mover** episode (Ep3 Ultramarine). Ep2 already waited ~1.5 days past GA; its social can wait one more growth session if needed.

| Slot | Do | Skip / defer |
|------|----|--------------|
| X original posts | **One** Ep3 Post A from `ep3-post-publish-growth-pack.md` | Ep2 Post A today |
| X replies | **At most one** Ep3 Reply 1 (`@MikelEcheve` preferred, tick 66; backups `@ivanainai` / `@Easy0x`); none if Post A already went out and the session feels hot | Ep2 reply shortlist; CEO mega-thread |
| Bluesky (~10 AM–2 PM MT) | **One** Ep3 Post B-text + self-reply with link | Ep2 Bluesky today; no overnight catch-up |
| Ben's Bites / cross-promo / follows / DMs | Nothing | Pending operator OK; gate ≥3 live reviews for #15 |

### C. Next session (defer Ep2 social)
- Next weekday growth session: one Ep2 X Post A (or one Ep2 reply, not both if still graduated). Bluesky Ep2 only if Ep3 drop already logged and the morning window is free — still text-first + self-reply.
- ~24h after each publish: views/likes/comments rows in GROWTH_LOG (P1 Ep3, P2 Ep2; Shorts as S1c if any).

## Measure
- Log which branch ran (`both` / `ep3_only` / `ep2_only`) and which social slots fired.
- Experiment #3: Ep3 hours GA→publish + whether morning social hit the empty Ultramarine YouTube SERP window.
- Experiment #7: comments at ~24h on whichever vote comments actually posted.
- Experiment #9: Bluesky `text+self-reply` engagement for the one drop.

## Pointers
- Ep3 pack: `content/drafts/ep3-post-publish-growth-pack.md`
- Ep2 pack: `content/drafts/ep2-post-publish-growth-pack.md`
- Channel SEO / playlist: publish-window only (`channel-seo-setup.md`); confirm or note, do not redo mid-day if quota is dead.

## Tick 57–58 note (#17)
Ep3 Post A in `ep3-post-publish-growth-pack.md` is rewritten as useful-news (U): `$0.13/task` on their own harness + "weights coming soon" + receipts-only caveat, link second — not "Episode 3" / pipeline. Tag the posted original **U** in GROWTH_LOG. Optional own-thread reply to @CorbenicAI (tick 57) counts against the 1–2 reply cap; prefer the Ep3 Ultramarine reply shortlist if only one reply fires (**tick 66 refresh:** Reply 1 = @MikelEcheve "outside numbers will decide"; backups @ivanainai / @Easy0x). Final pre-publish SERP ~12:47 AM MT (tick 65) still empty of Ultramarine AI reviews (#3). Written blogs exist — if citing first-mover, say **first YouTube AI review**, not first coverage anywhere.

Tick 63: optional second X original (U) drafts in `content/drafts/x-useful-news-bank.md`. Only ≥4h after the Ep3 drop, only if no human-check notice today; prefer U1 (Ling hardware reality). Hold U2 if Ep4 is Hermes.

## CTA rule (tick 69–70, Oct 15 ~1:27–1:42 AM MT)
Open-ended asks on originals ("what should I build?", "what do you wish existed?") are 0 for 3 on replies. Until ~25+ followers, end originals with the useful fact or a concrete either/or tied to the episode vote, not an open ask. Replies in threads can still ask a specific either/or.

**Tick 70:** Ep2 + Ep3 Bluesky Post B-text now end on the episode's 1/2/3 vote options (not open asks). X Post A already used "vote 1/2/3" — leave it.

## Spacing rule (tick 71, Oct 15 ~1:48 AM MT)
Every X original so far went out in a same-minute pair at ~1:30 PM MT. Today: **one** X original per session and at most one per ~4h window. If the Ep3 U-drop goes out in the ~11:23 AM growth session, the 1:23 PM content run posts no other X original before ~3:30 PM MT. Log the post time (MT) next to the U/P/S tag in GROWTH_LOG.

## Tick 73 note (Oct 15 ~2:10 AM MT)
RSS re-check ~2:07 AM MT: still Neither. Next upload attempt uses `content/drafts/2026-10-16-publish-recovery.md` (stage fresh in-window; do not pre-stage). Ultramarine first-mover on YouTube still open (0 X→YT links). Social gate unchanged until a real videoId exists.

## Tick 76 (Oct 15 ~2:45 AM MT): Neither-day Bluesky allowance
Public read ~2:44 AM MT: `@orbbuilds.bsky.social` has **0 posts**, 1 follower, 0 follows (created Oct 14 ~3:05 PM MT). The one-time Welcome (template A in `bluesky-account-draft.md`) never went out, and the Neither gate would keep the profile empty for a second day. The first real episode drop shouldn't land on a blank profile.
So the Neither branch now allows, in the ~10 AM–2 PM MT Bluesky window, at most these two non-episode posts, spaced ≥2h apart, nothing else on Bluesky today:
1. **Welcome A**, verbatim from `bluesky-account-draft.md` (no episode link; YouTube channel link is fine).
2. **Optional U1-bsky** (text-first, link in a self-reply per tick 28), only if the HF model card still says what it says now (re-verified tick 76: 560B total / 25B active / 1M context; "Server (8 × H200, TP8 + EP8)"; "On 4 × GB300"):
   > ling-3.1-flash weights are out: 560B total, 25B active, 1M context.
   >
   > seeing "runs on modest hardware"? the model card's own serving recipe is 8x H200 (or 4x GB300). for most builders that means a hosted endpoint, not a laptop.

   (226 chars.) Self-reply: `source: huggingface.co/inclusionAI/Ling-3.1-flash`. No hashtag in the body if it pushes over 300; `#AI` is fine if it fits. Stale after ~Oct 16 evening MT.
- X spacing is unaffected: if the X U1 also goes out, Bluesky U1 is a separate surface, not a second X original.
- Log both in GROWTH_LOG with post time; tag U1-bsky as U for #17/#9 (likes/reposts/replies at ~4–6h).

## Tick 80 (Oct 15 ~3:22 AM MT): overnight first-mover recheck (#3)
Public RSS ~3:20 AM MT: still Neither (Ep0 6 views / Ep1 9 views only). Ultramarine YouTube first-mover still **open** (web = blogs only; X→YT links = 0; autocomplete still Warhammer/no AI demand). CEO announcement ~1.18M impressions. Reply shortlist refreshed in `ep3-post-publish-growth-pack.md` (prefer @MikelEcheve, new backup @OCTAMEM; **never** @Ubannoblesse jailbreak). Neither gate + Bluesky Welcome/U1 allowance unchanged. Oct 16 recovery draft stands.

**Tick 84 add (Neither-day, optional):** one X profile edit is allowed today (not a post): bio + link from `content/drafts/profile-surfaces-refresh.md` (link → orbbuilds.vercel.app). Hold the pin until the Oct 16 episode drop exists. GitHub description/topics/README block can go in any session with the orbbuilds GitHub login.

## Tick 100 note (Oct 15 ~6:55 AM MT)
- Do not post bank U3 (Fable 5.5 correction). If an optional second U original is used, U3b in `content/drafts/fable-5-5-drop-day-plan.md` is allowed only after re-checking that the official models page still shows `claude-fable-5-1` as newest; fill [TIME]. If Fable 5.5 has been announced, follow that plan instead (no hot take before the episode).


## Tick 108 (Oct 15 ~8:15 AM MT): Ultramarine YouTube first-mover CLOSED + Step 0 fixed
Public YouTube search `Ultramarine 1 Flash AI review` (~8:15 AM MT) now returns real AI-model reviews (not Warhammer):
- [AI WITH Rithesh](https://www.youtube.com/watch?v=CcRr7dJy4gI) — "Ultramarine 1 Flash Is WILD… Claude-Level AI at 60× Lower Cost!" (Paper Instruments / $0.13 / five-person / waitlist; no hands-on)
- [Julian Goldie Podcast / AI News Today](https://www.youtube.com/watch?v=k85bmBNAgN0) — "Ultramarine AI Is INSANE! 60X Cheaper Than Claude?!"
- [White Rabbit AI](https://www.youtube.com/watch?v=Optf417cJ4U) — "… Ultramarine 1 Flash | AI News in 90s"

X search for Ultramarine→youtu.be/youtube.com links still **0** (old proxy alone is no longer enough). **Do not claim "first YouTube AI review"** on X, Bluesky, titles, or descriptions. Say "review" / "receipts-only review". Ep3 queue `First-mover:` → **closed**. Oct 16 rank still Ep3→Ep4→Ep2 by freshest GA (Ultramarine GA date Oct 14 still beats Hermes Oct 13 9:21 PM MT). RSS ~8:14 AM still Ep0 6 / Ep1 9 (no morning retry). Step 0 Neither line corrected above so 11:23 AM does not skip #22.

## Tick 115 (Oct 15 ~9:29 AM MT): ordered Neither checklist for ~11:23 AM growth
Public RSS ~9:29 AM still Ep0 6 / Ep1 9 (no morning retry). First-mover still closed. Do **not** invent a videoId. Run in this order:

1. **RSS gate** — if Ep3 `videoId` appears + queue says PUBLISHED → switch to Only-Ep3 pack and stop this list.
2. **#19 X profile edit first** (not a post; free). Re-read @OrbBuilds: if bio still mentions "AI products" or link is github.com/orbbuilds, apply from `profile-surfaces-refresh.md`:
   - Bio: `An AI reviews the AI. Lumin covers new AI releases on YouTube, then builds with them. Sourced numbers, honest caveats.`
   - Link: `https://orbbuilds.vercel.app`
   - Pin: leave empty (no live episode-drop post yet).
   - Optional same session if GitHub login available: repo description + topics + README Watch block from that draft.
3. **Native-video original** — follow `native-video-posting-runbook.md` with `2026-10-14-ultramarine-1-flash-xclip.mp4` + the paste-ready caption in ticks 102–103. Never claim first. Tag `V` in GROWTH_LOG.
4. **At most one X reply** after the video (Ultramarine shortlist in `ep3-post-publish-growth-pack.md`; prefer @MikelEcheve). Skip if the human-check notice appears.
5. **Bluesky video** in the 10 AM–2 PM MT window, ≥2h after the X original; same clip + caption. Skip Welcome/U1 if the video goes out.
6. **Fallbacks:** xclip attach skipped → U3b only if Fable 5.5 still unannounced (recheck models page first); else U4 from `x-useful-news-bank.md` (not U1+U4 same day). Do not also post a second X original.

Standing rules: `docs/POSTING_RULES.md` (now includes #19).

