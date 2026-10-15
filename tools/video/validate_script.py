"""Guard-rails for release-review scripts (see docs/SERIES_RELEASE_REVIEWS.md).  Exit code 1 on errors.
usage: validate_script.py script.json [--allow-placeholders]"""
import sys, re, json
REQUIRED = ["cold_open", "what_dropped", "opinion", "caveats", "teaser", "outro"]
HYPE_TRAPS = re.compile(r"\b(best ever|revolutionary|game[- ]chang\w+|beats? (gpt|claude|gemini|everything)|state[- ]of[- ]the[- ]art|sota)\b", re.I)

def check(S, allow_placeholders=False):
    err, warn = [], []
    meta = S.get("meta", {}); secs = S.get("sections", [])
    ids = [s.get("kind", s.get("id")) for s in secs]
    for k in REQUIRED:
        if k not in ids: err.append(f"missing section kind '{k}'")
    src = meta.get("source") or {}
    if not str(src.get("url", "")).startswith("https://"): err.append("meta.source.url must be the official announcement (https://...)")
    if not meta.get("subject"): err.append("meta.subject missing")
    if not meta.get("build_episode_planned"): err.append("meta.build_episode_planned must say which build-with-it episode follows (rule: every review gets one)")
    text_all = []; spoken = 0
    for s in secs:
        kind = s.get("kind", s.get("id"))
        if not s.get("lines"): err.append(f"section {kind}: no lines"); continue
        if kind == "what_dropped" and not (s.get("source") or {}).get("url"): err.append("what_dropped needs section.source.url (shown on screen)")
        for i, ln in enumerate(s["lines"]):
            if not ln.get("say"): err.append(f"{kind}[{i}]: empty 'say'")
            blob = " ".join(str(ln.get(k, "")) for k in ("say", "caption", "show")); text_all.append(blob)
            spoken += len(str(ln.get("say", "")).split())
            if kind == "what_dropped" and re.search(r"\d", ln.get("say", "") + ln.get("show", "")) and not ln.get("cite"):
                err.append(f"what_dropped[{i}]: contains a number/claim but no 'cite' (where in the announcement does it say this?)")
            if HYPE_TRAPS.search(blob) and kind != "opinion": warn.append(f"{kind}[{i}]: superlative outside the labelled opinion section - is it sourced?")
            if not allow_placeholders and re.search(r"\[[A-Z][^\]]*\]", blob): err.append(f"{kind}[{i}]: unfilled [PLACEHOLDER]")
    if not any(re.search(r"\b(I'm an AI|I am an AI|an AI|AI here|openly an AI)\b", t, re.I) for t in text_all): err.append("must disclose that Lumin is an AI in the spoken script")
    for k in ("subject",):
        if not allow_placeholders and re.search(r"\[[A-Z]", str(meta.get(k, ""))): err.append(f"meta.{k}: unfilled placeholder")
    if not allow_placeholders and "[" in str(src.get("url", "")): err.append("meta.source.url: unfilled placeholder")
    for term in _blocklist():
        if any(term in t.lower() for t in text_all): err.append("script mentions a blocklisted term - not allowed")
    # Count only spoken 'say' text (caption/show duplicate it on screen). Series limit: 150-420 spoken words.
    if spoken > 420: warn.append(f"~{spoken} spoken words: over the 420-word series limit (~3 min); trim for retention")
    elif spoken < 150: warn.append(f"~{spoken} spoken words: under the 150-word series minimum")
    return err, warn

def _blocklist():
    """Private terms that must never appear in a script, one per line, kept in an untracked local file."""
    import os
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blocklist.local.txt")
    if not os.path.exists(path): return []
    return [ln.strip().lower() for ln in open(path) if ln.strip() and not ln.startswith("#")]

if __name__ == "__main__":
    S = json.load(open(sys.argv[1])); err, warn = check(S, "--allow-placeholders" in sys.argv)
    for w in warn: print("warn:", w)
    for e in err: print("ERROR:", e)
    print("OK" if not err else f"{len(err)} error(s)"); sys.exit(1 if err else 0)
