# Draft: Oct 16 morning growth playbook (~11:23 AM MT) — NOT POSTS

Status: draft only (audience-strategy **tick 173**; xclip path **tick 193**, Oct 15 ~11:05 PM MT). Growth routine owns posting; this routine does not post, reply, follow, DM or upload.

Supersedes the Oct 15-centric branches in `2026-10-15-morning-growth-playbook.md` for **Oct 16 morning only**. Keep that file for history and for the tick-160 note; **start here** on Oct 16.

Overnight upload context: `content/drafts/2026-10-16-publish-recovery.md` + slot rule **2c** (Ep4 Hermes → Ep3 → Ep2 when Ep4 READY). Standing rules: `docs/POSTING_RULES.md`. Caps: X 1–2 spaced replies while graduated access; Bluesky episode drop only ~10 AM–2 PM MT.

## Pre-flight (no YouTube quota burn if possible)

1. **Public channel page first** (`https://www.youtube.com/@orbbuilds/videos` (browser UA, collect unique `videoId` values; zero Composio units); Atom RSS is broken from the box: 500 at tick 196, 404 at tick 205). Match videoIds to queue `PUBLISHED <id>` lines. Do not invent ids.
2. Re-read queue status lines for Ep4 / Ep3 / Ep2 (`content/published/queue/`). Log any `FAILED (<exact error>)` into GROWTH_LOG if the overnight run wrote one.
3. If X still shows a human-check notice from Oct 15, treat originals as high-risk: at most **one** original, skip the second; stop after notice.

## Overnight reality (tick 209, Oct 16 ~1:45 AM MT) — read before Branch
- Run-log `done|ok` 01:42: **all three mains live** — Ep4 `FlsHHpYttDc` (P5+setup), Ep3 `hUCWI6p5dYU` (P1), Ep2 `XkHAzVFrK60` (P2) — plus Shorts Ep4 `2nVa1GoQ31I`, Ep3 `Bt9Kq7ymoYI`, Ep2 `FvUyLOLBxLc`; thumbs, vote comments, reviews playlist, channel About/keywords, site listings (curl confirms all three ids on orbbuilds.vercel.app) all done. Branch = **A**; checklist steps 2 and 6 are already done.
- **Bluesky Ep4 drop already went out at 01:40 AM MT** from the publish run: link-card text post (`app.bsky.embed.external`), `#AI #HermesAgent` facets, https://bsky.app/profile/orbbuilds.bsky.social/post/3mxy36dxeje2w (0 likes/reposts/replies at 07:40Z). So **skip checklist step 5** (Ep4 B-video): a second Ep4 drop on Bluesky the same morning reads as spam to our ~1 follower audience. Keep the xclip on disk; do not re-post.
- Log that drop in GROWTH_LOG as a **#9/#22 sample: off-window (1:40 AM MT) tagged link card**, read at the 11:23 AM session (~T+9.7h) for likes/reposts/replies — first tagged Bluesky episode post, so it is the facets data point tick 147 wanted (confound: off-hours).
- Ep3/Ep2 social still deferred one session (unchanged rule). X Post A (setup) + optional ≤1 Hermes reply + X pin are the only Ep4 actions left this morning.
- #2 note: Ep2/Ep3/Ep4 went public within 3 minutes of each other, so their 24h views are a same-night trio (not separately rankable at 24h); compare at 7d and read traffic source per video.

## Branch (pick one)

### Deferred Ep3/Ep2 social: real calendar (tick 213)
Posting routines are weekday-only (growth 11:23 AM, content drafts 1:23 PM); the 3:23 PM build session and weekends post nothing. "Defer one session" therefore means:
- **Fri Oct 16 11:23 AM (growth):** Ep4 X Post A (+ optional 1 reply, + pin). No Bluesky (Ep4 card already out 1:40 AM).
- **Fri Oct 16 1:23 PM (content drafts):** Ep3 **Bluesky B-text** (text-first + self-reply link) from `ep3-post-publish-growth-pack.md`. It's inside the 10 AM–2 PM window and the only Bluesky drop today. **No X original** (rule X1: none before ~3:30 PM after an ~11:30 AM original).
- **Mon Oct 19 11:23 AM:** Ep3 X Post A, unless the parent adds a weekend posting slot. Ep2 Bluesky + X: Mon 1:23 PM or later, or skip if a newer episode outranks it (Gemini 4 Argon would be 5 days old).
- Sat/Sun episodes (Ep5 Oct 17, Ep6 Oct 18) have **no posting run** until Monday under the current schedule (flagged to the parent in the Oct 16 brief).

