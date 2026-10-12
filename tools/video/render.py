"""Render Orb Builds Episode 0 opener frames (pure numpy + PIL) and pipe them to ffmpeg.
usage: python3 render.py out.mp4 audio.wav      |  python3 render.py --frames 10 60 ... (PNG previews)"""
import sys, subprocess, numpy as np
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from timeline import *
import build_world as BW

B = "/workspace/video-build"
GF = "/usr/share/fonts/truetype/sand-box/google"
MONO = f"{GF}/IBM Plex Mono/IBMPlexMono-Medium.ttf"
MONOB = f"{GF}/IBM Plex Mono/IBMPlexMono-SemiBold.ttf"
def inter(size, wght):
    f = ImageFont.truetype(f"{GF}/Inter/Inter-VariableFont_opsz,wght.ttf", size)
    try: f.set_variation_by_axes([14, wght])
    except Exception:
        try: f.set_variation_by_axes([wght])
        except Exception: pass
    return f

ROOM = Image.open(f"{B}/room.png").convert("RGB")
LUM = Image.open(f"{B}/lumin_layer.png").convert("RGB")
DESK = Image.open(f"{B}/desk.png").convert("RGBA")
SX0, SY0, SX1, SY1 = BW.SCREEN
SW, SH = SX1 - SX0, SY1 - SY0
SC = ((SX0 + SX1) / 2, (SY0 + SY1) / 2)
OC = BW.LUMIN_CENTER
LW, LH = 480, 270

# ---------- camera ----------
def cam(t):
    a, b = DOLLY
    w0, w1 = 3300.0, float(SW)
    u = smooth((t - a) / (b - a))
    w = float(np.exp(np.log(w0) * (1 - u) + np.log(w1) * u))
    if t < a:
        w = 3340 - 40 * (t / a)
    c0 = (2100.0, 1100.0)
    cx = c0[0] * (1 - u) + SC[0] * u
    cy = c0[1] * (1 - u) + SC[1] * u
    k = np.clip((w - SW) / 1800, 0, 1)
    cx += 7 * np.sin(0.7 * t) * k; cy += 5 * np.sin(0.5 * t + 1) * k
    return cx, cy, w

# ---------- animation curves ----------
def flick(t, i):
    if t < T_POWER: return 0.0
    if t >= T_STEADY: return 1.0
    p = (t - T_POWER) / (T_STEADY - T_POWER)
    r = np.random.RandomState(1000 + i).rand()
    if t < T_POWER + 0.06: return 1.0           # first spark
    return 1.0 if r < 0.25 + 0.75 * p else 0.12

def lumin_bright(t):
    b = 0.09 + 0.91 * smooth((t - 2.9) / 3.8)
    for (tb, _, _) in BOOT:
        if t > tb: b += 0.12 * np.exp(-(t - tb) * 9)
    b += 0.25 * np.exp(-max(t - T_POWER, 0) * 6) * (t >= T_POWER)
    return b * (1 + 0.03 * np.sin(2 * np.pi * t / 2.2))

# ---------- screen textures ----------
F_BOOT = ImageFont.truetype(MONO, 46)
F_TERM = ImageFont.truetype(MONOB, 70)
F_BAR = ImageFont.truetype(MONO, 28)
SCAN = np.ones((H, 1, 1), np.float32); SCAN[::3] = 0.93
_yy, _xx = np.mgrid[0:H, 0:W]
SVIG = (1 - 0.35 * (((_xx - W / 2) / (W / 2)) ** 2 + ((_yy - H / 2) / (H / 2)) ** 2)).astype(np.float32)[..., None]

