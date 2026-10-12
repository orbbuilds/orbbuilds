"""Render an Orb Builds "release review" episode from a script + the voice timing made by tts.py.
Lumin is a still character, so he "talks" through voice-reactive glow, a small bob and breathing; the brand look matches Episode 0.

  review_render.py script.json outdir out.mp4 [--music music.wav]     (outdir holds voice.wav + timing.json from tts.py)
  review_render.py script.json outdir --frames 1.0 8.5 20       (PNG previews to outdir/preview_*.png, no video)"""
import os, sys, json, wave, subprocess, textwrap, numpy as np
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, "../../assets"))
GF = "/usr/share/fonts/truetype/sand-box/google"
MONO = f"{GF}/IBM Plex Mono/IBMPlexMono-Medium.ttf"
W, H, FPS = 1920, 1080, 30

def inter(size, wght=500):
    f = ImageFont.truetype(f"{GF}/Inter/Inter-VariableFont_opsz,wght.ttf", size)
    for axes in ([14, wght], [wght]):
        try: f.set_variation_by_axes(axes); break
        except Exception: pass
    return f
def smooth(x): x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)

BADGES = {  # kind -> (label, colour)
    "what_dropped": ("OFFICIAL SOURCE", (90, 200, 255)), "opinion": ("MY OPINION", (255, 200, 110)),
    "caveats": ("HONEST CAVEATS", (255, 140, 120)), "teaser": ("UP NEXT: I BUILD WITH IT", (130, 235, 170)),
    "outro": ("I'M AN AI", (170, 190, 255)), "info": ("", (150, 190, 255)),
}

# ---------- static art ----------
def make_bg():
    yy, xx = np.mgrid[0:H, 0:W]
    r = np.sqrt(((xx - 700) / 1100.) ** 2 + ((yy - 480) / 800.) ** 2)
    bg = np.array([3, 8, 32], np.float32) * (1.25 - r[..., None]).clip(0.2, 1.25) + np.array([8, 26, 80], np.float32) * np.exp(-r[..., None] ** 2 * 3)
    g = ((xx % 96 < 1) | (yy % 96 < 1)).astype(np.float32)[..., None] * 6        # faint blueprint grid
    return (bg + g * np.exp(-r[..., None] ** 2 * 1.5)).astype(np.float32)

def make_lumin():
    a = np.asarray(Image.open(f"{ASSETS}/lumin.png").convert("RGB")).astype(np.float32)
    diff = np.clip(a - np.array([0, 5, 34], np.float32), 0, 255)
    y2, x2 = np.mgrid[0:a.shape[0], 0:a.shape[1]]
    rr = np.sqrt(((x2 - 400) / 345.) ** 2 + ((y2 - 400) / 390.) ** 2)
    diff *= np.clip((1 - rr) / 0.18, 0, 1)[..., None]
    return Image.fromarray(diff.astype(np.uint8))
HEAD = (400, 265, 190)    # head centre / radius in the 800px art

def wrap_px(text, font, maxw):
    words = text.split(); lines = []; cur = ""
    d = ImageDraw.Draw(Image.new("L", (4, 4)))
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def rgba_text(lines, font, color, line_h, pad=0, shadow=True):
    d0 = ImageDraw.Draw(Image.new("L", (4, 4)))
    w = int(max(d0.textlength(l, font=font) for l in lines)) + 2 * pad + 16; h = line_h * len(lines) + 2 * pad + 10
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for i, l in enumerate(lines):
        if shadow: d.text((pad + 3, pad + i * line_h + 4), l, font=font, fill=(0, 0, 0, 170))
        d.text((pad, pad + i * line_h), l, font=font, fill=color + (255,))
    return im

class Layer:
    """Pre-rendered RGBA image drawn at (x,y) with alpha / dy / optional left-to-right reveal."""
    def __init__(self, im, x, y):
        self.a = np.asarray(im.convert("RGBA")).astype(np.float32); self.x, self.y = int(x), int(y)
        self.h, self.w = self.a.shape[:2]
    def draw(self, fr, alpha=1.0, dy=0, reveal=1.0):
        if alpha <= 0.003: return
        x, y = self.x, self.y + int(dy); w = max(1, int(self.w * reveal))
        x0, y0 = max(0, x), max(0, y); x1, y1 = min(W, x + w), min(H, y + self.h)
        if x1 <= x0 or y1 <= y0: return
        s = self.a[y0 - y:y1 - y, x0 - x:x1 - x]
        al = (s[..., 3:4] / 255.0) * alpha
        reg = fr[y0:y1, x0:x1]; reg[:] = reg * (1 - al) + s[..., :3] * al

