"""Lumin character animation for the review renderer (default on).
 - lip sync: glowing light-bar mouth whose openness follows the voice envelope (closed in silence)
 - blinks every ~2.5-5.5s, idle float/bob/sway, head tilt, halo wobble
 - glowing "energy hands" that perform gestures: wave, point, open_arms, shrug, rest
Gestures come from script.json line field "gesture" or are auto-picked (see auto_gesture). Peaks in the voice add emphasis."""
import re, numpy as np
from PIL import Image, ImageDraw, ImageFilter

FACE = (208, 218, 214)                     # face colour in the bg-subtracted art space
EYES = [(305, 308, 40, 40), (467, 303, 40, 40)]   # cx, cy, rx, ry in 800px art
MOUTH = (386, 372)
GESTURES = ("rest", "wave", "point", "open_arms", "shrug")

def auto_gesture(kind, say, first, last):
    s = say.lower()
    if re.search(r"\b(like|subscribe)\b", s) and "subscribe" in s: return "point"
    if kind == "cold_open" and first: return "wave"
    if kind == "outro" and last: return "wave"
    if re.search(r"\b(look|here's|this one|demo|on screen|watch this|check (this|it) out)\b", s): return "point"
    if kind == "caveats" or re.search(r"\b(haven't|not sure|unproven|bug|fail\w*|broke|honest(ly)?|caveat)\b", s): return "shrug"
    if kind == "opinion" or re.search(r"\b(insane|wild|huge|hyped|amazing|bonkers|love)\b", s): return "open_arms"
    if kind in ("what_dropped", "teaser"): return "point"
    return "rest"

def smooth(x): x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)

def erase_smile(base):
    """base: PIL RGB (bg-subtracted art). Paint over the drawn smile so the animated mouth replaces it."""
    m = Image.new("L", base.size, 0); ImageDraw.Draw(m).ellipse((MOUTH[0] - 46, MOUTH[1] - 16, MOUTH[0] + 46, MOUTH[1] + 16), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(6))
    patch = Image.new("RGB", base.size, FACE)
    return Image.composite(patch, base, m)

def blink_amount(t, seed=3):
    """0 open .. 1 closed. Blink ~0.16s, pseudo-random spacing, deterministic per t."""
    rs = np.random.RandomState(seed); tt = 0.8
    while tt < t + 1:
        d = t - tt
        if 0 <= d < 0.18: return float(np.sin(np.pi * d / 0.18))
        tt += rs.uniform(2.4, 5.5)
    return 0.0

def draw_face(img, t, openness):
    """Draw blink lids + mouth onto PIL RGB art copy."""
    d = ImageDraw.Draw(img); b = blink_amount(t)
    if b > 0.02:
        for cx, cy, rx, ry in EYES:
            top = cy - ry - 4; bot = top + (2 * ry + 8) * b
            lid = Image.new("L", img.size, 0); ImageDraw.Draw(lid).ellipse((cx - rx - 6, cy - ry - 6, cx + rx + 6, cy + ry + 6), fill=255)
            ImageDraw.Draw(lid).rectangle((0, bot, img.size[0], img.size[1]), fill=0)
            img.paste(Image.new("RGB", img.size, FACE), (0, 0), lid)
            if b > 0.6: d.line((cx - rx, bot - 2, cx + rx, bot - 2), fill=(40, 60, 120), width=4)
    o = max(0.0, min(1.0, openness)); w = 40 + 14 * o; h = 4 + 26 * o
    x0, y0, x1, y1 = MOUTH[0] - w / 2, MOUTH[1] - h / 2, MOUTH[0] + w / 2, MOUTH[1] + h / 2
    glow = Image.new("RGB", img.size, (0, 0, 0)); ImageDraw.Draw(glow).rounded_rectangle((x0 - 4, y0 - 4, x1 + 4, y1 + 4), 12, fill=(60, 150, 255))
    glow = glow.filter(ImageFilter.GaussianBlur(5))
    img.paste(Image.blend(img, Image.new("RGB", img.size, (70, 160, 255)), 0.85), (0, 0), glow.convert("L").point(lambda v: min(255, v * 2)))
    d.rounded_rectangle((x0, y0, x1, y1), int(min(h, w) / 2), fill=(16, 26, 70), outline=(120, 215, 255), width=3)
    if o > 0.25:   # inner light-bar
        d.rounded_rectangle((x0 + 8, MOUTH[1] - 2, x1 - 8, MOUTH[1] + 2), 2, fill=(150, 230, 255))
    return img

def _hand_sprite(r=34):
    n = r * 4; yy, xx = np.mgrid[-n // 2:n // 2, -n // 2:n // 2]; d = np.sqrt(xx ** 2 + yy ** 2)
    core = np.clip((r - d) / 3, 0, 1); glow = np.exp(-(d / (r * 1.1)) ** 2)
    a = core[..., None] * np.array([215, 230, 255], np.float32) + glow[..., None] * np.array([40, 110, 255], np.float32) * 0.9
    return a.astype(np.float32)
HAND = _hand_sprite()

# hand target poses, relative to figure centre, in units of figure size (L=viewer-left, R=viewer-right)
POSES = {
    "rest":      ((-0.27, 0.17), (0.27, 0.19)),
    "wave":      ((-0.27, 0.17), (0.31, -0.13)),
    "point":     ((-0.27, 0.17), (0.40, -0.02)),
    "open_arms": ((-0.36, -0.05), (0.36, -0.05)),
    "shrug":     ((-0.29, 0.01), (0.29, 0.01)),
}
TILT = {"rest": 0, "wave": 3, "point": -2, "open_arms": 0, "shrug": 6}

class Animator:
    def __init__(self, lines):
        """lines: [(start, end, gesture)] for every spoken line."""
        self.lines = sorted(lines)
    def gesture_at(self, t):
        g, st = "rest", 0
        for a, b, gg in self.lines:
            if a - 0.15 <= t <= b + 0.35: g, st = gg, a
        return g, st
    def pose(self, t):
        """Window-averaged pose (0.45s) = smooth eased transitions, no jitter. Returns hands, tilt, gesture, gesture start."""
        Ps, Ts = [], []
        for k in range(10):
            g, _ = self.gesture_at(t - 0.045 * k); w = 1.0
            Ps.append(np.array(POSES[g], np.float32)); Ts.append(TILT[g])
        g, st = self.gesture_at(t)
        return np.mean(Ps, 0), float(np.mean(Ts)), g, st
