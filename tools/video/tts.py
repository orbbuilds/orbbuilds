"""Lumin's voice.  Local CPU TTS (Kokoro-82M through kokoro-onnx) + a light "warm robot" ffmpeg chain.

  tts.py --say "text" out.wav [--voice am_puck:0.6,am_michael:0.4] [--fx lumin|clean] [--speed 1.05]
  tts.py script.json outdir          -> outdir/voice.wav (44.1k mono, FX applied, loudness-normalised) + outdir/timing.json

Run with the venv python made by setup_tts.sh:  /workspace/tts/.venv/bin/python tts.py ...
Voice spec may blend voices: "am_puck:0.6,am_michael:0.4".  The word-level caption alignment uses faster-whisper
(base.en, CPU) when installed and falls back to proportional timing."""
import os, sys, re, json, argparse, subprocess, wave
import numpy as np

TTS_DIR = os.environ.get("ORB_TTS_DIR", "/workspace/tts")
SR = 24000
OUT_SR = 44100
# Lumin is a male character.  Default = energetic am_puck blended with warmer am_michael (see docs/SERIES_RELEASE_REVIEWS.md).
DEFAULT_VOICE = "am_fenrir"
# NB: write the name as "Loomin" in meta.pronounce, not "LOO-min": upper-case chunks get spelled out letter by letter.
DEFAULT_PRONOUNCE = {"Lumin": "Loomin"}
DEFAULT_SPEED = 1.05
# subtle "warm robot": warmth + presence EQ, a 9 ms metallic double (very low mix), gentle compression, loudness target.
FX = {
    "clean": "highpass=f=70,loudnorm=I=-16:TP=-1.5:LRA=7",
    "lumin": ("highpass=f=80,equalizer=f=210:t=q:w=1:g=2,equalizer=f=3300:t=q:w=1.2:g=2.5,"
              "aecho=0.92:0.9:9|23:0.20|0.07,acompressor=threshold=-20dB:ratio=3:attack=8:release=120,"
              "loudnorm=I=-16:TP=-1.5:LRA=7"),
}
_k = None

def kokoro():
    global _k
    if _k is None:
        from kokoro_onnx import Kokoro
        _k = Kokoro(os.path.join(TTS_DIR, "kokoro-v1.0.onnx"), os.path.join(TTS_DIR, "voices-v1.0.bin"))
    return _k

def voice_arg(spec):
    if ":" not in spec and "," not in spec:
        return spec
    k = kokoro(); parts = [p.split(":") for p in spec.split(",")]
    ws = np.array([float(w) for _, w in parts]); ws = ws / ws.sum()
    return sum(w * k.get_voice_style(n) for (n, _), w in zip(parts, ws))

def trim(x, thr=0.006, keep=0.04):
    idx = np.where(np.abs(x) > thr)[0]
    if len(idx) == 0: return x
    a = max(0, idx[0] - int(keep * SR)); b = min(len(x), idx[-1] + int(keep * SR))
    return x[a:b]

def synth(text, voice=DEFAULT_VOICE, speed=DEFAULT_SPEED, pronounce=None):
    for a, b in (pronounce or {}).items():
        text = re.sub(rf"\b{re.escape(a)}\b", b, text)
    s, sr = kokoro().create(text, voice=voice_arg(voice), speed=speed, lang="en-us")
    assert sr == SR
    return trim(np.asarray(s, np.float32))

def write_wav(path, x, sr=SR):
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes())

def apply_fx(raw_wav, out_wav, fx="lumin", total=None):
    chain = FX.get(fx, fx)
    if total: chain += f",apad=whole_dur={total:.3f},atrim=0:{total:.3f}"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw_wav, "-af", chain, "-ar", str(OUT_SR), "-ac", "1", out_wav], check=True)

def chunk_caption(text, max_chars=46):
    """Split into on-screen caption chunks at punctuation / word boundaries."""
    words = text.split(); chunks = []; cur = []
    name = lambda x: bool(re.match(r"^([A-Z][\w\-]*|\d[\w.\-]*)$", x))
    for i, w in enumerate(words):
        cur.append(w); s = " ".join(cur)
        if re.search(r"[.!?,;:\u2014]$", w) and len(s) >= 18:
            chunks.append(s); cur = []
        elif len(s) >= max_chars:
            # don't split a product name across chunks ("Claude Fable | 5", "Ultramarine | 1 Flash"):
            # if the next word continues a trailing run of capitalised words/numbers, carry that run to the next chunk
            nxt = re.sub(r"[.,!?;:]$", "", words[i + 1]) if i + 1 < len(words) else ""
            k = len(cur)
            while k > 1 and len(cur) - k < 4 and name(cur[k - 1]): k -= 1
            if nxt and name(nxt) and name(w) and k < len(cur) and len(" ".join(cur[:k])) >= 10:
                chunks.append(" ".join(cur[:k])); cur = cur[k:]
            else:
                chunks.append(s); cur = []
    if cur:
        if chunks and len(" ".join(cur)) < 10: chunks[-1] += " " + " ".join(cur)
        else: chunks.append(" ".join(cur))
    return chunks

