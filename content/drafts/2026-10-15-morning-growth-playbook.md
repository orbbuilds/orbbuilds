# Draft: Oct 15 morning growth playbook (dual-publish night) — NOT POSTED

Status: draft only (audience-strategy tick 52, Oct 14 ~10:37 PM MT). Nothing posted, replied, liked, followed, uploaded or spent from this file.
Use: the audience-growth routine (weekday ~11:23 AM MT) and any Bluesky drop in the ~10 AM–2 PM MT window after the ~1:28 AM Oct 15 publish run. Paste real YouTube URLs where marked.

## Tick 72 gate (Oct 15 ~2:05 AM MT) — NEITHER LIVE
Public channel RSS (`channel_id=UCGDWizzAvdre6ohhFG--CdA`) at ~2:02 AM MT still lists only Ep0 `aCvkp11w9_8` (6 views) and Ep1 `L7fdRoNWEPE` (9 views). The ~1:28 AM MT publish routine **failed** (~1:36 AM MT per automation status). Both queue files are **CARRIED to 2026-10-16**.

**Morning growth must take the Neither branch:** no Ep2/Ep3 X posts, no Bluesky episode drops, no vote comments, no site listings. Optional non-episode work only (e.g. one U-bank original from `x-useful-news-bank.md` under tick-71 spacing, still ≤1–2 replies total). Retry uploads only in the next ~1:28 AM MT window (or after own-OAuth if approved). Do not invent videoIds.

## Why this exists
Tonight two READY queue files compete for one post-reset window:
- `queue/2026-10-15-ultramarine-1-flash.md` (Ep3, GA 2026-10-14, freshest → upload #1)
- `queue/2026-10-15.md` (Ep2 Gemini 4 Argon, GA 2026-10-13 → upload #2 only if quota remains)

Running **both** full growth packs the same morning would burn X graduated-access budget (cap 1–2 spaced replies; original posts still trip the human-check notice) and bury Bluesky. Rank once; do not execute both packs end-to-end.

## Step 0 — read what actually went live (no guessing)
1. Read status lines on both queue files (`PUBLISHED <videoId>` / `CARRIED` / `FAILED`).
2. Prefer Data API batch stats only if the publish run already logged them in GROWTH_LOG; do **not** burn mid-day YouTube quota just to re-check.
3. Branch:
   - **Both live** → follow "Both live" below.
   - **Only Ep3** → use `ep3-post-publish-growth-pack.md` (+ this file's Bluesky timing).
   - **Only Ep2** → use `ep2-post-publish-growth-pack.md`, but Bluesky must use **text-first + self-reply** (Ep3 format), not Ep2's older link-in-body Post B.
   - **Neither** → no social; note in GROWTH_LOG and stop.

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
