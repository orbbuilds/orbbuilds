#!/usr/bin/env python3
"""YouTube search-autocomplete check (public suggestqueries, no API quota).

usage:
  youtube_autocomplete.py "ultramarine 1 flash" ["paper instruments"] ...
  youtube_autocomplete.py --check-tags "Ultramarine 1 Flash" "Ultramarine 1 Flash AI model"

Prints suggestions per query. Exit 0 always (advisory). Use before locking
meta.tags / publish_title when the product name might collide with another niche
(see docs/AUDIENCE_STRATEGY.md experiment #8).
"""
from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; OrbBuildsAutocomplete/1.0)"
URL = "https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q={q}"

# Phrases that often mean the product name is colliding with another niche
COLLISION_HINTS = (
    "warhammer",
    "ultramarines",
    "iphone",
    "color",
    "colour",
    "paint",
    "painting",
    "movie",
    "lore",
    "battle report",
    "successor",
)


def suggest(q: str) -> list[str]:
    req = urllib.request.Request(URL.format(q=urllib.parse.quote(q)), headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=15) as r:
        data = json.loads(r.read().decode("utf-8", errors="replace"))
    # firefox client: [query, [suggestions...], ...]
    if isinstance(data, list) and len(data) > 1 and isinstance(data[1], list):
        return [str(s) for s in data[1]]
    return []


def looks_colliding(suggestions: list[str], product: str) -> bool:
    """True when suggestions ignore the product and point at another niche."""
    if not suggestions:
        return True  # no demand formed yet — treat as search-weak
    # Any hard niche hit (Warhammer, iPhone color, etc.) is enough.
    hard = sum(1 for s in suggestions if any(h in s.lower() for h in COLLISION_HINTS))
    if hard >= 1:
        return True
    # Also colliding when suggestions drop distinctive tokens from a multi-word product
    # (e.g. "ultramarine 1 flash" → painting results with no "1" / "flash").
    tokens = [t for t in product.lower().split() if len(t) > 1 and t not in {"the", "an", "a", "of"}]
    if len(tokens) >= 2:
        kept = 0
        for s in suggestions:
            sl = s.lower()
            if sum(1 for t in tokens if t in sl) >= 2:
                kept += 1
        if kept == 0:
            return True
    return False


def main(argv: list[str]) -> int:
    args = argv[1:]
    check_tags = False
    if args and args[0] == "--check-tags":
        check_tags = True
        args = args[1:]
    if not args:
        print(__doc__.strip(), file=sys.stderr)
        return 2

    any_collision = False
    for q in args:
        try:
            sug = suggest(q)
        except Exception as e:
            print(f"ERROR {q!r}: {e}", file=sys.stderr)
            continue
        print(f"q={q!r}")
        if not sug:
            print("  (no suggestions)")
            any_collision = True
            print("  -> WARN: no autocomplete demand; keep full product name + 'AI' in title/tags; don't score as a search (#8) test")
            continue
        for s in sug:
            print(f"  - {s}")
        if looks_colliding(sug, q):
            any_collision = True
            print("  -> WARN: suggestions look like a name collision or off-niche; use full product string + 'AI model' in tags; never bare ambiguous words")
        else:
            # surface review/vs/setup cues when present
            cues = [s for s in sug if any(w in s.lower() for w in ("review", " vs", "vs ", "test", "demo", "benchmark", "setup", "tutorial"))]
            if cues:
                print("  -> OK cues to put in tags (and title only if the video delivers): " + "; ".join(cues[:5]))
            else:
                print("  -> OK (no obvious collision in this sample)")

    if check_tags and any_collision:
        print("\nchecklist: prefer tags like '<Product> AI model', '<Lab> AI'; drop bare colliding words (e.g. Ultramarines)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
