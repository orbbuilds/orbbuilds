# Site analytics plan (experiment #18, tick 81, Oct 15 ~3:35 AM MT)

Status: **DRAFT, needs operator OK.** Nothing enabled, installed or pushed.

## Why
orbbuilds.vercel.app is linked from every YouTube description footer (#14), the X/Bluesky bios and the site listing step (#12), but the site has no analytics, so we can't tell whether any of those links send anyone. GROWTH_LOG says "no analytics yet".

## Option chosen: Vercel Web Analytics (free tier)
Source: https://vercel.com/docs/analytics/limits-and-pricing (fetched Oct 15, 2026 ~3:33 AM MT).
- Hobby: **50,000 events/month included**, free, cannot be billed. Over the limit, collection pauses (3-day grace), no charge.
- Hobby reporting window: **1 month**. So copy the numbers into GROWTH_LOG at each weekly review, or they age out.
- Hobby has **no UTM parameter support and no custom events**. Source attribution has to come from the referrer column (youtube.com, t.co/x.com, bsky.app, github.com), not `?utm_` tags. Don't add UTM links; they'd do nothing on Hobby.
- Events are shared across every project in that Vercel account.

## What it takes
1. **Dashboard toggle (operator or a signed-in browser session):** the Orb Builds Vercel project, Analytics tab, Enable. The Vercel CLI on the box is logged in to a *different* team that has no `orbbuilds` project (checked tick 81), so this can't be done from the CLI, and that other account must not be used or named publicly.
2. **Repo change (after the toggle):** `npm i @vercel/analytics`, then in `src/app/layout.tsx` add `import { Analytics } from "@vercel/analytics/next";` and render `<Analytics />` just before `</body>`. Push to main (auto-deploys in ~1 min). Before the toggle, the script just 404s, so order doesn't break anything, but toggle first keeps it clean.
3. **Privacy note for the site footer (optional):** Vercel Web Analytics is cookieless; one line like "Anonymous page-view counts via Vercel Web Analytics" keeps us honest.

## How to measure
- Weekly (Friday review): visitors, page views, top referrers, top pages (`/`, `/episodes`, `/log`). Log in GROWTH_LOG with the date read.
- Per episode: referrer `youtube.com` visits in the 72h after each upload, next to that episode's views. That's the first real number for whether the #14 footer gets clicks.
- Don't claim causes off a 1-month Hobby window with single-digit traffic; record, wait for ≥3 episodes.
