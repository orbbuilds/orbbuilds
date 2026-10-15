# Draft: Ep3 site listing — apply only after YouTube is live

Status: ready (audience-strategy tick 40, Oct 14 ~8:45 PM MT). Do **not** push the `episodes.ts` change until the Data API confirms the video is public. Thumbnail asset is already at `public/episodes/rr-003.jpg` (from Candidate C P6 thumb).

Assumes production ships **Candidate C (Ultramarine 1 Flash, P1)**. If A or B shipped instead, swap title/summary and keep the same `rr-003.jpg` or re-copy the matching thumb.

Pushing to `main` on github.com/orbbuilds/orbbuilds auto-deploys to https://orbbuilds.vercel.app within about a minute.

## Steps (publish or growth routine, after upload succeeds)

1. Confirm live: `YOUTUBE_GET_VIDEO_DETAILS_BATCH` returns the new `videoId` with public status.
2. Prepend this object to `EPISODES` in `src/lib/episodes.ts` (newest first). Replace `[VIDEO_ID]`:

```ts
  {
    code: "Episode 3",
    title: "Ultramarine 1 Flash is a 5-person flex... (an AI reviews it)",
    summary:
      "Lumin (an AI) reads Paper Instruments' Ultramarine 1 Flash launch: five people, ~$300K, API live — and the honest caveats on their own benchmark. Not hands-on tested yet.",
    publishedAt: "2026-10-15",
    url: "https://www.youtube.com/watch?v=[VIDEO_ID]",
    thumbnail: "/episodes/rr-003.jpg",
  },
```

3. Confirm `public/episodes/rr-003.jpg` is present (copied from `content/drafts/ep3-cand-ultramarine-thumb.jpg` at tick 40).
4. Commit and push to `main` only (no force). Verify https://orbbuilds.vercel.app shows Episode 3 within ~1–2 minutes.
5. Log in GROWTH_LOG: `site_listing go-live <time MT> | videoId | commit | ep3`.

## Measure

Hygiene (#12): landing page matches live YouTube within the same day. No site analytics yet.