def term_base(bar=True):
    im = Image.new("RGB", (W, H), (6, 12, 24))
    d = ImageDraw.Draw(im)
    if bar:
        d.rectangle((0, 0, W, 70), fill=(14, 24, 44))
        for k, c in enumerate([(220, 90, 90), (230, 190, 80), (90, 200, 120)]):
            d.ellipse((32 + k * 44, 24, 52 + k * 44, 44), fill=c)
        d.text((W // 2, 35), "lumin  \u2014  orb-builds", font=F_BAR, fill=(120, 150, 190), anchor="mm")
    return im, d

def screen_tex(t, i):
    """RGB uint8 1920x1080 of whatever the monitor shows at time t."""
    g = flick(t, i)
    if t < T_POWER or g < 0.2 and t < T_STEADY:
        im = Image.new("RGB", (W, H), (4, 6, 10))
        a = np.asarray(im).astype(np.float32)
        a += (np.linspace(0, 10, W)[None, :, None] * (np.linspace(1, 0, H)[:, None, None]))  # glass sheen
        if t >= T_POWER:   # dying-flicker lines
            r = np.random.RandomState(i)
            for _ in range(4):
                y = r.randint(0, H - 30); a[y:y + r.randint(4, 30)] += 25
        return np.clip(a, 0, 255).astype(np.uint8)
    if t < T_STEADY:   # unstable flash
        r = np.random.RandomState(i + 77)
        a = np.full((H, W, 3), 150, np.float32) * np.array([0.5, 0.8, 1.0], np.float32)
        for _ in range(6):
            y = r.randint(0, H - 60); a[y:y + r.randint(10, 80)] *= r.uniform(0.2, 1.7)
        return np.clip(a, 0, 255).astype(np.uint8)
    t_ty0 = TYPE[0][1]
    if t < BOOT_CLEAR:
        im, d = term_base(bar=False)
        y = 90
        for (tb, lab, st) in BOOT:
            if t >= tb:
                n_l = int(min(1, (t - tb) / 0.30) * len(lab))
                d.text((70, y), lab[:n_l], font=F_BOOT, fill=(130, 190, 255))
                if n_l == len(lab) and t > tb + 0.3:
                    n_s = int(min(1, (t - tb - 0.3) / 0.25) * len(st))
                    xs = 70 + int(F_BOOT.getlength(lab + " "))
                    col = (255, 190, 120) if "not found" in st or "$0" in st or "danger" in st else (140, 255, 190)
                    if lab.startswith("LUMIN"): col = (230, 240, 255)
                    d.text((xs, y), st[:n_s], font=F_BOOT, fill=col)
            y += 90
        return finish(im)
    if t < t_ty0 - 0.2 and t >= BOOT_CLEAR:
        return finish(term_base()[0])
    im, d = term_base()
    times = type_char_times()
    y = 150; x0 = 90
    last_xy = (x0, y)
    for li, (text, t0, dt) in enumerate(TYPE):
        if t < t0 - 0.0 and li > 0 and t < t0: break
        n = sum(1 for ct in times[li] if t >= ct)
        if t < t0 and li == 0: n = 0
        d.text((x0, y), ">", font=F_TERM, fill=(80, 200, 255))
        px = x0 + int(F_TERM.getlength("> "))
        d.text((px, y), text[:n], font=F_TERM, fill=(228, 240, 255) if li < 3 else (255, 255, 255))
        last_xy = (px + int(F_TERM.getlength(text[:n])), y)
        if n < len(text): break
        y += 130
    blink = (int(t / 0.53) % 2 == 0) or (t < TYPE[-1][1] + 0.1 + 12 * TYPE[-1][2] and any(t - ct < 0.15 and t >= ct for tt in times for ct in tt))
    if blink:
        cx, cy = last_xy
        d.rectangle((cx + 6, cy + 6, cx + 6 + 38, cy + 6 + 72), fill=(80, 200, 255))
    return finish(im)

def finish(im):
    a = np.asarray(im).astype(np.float32) * SCAN * SVIG
    return np.clip(a, 0, 255).astype(np.uint8)

# ---------- text overlays ----------
def text_mask(text, font, pad=40, spacing=0):
    tmp = Image.new("L", (10, 10)); bb = ImageDraw.Draw(tmp).textbbox((0, 0), text, font=font)
    w, h = bb[2] - bb[0] + 2 * pad, bb[3] - bb[1] + 2 * pad
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).text((pad - bb[0], pad - bb[1]), text, font=font, fill=255)
    return m, (w, h)

class Overlay:
    def __init__(self, text, font, anchor, xy):
        m, (w, h) = text_mask(text, font)
        sh = m.filter(ImageFilter.GaussianBlur(8))
        self.m = np.asarray(m).astype(np.float32) / 255
        self.sh = np.clip(np.asarray(sh).astype(np.float32) / 255 * 1.8, 0, 1)
        self.w, self.h = w, h
        ax, ay = xy
        self.x = int(ax - (w / 2 if anchor[0] == "c" else 0))
        self.y = int(ay - (h / 2 if anchor[1] == "m" else 0))
    def draw(self, f, alpha, color=(255, 255, 255), dy=0, shadow=True):
        if alpha <= 0.003: return
        x, y = self.x, self.y + int(dy)
        y0, y1 = max(0, y), min(H, y + self.h); x0, x1 = max(0, x), min(W, x + self.w)
        if y1 <= y0 or x1 <= x0: return
        sl = (slice(y0 - y, y1 - y), slice(x0 - x, x1 - x))
        reg = f[y0:y1, x0:x1]
        if shadow: reg *= (1 - self.sh[sl] * 0.55 * alpha)[..., None]
        m = (self.m[sl] * alpha)[..., None]
        reg[:] = reg * (1 - m) + np.array(color, np.float32) * m

CAPS = [Overlay(c[2], inter(46, 560), "cm", (W // 2, 960)) for c in CAPTIONS]
LT = Overlay(LOWER_THIRD[2], inter(34, 600), "lm", (90, 100))
T_TITLE_O = Overlay("Orb Builds", inter(138, 780), "lm", (930, 470))
T_SUB = Overlay("Episode 0  \u2022  Let's begin.", inter(54, 450), "lm", (940, 590))
T_TAG = Overlay("an AI, building in public. badly, at first.", inter(36, 420), "lm", (940, 670))
def fade(t, a, b, d=0.35):
    return min(smooth((t - a) / d), smooth((b - t) / d))

# ---------- title card ----------
def title_base():
    yy, xx = np.mgrid[0:H, 0:W]
    r = np.sqrt(((xx - 560) / 900.) ** 2 + ((yy - 500) / 700.) ** 2)
    bg = np.zeros((H, W, 3), np.float32)
    bg[...] = np.array([2, 8, 40], np.float32) * (1.2 - r[..., None]).clip(0.15, 1.2)
    bg += np.array([10, 30, 90], np.float32) * np.exp(-r ** 2 * 3)[..., None]
    a = np.asarray(Image.open(f"{BW.ASSETS}/lumin.png").convert("RGB")).astype(np.float32)
    diff = np.clip(a - np.array([0, 5, 34], np.float32), 0, 255)
    y2, x2 = np.mgrid[0:800, 0:800]
    rr = np.sqrt(((x2 - 400) / 340.) ** 2 + ((y2 - 400) / 385.) ** 2)
    diff *= np.clip((1 - rr) / 0.18, 0, 1)[..., None]
    big = np.asarray(Image.fromarray(diff.astype(np.uint8)).resize((960, 960), Image.LANCZOS)).astype(np.float32)
    ox, oy = 560 - 480, 540 - 480 + 20
    bg[max(oy, 0):oy + 960 if oy + 960 <= H else H, ox:ox + 960] += big[(0 if oy >= 0 else -oy):(960 if oy + 960 <= H else H - oy)]
    return Image.fromarray(np.clip(bg, 0, 255).astype(np.uint8))
TITLE = title_base()

# ---------- misc ----------
GRAIN = [np.random.RandomState(s).randn(H, W, 1).astype(np.float32) * 2.2 for s in range(6)]
_yy2, _xx2 = np.mgrid[0:H, 0:W]
VIG = (1 - 0.55 * np.clip(((_xx2 - W / 2) / (W * 0.62)) ** 2 + ((_yy2 - H / 2) / (H * 0.66)) ** 2, 0, 1.2)).astype(np.float32)[..., None]

def up(small, size=(W, H)):
    chans = [np.asarray(Image.fromarray(small[..., c].astype(np.float32), "F").resize(size, Image.BILINEAR)) for c in range(small.shape[-1])]
    return np.stack(chans, -1)

def render(i):
    t = i / FPS
    cx, cy, w = cam(t); s = W / w; h = w * 9 / 16
    x0, y0 = cx - w / 2, cy - h / 2
    box = (x0, y0, x0 + w, y0 + h)
    covered = x0 >= SX0 - 1 and y0 >= SY0 - 1 and x0 + w <= SX1 + 1 and y0 + h <= SY1 + 1
    g = flick(t, i)
    lb = lumin_bright(t)
    gx = (np.arange(LW) + .5) / LW * w + x0; gy = (np.arange(LH) + .5) / LH * h + y0
    GX, GY = np.meshgrid(gx, gy)
    spread = 250 + 2300 * smooth((t - T_POWER) / 3.6)
    ds = ((GX - SC[0]) ** 2 + ((GY - SC[1]) * 1.25) ** 2)
    do = ((GX - OC[0]) ** 2 + (GY - OC[1]) ** 2)
    L = np.zeros((LH, LW, 3), np.float32)
    amb = np.array([0.55, 0.75, 1.0], np.float32) * 0.10
    L += amb + np.array([0.5, 0.7, 1.0], np.float32) * 0.05 * np.exp(-((GX - 600) / 900) ** 2)[..., None]
    L += (g * 1.05 * np.exp(-ds / (2 * spread ** 2)))[..., None] * np.array([0.45, 0.82, 1.25], np.float32)
    L += (lb * 0.55 * np.exp(-do / (2 * 700 ** 2)))[..., None] * np.array([0.8, 0.95, 1.15], np.float32)
    Lf = up(L)

    if not covered:
        bob = 5 * np.sin(2 * np.pi * t / 2.2)
        room = np.asarray(ROOM.resize((W, H), Image.BILINEAR, box=box)).astype(np.float32)
        lum = np.asarray(LUM.resize((W, H), Image.BILINEAR, box=(box[0], box[1] - bob, box[2], box[3] - bob))).astype(np.float32)
        fr = room * Lf + lum * lb
        dk = DESK.resize((W, H), Image.BILINEAR, box=box)
        da = np.asarray(dk).astype(np.float32)
        al = da[..., 3:4] / 255
        fr = fr * (1 - al) + da[..., :3] * Lf * al
    else:
        fr = np.zeros((H, W, 3), np.float32)

    tex = screen_tex(t, i)
    tx = tex.astype(np.float32) * g if t < T_STEADY else tex.astype(np.float32)
    if t < T_STEADY and t >= T_POWER: tx = tex.astype(np.float32)
    sw, sh = int(round(SW * s)), int(round(SH * s))
    px, py = int(round((SX0 - x0) * s)), int(round((SY0 - y0) * s))
    if sw > 0 and not (px >= W or py >= H or px + sw <= 0 or py + sh <= 0):
        if sw == W and sh == H: scr = tex
        else: scr = np.asarray(Image.fromarray(tex).resize((sw, sh), Image.BILINEAR))
        ax0, ay0 = max(px, 0), max(py, 0); ax1, ay1 = min(px + sw, W), min(py + sh, H)
        fr[ay0:ay1, ax0:ax1] = scr[ay0 - py:ay1 - py, ax0 - px:ax1 - px].astype(np.float32)
    # glow / bloom (low res)
    small = Image.new("RGB", (LW, LH), (0, 0, 0))
    sm_s = Image.fromarray(tex).resize((max(1, int(sw / 4)), max(1, int(sh / 4))), Image.BILINEAR)
    small.paste(sm_s, (px // 4, py // 4))
    b1 = np.asarray(small.filter(ImageFilter.GaussianBlur(3))).astype(np.float32)
    b2 = np.asarray(small.filter(ImageFilter.GaussianBlur(14))).astype(np.float32)
    sg = 1.0 if (t >= T_STEADY or t < T_POWER) else g
    bloom = (b1 * 0.45 + b2 * 0.9) * (0 if t < T_POWER else sg)
    ho = ((GX - OC[0]) ** 2 + (GY - (OC[1] - 20)) ** 2)
    orb = (lb * (0.95 + 0.07 * np.sin(2 * np.pi * t / 1.6)) * 90 * np.exp(-ho / (2 * 330 ** 2)))[..., None] * np.array([0.7, 0.85, 1.0], np.float32)
    if covered: orb = orb * 0
    fr += up(np.clip(bloom + orb, 0, 255))

    fr *= VIG
    fr += GRAIN[i % 6]

    # flash into title
    if t > T_FLASH - 0.4:
        flash = smooth((t - (T_FLASH - 0.4)) / 0.5) * (1 - smooth((t - (T_FLASH + 0.2)) / 0.5))
        fr += flash * 120 * np.array([0.7, 0.9, 1.0], np.float32)
    if t > T_FLASH:
        a = smooth((t - T_FLASH - 0.2) / 0.6)
        z = 1 + 0.045 * smooth((t - T_FLASH) / 5.0)
        bw, bh = W / z, H / z
        tc = np.asarray(TITLE.resize((W, H), Image.BILINEAR, box=((W - bw) / 2, (H - bh) / 2, (W + bw) / 2, (H + bh) / 2))).astype(np.float32)
        # head pulse on the title card
        yy = (np.arange(H) - 395)[:, None]; xx = (np.arange(W) - 560)[None, :]
        pulse = (28 * (0.6 + 0.4 * np.sin(2 * np.pi * (t - T_FLASH) / 1.8)) * np.exp(-(xx ** 2 + yy ** 2) / (2 * 300 ** 2)))[..., None]
        tc = tc + pulse * np.array([0.6, 0.8, 1.0], np.float32)
        fr = fr * (1 - a) + (tc * VIG + GRAIN[i % 6]) * a

    # text
    for ov, (a, b, _) in zip(CAPS, CAPTIONS):
        ov.draw(fr, fade(t, a, b), dy=8 * (1 - fade(t, a, b, 0.5)))
    LT.draw(fr, fade(t, LOWER_THIRD[0], LOWER_THIRD[1]) * 0.9, color=(170, 215, 255))
    T_TITLE_O.draw(fr, smooth((t - 17.2) / 0.9), color=(240, 248, 255), dy=18 * (1 - smooth((t - 17.2) / 0.9)))
    T_SUB.draw(fr, smooth((t - 18.2) / 0.7), color=(140, 200, 255), dy=12 * (1 - smooth((t - 18.2) / 0.7)))
    T_TAG.draw(fr, smooth((t - 19.3) / 0.8) * 0.85, color=(160, 175, 205))
    # fades
    fr *= smooth(t / 0.9) * smooth((DUR - t) / 0.8)
    return np.clip(fr, 0, 255).astype(np.uint8)

def main():
    if sys.argv[1] == "--frames":
        for ts in sys.argv[2:]:
            tt = float(ts); Image.fromarray(render(int(tt * FPS))).save(f"{B}/f_{tt:05.2f}.png")
        return
    out, wav = sys.argv[1], sys.argv[2]
    n = int(DUR * FPS)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", wav, "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p", "-profile:v", "high",
           "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-movflags", "+faststart", "-t", f"{DUR}", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    with Pool(7) as pool:
        for k, fr in enumerate(pool.imap(render, range(n), chunksize=3)):
            p.stdin.write(fr.tobytes())
            if k % 60 == 0: print("frame", k, "/", n, flush=True)
    p.stdin.close(); p.wait()

if __name__ == "__main__":
    main()
