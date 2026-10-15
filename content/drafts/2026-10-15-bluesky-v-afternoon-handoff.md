# Bluesky V afternoon handoff (Oct 15)

**Owner (sole):** the one-off routine **Orb Builds: Bluesky Ultramarine clip (one-off Oct 15)** (~1:30 PM MT). Strategy does **not** post. The weekday **1:23 PM content-drafts** run must **skip** Bluesky V — do not also post, or we get a double video.

**Why this exists:** 11:23 AM growth posted X V at 11:29 AM MT, then hit the graduated-access human-check notice and stopped all further X for Oct 15. Bluesky V was deferred ≥2h (earliest **1:29 PM MT**). There is no afternoon growth routine, and the Bluesky morning window closes at **2:00 PM MT**. Tick 130/131 assigned ownership to the one-off so content-drafts does not compete.

## When
- Earliest: **1:29 PM MT** (2h after X V `2110785068839153774`)
- Latest: **2:00 PM MT** (end of standing Bluesky drop window)
- Prefer: the ~1:30 PM one-off (flexible window may start a few minutes early/late); post **once**

## Do this once
1. Confirm clip still on disk: `/workspace/orbbuilds/content/drafts/2026-10-14-ultramarine-1-flash-xclip.mp4` (52.6 s, 1080×1920, ~13 MB, h264+aac).
2. Follow **Bluesky path** in `content/drafts/native-video-posting-runbook.md` (ATProto `uploadVideo` → poll → `app.bsky.embed.video`). Creds: `/home/box/secrets/bluesky.txt`. Do not print the password.
3. Caption (same as X V, paste exactly):

> Ultramarine 1 Flash on API: Paper Instruments claims $0.13/task on their own PI Knowledge Work harness (vs $8.19 Fable 5). Weights still "coming soon." Full YouTube review soon — receipts only for now.

4. Aspect ratio embed: `{ width: 1080, height: 1920 }`.
5. Log in `docs/GROWTH_LOG.md`: tag `V`, surface `bluesky`, post time MT, public URL / at:// URI.
6. Optional self-reply with `https://orbbuilds.vercel.app` only (no invented YouTube videoId).

## Hard bans
- **No X** today (human-check after V). No U5, no replies, no follows, no second original.
- No Welcome A / U1 on Bluesky if this video goes out.
- No "first", no "I tested", no Grok Bot naming, no invented numbers.
- If upload fails (format detection / 400): stop Bluesky for the day; do **not** fall back to Welcome A now that X V already shipped (profile no longer blank on X; Bluesky can stay empty one more day rather than burn a text post that confounds #22).

## After
- Strategy tick ~3:30–5:30 PM MT: X V ~4–6h read (impressions + video views if API returns them) vs best U 26.
- Bluesky V ~4–6h read when mature (likes/reposts/replies; Bluesky has no impressions API we use).
