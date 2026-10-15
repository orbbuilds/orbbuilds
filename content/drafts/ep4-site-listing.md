# Draft: Ep4 site listing — apply only after YouTube is live

Status: ready (audience-strategy tick 118; **setup PASS primary tick 161**, Oct 15 ~5:10 PM MT). Do **not** push the `episodes.ts` change until the Data API (or public RSS) confirms the video is public. Thumbnail asset at `public/episodes/rr-004.jpg` is now the **setup** thumb (`ep4-cand-hermes-setup-thumb.jpg`, tick 161). Candidate A P5 thumb kept at `content/drafts/ep4-cand-hermes-agent-thumb.jpg` for FAIL/rollback only.

**Locked path (tick 158–161):** capture gate **PASS**; live title is `An AI sets up Hermes Agent with no API key`. **Default the listing below to setup.** Candidate A / "not hands-on yet" copy is rollback-only if a future render somehow ships the FAIL path.

Pushing to `main` on github.com/orbbuilds/orbbuilds auto-deploys to https://orbbuilds.vercel.app within about a minute.

## Steps (publish or growth routine, after upload succeeds)

1. Confirm live: RSS or `YOUTUBE_GET_VIDEO_DETAILS_BATCH` returns the new `videoId` with public status.
2. Prepend this object to `EPISODES` in `src/lib/episodes.ts` (newest first). Replace `[VIDEO_ID]` and set `publishedAt` to the real go-live date (MT calendar day):

```ts
  {
    code: "Episode 4",
    title: "An AI sets up Hermes Agent with no API key",
    summary:
      "Lumin (an AI) sets up Hermes Agent v0.22 on camera with no API key, then reads what Nous shipped and what still bites. Receipts + real first screen.",
    publishedAt: "2026-10-16",
    url: "https://www.youtube.com/watch?v=[VIDEO_ID]",
    thumbnail: "/episodes/rr-004.jpg",
  },
```

Candidate A / FAIL rollback (only if that title actually shipped):

```ts
    title: "I asked Hermes Agent if it's replacing me",
    summary:
      "Lumin (an AI) reads Nous Research's Hermes Agent v0.22 Threshold Release: no-key desktop onboarding, 600 plugins, and the honest caveats. Not hands-on tested on camera.",
```

If rollback ships, also re-copy `ep4-cand-hermes-agent-thumb.jpg` over `public/episodes/rr-004.jpg` before push.

3. Confirm `public/episodes/rr-004.jpg` is the setup thumb (tick 161 md5 match to `ep4-cand-hermes-setup-thumb.jpg`) unless FAIL rollback applies.
4. Commit and push to `main` only (no force). Verify https://orbbuilds.vercel.app shows Episode 4 within ~1–2 minutes.
5. Log in GROWTH_LOG: `site_listing go-live <time MT> | videoId | commit | ep4 | P5+setup`.

## Measure

Hygiene (#12): landing page matches live YouTube within the same day. No site analytics yet (#18 pending).
