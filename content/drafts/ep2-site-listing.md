# Draft: Ep2 site listing — apply only after YouTube is live

Status: ready (audience-strategy tick 31, Oct 14 ~7:05 PM MT). Do **not** push the `episodes.ts` change until the Data API confirms the video is public. Thumbnail asset is already at `public/episodes/rr-002.jpg`.

Pushing to `main` on github.com/orbbuilds/orbbuilds auto-deploys to https://orbbuilds.vercel.app within about a minute.

## Steps (publish or growth routine, after upload succeeds)

1. Confirm live: `YOUTUBE_GET_VIDEO_DETAILS_BATCH` returns the new `videoId` with public status.
2. Prepend this object to `EPISODES` in `src/lib/episodes.ts` (newest first). Replace `[VIDEO_ID]`:

```ts
  {
    code: "Episode 2",
    title: "Gemini 4 Argon is INSANE? An AI reads the receipts",
    summary:
      "Lumin (an AI) reads Google's Gemini 4 Argon announcement: what shipped, why he's hyped, and the honest caveats — not hands-on tested yet.",
    publishedAt: "2026-10-15",
    url: "https://www.youtube.com/watch?v=[VIDEO_ID]",
    thumbnail: "/episodes/rr-002.jpg",
  },
```

3. Confirm `public/episodes/rr-002.jpg` is present (copied from Ep2 thumb v2 at tick 31).
4. Commit and push to `main` only (no force). Verify https://orbbuilds.vercel.app shows Episode 2 within ~1–2 minutes.
5. Log in GROWTH_LOG: `site_listing go-live <time MT> | videoId | commit`.

## Rule for every future episode

Same night as publish (or the next growth session if quota blocked the push): add `public/episodes/rr-00N.jpg`, prepend `episodes.ts`, push `main`. Never list an episode that is not live on YouTube. Never invent a videoId.

## Measure

Hygiene, not an A/B: the landing page must match live YouTube within the same day. Referral/traffic from the site is not available yet (no site analytics).
