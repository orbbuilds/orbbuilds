#!/usr/bin/env python3
"""Fill (or refuse) the Short description's full-episode URL placeholder.

  fill_short_episode_url.py <short-meta.json> --url https://www.youtube.com/watch?v=VIDEOID
  fill_short_episode_url.py <short-meta.json> --video-id VIDEOID
  fill_short_episode_url.py <short-meta.json> --check   # exit 1 if placeholder still present

The generator writes [PASTE_FULL_EPISODE_URL_AFTER_UPLOAD] because the main
episode videoId does not exist until after upload. Publish must run fill
(or an equivalent replace) before YOUTUBE_MULTIPART_UPLOAD_VIDEO on a Short.
Never upload a description that still contains the placeholder token.
Audience-strategy tick 200 / experiment #5/#13.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PLACEHOLDER = "[PASTE_FULL_EPISODE_URL_AFTER_UPLOAD]"
WATCH_RE = re.compile(
    r"^https://(?:www\.)?youtube\.com/watch\?v=([A-Za-z0-9_-]{11})(?:&.*)?$"
)
ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


def to_watch_url(url_or_id: str) -> str:
    s = (url_or_id or "").strip()
    if ID_RE.match(s):
        return f"https://www.youtube.com/watch?v={s}"
    m = WATCH_RE.match(s)
    if m:
        return f"https://www.youtube.com/watch?v={m.group(1)}"
    raise SystemExit(
        f"need a 11-char videoId or https://www.youtube.com/watch?v=… URL, got: {s[:80]!r}"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("meta_json", type=Path)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--url", help="full watch URL")
    g.add_argument("--video-id", help="11-char YouTube videoId")
    g.add_argument(
        "--check",
        action="store_true",
        help="exit 0 if no placeholder; exit 1 if still present (no write)",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="print filled description to stdout; do not write the JSON",
    )
    args = ap.parse_args()

    path: Path = args.meta_json
    data = json.loads(path.read_text())
    desc = data.get("description") or ""

    if args.check:
        if PLACEHOLDER in desc:
            print(f"FAIL: {path} still has {PLACEHOLDER}", file=sys.stderr)
            return 1
        print(f"OK: {path} has no episode-URL placeholder")
        return 0

    watch = to_watch_url(args.url or args.video_id)
    if PLACEHOLDER not in desc:
        # Already filled, or never had one — refuse to rewrite blindly.
        if watch in desc:
            print(f"OK: {path} already links {watch}")
            return 0
        print(
            f"FAIL: {path} has no {PLACEHOLDER} to replace "
            f"(and does not already contain {watch})",
            file=sys.stderr,
        )
        return 1

    filled = desc.replace(PLACEHOLDER, watch)
    if PLACEHOLDER in filled:
        print("FAIL: placeholder still present after replace", file=sys.stderr)
        return 1
    if args.dry_run:
        print(filled)
        return 0

    data["description"] = filled
    data["full_episode_url_filled"] = watch
    path.write_text(json.dumps(data, indent=2) + "\n")
    print(f"filled: {path} → {watch}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
