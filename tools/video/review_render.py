"""Render an Orb Builds "release review" episode from a script + the voice timing made by tts.py.
Lumin is a still character, so he "talks" through voice-reactive glow, a small bob and breathing; the brand look matches Episode 0.

  review_render.py script.json outdir out.mp4 [--music music.wav]     (outdir holds voice.wav + timing.json from tts.py)
  review_render.py script.json outdir --frames 1.0 8.5 20       (PNG previews to outdir/preview_*.png, no video)"""
import os, sys, json, wave, subprocess, textwrap, numpy as np
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import character, cta

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
BG_PALETTES = [  # (base, glow) RGB; index 0 is the legacy Episode 0 look
    ((3, 8, 32), (8, 26, 80)), ((2, 14, 28), (6, 48, 72)), ((10, 6, 34), (34, 16, 84)),
    ((4, 10, 24), (12, 34, 64)), ((3, 10, 36), (10, 38, 96)),
]
def bg_seed(meta=None):
    """Per-episode background seed: meta.bg_seed > env BG_SEED > None (legacy bg). Spam-policy hygiene (#20)."""
    v = (meta or {}).get("bg_seed", os.environ.get("BG_SEED"))
    try: return int(v) if v not in (None, "") else None
    except ValueError: return None

def make_bg(seed=None):
    """seed None/1 -> legacy blueprint bg byte-for-byte; other seeds vary palette, glow centre and grid pitch (brand stays dark-blue glass)."""
    cx, cy, base, glow, pitch = 700, 480, BG_PALETTES[0][0], BG_PALETTES[0][1], 96
    if seed not in (None, 1):
        rng = np.random.default_rng(int(seed))
        base, glow = BG_PALETTES[int(rng.integers(1, len(BG_PALETTES)))]
        cx, cy = int(rng.integers(560, 841)), int(rng.integers(400, 561)); pitch = int(rng.choice([80, 88, 104, 112]))
    yy, xx = np.mgrid[0:H, 0:W]
    r = np.sqrt(((xx - cx) / 1100.) ** 2 + ((yy - cy) / 800.) ** 2)
    bg = np.array(base, np.float32) * (1.25 - r[..., None]).clip(0.2, 1.25) + np.array(glow, np.float32) * np.exp(-r[..., None] ** 2 * 3)
    g = ((xx % pitch < 1) | (yy % pitch < 1)).astype(np.float32)[..., None] * 6        # faint blueprint grid
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


def resolve_screen(path):
    """Repo-relative or absolute path to a screenshot/clip frame. Missing -> None + warn."""
    if not path: return None
    path = str(path)
    if os.path.isabs(path) and os.path.isfile(path): return path
    root = os.path.normpath(os.path.join(HERE, "../.."))
    for cand in (os.path.join(root, path), path, os.path.join(os.getcwd(), path)):
        if os.path.isfile(cand): return os.path.abspath(cand)
    print(f"warn: screen not found: {path}", flush=True)
    return None

