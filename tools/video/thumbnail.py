#!/usr/bin/env python3
"""P6 thumbnail grammar (docs/AUDIENCE_STRATEGY.md): Lumin's face big and clear,
2-4 words of huge text with ONE highlighted word, small product chip, no text over the face.
Text should ADD to the title, not repeat it.

Usage:
  thumbnail.py out.jpg --product "GEMINI 4 ARGON" --line1 "HYPE" --line2 "CHECK" \
      [--hl 2] [--tag "AI host · not tested yet"] [--bg assets/lumin-full.png]
--hl picks which line gets the contrast color (1 or 2).
"""
import argparse, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
W, H = 1280, 720
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
COND = "/usr/share/fonts/truetype/sand-box/google/Antonio/Antonio-VariableFont_wght.ttf"


def font(path, size, bold=True):
    f = ImageFont.truetype(path, size)
    if bold:
        try:
            f.set_variation_by_name("Bold")
        except Exception:
            pass
    return f


def fit(text, path, max_w, start, draw, max_h=10_000):
    s = start
    while s > 40:
        f = font(path, s)
        b = draw.textbbox((0, 0), text, font=f, stroke_width=8)
        if b[2] - b[0] <= max_w and b[3] - b[1] <= max_h:
            return f
        s -= 4
    return font(path, 40)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--product", required=True)
    ap.add_argument("--line1", required=True)
    ap.add_argument("--line2", default="")
    ap.add_argument("--hl", type=int, default=2)
    ap.add_argument("--tag", default="")
    ap.add_argument("--bg", default=os.path.join(ROOT, "assets", "lumin-full.png"))
    a = ap.parse_args()

    src = Image.open(a.bg).convert("RGB")
    # Zoom so Lumin's head+torso fill the right ~55%: scale 1.55x, anchor his head.
    z = 1.55
    big = src.resize((int(src.width * z), int(src.height * z)), Image.LANCZOS)
    # Lumin's face centre in lumin-full is ~ (640, 230) at 1280x720.
    fx, fy = int(640 * z), int(230 * z)
    target_x, target_y = int(W * 0.72), int(H * 0.40)
    canvas = Image.new("RGB", (W, H), (6, 10, 30))
    canvas.paste(big, (target_x - fx, target_y - fy))

    # Soft left-to-right darkening (no hard seam) so text reads without covering the face.
    grad = Image.new("L", (W, 1))
    for x in range(W):
        t = x / W
        grad.putpixel((x, 0), int(235 * max(0.0, 1 - t / 0.55) ** 1.4))
    grad = grad.resize((W, H))
    canvas = Image.composite(Image.new("RGB", (W, H), (4, 6, 20)), canvas, grad)

    d = ImageDraw.Draw(canvas)
    left, max_w = 56, int(W * 0.42)

    # Product chip (small, top-left): search cue, not the headline.
    pf = font(FONT, 40)
    pw = d.textlength(a.product, font=pf)
    d.rounded_rectangle((left - 14, 48, left + pw + 14, 108), radius=12, fill=(30, 120, 255))
    d.text((left, 54), a.product, font=pf, fill="white")

    lines = [a.line1] + ([a.line2] if a.line2 else [])
    y = 140
    line_h = (H - 140 - 100) // len(lines) - 10  # keep the block clear of the tag row
    for i, ln in enumerate(lines, 1):
        f = fit(ln, COND, max_w, 260, d, line_h)
        col = (255, 214, 10) if i == a.hl else (255, 255, 255)
        oy = d.textbbox((0, 0), ln, font=f, stroke_width=8)[1]
        d.text((left, y - oy), ln, font=f, fill=col, stroke_width=8, stroke_fill=(0, 0, 0))
        y += line_h + 10

    if a.tag:
        tf = font(FONT, 30)
        d.text((left, H - 70), a.tag, font=tf, fill=(220, 230, 255), stroke_width=3, stroke_fill=(0, 0, 0))

    canvas = canvas.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=3))
    canvas.save(a.out, quality=92)
    print(a.out, os.path.getsize(a.out), "bytes")


if __name__ == "__main__":
    main()
