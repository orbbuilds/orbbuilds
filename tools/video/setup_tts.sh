#!/usr/bin/env bash
# One-time setup for Lumin's voice: local, free, CPU-only TTS (Kokoro-82M via kokoro-onnx, Apache-2.0).
# Creates a venv + downloads ~350 MB of model files into $ORB_TTS_DIR (default /workspace/tts).  No accounts, no keys.
set -e
D="${ORB_TTS_DIR:-/workspace/tts}"; mkdir -p "$D"; cd "$D"
command -v uv >/dev/null || pip install uv
[ -d .venv ] || uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python kokoro-onnx soundfile numpy pillow faster-whisper piper-tts
R=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
[ -f kokoro-v1.0.onnx ] || curl -fL -o kokoro-v1.0.onnx "$R/kokoro-v1.0.onnx"
[ -f voices-v1.0.bin ]  || curl -fL -o voices-v1.0.bin  "$R/voices-v1.0.bin"
echo "ok: use $D/.venv/bin/python tools/video/tts.py --say 'hello' out.wav"
