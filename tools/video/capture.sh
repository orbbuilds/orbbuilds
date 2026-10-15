#!/usr/bin/env bash
# Capture real build footage from the agent's box desktop for the review `screen` field (experiment #20).
# Read-only: grabs pixels from the X display. It never clicks or types; GUI driving stays with computerUse.
#   capture.sh still  <slug> <label>        -> content/drafts/captures/<slug>/<NN>-<label>.png
#   capture.sh start  <slug>                -> background screen recording (rec.mp4, 8 fps, 1920 wide)
#   capture.sh stop   <slug>                -> stop recording
#   capture.sh stills <slug> [max=6]        -> scene-change stills from rec.mp4 (NN-rec-<t>s.png)
# Then point a script line at one:  {"say": "...", "screen": "content/drafts/captures/<slug>/01-welcome.png", "show": "caption"}
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
DISP="${CAPTURE_DISPLAY:-${DISPLAY:-:2}}"
mode="${1:?mode}"; slug="${2:?slug}"
dir="$ROOT/content/drafts/captures/$slug"; mkdir -p "$dir"
size="$(xdpyinfo -display "$DISP" 2>/dev/null | awk '/dimensions:/{print $2}')"; size="${size:-1920x1200}"
next_n() { printf '%02d' $(( $(ls "$dir"/[0-9][0-9]-*.png 2>/dev/null | wc -l) + 1 )); }
case "$mode" in
  still)
    label="${3:?label}"; out="$dir/$(next_n)-${label}.png"
    ffmpeg -hide_banner -loglevel error -f x11grab -video_size "$size" -i "$DISP" -frames:v 1 -y "$out"
    echo "$out" ;;
  start)
    [ -f "$dir/rec.pid" ] && kill -0 "$(cat "$dir/rec.pid")" 2>/dev/null && { echo "already recording"; exit 0; }
    nohup ffmpeg -hide_banner -loglevel error -f x11grab -framerate 8 -video_size "$size" -i "$DISP" \
      -vf "scale=1920:-2" -c:v libx264 -preset veryfast -crf 26 -pix_fmt yuv420p -y "$dir/rec.mp4" \
      >"$dir/rec.log" 2>&1 & echo $! > "$dir/rec.pid"; date -Iseconds > "$dir/rec.started"; echo "recording -> $dir/rec.mp4" ;;
  stop)
    pid="$(cat "$dir/rec.pid" 2>/dev/null || true)"; [ -n "$pid" ] && kill -INT "$pid" 2>/dev/null || true
    for _ in $(seq 20); do kill -0 "$pid" 2>/dev/null || break; sleep 0.5; done; rm -f "$dir/rec.pid"
    ls -la "$dir/rec.mp4" ;;
  stills)
    max="${3:-6}"; tmp="$(mktemp -d)"
    ffmpeg -hide_banner -loglevel error -i "$dir/rec.mp4" -vf "select='gt(scene,0.08)',showinfo" -vsync vfr "$tmp/s%03d.png" 2>"$tmp/info" || true
    mapfile -t ts < <(grep -o 'pts_time:[0-9.]*' "$tmp/info" | cut -d: -f2)
    files=("$tmp"/s*.png); n=${#files[@]}; if [ ! -f "${files[0]:-}" ]; then  # static screen: fall back to the first frame
      ffmpeg -hide_banner -loglevel error -i "$dir/rec.mp4" -frames:v 1 -y "$dir/$(next_n)-rec-0s.png"; rm -rf "$tmp"; ls "$dir"; exit 0; fi
    step=$(( (n + max - 1) / max )); [ "$step" -lt 1 ] && step=1
    for ((i=0; i<n; i+=step)); do t="$(printf '%.0f' "${ts[$i]:-0}")"; cp "${files[$i]}" "$dir/$(next_n)-rec-${t}s.png"; done
    rm -rf "$tmp"; ls "$dir" ;;
  *) echo "unknown mode $mode"; exit 2 ;;
esac
