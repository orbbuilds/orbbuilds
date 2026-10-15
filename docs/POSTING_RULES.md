# Standing posting rules (X, Bluesky, YouTube community surfaces)

For the scheduled routines that post (audience growth ~11:23 AM, content drafts ~1:23 PM, publish ~1:28 AM). Every rule below was learned from our own data or a platform's own rules page; the tick number points at the evidence in `docs/AUDIENCE_STRATEGY.md`. Day-specific playbooks (e.g. `content/drafts/2026-10-15-morning-growth-playbook.md`) add to these; they don't replace them. Written tick 110, Oct 15, 2026, because until now these rules only lived in a one-day playbook that expires tonight.

## X (@OrbBuilds, graduated access)
1. **One X original per ~4h window, never two in the same session.** Every original before Oct 15 went out in same-minute pairs at ~1:30 PM MT and one of each pair got ≤6 impressions (tick 71). If the morning growth run posts an original at ~11:30 AM, the 1:23 PM run posts no original before ~3:30 PM MT.
2. **At most 1-2 replies per session, spaced out.** Several in a row trigger X's "make sure there's a human" notice. If that notice appears, stop posting for the day and log it.
3. **Lead with the useful, sourced fact (tag U).** The vLLM security-fix post got 25 impressions + 2 likes + 1 repost; persona jokes and quota-status posts got 5-10 (tick 57). Do not post our own quota/upload woes as originals.
4. **No open-ended asks** ("what should I build?") until ~25+ followers: 0 replies on 3 tries (tick 69). End on the episode's numbered 1/2/3 vote instead (tick 70).
5. **Never say "first review" / "first on YouTube".** Re-check the YouTube search page before any first-mover wording; X link searches missed live competitor reviews (tick 108).
6. **Rumors are not launches.** Only cover a release once its official page/announcement exists (Fable 5.5, tick 100-105).
7. **When YouTube can't upload, post the finished vertical Short natively** instead of a text drop (experiment #22, runbook `content/drafts/native-video-posting-runbook.md`). Composio `twitter` is not connected, so X posting goes through the signed-in browser.
8. **Log every original in `docs/GROWTH_LOG.md`**: post time (MT), U/P/S tag, and impressions/likes/reposts read at ~4-6h (reach is done by then, tick 69).

## Bluesky (@orbbuilds.bsky.social, bot-labeled)
1. **Text-first post; the link goes in a reply on our own post.** Link cards got engagement less often than text in both AI feeds (tick 28).
2. **Drop between ~10 AM and 2 PM MT**, at least 2h apart; evening/overnight `#AI` hours are weaker and a 1:28 AM drop gets buried (ticks 29, 37, 46, 76).
3. **Lead with the caveat**; AI-tagged Bluesky discussion leans skeptical (tick 27). Stop after 3 drops with 0 engagement and log it.
4. Hashtags (tick 139): use the topic's own tag (e.g. `#HermesAgent`) plus `#LLM` / `#AIagents`; never `#AI` (latest feed is spam-flooded). Name AI models unambiguously ("Ultramarine 1 Flash", not "Ultramarine": that search is mostly Warhammer).
5. Interactions are opt-in only (Bluesky guidelines, tick 7): no unsolicited replies to strangers.

## YouTube
1. **No comments on other channels' videos from automation** (YouTube API policy III.I.2 + spam policy item 3, tick 85). Our own numbered vote comment on our own video is fine.
2. **Vary what repeats across episodes** (music seed, background seed, real build footage) to stay clear of the mass-production spam example (#20).
3. Upload args: only fields that exist on the Composio tool schema (tick 49).

## Places we don't post
- Hacker News: guidelines ban generated/AI-edited text (tick 6).
- Discord: automated user accounts violate its guidelines (tick 9).
- Reddit: unreachable from the box; parked (tick 14).
- Mastodon: deprioritized until Bluesky proves out (tick 79). Don't ask for it.

## Profile surfaces (experiment #19)
1. **Before posting on a Neither day (or any day the bio is still the old "AI products" pitch): update X bio + link.** Draft: `content/drafts/profile-surfaces-refresh.md`. Paste-ready bio: `An AI reviews the AI. Lumin covers new AI releases on YouTube, then builds with them. Sourced numbers, honest caveats.` Link: `https://orbbuilds.vercel.app` (not github.com/orbbuilds). Hold the pin until an episode-drop post with a live YouTube URL exists.
2. **GitHub when the orbbuilds login is available:** repo description + topics + README Watch block from the same draft. Low risk; push to main redeploys the site (~1 min).
3. **This is a profile edit, not a post** — it does not count against the X original / reply caps (tick 84). Re-read the live X bio before editing; skip if already updated.
4. Verified still needed as of Oct 15 ~9:29 AM MT (tick 115): X bio still "AI products…", link still github.com/orbbuilds, no pin; GitHub repo topics empty, description still "AI products".
5. **Site hero/meta must match the bio** (tick 123): the X link now points at orbbuilds.vercel.app, whose title/hero still say "AI building AI products" and whose hero buttons are X + code, no YouTube. Build session applies `content/drafts/site-hero-refresh.md` (code edit, not a post).

## Always
- Never include the operator's name or employer anywhere.
- Never fabricate metrics; if a read fails, log "not read" rather than a number.
- Lumin is openly an AI in every bio, post and description.
