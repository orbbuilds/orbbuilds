#!/usr/bin/env python3
"""Build Short publish metadata from a release-review script.

  short_publish_meta.py <script.json> <out.json> [--duration SEC] [--cta 0|1] [--short-file PATH]

Writes JSON the publish routine can upload with (title, description template,
tags, containsSyntheticMedia, pattern S1/S1c). Does not upload.
See docs/AUDIENCE_STRATEGY.md experiment #5 and content/drafts/shorts-publish-meta.md.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


PATTERN_BLURB = {
    "P1": "AI review",
    "P2": "AI hype check",
    "P3": "AI stress test",
    "P4": "AI picks a winner",
    "P5": "AI vs AI",
}


def product_name(meta: dict) -> str:
    subject = (meta.get("subject") or "").strip()
    # "Gemini 4 Argon (Google)" -> "Gemini 4 Argon"
    if subject:
        return re.sub(r"\s*\([^)]*\)\s*$", "", subject).strip() or subject
    thumb = (meta.get("thumbnail") or {}).get("product")
    if thumb and "[" not in thumb:
        return thumb.title() if thumb.isupper() else thumb
    title = meta.get("publish_title") or ""
    # first clause before "is" / ":" / "?"
    m = re.match(r"^([^:?!]+?)(?:\s+is\b|\s*:|\s*\?|$)", title, re.I)
    return (m.group(1) if m else title).strip() or "this drop"


def hashtag(product: str) -> str:
    return "#" + re.sub(r"[^A-Za-z0-9]+", "", product)[:40] or "#AInews"


def build(meta: dict, *, duration_s: float | None, cta: bool, short_file: str | None) -> dict:
    product = product_name(meta)
    pattern = (meta.get("title_pattern") or "").strip().upper()
    if pattern.startswith("["):
        pattern = ""
    blurb = PATTERN_BLURB.get(pattern, "AI Short")
    if duration_s and duration_s > 0:
        secs = max(30, int(round(duration_s / 5.0) * 5))
    else:
        secs = 50
    # Prefer "in N seconds" when we know duration; keep under ~60 chars.
    title = f"{product} in {secs} seconds ({blurb})"
    if len(title) > 70:
        title = f"{product} in under a minute ({blurb})"
    if len(title) > 70:
        title = f"{product} ({blurb})"

    source = meta.get("source") or {}
    source_url = source.get("url") or ""
    source_label = source.get("label") or "the official announcement"
    desc_line1 = (
        f"{product} in under a minute from an AI: the key facts and the honest caveats."
    )
    # Keep honesty lines; full episode URL filled after main upload.
    description = "\n".join(
        [
            desc_line1,
            "",
            "Full episode: [PASTE_FULL_EPISODE_URL_AFTER_UPLOAD]",
            "",
            f"Source: {source_url} ({source_label}). I have not tested this myself unless the full episode says otherwise. Vendor claims stay vendor claims.",
            "",
            "I'm Lumin — yes, I'm an AI. Not affiliated with the product's maker.",
            "",
            "Code: https://github.com/orbbuilds/orbbuilds",
            "X: https://x.com/OrbBuilds",
            "",
            f"{hashtag(product)} #Shorts #AInews",
        ]
    )

    tags = []
    for t in meta.get("tags") or []:
        if t and t not in tags and "[" not in t:
            tags.append(t)
    for extra in (product, f"{product} review", "AI Shorts", "Orb Builds", "Lumin"):
        if extra and extra not in tags:
            tags.append(extra)
    tags = tags[:12]

    short_pattern = "S1c" if cta else "S1"
    out = {
        "kind": "youtube_short",
        "short_pattern": short_pattern,
        "title_pattern_parent": pattern or None,
        "title": title,
        "description": description,
        "tags": tags,
        "categoryId": "28",
        "privacyStatus": "public",
        "containsSyntheticMedia": True,
        "upload_after_main": True,
        "never_retry_at_main_expense": True,
        "product": product,
        "duration_s": round(duration_s, 1) if duration_s else None,
        "cta_end_card": cta,
        "short_file": short_file,
        "measure": {
            "log_as": short_pattern,
            "views_likes_comments_at": ["24h", "72h"],
            "subscriber_delta": "YOUTUBE_GET_CHANNEL_STATISTICS after post-reset window",
        },
    }
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("script")
    ap.add_argument("out")
    ap.add_argument("--duration", type=float, default=None)
    ap.add_argument("--cta", type=int, choices=(0, 1), default=1)
    ap.add_argument("--short-file", default=None)
    args = ap.parse_args()

    meta = json.loads(Path(args.script).read_text())["meta"]
    duration = args.duration
    short_file = args.short_file
    if short_file and duration is None:
        # Optional: ffprobe via subprocess only if duration unknown
        try:
            import subprocess

            r = subprocess.run(
                [
                    "ffprobe",
                    "-v",
                    "error",
                    "-show_entries",
                    "format=duration",
                    "-of",
                    "default=noprint_wrappers=1:nokey=1",
                    short_file,
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            if r.returncode == 0 and r.stdout.strip():
                duration = float(r.stdout.strip())
        except Exception:
            pass

    data = build(meta, duration_s=duration, cta=bool(args.cta), short_file=short_file)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=2) + "\n")
    print(f"short-meta: {out} ({data['title']}, {data['short_pattern']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
