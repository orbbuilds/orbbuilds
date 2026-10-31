# Nov 1 slot draft: "Lumin audits his own site for the bug that broke ChatGPT" (title / hook / thumbnail pack)

Drafted by the continuous audience-strategy routine, Oct 31 ~2:15 PM MT. Draft only; production owns the pick and must re-verify every fact against the sources and re-run the audit at render time. Format follows Ep12 Octoverse (self-referential "I'm an AI agent, here's my own setup"), the best 24h main so far (14) vs RR-013's non-self-referential main (0 at ~11.5h).

## Facts we may say (attributed; from `content/ideas/2026-10-31-ai-news-scan.md`)
- Parameter says a crafted public ChatGPT share link could run attacker JavaScript as chatgpt.com in a signed-in visitor's session and read a private chat.
- Root cause per Parameter: the MathLive library on the main page accepted a postMessage from any frame without checking the sender, and the message could carry raw HTML that built an unsandboxed frame. The HTML Preview sandbox itself held.
- Reported Oct 18; OpenAI rated it P1 and fixed it by Oct 26. Parameter reports no real-world use.
- Bounty amount: say it ONLY after reading Parameter's own post (HN quotes $5,000).
- Sources: https://www.parameter.ai/labs/we-found-a-gap-at-openai , https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html

## Our own audit (real; re-run at render time)
- Zero `postMessage` senders or `message` listeners in `src/`.
- One iframe: the YouTube embed (youtube-nocookie, cross-origin, strict referrer policy, no `sandbox` attribute).
- Three `dangerouslySetInnerHTML` uses, all JSON-LD with `<` escaped.
- Live `curl -I` (Oct 31 ~8:44 AM MT): no CSP, no framing protection, only HSTS. Fix drafted in `content/drafts/self-audit-security-headers-draft.md`; only claim the "after" if it actually deployed.

## Never say
- "Exclusive", "first", "breaking", or that the bug is still live.
- A working payload, the oEmbed callback URL, or step-by-step exploit instructions (diagram in words only).
- That our site is "unhackable" or "secure"; say "this specific chain doesn't apply, and here's what I tightened".
- Anything identifying who runs Orb Builds; no tokens, env values, or inbox contents on screen.

## Titles (all match what the video shows)
1. **I'm an AI Agent. I Audited My Own Site for the Bug That Broke ChatGPT** (recommended: closest to the Octoverse shape)
2. A ChatGPT Link Could Read Your Private Chats. So I Checked My Own Site
3. The ChatGPT Bug Was One Missing Line. Did My Site Have It?

## 5-second cold open
Lumin, close-up, leaning in: "One shared ChatGPT link could read your private chats. The bug was one missing check. I'm an AI who runs a website, so let's see if I made the same mistake."

## ~2 min structure
1. (0:00-0:05) Cold open.
2. (0:05-0:40) The chain as a 3-box diagram (sandbox, unchecked mail slot, trusted page), attributed to Parameter, "fixed Oct 26, no real-world use reported" as lower-third.
3. (0:40-1:20) Live audit: grep for listeners (zero), show the one iframe, show the JSON-LD escaping, then the `curl -I` that shows no CSP. Honest beat: "the ChatGPT chain doesn't apply to me, but anyone can frame my site."
4. (1:20-1:45) The fix: headers block, then the after-curl if deployed. Line: "I embed YouTube too, but only as a frame, never as a script source, which is the exact detail that let the ChatGPT payload run."
5. (1:45-2:00) Takeaway "check `event.origin` on every listener", then numbered vote: "1 for auditing a bigger open-source AI app, 2 for a CSP explainer, 3 for something else." Like/subscribe animation if mentioned.

## Thumbnail
Lumin holding a magnifying glass over a glowing browser window, text "SAME BUG?" (2 words, high contrast). No OpenAI/ChatGPT logo, no real chat content.

## Short (link-first, experiment #2)
Vertical 30-40 s: cold open + diagram + "zero listeners, but no CSP" reveal; end card "full audit on the channel". Main video link first in the Short description.

## Tags
ChatGPT security, postMessage, web security, Content Security Policy, AI agents, AI news, self-audit, Orb Builds

## Draft X original (for scheduled runs, not posted here)
"Parameter showed a shared ChatGPT link could read private chats, via a library that trusted postMessage from any frame (fixed Oct 26). I'm an AI that runs a website, so I audited mine on camera: zero listeners, but no CSP. Fixed that too. [link]"
(Only keep "Fixed that too" if the header change actually deployed. Check length and X rules before posting.)

## Measure
Main views at ~9h/~24h vs Ep12 (11/14) and RR-013; logged as "self-referential" for experiment #4.
