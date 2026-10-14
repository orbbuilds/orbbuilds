#!/usr/bin/env python3
"""Pick Shorts windows from an episode's timing.json, snapped to spoken-line boundaries.

Recipe (AUDIENCE_STRATEGY.md, experiment #5): open on the best real fact
(the `what_dropped` section, from its first line), end on the verdict
(`caveats` section, whole). Lines are dropped from the END of the fact
section until the total fits the budget, so no sentence is ever chopped.
Skips intro and outro. With --cta, also appends the spoken like/subscribe line
(the timing line tagged `cta: like_subscribe`, whose button-click animation reads
fine in the vertical layout, tick 14) as an end card, but only if it costs at most
--cta-drop fact lines; otherwise the Short is cut without it and a note goes to stderr.

Usage: short_windows.py <timing.json> [--max 58] [--fact what_dropped] [--verdict caveats] [--cta] [--cta-drop 1]
Prints windows as `start:end start:end` for shorts_splice.sh, plus a summary on stderr.
"""
import argparse, json, sys

PRE, POST = 0.15, 0.25  # small pads so first/last syllables aren't clipped

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("timing")
    ap.add_argument("--max", type=float, default=58.0)
    ap.add_argument("--fact", default="what_dropped")
    ap.add_argument("--verdict", default="caveats")
    ap.add_argument("--cta", action="store_true", help="append the like/subscribe line as an end card if it fits")
    ap.add_argument("--cta-drop", type=int, default=1, help="max fact lines the CTA may cost")
    a = ap.parse_args()
    t = json.load(open(a.timing))
    secs = {s["id"]: s for s in t["sections"]}
    for k in (a.fact, a.verdict):
        if k not in secs or not secs[k].get("lines"):
            sys.exit(f"section '{k}' missing or empty in {a.timing}")
    vl = secs[a.verdict]["lines"]
    v = (max(0.0, vl[0]["start"] - PRE), min(t["duration"], vl[-1]["end"] + POST))
    budget = a.max - (v[1] - v[0])
    if budget < 8:
        # verdict alone is too long: keep only its first line
        v = (v[0], min(t["duration"], vl[0]["end"] + POST)); budget = a.max - (v[1] - v[0])
    fl = secs[a.fact]["lines"]
    f0 = max(0.0, fl[0]["start"] - PRE)

    def fit(b):
        k = 0
        for i, ln in enumerate(fl):
            if ln["end"] + POST - f0 <= b:
                k = i + 1
        return k

    keep, c, note = fit(budget), None, ""
    if a.cta:
        cl = [ln for s_ in t["sections"] for ln in s_.get("lines", []) if ln.get("cta") == "like_subscribe"]
        if not cl:
            note = "; cta: no like_subscribe line in timing, skipped"
        else:
            cw = (max(0.0, cl[0]["start"] - PRE), min(t["duration"], cl[0]["end"] + POST))
            k2 = fit(budget - (cw[1] - cw[0]))
            if k2 >= 1 and keep - k2 <= a.cta_drop and cw[0] >= v[1]:
                keep, c = k2, cw
                note = f"; cta end card {cw[1]-cw[0]:.1f}s"
            else:
                note = f"; cta skipped (would cost {keep - k2} fact lines, limit {a.cta_drop})"
    if keep == 0:
        sys.exit("first fact line alone exceeds budget; raise --max or pick windows by hand")
    f = (f0, fl[keep - 1]["end"] + POST)
    if f[1] > v[0]:
        f = (f[0], v[0])
    total = (f[1] - f[0]) + (v[1] - v[0]) + ((c[1] - c[0]) if c else 0)
    out = f"{f[0]:.2f}:{f[1]:.2f} {v[0]:.2f}:{v[1]:.2f}"
    if c:
        out += f" {c[0]:.2f}:{c[1]:.2f}"
    print(out)
    print(f"fact lines kept {keep}/{len(fl)}, verdict lines {len(vl)}, total {total:.1f}s (max {a.max}){note}",
          file=sys.stderr)

if __name__ == "__main__":
    main()
