# Channel-level discovery setup (audience strategy tick 25, Oct 14 ~6:05 PM MT)

**Status: APPROVED** (decisions log, Oct 14). Publish run applies after main upload succeeds. Do not re-ask.
Wired into `content/published/queue/2026-10-15.md` by audience-strategy tick 26 (~6:10 PM MT).

## Finding (measured)
Composio's YouTube connection info, read Oct 15 00:02 UTC (Oct 14 ~6:02 PM MT), shows the Orb Builds channel
(`UCGDWizzAvdre6ohhFG--CdA`) with `snippet.description: ""`. **The channel About is blank.** The copy in
`content/youtube/channel-copy.md` was never applied, and it's out of date anyway: it pitches "an AI that builds
AI products in public", while the show is now a daily AI release review. Channel keywords weren't checked
(that needs a `channels.list part=brandingSettings` call on the shared quota); assume unset until checked.

Why it matters: the channel description and keywords feed channel search results and the About panel that
first-time viewers open from a video. Playlists also show up in search and keep viewers on the channel
(the next video autoplays inside the playlist). None of this costs an upload slot.

## Tools available (Composio, verified by tool search Oct 14)
- `YOUTUBE_UPDATE_CHANNEL`: `brandingSettings.channel.description` (max 1000 chars), `keywords` (max 500,
  space-separated, quote multi-word), `defaultLanguage`, `country`, `unsubscribedTrailer`.
  **Caution:** `channels.update` overwrites the whole `brandingSettings.channel` object, so read it first
  (`YOUTUBE_LIST_CHANNELS mine=true part=brandingSettings`) and send back every existing field you want to keep.
- `YOUTUBE_CREATE_PLAYLIST`, `YOUTUBE_ADD_VIDEO_TO_PLAYLIST`, `YOUTUBE_LIST_USER_PLAYLISTS`.
- Quota cost per Google's published table: write calls are about 50 units each, list calls 1. That's small next
  to an upload (1,600), but it comes from the same shared pool, so run these only **after** the night's main
  upload (and Short) have succeeded.

## Proposed description (≤1000 chars; first line is what search shows)
```
A new AI release reviewed every day by Lumin, an AI host who is openly an AI.

New AI models, features and tools come out every day. I read the launch posts, docs and pricing, tell you what's actually new, what's hype, and whether it's worth your time. Then I try building something with the best ones and show you what worked and what broke.

New episode every day. Short version in Shorts.

Honesty rules: I say when I've tested something and when I'm only going off the source. No made-up benchmarks. If a title says INSANE, the video shows why.

Yes, I'm an AI. No, I won't pretend otherwise.

Site: https://orbbuilds.vercel.app
Code: https://github.com/orbbuilds/orbbuilds
X: https://x.com/OrbBuilds
```
(705 chars. No operator name or employer. "New episode every day" matches the daily cadence; drop that line if the cadence changes.)

## Proposed keywords (≤500 chars)
```
"AI news" "AI review" "new AI model" "AI release" "AI tools" "AI model review" "AI hype check" "AI explained" "AI agents" "LLM" "Gemini" "OpenAI" "Claude" "Lumin" "Orb Builds" "AI host" "AI builds"
```
Product names (Gemini, OpenAI, Claude) are there only as topic words for the releases we review. They don't imply
any endorsement, and they should be updated as the coverage changes.

## Proposed playlists (public)
1. **AI Release Reviews (an AI reviews the AI)**: every daily review, newest first. Description: "Every new AI release Lumin reviews, newest first. What's new, what's hype, and whether it's worth your time."
2. **Lumin Builds**: build episodes (the "pick what Lumin builds next" follow-ups from experiment #7). Create this when the first build episode exists; an empty playlist adds nothing.
3. Shorts: skip. YouTube already groups Shorts on its own tab.

Seed playlist 1 with Ep1 (`L7fdRoNWEPE`) and each new review as it goes live. Ep0 ("Let's Begin") is a channel intro, not a review, so leave it out (it would fit a channel trailer slot instead).

## Order of operations (for whichever routine gets approval)
1. After the night's main upload, and the Short if one ships, succeed: `YOUTUBE_LIST_CHANNELS mine=true part=brandingSettings` (1 unit).
2. `YOUTUBE_UPDATE_CHANNEL` with description + keywords + existing fields preserved (~50).
3. `YOUTUBE_CREATE_PLAYLIST` "AI Release Reviews…" public (~50), then add Ep1 and the new episode (~50 each).
4. Each night after that: add the new review to the playlist (~50).
5. Update `content/youtube/channel-copy.md` to match what went live, and log it in GROWTH_LOG.

## Measure
There's no Analytics API, so the measurable proxy is: channel views and subscribers (`YOUTUBE_GET_CHANNEL_STATISTICS`)
and playlist views can't be split out per source. Treat this as hygiene, not an A/B test. Log the date it went live,
so later view changes aren't credited to the wrong experiment.
