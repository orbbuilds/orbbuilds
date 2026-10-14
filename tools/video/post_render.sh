#!/usr/bin/env bash
# Post-render extras for a release-review episode (AUDIENCE_STRATEGY.md #5 and #6):
#   post_render.sh content/scripts/<script>.json <episode.mp4> [outdir]
# - Thumbnail: if meta.thumbnail = {product, line1, line2?, hl?, tag?} exists, renders <name>-thumb.jpg (P6 grammar).
# - Short: picks fact+verdict windows from timing.json and splices <name>-short.mp4 (vertical, <=58 s). Skip with NO_SHORT=1.
#   Appends the like/subscribe line (button-click animation) as an end card when it costs <=1 fact line; NO_SHORT_CTA=1 turns that off.
# Failures here only warn; they never block the main episode.
set -u
SCRIPT="$(realpath "$1")"; EP="$(realpath "$2")"; NAME="$(basename "$SCRIPT" .json)"
OUTDIR="$(realpath -m "${3:-$(dirname "$EP")}")"; mkdir -p "$OUTDIR"
cd "$(dirname "$0")"
WORK="/workspace/video-build/${NAME}"
THUMB_ARGS=$(python3 - "$SCRIPT" <<'PY'
import json, shlex, sys
t = json.load(open(sys.argv[1]))["meta"].get("thumbnail")
if not t or not t.get("product") or not t.get("line1") or "[" in json.dumps(t):
    sys.exit(0)
a = ["--product", t["product"], "--line1", t["line1"]]
for k in ("line2", "hl", "tag"):
    if t.get(k) not in (None, ""): a += ["--" + k, str(t[k])]
print(" ".join(shlex.quote(x) for x in a))
PY
)
if [ -n "$THUMB_ARGS" ]; then
  eval python3 thumbnail.py "$OUTDIR/${NAME}-thumb.jpg" $THUMB_ARGS \
    && echo "thumbnail: $OUTDIR/${NAME}-thumb.jpg" || echo "WARN: thumbnail failed" >&2
else
  echo "WARN: no meta.thumbnail (or placeholders left); thumbnail skipped" >&2
fi
if [ -z "${NO_SHORT:-}" ]; then
  CTA_FLAG="--cta"; [ -n "${NO_SHORT_CTA:-}" ] && CTA_FLAG=""
  WIN=$(python3 short_windows.py "$WORK/timing.json" $CTA_FLAG) || WIN=""
  if [ -n "$WIN" ]; then
    bash shorts_splice.sh "$EP" "$OUTDIR/${NAME}-short.mp4" $WIN \
      && echo "short: $OUTDIR/${NAME}-short.mp4 ($WIN)" || echo "WARN: short failed" >&2
  else
    echo "WARN: no short windows from $WORK/timing.json; short skipped" >&2
  fi
fi
