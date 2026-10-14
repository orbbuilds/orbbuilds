#!/usr/bin/env bash
# Vertical 1080x1920 Shorts cut from a 1920x1080 review_render.py episode.
# Layout (stacked, no re-render): source panel on top, caption band under it,
# Lumin below (bottom ~20% sits under the Shorts UI, so only his feet go there).
# Caption band crop is 1500 px wide (x 210-1710) so the longest caption lines (~1360 px) are not clipped.
# Usage: shorts_cut.sh <episode.mp4> <start_s> <end_s> <out.mp4>
# Keep end-start <= 180 s (YouTube classifies vertical <=3 min uploads as Shorts);
# aim for 30-45 s: best real result first, then the verdict.
set -euo pipefail
in="$1"; ss="$2"; to="$3"; out="$4"
ffmpeg -y -v error -ss "$ss" -to "$to" -i "$in" -filter_complex "\
[0:v]split=3[a][b][c];\
[a]crop=1010:700:830:120,scale=1080:-2[p];\
[c]crop=1500:150:210:900,scale=1080:-2[cap];\
[b]crop=830:880:0:20,scale=-2:900[l];\
color=c=0x0b1020:s=1080x1920:r=30[bg];\
[bg][p]overlay=0:20:shortest=1[t1];[t1][cap]overlay=0:780[t2];[t2][l]overlay=(W-w)/2:930[v]" \
  -map "[v]" -map 0:a? -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart "$out"
