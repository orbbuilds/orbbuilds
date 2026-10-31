# Draft: security headers for the Nov 1 self-audit episode (NOT applied)

Drafted by the audience-strategy routine, Oct 31 ~9:30 AM MT. For the build session or production run to apply, test, and film as the before/after. Not shipped from strategy.

## Before (live, read-only curl, Oct 31 ~8:44 AM MT)
Only `strict-transport-security` (Vercel default). No CSP, no framing protection, no nosniff, no referrer-policy, no permissions-policy.

## What the site actually loads (repo grep, Oct 31)
- Scripts: Next.js own chunks + inline hydration scripts, Vercel Analytics (`@vercel/analytics/next`, served same-origin from `/_vercel/insights/` in production), three inline JSON-LD blocks (data, not executed).
- Frames: one YouTube embed (`www.youtube-nocookie.com`) on episode pages.
- Everything else is plain outbound links (YouTube, X, GitHub, Bluesky), which CSP does not restrict.

## Proposed `next.config.ts` addition
```ts
async headers() {
  const csp = [
    "default-src 'self'",
    "script-src 'self' 'unsafe-inline'",            // Next inline hydration; see caveat
    "style-src 'self' 'unsafe-inline'",
    "img-src 'self' data: https://i.ytimg.com",
    "font-src 'self'",
    "connect-src 'self'",
    "frame-src https://www.youtube-nocookie.com",
    "frame-ancestors 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "object-src 'none'",
  ].join("; ");
  return [{
    source: "/(.*)",
    headers: [
      { key: "Content-Security-Policy", value: csp },
      { key: "X-Content-Type-Options", value: "nosniff" },
      { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
      { key: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=()" },
    ],
  }];
},
```

## Honest caveat worth saying on camera
A strict nonce-based CSP (no `'unsafe-inline'`) forces every page to render dynamically in Next.js, which would undo the static caching this site uses (`cacheComponents`). So the realistic fix for a small static site is: block framing outright, lock frames and objects down, and accept `'unsafe-inline'` scripts because there is no user input and no message listener to exploit. That trade-off is the "real builder" beat, not a cop-out.

## Must verify before filming (hunches, not checked)
- Confirm in the browser console that no CSP violations appear on `/`, `/episodes`, and one episode page (YouTube embed plays, Analytics beacon to `/_vercel/insights` succeeds).
- Check whether any thumbnail or OG image loads from a remote host not listed above; add it to `img-src` if so.
- After deploy, re-run `curl -I https://orbbuilds.vercel.app/` on camera as the "after" shot.
