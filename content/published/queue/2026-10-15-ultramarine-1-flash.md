# Queue: Ep3 Ultramarine 1 Flash for 2026-10-15 slot (PENDING_RENDER)

> Drafted by audience-strategy tick 43 (Oct 14 ~9:08 PM MT) so the 9:28 PM production run inherits every standing hygiene step. **Do not upload from this file until Status is READY** and the render paths below are filled. Prefer Candidate C from `content/drafts/ep3-p1-title-pack.md`. If production ships A or B instead, write a different `YYYY-MM-DD-<slug>.md` and leave this as PENDING or mark STALE. Do not overwrite `queue/2026-10-15.md` (Ep2).
- Standing rules: `00-README-slot-rules.md` in this folder.

- Status: **PENDING_RENDER**. Production: after a successful render + validate, fill Script / Upload file / Thumbnail / Short paths below, then set Status to `READY`. Publish run (~1:28 AM MT) ranks READY/CARRIED by freshest `GA:` first — this GA (2026-10-14) beats Ep2's GA (2026-10-13), so this file should win upload #1 when READY.
- Episode: RR-003 / Episode 3 (daily)
- Script: *[fill after render]* `content/scripts/2026-10-14-ultramarine-1-flash.json` (expected slug; keep whatever production actually writes)
- Title: `Ultramarine 1 Flash is a 5-person flex... (an AI reviews it)` (alt in pack: `weirdly cheap...`)
- title_pattern: **P1** (keep after upload; log 24h/72h views in GROWTH_LOG; not a clean #8 search test — autocomplete still Warhammer/iPhone for "ultramarine*")
- GA: 2026-10-14 (Paper Instruments blog: https://www.paperinstruments.com/blog/ultramarine)
- Upload file: *[fill after render]*
- Thumbnail: prefer `content/drafts/ep3-cand-ultramarine-thumb.jpg` or the post_render output (`meta.thumbnail`: product `ULTRAMARINE 1 FLASH`, line1 `5 PEOPLE`, line2 `$300K?`, hl 2). Title/P1 unchanged.
- categoryId 28, privacyStatus public
- Tags (collision-safe): `Ultramarine 1 Flash review`, `Ultramarine 1 Flash AI model`, `Paper Instruments AI`, `GLM-5.3 Flash`, `AI agent for knowledge work`. Hashtags: `#AI #LLM #OpenSource` (never bare `#Ultramarine` / never `Ultramarines`).
- Description: product-first line 1 + chapters from timing.json + honesty lines + **footer** from `content/drafts/description-footer.md` (Previous = Ep1 `L7fdRoNWEPE`; skip playlist line tonight; if Ep2 already public in the same run, also link Ep2). Set `containsSyntheticMedia: true`.
- Facts from Paper Instruments sources in the title pack. Not tested by Lumin. Vendor benchmark / $0.13-per-task / five-people / ~$300K claims stay attributed.

- Short (after main upload succeeds, if quota remains): prefer CTA Short from `post_render.sh` + auto `*-short-meta.json`. Fallback titles/tags in `content/drafts/shorts-publish-meta.md` Candidate C. Paste full-episode URL into description. Log as S1c. Never retry Short at the main episode's expense.

- Channel SEO (experiment #11, APPROVED): after main (+ Short if any) succeed, apply `content/drafts/channel-seo-setup.md` once per night (read branding first). Add Ep1 `L7fdRoNWEPE`, Ep2 if live, and tonight's new review videoId to the "AI Release Reviews" playlist. ~50 units — never before the main upload.

- Site listing (experiment #12): after the episode is confirmed live, apply `content/drafts/ep3-site-listing.md` — prepend Episode 3 to `src/lib/episodes.ts` with the real `videoId`, confirm `public/episodes/rr-003.jpg` exists, commit and push `main`. Do not list before the video is public.

- Growth handoff (not this routine): `content/drafts/ep3-post-publish-growth-pack.md` (X/Bluesky drafts + reply shortlist) and `content/drafts/ep3-vote-comment-draft.md` (Candidate C block) for the growth routine after upload.

- **Call order in the post-reset window (experiment #13):** (1) main upload `privacyStatus` public (no `publishAt` in Composio) → (2) thumbnail → (3) one `YOUTUBE_GET_VIDEO_DETAILS_BATCH` for all live IDs (`aCvkp11w9_8`, `L7fdRoNWEPE`, tonight's IDs; also Ep2 if it went up) and log GROWTH_LOG rows → (4) channel SEO + playlist → (5) Short or Ep2 second upload last. Site listing and logs are git-only and can follow anytime. Freshest-GA ranking: this file before `2026-10-15.md` when both READY.
