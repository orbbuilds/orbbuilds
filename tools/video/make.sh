#!/usr/bin/env bash
# Rebuild the Episode 0 opener: world layers -> soundtrack -> frames+mux.  Needs ffmpeg, python3, numpy, Pillow.
set -e
cd "$(dirname "$0")"
python3 build_world.py
python3 audio.py /workspace/video-build/audio.wav
python3 render.py "${1:-/workspace/orbbuilds/content/drafts/test-lumin-at-computer.mp4}" /workspace/video-build/audio.wav
