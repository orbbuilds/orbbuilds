# Oct 16 post-publish first-read — strategy ticks after ~1:28 AM MT

Status: draft only (audience-strategy **tick 195**, Oct 15 ~11:19 PM MT; RSS fallback **tick 196** ~11:25 PM MT). Not an upload. Use this as the **first** checklist any continuous-strategy tick runs after the Oct 16 publish window opens. Do not invent videoIds or error strings.

Companion: `2026-10-16-0128-publish-brief.md` (owner sheet) · `2026-10-16-publish-recovery.md` (staging/fail) · morning ping `2026-10-16-user-decision-brief.md` · growth `2026-10-16-morning-growth-playbook.md`.

## Order (do not skip)

1. **Run log first.** Read `content/published/queue/run-log-2026-10-16.md` if it exists. Last line = last step reached. If the file is missing, the run died before Step 0 or skipped breadcrumb — log that exact fact; do not guess a YouTube error.
2. **Public channel check (zero Composio units).** Prefer `https://www.youtube.com/@orbbuilds/videos` (browser UA) and collect unique `videoId` values from the page (tick 196: Atom RSS `feeds/videos.xml?channel_id=UCGDWizzAvdre6ohhFG--CdA` returned **500** from the box; do not treat RSS failure as "channel empty"). Match titles via watch-page/`oEmbed` to Ep4 / Ep3 / Ep2; copy real videoIds only. Known pre-publish baseline (tick 196 ~11:25 PM MT Oct 15, watch-page): Ep0 `aCvkp11w9_8` **6** views, Ep1 `L7fdRoNWEPE` **9** views — only those two live.
3. **Queue status lines.** Open Ep4 → Ep3 → Ep2 queue files. Expect `PUBLISHED <id>` or `FAILED (<exact error>)` / `CARRIED …`. If Status is still READY and RSS has no new id, the run may still be in flight or failed silent — wait one more tick or note "no run-log + still READY".
4. **Ep4 confirm (when live).** Title still setup-first (`An AI sets up Hermes Agent with no API key`). Log pattern **P5+setup**, publish time MT, `GA: 2026-10-14 03:21 UTC`, hours GA→publish into GROWTH_LOG. Short title if uploaded: `Hermes Agent v0.22 setup in 55 seconds (no API key)`.
5. **Rank note.** Slot rule 2c: Ep4 was supposed to be upload #1. If Ep3/Ep2 went up and Ep4 did not, say so plainly (do not invent cause). If Ep4 + Short both live, drop Ep4 from any "still CARRIED" lists in morning drafts.
6. **Quiet hours.** Before ~8 AM MT: update strategy Last tick + GROWTH_LOG only; **no WakeParent** unless Ep4 cannot be recovered and a human decision is required tonight. At/after ~8 AM MT: Step 0 of `2026-10-16-user-decision-brief.md`, fill A/B/C status from this read, then WakeParent once.
7. **Hard bans.** No mid-day YouTube upload retries on shared quota. No Muse signup/Together spend. No Mastodon. No vs-Grok-Bot retitle. No posts/replies/DMs from this routine.

## FILL after the read (paste into Last tick)

```
Ep4: live? Y/N  videoId=…  title=…  Short? Y/N
Ep3: live? Y/N  videoId=…
Ep2: live? Y/N  videoId=…
run-log last line: …
exact fail (if any): …
GA→publish hours (Ep4): …
```

## Later same day (not this sheet)

- ~10 AM MT: Muse SERP + X vs tick-194 thresholds (`ep5-muse-spark-open-title-pack.md`); pick P2 vs Ling (P3 only with Together $15 OK).
- ~11:23 AM: morning growth playbook branch A if Ep4 live.
- ~10 AM–noon: Ep1 Analytics only if daytime units allow (tick 125).
