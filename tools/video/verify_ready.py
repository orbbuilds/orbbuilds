#!/usr/bin/env python3
"""Post-render READY gate for a review episode, recomputed from disk (no reliance on render logs).

  verify_ready.py content/scripts/<stem>.json [--thumb-ref path.jpg] [--short-prefix "Title starts"]

Checks: screen files exist; validate_script OK; expected music seed != 1; outputs exist
(mp4, -short.mp4, -short-meta.json, -xclip.mp4, -thumb.jpg); thumb matches a reference
(mean abs pixel diff); Short title prefix; xclip windows keep every screen line; chapters valid.
Exit 0 = all PASS, 1 = any FAIL. Read-only: renders nothing, uploads nothing.
"""
import argparse, json, os, subprocess, sys

ROOT = "/workspace/orbbuilds"
TV = os.path.join(ROOT, "tools/video")
ap = argparse.ArgumentParser()
ap.add_argument("script"); ap.add_argument("--thumb-ref"); ap.add_argument("--short-prefix")
ap.add_argument("--max-thumb-diff", type=float, default=6.0)
ap.add_argument("--expect-screens", type=int, default=0)
a = ap.parse_args()
script = os.path.realpath(a.script); stem = os.path.basename(script)[:-5]
s = json.load(open(script)); work = f"/workspace/video-build/{stem}"; d = os.path.join(ROOT, "content/drafts")
res = []
def rec(ok, name, info=""): res.append((ok, name, info))

screens = []
def walk(o):
    if isinstance(o, dict):
        if isinstance(o.get("screen"), str): screens.append(o["screen"])
        [walk(v) for k, v in o.items() if not k.startswith("_")]
    elif isinstance(o, list): [walk(v) for v in o]
walk({k: v for k, v in s.items() if k != "meta"})
miss = [p for p in screens if not os.path.exists(p if os.path.isabs(p) else os.path.join(ROOT, p))]
rec(len(screens) >= a.expect_screens and not miss, "screens on disk", f"{len(screens)} referenced, missing={miss}")

v = subprocess.run([sys.executable, os.path.join(TV, "validate_script.py"), script], capture_output=True, text=True)
out = (v.stdout + v.stderr).strip().splitlines()
rec(v.returncode == 0 and not any("warn" in l.lower() for l in out), "validate_script", " | ".join(out))

ck = subprocess.run(f"printf %s '{stem}' | cksum", shell=True, capture_output=True, text=True).stdout.split()[0]
seed = int(ck) % 2147483646 + 2
rec(seed != 1 and not os.environ.get("MUSIC_SEED"), "music seed", f"expected {seed} (only valid if production did not set MUSIC_SEED/BG_SEED)")

files = {k: os.path.join(d, stem + k) for k in [".mp4", "-short.mp4", "-short-meta.json", "-xclip.mp4", "-thumb.jpg"]}
for k, p in files.items():
    rec(os.path.exists(p) and os.path.getsize(p) > 0, f"output {k}", p if os.path.exists(p) else "MISSING")
up = os.path.join(d, stem + "-upload.mp4"); rec(True, "output -upload.mp4 (info)", "present" if os.path.exists(up) else "absent (fine if publish uses the main mp4)")

if a.thumb_ref and os.path.exists(files["-thumb.jpg"]):
    from PIL import Image, ImageChops, ImageStat
    A = Image.open(files["-thumb.jpg"]).convert("RGB"); B = Image.open(a.thumb_ref).convert("RGB").resize(A.size)
    diff = sum(ImageStat.Stat(ImageChops.difference(A, B)).mean) / 3
    rec(diff <= a.max_thumb_diff, "thumb matches ref", f"mean abs diff {diff:.2f} (max {a.max_thumb_diff}) vs {a.thumb_ref}")

if a.short_prefix:
    p = files["-short-meta.json"]
    t = json.load(open(p)).get("title", "") if os.path.exists(p) else ""
    rec(t.startswith(a.short_prefix), "Short title prefix", repr(t))

tj = os.path.join(work, "timing.json")
if os.path.exists(tj):
    x = subprocess.run([sys.executable, os.path.join(TV, "xclip_windows.py"), tj, "--script", script], capture_output=True, text=True)
    rec(x.returncode == 0 and "screen lines dropped" not in x.stderr, "xclip keeps screen lines", x.stderr.strip())
    c = subprocess.run([sys.executable, os.path.join(TV, "chapters.py"), "check", tj, script], capture_output=True, text=True)
    rec(c.returncode == 0, "chapters valid", (c.stdout + c.stderr).strip()[:200])
else:
    rec(False, "timing.json", f"missing {tj} (not rendered yet)")

for ok, n, i in res: print(f"{'PASS' if ok else 'FAIL'}  {n}: {i}")
bad = [n for ok, n, _ in res if not ok]
print("READY GATE:", "PASS" if not bad else f"FAIL ({len(bad)}: {', '.join(bad)})")
sys.exit(1 if bad else 0)