# ---------- episode ----------
class Episode:
    def __init__(self, script, timing, voice_wav):
        self.S, self.T = script, timing; self.meta = script.get("meta", {}); self.dur = timing["duration"]
        self.bg = make_bg(bg_seed(self.meta)); self.lum = make_lumin()
        self.lum_base = character.erase_smile(self.lum)
        glines, self.ctas = [], []
        for si, sec in enumerate(timing["sections"]):
            src = script["sections"][si]["lines"] if si < len(script.get("sections", [])) else []
            for li, ln in enumerate(sec["lines"]):
                sl = dict(src[li]) if li < len(src) else {}; sl.setdefault("say", ln["say"])
                for k in ("gesture", "cta"):
                    if ln.get(k) and not sl.get(k): sl[k] = ln[k]
                g = sl.get("gesture") or character.auto_gesture(sec["kind"], ln["say"], si == 0 and li == 0, si == len(timing["sections"]) - 1 and li == len(sec["lines"]) - 1)
                if g not in character.GESTURES: g = "rest"
                if cta.is_cta(sl):
                    words = ln["say"].lower(); k = words.find("like"); frac = max(0, k) / max(1, len(words))
                    self.ctas.append(ln["start"] + frac * (ln["end"] - ln["start"]) - 0.2)
                glines.append((ln["start"], ln["end"], g))
        self.anim = character.Animator(glines)
        self.env = self._envelope(voice_wav)
        self.halo = self._halo()
        # overlay script visual fields onto timing (so --frames picks up screen without re-tts)
        for si, sec in enumerate(timing["sections"]):
            src_lines = script["sections"][si]["lines"] if si < len(script.get("sections", [])) else []
            for li, ln in enumerate(sec["lines"]):
                if li < len(src_lines) and src_lines[li].get("screen"):
                    ln["screen"] = src_lines[li]["screen"]
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
            # hook cards: a cold-open line's `show` ("5 PEOPLE · 13¢ / TASK") becomes big stacked chips in the
            # right column, so muted viewers can read the sourced hook numbers too (max 3 chips, staggered in)
            P["hook"] = []; yy = 330
            for ln in sec["lines"]:
                parts = [x.strip() for x in str(ln.get("show") or "").split("·") if x.strip()]
                for i, txt in enumerate(parts):
                    if len(P["hook"]) >= 3: break
                    chip = self._hook_chip(txt); st = ln["start"] + i * min(0.9, (ln["end"] - ln["start"]) * 0.6 / max(1, len(parts)))
                    P["hook"].append((st, Layer(chip, 1655 - chip.size[0] // 2, yy))); yy += chip.size[1] + 26
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
        text_lines = [ln for ln in sec["lines"] if not ln.get("screen") and ln.get("show")]
        screen_lines = [ln for ln in sec["lines"] if ln.get("screen")]
        content_bottom = py + ph - foot - 20
        P["bul"] = {}
        yy = y + 8
        if screen_lines and text_lines:
            # mixed: shrink bullets into the top strip; screens keep >=55% of the content area
            total_h = max(80, content_bottom - yy)
            reserve = int(total_h * 0.55)
            bullets = [ln["show"] for ln in text_lines]
            avail = max(60, total_h - reserve - 16)
            for fs in (58, 54, 50, 46, 42, 38, 34, 28, 24):
                font = inter(fs, 500); lh = int(fs * 1.3)
                wr = [wrap_px(b, font, pw - 150) for b in bullets]
                need = sum(len(w) * lh + 28 for w in wr)
                if need <= avail: break
            mono = kind == "teaser"
            if mono: font = ImageFont.truetype(MONO, max(18, fs - 4))
            for ln in text_lines:
                wl = wrap_px(ln["show"], font, pw - 150); h = len(wl) * lh
                im = Image.new("RGBA", (pw - 80, h + 6), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
                if mono: d.text((0, 0), ">", font=font, fill=(110, 235, 170, 255))
                else: d.ellipse((2, lh // 2 - 7, 16, lh // 2 + 7), fill=col + (255,))
                for i, l in enumerate(wl): d.text((44 if not mono else 40, i * lh), l, font=font, fill=(228, 238, 255, 255))
                P["bul"][ln["start"]] = (Layer(im, px + 44, yy), ln["end"])
                yy += h + 28
        elif text_lines:
            # ORIGINAL no-screen bullet path (must stay byte-identical for regression)
            bullets = [ln["show"] for ln in text_lines]
            avail = content_bottom - yy - 20
            for fs in (58, 54, 50, 46, 42, 38, 34, 30):
                font = inter(fs, 500); lh = int(fs * 1.3)
                wr = [wrap_px(b, font, pw - 150) for b in bullets]
                need = sum(len(w) * lh + 36 for w in wr)
                if need <= avail: break
            mono = kind == "teaser"
            if mono: font = ImageFont.truetype(MONO, fs - 4)
            for ln in text_lines:
                wl = wrap_px(ln["show"], font, pw - 150); h = len(wl) * lh
                im = Image.new("RGBA", (pw - 80, h + 6), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
                if mono: d.text((0, 0), ">", font=font, fill=(110, 235, 170, 255))
                else: d.ellipse((2, lh // 2 - 7, 16, lh // 2 + 7), fill=col + (255,))
                for i, l in enumerate(wl): d.text((44 if not mono else 40, i * lh), l, font=font, fill=(228, 238, 255, 255))
                P["bul"][ln["start"]] = (Layer(im, px + 44, yy), ln["end"])
                yy += h + 36
        # real screenshots / capture frames (experiment #20): line.screen = path relative to repo root
        P["screens"] = {}
        screen_top = yy + (10 if text_lines and screen_lines else 0)
        max_h = max(160, content_bottom - screen_top)
        max_w = pw - 80
        for ln in screen_lines:
            path = resolve_screen(ln.get("screen"))
            if not path: continue
            card = self._screen_card(path, max_w, max_h - (44 if ln.get("show") else 0), col)
            if ln.get("show"):
                cap = rgba_text(wrap_px(ln["show"], inter(32, 600), max_w - 40), inter(32, 600), (200, 220, 255), 40, shadow=False)
                combined = Image.new("RGBA", (max(card.size[0], cap.size[0] + 16), card.size[1] + cap.size[1] + 14), (0, 0, 0, 0))
                combined.alpha_composite(card, ((combined.size[0] - card.size[0]) // 2, 0))
                combined.alpha_composite(cap, ((combined.size[0] - cap.size[0]) // 2, card.size[1] + 10))
                card = combined
            lx = px + (pw - card.size[0]) // 2
            P["screens"][ln["start"]] = (Layer(card, lx, screen_top), ln["end"])
        return P

    def _screen_card(self, path, max_w, max_h, col):
        """Fit a real screenshot into the panel with a rounded frame (no upscale past native size)."""
        src = Image.open(path).convert("RGB")
        sw, sh = src.size
        scale = min(max_w / max(1, sw), max_h / max(1, sh), 1.0)
        # if the image is tiny, allow mild upscale so it isn't a postage stamp
        if scale < 0.5 and max(sw, sh) < 400:
            scale = min(max_w / max(1, sw), max_h / max(1, sh))
        nw, nh = max(1, int(sw * scale)), max(1, int(sh * scale))
        src = src.resize((nw, nh), Image.LANCZOS)
        pad = 8
        im = Image.new("RGBA", (nw + 2 * pad, nh + 2 * pad), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((0, 0, im.size[0] - 1, im.size[1] - 1), 18, fill=(4, 10, 30, 230), outline=col + (200,), width=2)
        photo = src.convert("RGBA")
        mask = Image.new("L", (nw, nh), 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, nw - 1, nh - 1), 12, fill=255)
        photo.putalpha(mask)
        im.alpha_composite(photo, (pad, pad))
        return im

    def _hook_chip(self, text, col=(255, 120, 140)):
        f = inter(66, 800); lines = wrap_px(text, f, 400); lh = 78
        d0 = ImageDraw.Draw(Image.new("L", (4, 4))); tw = max(int(d0.textlength(l, font=f)) for l in lines)
        im = Image.new("RGBA", (tw + 64, len(lines) * lh + 34), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.rounded_rectangle((0, 0, im.size[0] - 1, im.size[1] - 1), 26, fill=(8, 18, 46, 200), outline=col + (220,), width=3)
        for i, l in enumerate(lines): d.text((32, 12 + i * lh), l, font=f, fill=(250, 252, 255, 255))
        return im

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
        # roam: each panel section parks Lumin at a slightly different spot (eased glide between them)
        idx = secs.index(cur); OFF = [(0, 0), (0, 0), (60, 25), (-45, -10), (35, 30), (-20, -15)]
        prv = OFF[max(0, idx - 1) % 6]; nxt = OFF[idx % 6]; g8 = smooth((t - cur["sec"]["start"] + 0.2) / 0.9)
        if kind != "cold_open": cx += prv[0] + (nxt[0] - prv[0]) * g8; cy += prv[1] + (nxt[1] - prv[1]) * g8
        cx += 9 * np.sin(2 * np.pi * t / 7.3)                      # slow idle sway
        size = size * (1 + 0.012 * e) * (1 + 0.006 * np.sin(t * 1.9)); bob = 6 * np.sin(2 * np.pi * t / 2.4) + 4 * np.sin(2 * np.pi * t / 5.1)
        s = int(size)
        hands, tilt, gest, gst = self.anim.pose(t)
        ang = tilt + 1.6 * np.sin(2 * np.pi * t / 6.1)
        mouth = min(1.0, max(0.0, (e - 0.1) / 0.55))
        art = character.draw_face(self.lum_base.copy(), t, mouth).rotate(ang, center=(400, 720), resample=Image.BICUBIC)
        L = np.asarray(art.resize((s, s), Image.BILINEAR)).astype(np.float32)
        hx = cx - s / 2 + HEAD[0] * s / 800; hy = cy - s / 2 + bob + HEAD[1] * s / 800; hr = HEAD[2] * s / 800
        hs = int(hr * 5.2); halo = np.asarray(Image.fromarray(self.halo).resize((hs, hs), Image.BILINEAR))[..., None]
        self._add(fr, halo * np.array([0.55, 0.8, 1.0], np.float32) * (22 + 120 * e), hx - hs / 2 + 6 * np.sin(t * 1.3), hy - hs / 2 + 5 * np.sin(t * 1.7))
        self._add(fr, L * (0.94 + 0.16 * e), cx - s / 2, cy - s / 2 + bob)
        # energy hands
        hsz = max(8, int(character.HAND.shape[0] * s / 790)); spr = np.asarray(Image.fromarray(character.HAND.clip(0, 255).astype(np.uint8)).resize((hsz, hsz), Image.BILINEAR)).astype(np.float32)
        rest_w = float(np.mean([1.0 if self.anim.gesture_at(t - 0.05 * k)[0] == "rest" else 0.0 for k in range(8)]))
        for side, (dx, dy) in enumerate(hands):
            ex = ey = 0.0; tg = t - gst
            if gest == "wave" and side == 1: ex = 0.05 * np.sin(tg * 9); ey = 0.015 * np.cos(tg * 18)
            if gest == "point" and side == 1: ex = 0.03 * e
            if gest == "open_arms": ey = -0.05 * e; ex = (0.03 * e) * (1 if side else -1)
            if gest == "shrug": ey = -0.035 * np.exp(-((tg % 2.2) - 0.4) ** 2 * 6)
            px = cx + (dx + ex) * s; py = cy + bob + (dy + ey) * s
            self._add(fr, spr * (0.35 + 0.65 * (1 - rest_w)) * (0.9 + 0.2 * e), px - hsz / 2, py - hsz / 2)
            if gest == "point" and side == 1 and rest_w < 0.5:      # faint pointer beam toward the panel
                for k in range(1, 7): self._add(fr, spr[::3, ::3] * 0.12 * (1 - k / 7), px + k * 0.05 * s - hsz / 6, py - hsz / 6)
        # section content
        sec = cur["sec"]; fi = smooth((t - sec["start"] + 0.2) / 0.5) * smooth((sec["end"] + 0.25 - t) / 0.3)
        if kind == "cold_open":
            a = smooth((t - 0.3) / 0.5)
            cur["pill"].x = int(W / 2 - cur["pill"].w / 2); cur["pill"].y = 70; cur["pill"].draw(fr, a, dy=-20 * (1 - a))
            if cur["subject"]:
                sj = cur["subject"]; sj.x = int(W / 2 - sj.w / 2); sj.y = 135; sj.draw(fr, smooth((t - 0.7) / 0.6), dy=14 * (1 - smooth((t - 0.7) / 0.6)))
            for st, lay in cur.get("hook", []):
                a = smooth((t - st) / 0.3) * fi; lay.draw(fr, a, dy=18 * (1 - a))
        else:
            cur["panel"].draw(fr, fi * 0.97)
            for k in ("badge", "head", "src_tag", "src"):
                if k in cur: cur[k].draw(fr, fi, dy=10 * (1 - fi))
            teaser = kind == "teaser"
            for st, (lay, en) in cur.get("bul", {}).items():
                a = smooth((t - st) / 0.35)
                if teaser:
                    prog = min(1.0, max(0.0, (t - st) / max(0.4, (en - st) * 0.8))); lay.draw(fr, 1.0 if prog > 0 else 0, reveal=prog)
                else: lay.draw(fr, a * fi, dy=14 * (1 - a))
            for st, (lay, en) in cur.get("screens", {}).items():
                a = smooth((t - st) / 0.35) * fi
                lay.draw(fr, a, dy=14 * (1 - a))
        # captions
        for (a, b, lay) in self.caps:
            if a - 0.05 <= t <= b + 0.12:
                k = min(smooth((t - a + 0.05) / 0.12), smooth((b + 0.12 - t) / 0.12)); lay.draw(fr, k)
        # like/subscribe CTA (lower third, above captions)
        for c0 in self.ctas:
            ov = cta.frame(t - c0)
            if ov is not None: Layer(ov, (W - ov.size[0]) // 2 + 300, 700).draw(fr, 1.0)
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
