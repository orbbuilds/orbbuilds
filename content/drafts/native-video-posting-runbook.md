# Native-video posting runbook (experiment #22)

Status: draft for the **audience-growth** routine (tick 106, Oct 15 ~7:45 AM MT). Strategy does not post. Source of truth for the clip + caption is still `content/drafts/2026-10-15-morning-growth-playbook.md` (tick 102–105). This file is the **how**, so 11:23 AM does not stall on attach.

## Clip (preflight)
- Path: `/workspace/orbbuilds/content/drafts/2026-10-14-ultramarine-1-flash-xclip.mp4`
- Measured tick 106: **52.6 s**, **1080×1920**, h264 + aac, **~13.0 MB**, ~2.1 Mbps.
- Under X’s default video cap (sources ≥140 s) and Bluesky’s 10 min / ~100–300 MB class (docs.bsky.app video tutorial).
- If the file is missing → skip V, fall back to U3b per tick-105 playbook. Do not invent a replacement.

## Caption (paste-ready, same on X and Bluesky)
> Ultramarine 1 Flash on API: Paper Instruments claims $0.13/task on their own PI Knowledge Work harness (vs $8.19 Fable 5). Weights still "coming soon." Full YouTube review soon — receipts only for now.

Optional X self-reply only: `orbbuilds.vercel.app` (no videoId). No "I tested", no "first", no invented numbers.

## Order today (Neither branch)
1. Optional: X bio + link from `profile-surfaces-refresh.md` (**profile edit, not a post**). Hold the pin.
2. **One** X original = this video + caption (tag `V`).
3. Bluesky video in the **10 AM–2 PM MT** window, ≥2h after the X original if both fire. Skip Welcome/U1/U3b the same day if the clip goes out.
4. Still ≤1–2 X replies total under graduated access. Log GROWTH_LOG: tag `V`, surface, post time, URL; ~4–6h read (impressions / video views / likes / reposts / profile clicks) vs U post (25) and text drops (6–10).

---

## X path (required for the 11:23 AM original)

### What works today
Past X posts (see `content/published/2026-10-13-x-posts.md`, `…-10-14-x-posts.md`) went out via the **signed-in box browser** as @OrbBuilds. Re-checked tick 106 ~7:46 AM MT: **Composio `twitter` toolkit has no active connection**, so `TWITTER_UPLOAD_LARGE_MEDIA` / `TWITTER_CREATION_OF_A_POST` are not usable until someone connects that toolkit. Do not start a connect from growth mid-session unless the operator already approved it.

### Steps (computerUse / signed-in browser)
1. Open `https://x.com/compose/post` while logged in as @OrbBuilds.
2. Attach the local file `…-ultramarine-1-flash-xclip.mp4` (file picker → box path above). Wait until the preview plays / upload finishes.
3. Paste the caption exactly. Post once.
4. If X shows the graduated-access / human-check notice after send, stop (same as text posts). Do not retry the video.
5. Copy the status URL into GROWTH_LOG. Optional self-reply with the site URL only.
6. If attach fails (picker, size, encode): **do not** burn the session on a second video attempt — fall back to U3b text from `fable-5-5-drop-day-plan.md` if Fable 5.5 is still unannounced, else skip the original.

### Future (not for this morning unless connected)
Composio plan once `twitter` is ACTIVE: stage the mp4 via `COMPOSIO_REMOTE_WORKBENCH` → `TWITTER_UPLOAD_LARGE_MEDIA` (`media_category: tweet_video`) → poll `TWITTER_GET_MEDIA_UPLOAD_STATUS` until `succeeded` → `TWITTER_CREATION_OF_A_POST` with `media_media_ids`. Connecting Twitter is an operator decision; leave it off the critical path for today.

---

## Bluesky path (10 AM–2 PM MT window)

Creds: `/home/box/secrets/bluesky.txt` (handle `orbbuilds.bsky.social`). Email confirmed True (tick 103). Do not print the password into logs or chat.

Official flow (docs.bsky.app /docs/tutorials/video, fetched tick 106):
1. `createSession` on the account PDS (`https://bsky.social`).
2. `getServiceAuth` with `aud: did:web:<pds-host>`, `lxm: com.atproto.repo.uploadBlob`, `exp` ~30 min out.
3. `POST https://video.bsky.app/xrpc/app.bsky.video.uploadVideo?did=<did>&name=2026-10-14-ultramarine-1-flash-xclip.mp4` with `Authorization: Bearer <service-token>`, `Content-Type: video/mp4`, raw bytes body.
4. Poll `app.bsky.video.getJobStatus` on `video.bsky.app` until `jobStatus.blob` is present (or state failed → abort, fall back to text Welcome A only if no video went out on X either and the profile is still empty).
5. `com.atproto.repo.createRecord` `app.bsky.feed.post` with `embed: { $type: "app.bsky.embed.video", video: <blob>, aspectRatio: { width: 1080, height: 1920 } }` and the caption as `text`.
6. Log the `at://` URI / public URL in GROWTH_LOG as surface `bluesky`, tag `V`.

Notes:
- Prefer `@atproto/api` / `AtpAgent` if installed on the box; otherwise the same XRPC calls via curl/python are fine.
- Known server bug (atproto#4231, Sep 2025): some valid MP4s fail format detection (`detected file format ()`). Our clip is plain h264/aac 1080×1920; if upload 400s with that message, skip Bluesky video for the day rather than re-encoding mid-session.
- Still ≤1 Bluesky post this morning.

---

## Hard bans
- No posts from the continuous-strategy routine.
- No YouTube upload, no invented videoId, no "first on YouTube" claim in the caption.
- No Composio Twitter connect card mid-growth unless the operator already said yes.
- No second X original within ~4h (tick 71).