def short_url(u, n=62):
    u = u.replace("https://", "").replace("http://", "").rstrip("/")
    return u if len(u) <= n else u[:n - 1] + "\u2026"

# ---------- episode ----------
class Episode:
    def __init__(self, script, timing, voice_wav):
        self.S, self.T = script, timing; self.meta = script.get("meta", {}); self.dur = timing["duration"]
        self.bg = make_bg(); self.lum = make_lumin()
        self.env = self._envelope(voice_wav)
        self.halo = self._halo()
        self.parts = []
        for sec in timing["sections"]: self.parts.append(self._build_section(sec))
        self.caps = []
        for sec in timing["sections"]:
            for ln in sec["lines"]:
                for c in ln["captions"]:
                    lines = wrap_px(c["text"], inter(54, 600), 1500)
                    im = rgba_text(lines, inter(54, 600), (255, 255, 255), 68, pad=0)
                    bw, bh = im.size
                    plate = Image.new("RGBA", (bw + 80, bh + 30), (4, 10, 30, 175)); plate = plate.filter(ImageFilter.GaussianBlur(0))
                    mask = Image.new("L", plate.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, plate.size[0] - 1, plate.size[1] - 1), 26, fill=255)
                    plate.putalpha(Image.eval(mask, lambda v: int(v * 0.69)))
                    plate.alpha_composite(im, (40, 12))
                    self.caps.append((c["start"], c["end"], Layer(plate, (W - plate.size[0]) // 2, 1010 - plate.size[1])))
        rs = np.random.RandomState(5)
        self.sparks = [(rs.uniform(0, W), rs.uniform(0, H), rs.uniform(10, 40), rs.uniform(0.3, 1.0), rs.uniform(0, 6.28)) for _ in range(46)]
        spr = np.exp(-(np.mgrid[-6:7, -6:7] ** 2).sum(0) / 6.0).astype(np.float32); self.spr = spr[..., None] * np.array([0.5, 0.75, 1.0], np.float32) * 70

    def _envelope(self, path):
        with wave.open(path) as w:
            sr = w.getframerate(); x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
        n = int(len(x) / sr * FPS) + 2; hop = sr // FPS; x = np.concatenate([x, np.zeros(hop * 3, np.float32)])
        r = np.array([np.sqrt(np.mean(x[i * hop:(i + 1) * hop] ** 2) + 1e-12) for i in range(n)])
        r = np.clip(r / (np.percentile(r, 95) + 1e-9), 0, 1.2)
        out = np.zeros(n); v = 0.0
        for i, a in enumerate(r):          # fast attack, slower release
            v = a if a > v else v * 0.72 + a * 0.28
            out[i] = v
        return out
    def env_at(self, t): return float(self.env[min(len(self.env) - 1, max(0, int(t * FPS)))])
    def _halo(self):
        yy, xx = np.mgrid[-128:128, -128:128]; return np.exp(-(xx ** 2 + yy ** 2) / (2 * 55.0 ** 2)).astype(np.float32)

    def _build_section(self, sec):
        kind = sec["kind"]; P = {"sec": sec, "kind": kind, "layers": []}
        if kind == "cold_open":
            subj = self.meta.get("subject", "")
            P["pill"] = Layer(self._pill("NEW RELEASE", (255, 120, 140), 34), 0, 0)
            P["subject"] = Layer(rgba_text(wrap_px(subj, inter(84, 780), 1500), inter(84, 780), (240, 248, 255), 100), 0, 0) if subj else None
            return P
        label, col = BADGES.get(kind, BADGES["info"]); label = sec.get("badge") or label
        px, py, pw, ph = 830, 120, 1010, 700
        panel = Image.new("RGBA", (pw, ph), (0, 0, 0, 0)); m = Image.new("L", (pw, ph), 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, pw - 1, ph - 1), 34, fill=255)
        glass = Image.new("RGBA", (pw, ph), (8, 18, 46, 205)); glass.putalpha(Image.eval(m, lambda v: int(v * 0.8)))
        panel.alpha_composite(glass)
        ImageDraw.Draw(panel).rounded_rectangle((0, 0, pw - 1, ph - 1), 34, outline=col + (110,), width=2)
        P["panel"] = Layer(panel, px, py)
        y = py + 42
        if label: P["badge"] = Layer(self._pill(label, col, 28), px + 44, y); y += 70
        head = sec.get("heading") or ""
        if head:
            hl = rgba_text(wrap_px(head, inter(66, 760), pw - 100), inter(66, 760), (245, 250, 255), 78, shadow=False); P["head"] = Layer(hl, px + 40, y); y += hl.size[1] + 14
        src = sec.get("source")
        foot = 0
        if src and src.get("url"):
            f = ImageFont.truetype(MONO, 25)
            im = rgba_text([short_url(src["url"])], f, (150, 200, 255), 32, shadow=False)
            tag = rgba_text([(src.get("label") or "Source") + ":"], f, (110, 150, 200), 32, shadow=False)
            P["src_tag"] = Layer(tag, px + 44, py + ph - 96); P["src"] = Layer(im, px + 44, py + ph - 62); foot = 110
        bullets = [ln["show"] for ln in sec["lines"] if ln.get("show")]
        avail = py + ph - foot - y - 20
        for fs in (58, 54, 50, 46, 42, 38, 34, 30):
            font = inter(fs, 500); lh = int(fs * 1.3)
            wr = [wrap_px(b, font, pw - 150) for b in bullets]
            need = sum(len(w) * lh + 36 for w in wr)
            if need <= avail: break
        mono = kind == "teaser"
        if mono: font = ImageFont.truetype(MONO, fs - 4)
        P["bul"] = {}
        yy = y + 8
        for ln in sec["lines"]:
            if not ln.get("show"): continue
            wl = wrap_px(ln["show"], font, pw - 150); h = len(wl) * lh
            im = Image.new("RGBA", (pw - 80, h + 6), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
            if mono: d.text((0, 0), ">", font=font, fill=(110, 235, 170, 255))
            else: d.ellipse((2, lh // 2 - 7, 16, lh // 2 + 7), fill=col + (255,))
            for i, l in enumerate(wl): d.text((44 if not mono else 40, i * lh), l, font=font, fill=(228, 238, 255, 255))
            P["bul"][ln["start"]] = (Layer(im, px + 44, yy), ln["end"])
            yy += h + 36
        return P

    def _pill(self, text, col, size):
        f = inter(size, 700); d0 = ImageDraw.Draw(Image.new("L", (4, 4))); tw = int(d0.textlength(text, font=f))
        im = Image.new("RGBA", (tw + 56, size + 28), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.rounded_rectangle((0, 0, im.size[0] - 1, im.size[1] - 1), (size + 28) // 2, fill=col + (50,), outline=col + (230,), width=2)
        d.text((28, 12), text, font=f, fill=col + (255,)); return im

    def frame(self, t):
        fr = self.bg.copy()
        for (x, y, sp, a, ph) in self.sparks:         # drifting motes
            px = int((x + t * sp * 0.3) % (W - 14)); py = int((y - t * sp) % (H - 14))
            fr[py:py + 13, px:px + 13] += self.spr * (0.5 + 0.5 * np.sin(t * 0.9 + ph)) * a
        # which section?
        secs = self.parts; cur = secs[-1]
        for P in secs:
            if t < P["sec"]["end"] + 0.27: cur = P; break
        kind = cur["kind"]; e = self.env_at(t)
        # Lumin layout: centred hero in the cold open, glides left once the first panel section starts
        first_end = secs[0]["sec"]["end"] if secs[0]["kind"] == "cold_open" else 0.0
        u = smooth((t - first_end) / 0.7) if secs[0]["kind"] == "cold_open" else 1.0
        size, cx, cy = 860 + (790 - 860) * u, W / 2 + (440 - W / 2) * u, 680 + (500 - 680) * u
        size = size * (1 + 0.012 * e) * (1 + 0.006 * np.sin(t * 1.9)); bob = 6 * np.sin(2 * np.pi * t / 2.4)
        s = int(size)
        L = np.asarray(self.lum.resize((s, s), Image.BILINEAR)).astype(np.float32)
        hx = cx - s / 2 + HEAD[0] * s / 800; hy = cy - s / 2 + bob + HEAD[1] * s / 800; hr = HEAD[2] * s / 800
        hs = int(hr * 5.2); halo = np.asarray(Image.fromarray(self.halo).resize((hs, hs), Image.BILINEAR))[..., None]
        self._add(fr, halo * np.array([0.55, 0.8, 1.0], np.float32) * (22 + 120 * e), hx - hs / 2, hy - hs / 2)
        self._add(fr, L * (0.94 + 0.16 * e), cx - s / 2, cy - s / 2 + bob)
        # section content
        sec = cur["sec"]; fi = smooth((t - sec["start"] + 0.2) / 0.5) * smooth((sec["end"] + 0.25 - t) / 0.3)
        if kind == "cold_open":
            a = smooth((t - 0.3) / 0.5)
            cur["pill"].x = int(W / 2 - cur["pill"].w / 2); cur["pill"].y = 70; cur["pill"].draw(fr, a, dy=-20 * (1 - a))
            if cur["subject"]:
                sj = cur["subject"]; sj.x = int(W / 2 - sj.w / 2); sj.y = 135; sj.draw(fr, smooth((t - 0.7) / 0.6), dy=14 * (1 - smooth((t - 0.7) / 0.6)))
        else:
            cur["panel"].draw(fr, fi * 0.97)
            for k in ("badge", "head", "src_tag", "src"):
                if k in cur: cur[k].draw(fr, fi, dy=10 * (1 - fi))
            teaser = kind == "teaser"
            for st, (lay, en) in cur["bul"].items():
                a = smooth((t - st) / 0.35)
                if teaser:
                    prog = min(1.0, max(0.0, (t - st) / max(0.4, (en - st) * 0.8))); lay.draw(fr, 1.0 if prog > 0 else 0, reveal=prog)
                else: lay.draw(fr, a * fi, dy=14 * (1 - a))
        # captions
        for (a, b, lay) in self.caps:
            if a - 0.05 <= t <= b + 0.12:
                k = min(smooth((t - a + 0.05) / 0.12), smooth((b + 0.12 - t) / 0.12)); lay.draw(fr, k)
        # vignette + global fades
        fr *= VIG
        fr *= smooth(t / 0.8) * smooth((self.dur - t) / 1.0)
        return np.clip(fr, 0, 255).astype(np.uint8)

    @staticmethod
    def _add(fr, img, x, y):
        x, y = int(round(x)), int(round(y)); h, w = img.shape[:2]
        x0, y0 = max(0, x), max(0, y); x1, y1 = min(W, x + w), min(H, y + h)
        if x1 > x0 and y1 > y0: fr[y0:y1, x0:x1] += img[y0 - y:y1 - y, x0 - x:x1 - x]

_yy, _xx = np.mgrid[0:H, 0:W]
VIG = (1 - 0.5 * np.clip(((_xx - W / 2) / (W * 0.62)) ** 2 + ((_yy - H / 2) / (H * 0.66)) ** 2, 0, 1.2)).astype(np.float32)[..., None]

EP = None
def _init(sp, od):
    global EP
    EP = Episode(json.load(open(sp)), json.load(open(os.path.join(od, "timing.json"))), os.path.join(od, "voice.wav"))
def _frame(i): return EP.frame(i / FPS).tobytes()

def main():
    args = sys.argv[1:]; sp, od = args[0], args[1]
    _init(sp, od)
    if args[2] == "--frames":
        for ts in args[3:]:
            Image.fromarray(EP.frame(float(ts))).save(os.path.join(od, f"preview_{float(ts):05.1f}.png"))
        return
    out = args[2]; music = args[args.index("--music") + 1] if "--music" in args else None
    voice = os.path.join(od, "voice.wav"); mix = os.path.join(od, "mix.wav")
    dur = EP.dur
    if music:   # duck music under the voice (sidechain), then loudness-normalise the mix
        fc = ("[1:a]volume=0.55[m];[0:a]asplit=2[v][sc];[m][sc]sidechaincompress=threshold=0.015:ratio=10:attack=15:release=450:makeup=1[d];"
              "[v][d]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=9[o]")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", voice, "-i", music, "-filter_complex", fc, "-map", "[o]", "-ar", "44100", "-ac", "2", mix], check=True)
    else:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", voice, "-af", "loudnorm=I=-14:TP=-1.5", "-ar", "44100", "-ac", "2", mix], check=True)
    n = int(dur * FPS)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", mix,
           "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-profile:v", "high", "-c:a", "aac", "-b:a", "192k",
           "-movflags", "+faststart", "-t", f"{dur:.3f}", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    with Pool(7, initializer=_init, initargs=(sp, od)) as pool:
        for k, b in enumerate(pool.imap(_frame, range(n), chunksize=4)):
            p.stdin.write(b)
            if k % 90 == 0: print("frame", k, "/", n, flush=True)
    p.stdin.close(); p.wait(); print("wrote", out)

if __name__ == "__main__":
    main()
