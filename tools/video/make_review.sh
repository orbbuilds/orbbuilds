#!/usr/bin/env bash
# Render a release-review episode:  make_review.sh content/scripts/<script>.json [out.mp4]
#   validate -> TTS (Kokoro, local) + word-aligned captions -> music bed -> render frames -> duck music under voice -> mp4
#   then post_render.sh: P6 thumbnail from meta.thumbnail + vertical Short (NO_SHORT=1 to skip)
# Needs: tools/video/setup_tts.sh run once (venv at $ORB_TTS_DIR, default /workspace/tts), ffmpeg.
set -e
cd "$(dirname "$0")"
PY="${ORB_TTS_DIR:-/workspace/tts}/.venv/bin/python"
SCRIPT="$(realpath "$1")"; NAME="$(basename "$SCRIPT" .json)"
OUT="${2:-/workspace/orbbuilds/content/drafts/${NAME}.mp4}"
WORK="/workspace/video-build/${NAME}"; mkdir -p "$WORK"
"$PY" validate_script.py "$SCRIPT" ${ALLOW_PLACEHOLDERS:+--allow-placeholders}
"$PY" tts.py "$SCRIPT" "$WORK"
DUR=$("$PY" -c "import json;print(json.load(open('$WORK/timing.json'))['duration'])")
SEED=$(( $(printf %s "$NAME" | cksum | cut -d" " -f1) % 2147483646 + 2 ))   # per-episode music variation (never 1 = legacy bed)
"$PY" music_bed.py "$WORK/music.wav" "$DUR" "${MUSIC_SEED:-$SEED}"
"$PY" review_render.py "$SCRIPT" "$WORK" "$OUT" --music "$WORK/music.wav"
echo "draft (NOT published): $OUT"
bash post_render.sh "$SCRIPT" "$OUT" || true
