#!/usr/bin/env bash
# Splice hook-first social windows into one vertical 1080x1920 clip for X/Bluesky.
# Usage: xclip_splice.sh <episode.mp4> <out.mp4> <mode:start:end> [<mode:start:end> ...]
# mode is stacked|letterbox (from xclip_windows.py).
set -euo pipefail
in="$1"; out="$2"; shift 2
[ "$#" -ge 1 ] || { echo "need at least one mode:start:end window" >&2; exit 1; }
here="$(cd "$(dirname "$0")" && pwd)"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
i=0; total=0
for w in "$@"; do
  mode="${w%%:*}"; rest="${w#*:}"
  ss="${rest%%:*}"; to="${rest##*:}"
  case "$mode" in stacked|letterbox) ;; *)
    echo "bad window '$w' (want mode:start:end)" >&2; exit 1 ;;
  esac
  "$here/shorts_cut.sh" "$in" "$ss" "$to" "$tmp/part$i.mp4" "$mode"
  echo "file '$tmp/part$i.mp4'" >> "$tmp/list.txt"
  total=$(awk -v t="$total" -v a="$ss" -v b="$to" 'BEGIN{print t+(b-a)}')
  i=$((i+1))
done
ffmpeg -y -v error -f concat -safe 0 -i "$tmp/list.txt" \
  -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart "$out"
echo "xclip spliced $i window(s), ~${total}s -> $out"
