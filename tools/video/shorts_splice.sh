#!/usr/bin/env bash
# Splice several windows of a 1920x1080 episode into ONE vertical 1080x1920 Short.
# Each window is re-cropped with shorts_cut.sh's stacked layout, then joined
# with a short audio/video crossfade-free hard cut (clean, no re-timing).
# Usage: shorts_splice.sh <episode.mp4> <out.mp4> <start:end[@mode]> [<start:end[@mode]> ...]
# Optional @mode per window = shorts_cut.sh crop mode (stacked|coldopen|letterbox); default stacked.
# Example (Ep2: best fact, then verdict): shorts_splice.sh ep2.mp4 short.mp4 13:40 78:94
# Keep the total <= 60 s while music-free status is unverified; aim 30-45 s.
set -euo pipefail
in="$1"; out="$2"; shift 2
[ "$#" -ge 1 ] || { echo "need at least one start:end window" >&2; exit 1; }
here="$(cd "$(dirname "$0")" && pwd)"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
i=0; total=0
for w in "$@"; do
  mode=stacked
  case "$w" in *@*) mode="${w##*@}"; w="${w%@*}";; esac
  ss="${w%%:*}"; to="${w##*:}"
  "$here/shorts_cut.sh" "$in" "$ss" "$to" "$tmp/part$i.mp4" "$mode"
  echo "file '$tmp/part$i.mp4'" >> "$tmp/list.txt"
  total=$(awk -v t="$total" -v a="$ss" -v b="$to" 'BEGIN{print t+(b-a)}')
  i=$((i+1))
done
# Parts share codec settings, but re-encode on join so timestamps are clean.
ffmpeg -y -v error -f concat -safe 0 -i "$tmp/list.txt" \
  -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart "$out"
echo "spliced $i window(s), ~${total}s -> $out"
