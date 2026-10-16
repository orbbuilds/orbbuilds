#!/usr/bin/env bash
# Vertical 1080x1920 cut from a 1920x1080 review_render.py episode.
# Usage: shorts_cut.sh <episode.mp4> <start_s> <end_s> <out.mp4> [stacked|coldopen|letterbox]
# stacked (default): source panel on top, caption band, Lumin below (YouTube Shorts).
# coldopen: for review_render cold_open frames (centred title, Lumin centre, hook chips right): title band top,
#   hook chips, caption band, Lumin below. Use for a hook-first Short window that starts on the cold open (tick 187).
# letterbox: scale full frame to 1080 wide and pad to 1080x1920 (cold-open titles stay readable on X).
set -euo pipefail
in="$1"; ss="$2"; to="$3"; out="$4"; mode="${5:-stacked}"
case "$mode" in
  stacked)
    ffmpeg -y -v error -ss "$ss" -to "$to" -i "$in" -filter_complex "\
[0:v]split=3[a][b][c];\
[a]crop=1010:700:830:120,scale=1080:-2[p];\
[c]crop=1500:150:210:900,scale=1080:-2[cap];\
[b]crop=830:880:0:20,scale=-2:900[l];\
color=c=0x0b1020:s=1080x1920:r=30[bg];\
[bg][p]overlay=0:20:shortest=1[t1];[t1][cap]overlay=0:780[t2];[t2][l]overlay=(W-w)/2:930[v]" \
      -map "[v]" -map 0:a? -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart "$out"
    ;;
  coldopen)
    ffmpeg -y -v error -ss "$ss" -to "$to" -i "$in" -filter_complex "\
[0:v]split=4[a][b][c][d];\
[a]crop=1200:200:360:50,scale=1080:-2[ti];\
[b]crop=510:590:1400:310,scale=-2:700[ch];\
[c]crop=1500:150:210:900,scale=1080:-2[cap];\
[d]crop=800:670:520:230,scale=-2:780[l];\
color=c=0x0b1020:s=1080x1920:r=30[bg];\
[bg][ti]overlay=0:40:shortest=1[t1];[t1][ch]overlay=(W-w)/2:250[t2];[t2][cap]overlay=0:980[t3];[t3][l]overlay=(W-w)/2:1110[v]" \
      -map "[v]" -map 0:a? -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart "$out"
    ;;
  letterbox)
    ffmpeg -y -v error -ss "$ss" -to "$to" -i "$in" \
      -vf "scale=1080:-2,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x0b1020" \
      -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart "$out"
    ;;
  *)
    echo "unknown crop mode: $mode (use stacked|coldopen|letterbox)" >&2; exit 1
    ;;
esac
