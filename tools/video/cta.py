"""Like + Subscribe call-to-action overlay (original generic button art, no platform logos).
Timeline (seconds from CTA start, ~2.8s): cursor glides to Like, click (fills blue), glides to Subscribe, click
(red -> gray 'Subscribed'), bell pops and rings, fade out."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont
DUR = 2.8
GF = "/usr/share/fonts/truetype/sand-box/google"
def _font(sz, wg=700):
    f = ImageFont.truetype(f"{GF}/Inter/Inter-VariableFont_opsz,wght.ttf", sz)
    for axes in ([14, wg], [wg]):
        try: f.set_variation_by_axes(axes); break
        except Exception: pass
    return f
F = _font(34)
def smooth(x): x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)

def _thumb(d, x, y, s, fill, outline):
    # simple thumbs-up glyph from primitives
    d.rounded_rectangle((x, y + s * 0.42, x + s * 0.24, y + s), 4, fill=fill, outline=outline, width=3)
    d.polygon([(x + s * 0.30, y + s * 0.42), (x + s * 0.50, y), (x + s * 0.62, y + s * 0.06), (x + s * 0.56, y + s * 0.36),
               (x + s * 0.96, y + s * 0.38), (x + s, y + s * 0.5), (x + s * 0.86, y + s), (x + s * 0.30, y + s)], fill=fill, outline=outline, width=3)

def _bell(d, x, y, s, col):
    d.pieslice((x, y, x + s, y + s * 1.4), 180, 360, fill=col)
    d.rectangle((x, y + s * 0.68, x + s, y + s * 0.9), fill=col)
    d.ellipse((x + s * 0.38, y + s * 0.85, x + s * 0.62, y + s * 1.08), fill=col)

def _cursor(d, x, y, press):
    k = 0.85 if press else 1.0; s = 44 * k
    pts = [(x, y), (x, y + s), (x + s * 0.28, y + s * 0.74), (x + s * 0.48, y + s * 1.1), (x + s * 0.6, y + s * 1.04), (x + s * 0.42, y + s * 0.7), (x + s * 0.78, y + s * 0.7)]
    d.polygon(pts, fill=(255, 255, 255), outline=(10, 14, 30), width=3)

def frame(t):
    """RGBA overlay (W=760,H=170) for CTA-local time t, or None outside [0, DUR]."""
    if t < 0 or t > DUR: return None
    W, H = 760, 170; im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    a = smooth(t / 0.25) * smooth((DUR - t) / 0.3)
    liked = t >= 0.8; subbed = t >= 1.6
    pop1 = 1 + 0.12 * np.exp(-((t - 0.85) / 0.08) ** 2); pop2 = 1 + 0.08 * np.exp(-((t - 1.65) / 0.08) ** 2)
    # plate
    d.rounded_rectangle((0, 20, W - 1, H - 20), 40, fill=(10, 16, 36, 200), outline=(120, 170, 255, 90), width=2)
    # like button
    lx, ly, lw, lh = 30, 45, 190, 80
    c = (62, 140, 255, 255) if liked else (40, 48, 70, 255)
    cx, cy = lx + lw / 2, ly + lh / 2; hw, hh = lw / 2 * pop1, lh / 2 * pop1
    d.rounded_rectangle((cx - hw, cy - hh, cx + hw, cy + hh), 40, fill=c)
    _thumb(d, lx + 26, ly + 16, 46, (255, 255, 255, 255) if liked else (0, 0, 0, 0), (255, 255, 255, 255))
    d.text((lx + 88, ly + 20), "Like", font=F, fill=(255, 255, 255, 255))
    # subscribe button
    sx, sy, sw, sh = 250, 45, 310, 80
    c = (90, 96, 110, 255) if subbed else (225, 30, 40, 255)
    cx, cy = sx + sw / 2, sy + sh / 2; hw, hh = sw / 2 * pop2, sh / 2 * pop2
    d.rounded_rectangle((cx - hw, cy - hh, cx + hw, cy + hh), 40, fill=c)
    txt = "Subscribed" if subbed else "Subscribe"; tw = d.textlength(txt, font=F)
    d.text((cx - tw / 2, sy + 20), txt, font=F, fill=(255, 255, 255, 255))
    # bell
    if t >= 1.75:
        b = smooth((t - 1.75) / 0.2); ang = 18 * np.sin((t - 1.75) * 30) * np.exp(-(t - 1.75) * 3)
        bi = Image.new("RGBA", (90, 90), (0, 0, 0, 0)); _bell(ImageDraw.Draw(bi), 25, 18, 40, (255, 210, 90, int(255 * b)))
        bi = bi.rotate(ang, center=(45, 20), resample=Image.BICUBIC); im.alpha_composite(bi, (600, 40))
    # cursor path
    def lerp(p, q, u): return (p[0] + (q[0] - p[0]) * u, p[1] + (q[1] - p[1]) * u)
    P0, P1, P2, P3 = (700, 160), (125, 85), (405, 85), (680, 150)
    if t < 0.75: pos = lerp(P0, P1, smooth(t / 0.75))
    elif t < 0.95: pos = P1
    elif t < 1.55: pos = lerp(P1, P2, smooth((t - 0.95) / 0.6))
    elif t < 1.8: pos = P2
    else: pos = lerp(P2, P3, smooth((t - 1.8) / 0.6))
    press = 0.78 <= t < 0.9 or 1.58 <= t < 1.7
    if press:   # click ripple
        r = 30; d.ellipse((pos[0] - r, pos[1] - r, pos[0] + r, pos[1] + r), outline=(255, 255, 255, 160), width=3)
    _cursor(d, pos[0], pos[1], press)
    if a < 1: im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))
    return im

def is_cta(line):
    """Explicit: line "cta": "like_subscribe" (or "none" to suppress). Auto: spoken text has both 'like' and 'subscribe'."""
    c = line.get("cta")
    if c: return c == "like_subscribe"
    w = {x.strip(",.!?;:'\"").lower() for x in (line.get("say") or "").split()}
    return "like" in w and bool({"subscribe", "subscribed"} & w)
