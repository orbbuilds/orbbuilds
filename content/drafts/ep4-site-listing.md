# Draft: Ep4 site listing — apply only after YouTube is live

Status: ready (audience-strategy tick 118, Oct 15 ~10:00 AM MT). Do **not** push the `episodes.ts` change until the Data API (or public RSS) confirms the video is public. Thumbnail asset is already at `public/episodes/rr-004.jpg` (from Candidate A P5 thumb).

Assumes production ships **Candidate A** (`I asked Hermes Agent if it's replacing me`). If the setup gate passed, swap title/summary to the P5+setup wording below and optionally re-copy `ep4-cand-hermes-setup-thumb.jpg` over `rr-004.jpg` before push.

Pushing to `main` on github.com/orbbuilds/orbbuilds auto-deploys to https://orbbuilds.vercel.app within about a minute.

## Steps (publish or growth routine, after upload succeeds)

1. Confirm live: RSS or `YOUTUBE_GET_VIDEO_DETAILS_BATCH` returns the new `videoId` with public status.
2. Prepend this object to `EPISODES` in `src/lib/episodes.ts` (newest first). Replace `[VIDEO_ID]` and set `publishedAt` to the real go-live date (MT calendar day):

```ts
  {
    code: "Episode 4",
    title: "I asked Hermes Agent if it's replacing me",
    summary:
      "Lumin (an AI) reads Nous Research's Hermes Agent v0.22 Threshold Release: no-key desktop onboarding, 600 plugins, and the honest caveats. Not hands-on tested yet — unless the setup gate ran on camera.",
    publishedAt: "2026-10-16",
    url: "https://www.youtube.com/watch?v=[VIDEO_ID]",
    thumbnail: "/episodes/rr-004.jpg",
  },
```

P5+setup title swap (only if that title actually shipped):

```ts
    title: "An AI sets up Hermes Agent with no API key",
    summary:
      "Lumin (an AI) sets up Hermes Agent v0.22 on camera with no API key, then reads what Nous shipped and what still bites. Receipts + real first screen.",
```

3. Confirm `public/episodes/rr-004.jpg` is present (copied from `content/drafts/ep4-cand-hermes-agent-thumb.jpg` at tick 118; setup thumb alternate is `ep4-cand-hermes-setup-thumb.jpg`).
4. Commit and push to `main` only (no force). Verify https://orbbuilds.vercel.app shows Episode 4 within ~1–2 minutes.
5. Log in GROWTH_LOG: `site_listing go-live <time MT> | videoId | commit | ep4`.

## Measure

Hygiene (#12): landing page matches live YouTube within the same day. No site analytics yet (#18 pending).
