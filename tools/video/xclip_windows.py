#!/usr/bin/env python3
"""Pick hook-first social (X/Bluesky) windows from timing.json.

Recipe (AUDIENCE_STRATEGY #22 / #16, tick 104 + 121): open on the cold_open
(spoken hook + title; letterbox crop so centered title survives), then the
full caveats/verdict section (stacked Shorts crop), then the like/subscribe
CTA end card when present. Muted in-feed autoplay on X needs the hook first;
the YouTube Short keeps opening on the best fact instead.

Tick 166: with --script, verdict lines carrying a `screen` (real hands-on
footage) are kept first when the clip must be trimmed: the picker chooses the
contiguous run of verdict lines that fits and includes the most screen lines
(then the most lines, then the earliest start). Without --script, or when no
line has a screen, it trims from the end exactly as before.

Usage: xclip_windows.py <timing.json> [--script script.json] [--max 58] [--hook cold_open] [--verdict caveats]
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
    ap.add_argument("--script", default=None)
    a = ap.parse_args()
    t = json.load(open(a.timing))
    if a.script:
        sc = json.load(open(a.script))
        for si, sec in enumerate(t["sections"]):
            src = sc["sections"][si]["lines"] if si < len(sc.get("sections", [])) else []
            for li, ln in enumerate(sec.get("lines", [])):
                if li < len(src) and src[li].get("screen"):
                    ln["screen"] = src[li]["screen"]
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

    def span(i, j):  # verdict lines i..j inclusive
        return (max(0.0, vl[i]["start"] - PRE), min(t["duration"], vl[j]["end"] + POST))

    def total_of(v):
        return (h[1] - h[0]) + (v[1] - v[0]) + ((c[1] - c[0]) if c else 0)

    n = len(vl)
    if any(ln.get("screen") for ln in vl):
        best = None
        for i in range(n):
            for j in range(i, n):
                if total_of(span(i, j)) <= a.max:
                    score = (sum(1 for ln in vl[i:j + 1] if ln.get("screen")), j - i + 1, -i)
                    if best is None or score > best[0]:
                        best = (score, i, j)
        if best is None:
            sys.exit("hook alone exceeds --max; raise --max or trim the cold open")
        i0, j0 = best[1], best[2]
    else:
        i0, j0 = 0, n - 1
        while j0 >= 0 and total_of(span(0, j0)) > a.max:
            j0 -= 1
        if j0 < 0:
            sys.exit("hook alone exceeds --max; raise --max or trim the cold open")
    keep = j0 - i0 + 1

    note = ""
    if keep < n:
        note = f"; kept verdict lines {i0 + 1}-{j0 + 1} of {n} to fit"
    lost = [k + 1 for k in range(n) if vl[k].get("screen") and not (i0 <= k <= j0)]
    if lost:
        note += f"; WARN screen lines dropped: {lost}"
    if c is None:
        note += "; no like_subscribe CTA"

    v = span(i0, j0)
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
