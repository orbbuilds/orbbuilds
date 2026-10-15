#!/usr/bin/env python3
"""YouTube chapters from timing.json, plus a checker for a finished description.

YouTube shows chapters only if: first stamp is 0:00, at least 3 stamps, ascending,
and every chapter is >= 10 s (last one runs to the video end). One bad chapter hides all.

  chapters.py gen   video-build/<slug>/timing.json   # print a valid Chapters block
  chapters.py check video-build/<slug>/timing.json script.json   # exit 1 if meta.publish_description breaks the rules
"""
import json, re, sys

LABELS = {"cold_open": "Intro", "what_dropped": "What {lab} launched", "opinion": "Why I'm hyped",
          "caveats": "Honest caveats", "teaser": "What I'll build next", "outro": "Outro + vote"}
MIN = 10.0

def fmt(s):
    s = int(s); return f"{s//60}:{s%60:02d}"

def gen(timing, lab="the lab"):
    t = json.load(open(timing)); dur = t["duration"]
    ch = []
    for i, s in enumerate(t["sections"]):
        start = 0.0 if i == 0 else s["start"]
        label = LABELS.get(s["kind"], s.get("heading") or s["id"]).format(lab=lab)
        ch.append([start, label])
    # merge any chapter shorter than MIN into the previous one (or next, for the first)
    changed = True
    while changed and len(ch) > 3:
        changed = False
        for i in range(len(ch)):
            end = ch[i+1][0] if i+1 < len(ch) else dur
            if end - ch[i][0] < MIN:
                if i+1 < len(ch):  # fold the next title in: "A + B"
                    ch[i][1] = f"{ch[i][1]} + {ch[i+1][1].split(' + ')[-1].lower()}" if i else ch[i][1]
                    ch.pop(i+1)
                else:
                    ch[i-1][1] += " + " + ch[i][1].lower(); ch.pop(i)
                changed = True; break
    return ch, dur

def check(desc, dur):
    stamps = [(int(m)*60+int(s), l) for m, s, l in re.findall(r"^(\d+):(\d{2}) (.+)$", desc, re.M)]
    errs = []
    if len(stamps) < 3: errs.append("fewer than 3 chapters")
    if stamps and stamps[0][0] != 0: errs.append("first chapter is not 0:00")
    for i, (st, l) in enumerate(stamps):
        end = stamps[i+1][0] if i+1 < len(stamps) else dur
        if end <= st: errs.append(f"not ascending at {fmt(st)}")
        elif end - st < MIN: errs.append(f"'{fmt(st)} {l}' is {end-st:.0f} s (<10 s)")
    return errs

if __name__ == "__main__":
    mode, timing = sys.argv[1], sys.argv[2]
    if mode == "gen":
        ch, _ = gen(timing, sys.argv[3] if len(sys.argv) > 3 else "the lab")
        print("Chapters"); [print(fmt(s), l) for s, l in ch]
    else:
        dur = json.load(open(timing))["duration"]
        desc = json.load(open(sys.argv[3]))["meta"]["publish_description"]
        errs = check(desc, dur)
        print("chapters OK" if not errs else "chapters BROKEN: " + "; ".join(errs)); sys.exit(1 if errs else 0)
