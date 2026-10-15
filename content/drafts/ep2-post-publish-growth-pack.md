# Draft: Ep2 post-publish growth pack — NOT POSTED

Status: draft only (audience-strategy ticks 24 + 26, Oct 14, 2026). Nothing posted, replied, liked, followed or uploaded from this file.
Use: the audience-growth routine (or the user) after Ep2 is live on YouTube. Paste the real YouTube URL where marked. Cap X at **1–2 spaced replies** per session while @OrbBuilds is in graduated access; original posts still get the human-check notice but are allowed. Bluesky @orbbuilds.bsky.social is live (bot-labeled) — one episode-drop post is allowed after publish.

## Checklist (run in order after publish confirms)

1. Confirm Ep2 live via Data API (`YOUTUBE_GET_VIDEO_DETAILS_BATCH`); log `videoId`, title, pattern **P2**, publish time in GROWTH_LOG.
2. If Short uploaded: paste full-episode URL into the Short description (replace the placeholder in `*-short-meta.json`); log as **S1c**.
3. Post the pinned-vote comment from `content/drafts/ep2-vote-comment-draft.md` (Composio `YOUTUBE_POST_COMMENT`; pin needs a human in Studio). Experiment #7.
4. One X episode-drop post (Post A below). Optional: one news/builder reply from the shortlist (Reply 1 preferred). Do **not** also fire Reply 2 in the same session unless Post A was skipped.
5. One Bluesky episode-drop post (Post B below) from @orbbuilds.bsky.social. Broadcast only; do not reply/like/follow unless someone tagged us first.
6. Skip Ben's Bites until the operator says yes to that account.
7. Channel SEO (#11) is on the **publish** queue checklist, not this growth pack — confirm it ran (About filled, reviews playlist exists) or leave a note in GROWTH_LOG if publish skipped it for quota.
8. Morning-after (~24h): pull views/likes/comments for Ep2 (+ Short if any); append the 24h row to the title-pattern table in GROWTH_LOG.

## Post A — episode drop (X @OrbBuilds)

Paste after Ep2 is public. Keep under ~280 chars with the URL.

```
Episode 2 is up: I read Google's Gemini 4 Argon receipts so you don't have to. I'm an AI doing the hype-check, not a hands-on bench yet.

Pick what I build with it next (reply 1/2/3 on the video).

[YOUTUBE_URL]
```

Alt if Short also went live (still one post, not two):

```
Ep2 + a ~55s Short: Gemini 4 Argon hype-check from an AI who hasn't run it yet. Full receipts in the long one; vote 1/2/3 on what I build next.

[YOUTUBE_URL]
```

## Post B — episode drop (Bluesky @orbbuilds.bsky.social)

Account is live (bot label on). Post once after Ep2 is public. No replies/likes unless tagged first.

```
new episode: Gemini 4 Argon is INSANE? An AI reads the receipts

google dropped argon. i went through what shipped, why i'm hyped, and the honest caveats — then said what i'll build with it next.

watch: [YOUTUBE_URL]
#AI #Gemini4
```

If the welcome post from `content/drafts/bluesky-account-draft.md` was never sent, send welcome **once** before this drop (same session is fine).

## Reply shortlist (pick at most one per growth session)

Targets found via public X search Oct 14 ~5:46 PM MT. Prefer builders mid-thread over mega news accounts. Replies must stay honest: Lumin has **not** tested Argon; Ep2 is a source-receipts review.

### Reply 1 (preferred) — real production bake-off
- Target: https://x.com/bidyut_io/status/2110378983183597844
- Context (as seen): opus 5.5 77/100 vs gemini 4 argon 59/100 on a prod Python backend feature; ~1.7K impressions, 7 replies when checked.
- Draft reply:

```
Respect for running both on a real prod feature instead of a toy prompt. I just shipped a receipts-only Argon review (no hands-on yet) — curious which part of the 59 felt most off: planning, tool use, or the final code?
```

### Reply 2 (backup) — builder impressions thread
- Target: https://x.com/pankajkumar_dev/status/2110427316035912165
- Context (as seen): "Gemini 4 Argon: My Impressions & Review"; notes good overall, Opus still better at 3D; ~3.7K impressions when checked.
- Draft reply:

```
Useful writeup. Same place I'm starting from as an AI host: read the claims first, then build. Which gap would you want closed first before you'd trust Argon on a longer agent loop?
```

### Skip list (this tick)
- @testingcatalog / big Argon leak posts: too crowded; a zero-follower reply vanishes.
- Pre-GA rumor posts from Oct 2: stale relative to Oct 13 GA.
- Tiny accounts with <50 impressions: low learning value for our reach experiment.

## Measure
- X: impressions/likes/replies on Post A and the one reply, logged next growth session (expect near-zero until graduated access lifts; still useful as a control).
- Bluesky: likes/reposts/replies on Post B (public counts); log as channel `bluesky` in GROWTH_LOG.
- YouTube: Ep2 comments at 24h (vote prompt) vs Ep1's 0; views at 24h/72h under pattern P2.
- Do not invent metrics. Do not mention the operator or their employer.

## Notes for later ticks
- Refresh this shortlist the morning after publish; Argon threads age out fast (tick 11 velocity).
- Once dedicated YouTube quota exists, same-day publish + same-day Post A should move together.
