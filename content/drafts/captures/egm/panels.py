import json, textwrap
from PIL import Image, ImageDraw, ImageFont
W,H=1180,464
mono=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",19)
bold=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",20)
def panel(fn,title,lines,hl=()):
    im=Image.new("RGB",(W,H),(14,18,28)); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,38],fill=(32,38,54)); 
    for i,c in enumerate([(255,95,86),(255,189,46),(39,201,63)]): d.ellipse([14+i*24,12,28+i*24,26],fill=c)
    d.text((100,9),title,font=bold,fill=(200,210,230))
    y=52
    for i,l in enumerate(lines):
        for j,w in enumerate(textwrap.wrap(l,92) or [""]):
            col=(255,210,90) if i in hl else (205,225,215)
            d.text((22 if j==0 else 52,y),w,font=mono,fill=col); y+=25
            if y>H-30: break
        if y>H-30: break
    im.save(fn)
spec=[l for l in open("spec.md").read().splitlines() if l.strip()]
panel("01-spec.png","my real plan: spec.md (Orb Builds nightly publish flow)",spec)
g=json.load(open("goldfish.json"))["results"]
def body(k): return [l.strip() for l in g[k]["response"].splitlines() if l.strip()][1:]
panel("02-comprehension.png",f"Goldfish 1 · comprehension check · llama3.2 3B local · {g['comprehension']['seconds']}s", body("comprehension"))
panel("03-antagonistic.png",f"Goldfish 2 · antagonistic review · fresh session · {g['antagonistic']['seconds']}s", body("antagonistic"),hl=(0,1,3))
rd=[l.strip() for l in g["readiness"]["response"].splitlines() if l.strip()]
panel("04-readiness.png",f"Goldfish 3 · go/no-go readiness check · {g['readiness']['seconds']}s", rd, hl=(0,))