_wm = None
def word_times(x):
    """[(word,start,end)] from faster-whisper (base.en, CPU) on the dry line audio, or None if unavailable."""
    global _wm
    try:
        if _wm is None:
            from faster_whisper import WhisperModel
            _wm = WhisperModel("base.en", device="cpu", compute_type="int8")
        idx = np.linspace(0, len(x) - 1, int(len(x) * 16000 / SR))
        y16 = np.interp(idx, np.arange(len(x)), x).astype(np.float32)   # whisper wants 16 kHz float32
        segs, _ = _wm.transcribe(np.concatenate([np.zeros(4000, np.float32), y16]), language="en", word_timestamps=True)
        return [(w.word.strip(), w.start - 0.25, w.end - 0.25) for s in segs for w in s.words]
    except Exception as e:
        print("align skipped:", e, file=sys.stderr); return None

def chunk_times(chunks, dur, say, wt):
    """Start/end of each caption chunk inside a line of length dur (seconds)."""
    n_script = len(say.split())
    counts = [len(c.split()) for c in chunks]
    if wt and abs(len(wt) - n_script) <= max(1, n_script // 6) and sum(counts) == n_script:
        out = []; i = 0
        for c in counts:
            a = wt[min(i, len(wt) - 1)][1]
            j = min(len(wt) - 1, int(round((i + c) * len(wt) / n_script)) - 1)
            out.append([a, wt[j][2]]); i += c
        # close small gaps so captions do not flicker
        for k in range(len(out) - 1): out[k][1] = out[k + 1][0] = (out[k][1] + out[k + 1][0]) / 2
        out[0][0] = 0.0; out[-1][1] = dur
        return out
    wts = np.array([len(c) for c in chunks], float); cum = np.concatenate([[0], np.cumsum(wts) / wts.sum()]) * dur
    return [[cum[i], cum[i + 1]] for i in range(len(chunks))]

def build(script_path, outdir, align=True):
    S = json.load(open(script_path)); os.makedirs(outdir, exist_ok=True)
    meta = S.get("meta", {}); v = meta.get("voice", {})
    voice = v.get("name", DEFAULT_VOICE); speed = v.get("speed", DEFAULT_SPEED); fx = v.get("fx", "lumin")
    pron = {**DEFAULT_PRONOUNCE, **meta.get("pronounce", {})}
    lead, tail, sec_gap = 0.5, 1.6, 0.55
    t = lead; pieces = []; sections = []
    for sec in S["sections"]:
        t += sec.get("pre", sec_gap if sections else 0.0)
        sdict = {"id": sec["id"], "kind": sec.get("kind", sec["id"]), "heading": sec.get("heading", ""), "badge": sec.get("badge"),
                 "source": sec.get("source"), "start": t, "lines": []}
        for ln in sec["lines"]:
            x = synth(ln["say"], voice, ln.get("speed", speed), pron)
            dur = len(x) / SR
            wt = word_times(x) if align and not ln.get("caption") else None
            cap = ln.get("caption") or ln["say"]
            chunks = chunk_caption(cap)
            ct = chunk_times(chunks, dur, ln["say"], wt)
            sdict["lines"].append({"say": ln["say"], "show": ln.get("show"), "screen": ln.get("screen"), "cite": ln.get("cite"), "gesture": ln.get("gesture"), "cta": ln.get("cta"), "start": t, "end": t + dur,
                                   "captions": [{"text": c, "start": t + a, "end": t + b} for c, (a, b) in zip(chunks, ct)]})
            pieces.append((t, x)); t += dur + ln.get("pause", 0.28)
        sdict["end"] = t; sections.append(sdict)
    total = t + tail
    buf = np.zeros(int(total * SR) + SR, np.float32)
    for st, x in pieces:
        i = int(st * SR); buf[i:i + len(x)] += x
    raw = os.path.join(outdir, "voice_raw.wav"); write_wav(raw, buf[:int(total * SR)])
    apply_fx(raw, os.path.join(outdir, "voice.wav"), fx, total)
    timing = {"duration": total, "voice": voice, "fx": fx, "sections": sections}
    json.dump(timing, open(os.path.join(outdir, "timing.json"), "w"), indent=1)
    print(f"voice: {total:.1f}s, {sum(len(s['lines']) for s in sections)} lines -> {outdir}")
    return timing

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--say"); ap.add_argument("--voice", default=DEFAULT_VOICE); ap.add_argument("--fx", default="lumin")
    ap.add_argument("--speed", type=float, default=DEFAULT_SPEED); ap.add_argument("--no-align", action="store_true")
    ap.add_argument("a", nargs="?"); ap.add_argument("b", nargs="?")
    A = ap.parse_args()
    if A.say:
        x = synth(A.say, A.voice, A.speed, DEFAULT_PRONOUNCE); raw = A.a + ".raw.wav"; write_wav(raw, x)
        apply_fx(raw, A.a, A.fx); os.remove(raw)
    else:
        build(A.a, A.b, align=not A.no_align)
