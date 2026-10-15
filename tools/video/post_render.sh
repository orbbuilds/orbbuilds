#!/usr/bin/env bash
# Post-render extras for a release-review episode (AUDIENCE_STRATEGY.md #5, #6, #22):
#   post_render.sh content/scripts/<script>.json <episode.mp4> [outdir]
# - Thumbnail: if meta.thumbnail = {product, line1, line2?, hl?, tag?} exists, renders <name>-thumb.jpg (P6 grammar).
# - Short: picks fact+verdict windows from timing.json and splices <name>-short.mp4 (vertical, <=58 s). Skip with NO_SHORT=1.
#   Appends the like/subscribe line (button-click animation) as an end card when it costs <=1 fact line; NO_SHORT_CTA=1 turns that off.
# - Short publish meta: writes <name>-short-meta.json (title/description/tags/S1c) for the publish routine. Skip with NO_SHORT_META=1.
# - Xclip: hook-first social cut <name>-xclip.mp4 (cold-open letterbox + caveats + CTA) for native X/Bluesky when YouTube is quota-blocked. Skip with NO_XCLIP=1.
# - Chapters: checks meta.publish_description chapters against timing.json (>=10 s each). Warn only.
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
SHORT_OUT=""
CTA_USED=0
if [ -z "${NO_SHORT:-}" ]; then
  CTA_FLAG="--cta"; [ -n "${NO_SHORT_CTA:-}" ] && CTA_FLAG=""
  WIN=$(python3 short_windows.py "$WORK/timing.json" $CTA_FLAG) || WIN=""
  if [ -n "$WIN" ]; then
    SHORT_OUT="$OUTDIR/${NAME}-short.mp4"
    if bash shorts_splice.sh "$EP" "$SHORT_OUT" $WIN; then
      echo "short: $SHORT_OUT ($WIN)"
      # Detect whether the CTA window was included (third start:end from --cta).
      if [ -n "$CTA_FLAG" ]; then
        NWIN=$(echo "$WIN" | wc -w | tr -d ' ')
        [ "$NWIN" -ge 3 ] && CTA_USED=1
      fi
    else
      echo "WARN: short failed" >&2
      SHORT_OUT=""
    fi
  else
    echo "WARN: no short windows from $WORK/timing.json; short skipped" >&2
  fi
fi
if [ -z "${NO_SHORT_META:-}" ]; then
  META_OUT="$OUTDIR/${NAME}-short-meta.json"
  META_ARGS=(python3 short_publish_meta.py "$SCRIPT" "$META_OUT" --cta "$CTA_USED")
  # Prefer an existing CTA Short next to drafts if we didn't just render one with CTA.
  if [ -n "$SHORT_OUT" ] && [ -f "$SHORT_OUT" ]; then
    META_ARGS+=(--short-file "$SHORT_OUT")
  fi
  "${META_ARGS[@]}" && echo "short-meta: $META_OUT" || echo "WARN: short-meta failed" >&2
fi
# Hook-first social cut for X/Bluesky native video (AUDIENCE_STRATEGY #22, tick 121).
if [ -z "${NO_XCLIP:-}" ] && [ -f "$WORK/timing.json" ]; then
  XWIN=$(python3 xclip_windows.py "$WORK/timing.json") || XWIN=""
  if [ -n "$XWIN" ]; then
    XCLIP_OUT="$OUTDIR/${NAME}-xclip.mp4"
    if bash xclip_splice.sh "$EP" "$XCLIP_OUT" $XWIN; then
      echo "xclip: $XCLIP_OUT ($XWIN)"
    else
      echo "WARN: xclip failed" >&2
    fi
  else
    echo "WARN: no xclip windows from $WORK/timing.json; xclip skipped" >&2
  fi
fi
# Chapters check (AUDIENCE_STRATEGY #8, tick 47): YouTube hides ALL chapters if any is <10 s.
if [ -f "$WORK/timing.json" ]; then
  python3 chapters.py check "$WORK/timing.json" "$SCRIPT" >&2 \
    || echo "WARN: fix Chapters in meta.publish_description (suggested: python3 tools/video/chapters.py gen $WORK/timing.json '<Lab>')" >&2
fi
