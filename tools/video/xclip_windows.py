#!/usr/bin/env python3
"""Pick hook-first social (X/Bluesky) windows from timing.json.

Recipe (AUDIENCE_STRATEGY #22 / #16, tick 104 + 121): open on the cold_open
(spoken hook + title; letterbox crop so centered title survives), then the
full caveats/verdict section (stacked Shorts crop), then the like/subscribe
CTA end card when present. Muted in-feed autoplay on X needs the hook first;
the YouTube Short keeps opening on the best fact instead.

Usage: xclip_windows.py <timing.json> [--max 58] [--hook cold_open] [--verdict caveats]
Prints `mode:start:end ...` for xclip_splice.sh (mode = letterbox|stacked).
"""
import argparse, json, sys

PRE, POST = 0.15, 0.25

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("timing")
    ap.add_argument("--max", type=float, default=58.0)
    ap.add_argument("--hook", default="cold_open")
    ap.add_argument("--verdict", default="caveats")
    a = ap.parse_args()
    t = json.load(open(a.timing))
    secs = {s["id"]: s for s in t["sections"]}
    if a.hook not in secs or not secs[a.hook].get("lines"):
        sys.exit(f"section '{a.hook}' missing or empty in {a.timing}")
    if a.verdict not in secs or not secs[a.verdict].get("lines"):
        sys.exit(f"section '{a.verdict}' missing or empty in {a.timing}")

    hl = secs[a.hook]["lines"]
    h = (max(0.0, hl[0]["start"] - PRE), min(t["duration"], hl[-1]["end"] + POST))
    vl = secs[a.verdict]["lines"]

    cl = [ln for s_ in t["sections"] for ln in s_.get("lines", []) if ln.get("cta") == "like_subscribe"]
    c = None
    if cl:
        c = (max(0.0, cl[0]["start"] - PRE), min(t["duration"], cl[0]["end"] + POST))

    def vwin(keep):
        return (max(0.0, vl[0]["start"] - PRE), min(t["duration"], vl[keep - 1]["end"] + POST))

    keep = len(vl)
    while keep >= 1:
        v = vwin(keep)
        total = (h[1] - h[0]) + (v[1] - v[0]) + ((c[1] - c[0]) if c else 0)
        if total <= a.max:
            break
        keep -= 1
    else:
        sys.exit("hook alone exceeds --max; raise --max or trim the cold open")

    note = ""
    if keep < len(vl):
        note = f"; dropped {len(vl) - keep}/{len(vl)} caveat lines to fit"
    if c is None:
        note += "; no like_subscribe CTA"

    v = vwin(keep)
    parts = [f"letterbox:{h[0]:.2f}:{h[1]:.2f}", f"stacked:{v[0]:.2f}:{v[1]:.2f}"]
    if c:
        parts.append(f"stacked:{c[0]:.2f}:{c[1]:.2f}")
    total = (h[1] - h[0]) + (v[1] - v[0]) + ((c[1] - c[0]) if c else 0)
    print(" ".join(parts))
    print(
        f"hook {h[1]-h[0]:.1f}s + verdict lines {keep}/{len(vl)} + "
        f"{'cta' if c else 'no-cta'}, total {total:.1f}s (max {a.max}){note}",
        file=sys.stderr,
    )

if __name__ == "__main__":
    main()
