"""Tiny deterministic ambient music bed (soft pad + plucked arpeggio + gentle pulse) -> stereo 44.1k wav.
usage: music_bed.py out.wav duration_seconds [seed]"""
import sys, wave, numpy as np
SR = 44100
def hz(n): return 440 * 2 ** ((n - 69) / 12)
def make(dur, seed=1):
    rng = np.random.RandomState(seed); N = int(dur * SR); t = np.arange(N) / SR
    L = np.zeros(N, np.float32); R = np.zeros(N, np.float32)
    bar = 4.8                                        # seconds per chord (100 bpm, 2 beats/bar x ... slow feel)
    prog = [[57, 60, 64], [53, 57, 60], [48, 55, 64], [55, 59, 62]]   # Am F C(add) G
    for b in range(int(dur / bar) + 1):
        a = b * bar; ch = prog[b % 4]
        i0 = int(a * SR); n = min(int((bar + 1.2) * SR), N - i0)
        if n <= 0: break
        tt = np.arange(n) / SR
        env = np.minimum(1, tt / 1.2) * np.clip((bar + 1.2 - tt) / 1.2, 0, 1)
        for k, note in enumerate(ch):
            f = hz(note - 12)
            y = np.sin(2 * np.pi * f * tt) + 0.4 * np.sin(2 * np.pi * 2 * f * 1.002 * tt) + 0.15 * np.sin(2 * np.pi * 3 * f * tt)
            p = (k - 1) * 0.35
            L[i0:i0 + n] += (y * env * 0.045 * (1 - max(p, 0))).astype(np.float32); R[i0:i0 + n] += (y * env * 0.045 * (1 + min(p, 0))).astype(np.float32)
        # arpeggio (eighth-ish notes)
        step = bar / 8
        for j in range(8):
            note = ch[[0, 1, 2, 1, 2, 1, 0, 1][j]] + 12
            ts = a + j * step + (rng.rand() * 0.01)
            i = int(ts * SR); m = min(int(1.6 * SR), N - i)
            if m <= 0: continue
            x = np.arange(m) / SR; f = hz(note)
            y = (np.sin(2 * np.pi * f * x) + 0.3 * np.sin(2 * np.pi * 2 * f * x) * np.exp(-x * 5)) * np.exp(-x * 3.5) * np.minimum(1, x * 300)
            pan = 0.3 * np.sin(j + b)
            L[i:i + m] += (y * 0.05 * (1 - max(pan, 0))).astype(np.float32); R[i:i + m] += (y * 0.05 * (1 + min(pan, 0))).astype(np.float32)
        # soft pulse on the bar
        for j in range(4):
            i = int((a + j * bar / 4) * SR); m = min(int(0.35 * SR), N - i)
            if m <= 0: continue
            x = np.arange(m) / SR; y = np.sin(2 * np.pi * (52 - 14 * x) * x) * np.exp(-x * 11) * (0.55 if j % 2 == 0 else 0.3)
            L[i:i + m] += (y * 0.09).astype(np.float32); R[i:i + m] += (y * 0.09).astype(np.float32)
    fade = np.minimum(1, t / 1.5) * np.minimum(1, (dur - t) / 2.0)
    L *= fade; R *= fade
    st = np.stack([L, R], 1); st /= max(1e-6, np.abs(st).max()) / 0.8
    return st
if __name__ == "__main__":
    st = make(float(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 1)
    with wave.open(sys.argv[1], "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype(np.int16).tobytes())
