"""Synthesize the Episode 0 soundscape (drone, power-on, boot beeps, key clicks, soft music) -> wav."""
import sys, numpy as np, wave
from timeline import *
SR = 44100
N = int(DUR * SR)
rng = np.random.RandomState(3)
L = np.zeros(N, np.float32); R = np.zeros(N, np.float32)       # dry
ML = np.zeros(N, np.float32); MR = np.zeros(N, np.float32)     # music bus (reverbed)

def tt(n): return np.arange(n) / SR
def add(buf, x, t0, gain=1.0):
    i = int(t0 * SR)
    if i >= N: return
    x = x[:N - i]; buf[i:i + len(x)] += x * gain
def put(x, t0, gain=1.0, pan=0.0, bus=False):
    a, b = (ML, MR) if bus else (L, R)
    add(a, x, t0, gain * (1 - max(pan, 0))); add(b, x, t0, gain * (1 + min(pan, 0)))
def env(n, a, r):
    e = np.ones(n, np.float32); na = max(1, int(a * SR)); nr = max(1, int(r * SR))
    e[:na] = np.linspace(0, 1, na); e[-nr:] *= np.linspace(1, 0, nr)
    return e
def tone(f, dur, a=0.02, r=0.3, harm=(1.0, 0.0, 0.0), detune=0.0):
    t = tt(int(dur * SR)); y = np.zeros_like(t)
    for k, h in enumerate(harm):
        if h: y += h * np.sin(2 * np.pi * f * (k + 1) * t + k)
    if detune: y = 0.5 * y + 0.5 * sum(h * np.sin(2 * np.pi * f * (1 + detune) * (k + 1) * t) for k, h in enumerate(harm))
    return (y * env(len(t), a, r)).astype(np.float32)
def pluck(f, dur=1.4, g=1.0):
    t = tt(int(dur * SR))
    y = (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t * 6) + 0.12 * np.sin(2 * np.pi * 3 * f * t) * np.exp(-t * 9))
    return (y * np.exp(-t * 3.2) * np.minimum(1, t * 400) * g).astype(np.float32)
def hz(n): return 440 * 2 ** ((n - 69) / 12)

# --- room tone + dark drone (0 -> end), swells with the room lighting
t = tt(N)
brown = np.cumsum(rng.randn(N)).astype(np.float32); brown -= np.convolve(brown, np.ones(2000) / 2000, "same"); brown /= np.abs(brown).max()
swell = (0.25 + 0.75 * np.clip((t - 2.6) / 3.5, 0, 1)).astype(np.float32)
drone = (np.sin(2 * np.pi * 55 * t) * 0.5 + np.sin(2 * np.pi * 82.5 * t + 1) * 0.3 + np.sin(2 * np.pi * 110.3 * t) * 0.15 * np.clip((t - 2.6) / 3, 0, 1)) * (1 + 0.15 * np.sin(2 * np.pi * 0.18 * t))
L += (drone * 0.10 * swell + brown * 0.02).astype(np.float32); R += (drone * 0.10 * swell + brown * 0.02).astype(np.float32)

# --- power on: thunk, rising whine, crackle
x = tt(int(0.5 * SR)); thump = np.sin(2 * np.pi * (70 - 35 * x) * x) * np.exp(-x * 9) + rng.randn(len(x)) * np.exp(-x * 40) * 0.5
put(thump.astype(np.float32), T_POWER, 0.9)
x = tt(int(1.1 * SR)); f = 180 + 1800 * (x / 1.1) ** 2
put((np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.12 * np.minimum(1, x * 20) * np.linspace(1, 0.3, len(x))).astype(np.float32), T_POWER + 0.1, 1.0, bus=True)
for tc in [2.6, 2.74, 2.9, 3.05, 3.2, 3.38, 3.5]:
    n = int(0.05 * SR); put((rng.randn(n) * np.exp(-tt(n) * 80)).astype(np.float32), tc, 0.35)
# CRT-ish hum after steady
hum = np.sin(2 * np.pi * 120 * t) * 0.02 + np.sin(2 * np.pi * 7800 * t) * 0.0015
hum = (hum * np.clip((t - 3.6) / 0.5, 0, 1) * np.clip((T_FLASH - t) / 0.5 + 1, 0, 1)).astype(np.float32)
L += hum; R += hum

