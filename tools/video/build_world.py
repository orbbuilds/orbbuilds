"""Draw the static room / desk / monitor / Lumin layers (3840x2160 'world') used by render.py."""
import numpy as np, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont
OUT = "/workspace/video-build"
ASSETS = "/workspace/orbbuilds/assets"
WW, WH = 3840, 2160
SCREEN = (2450, 760, 3602, 1408)       # 1152x648 (16:9)
LUMIN_CENTER = (1750, 1120)             # head centre in world
rng = np.random.RandomState(7)
os.makedirs(OUT, exist_ok=True)
FONT = "/usr/share/fonts/truetype/sand-box/google/IBM Plex Mono/IBMPlexMono-Medium.ttf"

def room():
    y = np.linspace(0, 1, WH)[:, None, None]
    x = np.linspace(0, 1, WW)[None, :, None]
    top = np.array([62, 80, 120.]); bot = np.array([38, 50, 82.])
    img = top * (1 - y) + bot * y + 0 * x
    img = img + (rng.randn(WH // 8, WW // 8, 1).repeat(8, 0).repeat(8, 1) * 1.5)
    im = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(im)
    # window with night city
    wx0, wy0, wx1, wy1 = 160, 260, 1000, 1180
    d.rectangle((wx0 - 24, wy0 - 24, wx1 + 24, wy1 + 24), fill=(34, 40, 62))
    sky = Image.new("RGB", (wx1 - wx0, wy1 - wy0))
    sd = ImageDraw.Draw(sky)
    for k in range(sky.height):
        f = k / sky.height
        sd.line((0, k, sky.width, k), fill=(int(14 + 30 * f), int(22 + 34 * f), int(58 + 40 * f)))
    for _ in range(140):
        bx = rng.randint(0, sky.width); by = rng.randint(int(sky.height * .55), sky.height)
        r = rng.randint(3, 9)
        col = [(255, 210, 140), (180, 220, 255), (255, 170, 120)][rng.randint(0, 3)]
        sd.ellipse((bx - r, by - r, bx + r, by + r), fill=col)
    for _ in range(50):
        bx = rng.randint(0, sky.width); by = rng.randint(0, int(sky.height * .5))
        sd.ellipse((bx - 2, by - 2, bx + 2, by + 2), fill=(220, 230, 255))
    sky = sky.filter(ImageFilter.GaussianBlur(2))
    im.paste(sky, (wx0, wy0))
    d = ImageDraw.Draw(im)
    d.rectangle((wx0 - 24, (wy0 + wy1) // 2 - 10, wx1 + 24, (wy0 + wy1) // 2 + 10), fill=(34, 40, 62))
    d.rectangle(((wx0 + wx1) // 2 - 10, wy0 - 24, (wx0 + wx1) // 2 + 10, wy1 + 24), fill=(34, 40, 62))
    # shelf with books + plant
    d.rectangle((2900, 470, 3760, 500), fill=(70, 56, 52))
    bx = 2940
    for w_, h_, c in [(46, 150, (110, 70, 80)), (38, 180, (70, 100, 120)), (52, 140, (120, 100, 70)),
                      (40, 170, (80, 80, 130)), (44, 150, (100, 120, 90))]:
        d.rectangle((bx, 470 - h_, bx + w_, 470), fill=c); bx += w_ + 6
    d.polygon([(3480, 470), (3500, 380), (3680, 380), (3700, 470)], fill=(120, 90, 80))
    for ang in range(-60, 61, 20):
        ex = 3590 + ang * 2.6; ey = 380 - 170 + abs(ang)
        d.line((3590, 382, ex, ey), fill=(60, 120, 90), width=10)
        d.ellipse((ex - 26, ey - 18, ex + 26, ey + 18), fill=(66, 134, 98))
    # little wall clock (unhelpfully says 3:07)
    cx, cy, r = 1330, 520, 110
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(150, 160, 180), outline=(40, 46, 70), width=10)
    d.line((cx, cy, cx - 40, cy + 20), fill=(30, 34, 50), width=9)   # hour ~ 3-ish (cartoon)
    d.line((cx, cy, cx + 20, cy - 70), fill=(30, 34, 50), width=6)
    return im

def lumin_layer():
    a = np.asarray(Image.open(f"{ASSETS}/lumin.png").convert("RGB")).astype(np.float32)
    bg = np.array([0, 5, 34], np.float32)
    diff = np.clip(a - bg, 0, 255)
    yy, xx = np.mgrid[0:800, 0:800]
    r = np.sqrt(((xx - 400) / 330.) ** 2 + ((yy - 410) / 385.) ** 2)
    m = np.clip((1.0 - r) / 0.18, 0, 1)
    diff = diff * m[..., None]
    big = Image.fromarray(diff.astype(np.uint8)).resize((1600, 1600), Image.LANCZOS)
    canvas = Image.new("RGB", (WW, WH), (0, 0, 0))
    ox, oy = LUMIN_CENTER[0] - 800, 520
    # head centre in the avatar is at about (400, 300)/800 -> world (ox+800, oy+600)
    ox = LUMIN_CENTER[0] - 800
    oy = LUMIN_CENTER[1] - 600
    canvas.paste(big, (ox, oy))
    return canvas, (ox, oy)

def desk():
    im = Image.new("RGBA", (WW, WH), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    DT, DF = 1560, 1720
    # desk surface + front
    for k in range(DT, DF):
        f = (k - DT) / (DF - DT)
        d.line((0, k, WW, k), fill=(int(96 + 40 * f), int(98 + 38 * f), int(118 + 30 * f), 255))
    d.rectangle((0, DF, WW, WH), fill=(46, 48, 66, 255))
    d.rectangle((0, DF, WW, DF + 14), fill=(120, 124, 148, 255))
    # monitor
    bx0, by0, bx1, by1 = 2410, 720, 3642, 1448
    d.rounded_rectangle((2970, 1440, 3082, 1600), 10, fill=(40, 44, 58, 255))
    d.ellipse((2780, 1560, 3270, 1630), fill=(44, 48, 64, 255))
    d.rounded_rectangle((bx0, by0, bx1, by1), 26, fill=(34, 38, 52, 255))
    d.rounded_rectangle((bx0 + 6, by0 + 6, bx1 - 6, by1 - 6), 22, outline=(70, 76, 98, 255), width=3)
    d.rectangle(SCREEN, fill=(2, 3, 6, 255))
    d.ellipse((3000, 1425, 3020, 1445), fill=(80, 255, 170, 255))  # power LED
    # keyboard
    d.polygon([(2580, 1618), (3320, 1618), (3400, 1700), (2500, 1700)], fill=(30, 34, 48, 255))
    for r_ in range(4):
        yy = 1626 + r_ * 17
        xl = 2574 - r_ * 18; xr = 3326 + r_ * 18
        for kx in np.linspace(xl + 10, xr - 10, 24 - r_):
            d.rectangle((kx - 14, yy, kx + 14, yy + 11), fill=(58, 64, 88, 255))
    # mug
    d.rounded_rectangle((2250, 1470, 2350, 1590), 14, fill=(200, 205, 220, 255))
    d.arc((2330, 1495, 2395, 1560), -90, 90, fill=(200, 205, 220, 255), width=12)
    d.ellipse((2250, 1462, 2350, 1486), fill=(70, 50, 44, 255))
    # sticky note on the wall above monitor
    d.rectangle((3480, 610, 3606, 700), fill=(250, 226, 110, 255))
    f = ImageFont.truetype(FONT, 17)
    d.text((3490, 622), "TODO:", font=f, fill=(60, 50, 20, 255))
    d.text((3490, 648), "everything", font=f, fill=(60, 50, 20, 255))
    return im

if __name__ == "__main__":
    room().save(f"{OUT}/room.png")
    L, off = lumin_layer(); L.save(f"{OUT}/lumin_layer.png")
    desk().save(f"{OUT}/desk.png")
    print("ok", off)