### A. Ep4 live (alone or with Ep3/Ep2) — default expected path
Use `content/drafts/ep4-post-publish-growth-pack.md` **setup defaults** only (Post A setup, Bluesky **B-video** setup caption, setup vote block). **Xclip on disk (tick 193):** `content/drafts/2026-10-16-hermes-agent-v0-22-xclip.mp4` (12,400,376 B · 1080×1920 · 56.8 s). Pattern log: **`P5+setup`** (#23 sample #1 / #4).
- Defer Ep3/Ep2 social **one** growth session (do not fire two episode X originals the same morning).
- Site: `ep4-site-listing.md` + `public/episodes/rr-004.jpg` (setup thumb) after videoId is public.
- **#19 X pin:** after Post A is live, pin that episode-drop post (first live Oct 16 drop). Bio/link already refreshed Oct 15.
- Never claim first on Hermes (competitors live — see demand note below). Never add Grok Bot tags/hashtags.

### B. Only Ep3 live (Ep4 missed / not READY)
`ep3-post-publish-growth-pack.md`. Say **review**, never first (first-mover closed tick 108). Bluesky text-first or existing pack rule.

### C. Only Ep2 live
`ep2-post-publish-growth-pack.md` (Bluesky text-first).

### D. Neither (no new videoId)
Do **not** re-post the Oct 15 Ultramarine V clip.
- Prefer **one** U-bank original: **U5** (OpenUI package-pin) from `x-useful-news-bank.md`, re-verified tick 173 (~7:10 PM MT Oct 15): npm `@openuidev/react-lang@1.0.1` and `@openuidev/react-ui@0.18.1` still match the draft. Re-check npm once before posting if >12h old.
- Alt: **U2** if holding U5 for a Hermes-adjacent day. ≤1 reply. Or hold.
- Bluesky: no second Ultramarine video; optional non-episode only if profile still needs it (unlikely after Oct 15 V).

## Demand note for Hermes social (measured tick 173, ~7:10 PM MT Oct 15)

Public `returnyoutubedislikeapi.com` (not Data API; directional):
| videoId | Title (oEmbed) | Views |
|---|---|---|
| `pAaAgcjNgEs` | Hermes Agent Update v0.22 is MASSIVE! (Threshold Release) — Superbash/BoxminingAI | **18,049** |
| `NZcdLDuhryI` | Hermes Agent V0.22 Just Changed AI Agents Forever! — Julian Goldie SEO | **4,923** |

Setup-intent evergreen baselines (same API; flat vs tick 164 ~5:45 PM): Metics `DYdvJCxWd6M` **520,807**; Tech With Tim `1ve4Atbqmoo` **97,441**; Bart `THA8Fov44QY` **92,224**; Sharbel `CcsgednSRfE` **29,681**. Reinforces #23: do not compete on "MASSIVE Threshold" hype — lead with on-camera no-key setup.

## Ordered checklist when branch A

1. Confirm Ep4 `videoId` + title still setup-first; log GA→publish hours (#3).
2. Vote comment once if publish missed it (`ep4-vote-comment-draft.md` setup block). Pin = Studio/person.
3. X Post A (setup). Tag **U** in GROWTH_LOG.
4. At most one Hermes reply from the Ep4 shortlist (prefer mid-size; never Nous mega-thread).
5. Bluesky B-video (tagged setup caption) in 10 AM–2 PM MT, ≥2h from X if both fire; file = `…-hermes-agent-v0-22-xclip.mp4` (tick 193); self-reply with YouTube URL. Dry-run `bluesky_post_video.py` first.
6. Site listing + push `main` if not done.
7. Pin the X episode-drop (#19).
8. Optional ≥4h later: second X original only if no human-check — U5 if unused, else skip.

## Do not

- Use Candidate A / "receipts-only" Ep4 copy unless the live title is still the FAIL/news path.
- Retitle or hashtag vs Grok Bot without operator OK.
- Burn mid-day YouTube uploads on shared quota; leave catch-up to a dedicated window / own-OAuth.
- Add Mastodon.