# --- boot beeps
for k, (tb, _, _) in enumerate(BOOT):
    f0 = 660 + 110 * k
    b = np.sign(np.sin(2 * np.pi * f0 * tt(int(0.05 * SR)))) * 0.05 * env(int(0.05 * SR), 0.003, 0.02)
    put(b.astype(np.float32), tb, 1.0, pan=0.2)
put(tone(1320, 0.5, 0.005, 0.4, (1, 0.3, 0.1)), BOOT[-1][0] + 0.7, 0.07, bus=True)

# --- typing clicks
def click(strong=1.0):
    n = int(0.03 * SR); x = tt(n)
    nz = rng.randn(n); nz = np.diff(nz, prepend=0)       # crude high-pass
    y = nz * np.exp(-x * 220) * 0.5 + np.sin(2 * np.pi * (1500 + rng.randint(-300, 300)) * x) * np.exp(-x * 400) * 0.35
    return (y * strong).astype(np.float32)
for li, times in enumerate(type_char_times()):
    for ct, ch in zip(times, TYPE[li][0]):
        put(click(0.7 if ch == " " else rng.uniform(0.8, 1.2)), ct, 0.45, pan=rng.uniform(-0.2, 0.2))
    put(click(1.4), times[-1] + 0.25, 0.4)   # enter

# --- music: soft pad + sparse pluck arpeggio from the terminal on; bright resolve on the title
prog = [(57, [57, 60, 64]), (53, [53, 57, 60]), (48, [48, 52, 55]), (55, [55, 59, 62])]   # Am F C G (roots in octave 3)
pad_t0 = 6.4
for bar in range(5):
    t0 = pad_t0 + bar * 2.0
    if t0 >= T_FLASH + 0.3: break
    for n in prog[bar % 4][1]:
        put(tone(hz(n), 2.8, 1.0, 1.4, (1, 0.25, 0.08), 0.004), t0, 0.035 * min(1, (bar + 1) / 2), pan=0.3 if n % 2 else -0.3, bus=True)
scale = [69, 72, 76, 79, 81, 84, 79, 76]
k = 0; tp = 7.2
while tp < T_FLASH:
    n = scale[k % len(scale)]
    put(pluck(hz(n)), tp, 0.05, pan=((k % 4) - 1.5) / 4, bus=True); k += 1; tp += 0.4
# title: swell + resolve in A major
for n in [45, 57, 61, 64, 69, 73]:
    put(tone(hz(n), 6.0, 1.2, 2.5, (1, 0.3, 0.1), 0.003), T_FLASH + 0.1, 0.05, pan=(n % 5 - 2) / 6, bus=True)
for j, n in enumerate([69, 73, 76, 81, 85, 88, 93]):
    put(pluck(hz(n), 2.0), T_FLASH + 0.5 + 0.18 * j, 0.07, pan=(j % 3 - 1) * 0.3, bus=True)
put(pluck(hz(93), 2.5), T_TITLE + 1.2, 0.05, bus=True)
sw = np.sin(2 * np.pi * np.cumsum(200 + 2400 * np.linspace(0, 1, int(0.6 * SR)) ** 2) / SR) * np.linspace(0, 0.1, int(0.6 * SR)) ** 1
put(sw.astype(np.float32), T_FLASH - 0.4, 0.5, bus=True)

# --- reverb on music bus
def reverb(x, seed, sec=1.8):
    r = np.random.RandomState(seed); n = int(sec * SR)
    ir = r.randn(n) * np.exp(-tt(n) * 3.2); ir[0] = 0
    nfft = 1 << int(np.ceil(np.log2(len(x) + n)))
    y = np.fft.irfft(np.fft.rfft(x, nfft) * np.fft.rfft(ir, nfft), nfft)[:len(x)]
    return (0.45 * x + 0.55 * y * 0.07).astype(np.float32)
ML2, MR2 = reverb(ML, 1), reverb(MR, 2)
outL = L + ML2; outR = R + MR2
fo = np.clip((DUR - t) / 1.0, 0, 1) * np.clip(t / 0.4, 0, 1)
outL *= fo; outR *= fo
pk = max(np.abs(outL).max(), np.abs(outR).max()); g = 0.8 / pk
sig = np.tanh(np.stack([outL, outR], 1) * g * 2.4) * 0.88
st = (sig * 32767).astype(np.int16)
with wave.open(sys.argv[1], "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())
print("wav ok peak gain", g)
