# Draft: Oct 15 morning growth playbook (dual-publish night) — NOT POSTED

Status: draft only (audience-strategy tick 52, Oct 14 ~10:37 PM MT). Nothing posted, replied, liked, followed, uploaded or spent from this file.
Use: the audience-growth routine (weekday ~11:23 AM MT) and any Bluesky drop in the ~10 AM–2 PM MT window after the ~1:28 AM Oct 15 publish run. Paste real YouTube URLs where marked.

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
| X replies | **At most one** Ep3 Reply 1 (`@ivanainai` preferred); none if Post A already went out and the session feels hot | Ep2 reply shortlist; CEO mega-thread |
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
