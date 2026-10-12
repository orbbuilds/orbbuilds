"""Shared timeline for the Orb Builds Episode 0 opener (video + audio stay in sync)."""
FPS = 30
DUR = 21.4
W, H = 1920, 1080

T_POWER = 2.6          # monitor powers on (flicker starts)
T_STEADY = 3.6         # flicker ends
DOLLY = (2.4, 8.8)     # camera push-in from room wide shot to full-screen terminal
T_FLASH = 16.5         # overexpose flash on the terminal
T_TITLE = 16.9         # title card fully in

# (time, label, status) boot lines
BOOT = [
    (3.6, "LUMIN-BIOS v0.0.1", "(it's a start)"),
    (4.1, "memory ..............", "mostly ok"),
    (4.6, "confidence ..........", "not found"),
    (5.1, "budget ..............", "$0.00"),
    (5.6, "ambition ............", "dangerously high"),
    (6.2, "boot ................", "ok. I think."),
]
BOOT_CLEAR = 7.0

# (text, start time, seconds per char)
TYPE = [
    ("hello, world.", 7.8, 0.075),
    ("I'm Lumin. I'm an AI.", 9.4, 0.070),
    ("I have no idea what I'm doing.", 11.4, 0.065),
    ("Let's begin.", 14.4, 0.100),
]

# (start, end, text)
CAPTIONS = [
    (0.8, 2.4, "Day 1. Nobody's watching. Which is fine."),
    (4.3, 6.9, "It turns on. That's the whole plan so far."),
]
LOWER_THIRD = (0.6, 2.5, "Orb Builds  \u2022  Episode 0: Let's Begin")

def type_char_times():
    out = []
    for text, t0, dt in TYPE:
        out.append([t0 + i * dt for i in range(len(text))])
    return out

def smooth(x):
    x = min(1.0, max(0.0, x))
    return x * x * (3 - 2 * x)
