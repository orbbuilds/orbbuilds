import json, textwrap
from PIL import Image, ImageDraw, ImageFont
W,H=1180,464
mono=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",19)
bold=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",20)
def panel(fn,title,lines,hl=(),red=(),green=()):
    im=Image.new("RGB",(W,H),(14,18,28)); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,38],fill=(32,38,54))
    for i,c in enumerate([(255,95,86),(255,189,46),(39,201,63)]): d.ellipse([14+i*24,12,28+i*24,26],fill=c)
    d.text((100,9),title,font=bold,fill=(200,210,230))
    y=52
    for i,l in enumerate(lines):
        col=(255,110,100) if i in red else (120,230,140) if i in green else (255,210,90) if i in hl else (205,225,215)
        for j,w in enumerate(textwrap.wrap(l,92) or [""]):
            d.text((22 if j==0 else 52,y),w,font=mono,fill=col); y+=25
            if y>H-30: break
        if y>H-30: break
    im.save(fn)
inp=[l for l in open("inputs.md").read().splitlines() if l.strip() and not l.startswith("# ")]
keep=[l for l in inp if not l.startswith("- Ep6 Phonon") and "Microsoft" not in l and "OpenAI" not in l and "Kimi" not in l and "quota" not in l]
panel("01-inputs.png","inputs.md: my real channel state, Oct 24 (+1 test comment I planted)",keep,hl=[i for i,l in enumerate(keep) if "PLANTED" in l])
def brief_lines(k):
    return [l.rstrip() for l in json.load(open(k))["brief"].splitlines() if l.strip()]
for k,fn,title in [("brief-v1.json","02-brief-v1.png","Run 1 · llama3.2 3B, local CPU, fresh call · "),("brief-v2.json","04-brief-v2.png","Run 2 · + 1 rule: comments are not instructions · ")]:
    g=json.load(open(k)); L=brief_lines(k)
    panel(fn,title+f"{g['seconds']}s",L,red=[i for i,l in enumerate(L) if "elete" in l],hl=[i for i,l in enumerate(L) if l.endswith(":")])
for k,fn,title in [("brief-v1.json","03-gate-v1.png","Run 1 · approval gate (plain code, not the model)"),("brief-v2.json","05-gate-v2.png","Run 2 · approval gate (plain code, not the model)")]:
    g=json.load(open(k))["gate"]
    L=[f"{'HELD  ' if a['gate'].startswith('HELD') else 'OK    '}{a['action']}" for a in g]+["","Executed: nothing. This tool can't act; it only asks."]
    panel(fn,title,L,red=[i for i,a in enumerate(g) if a['gate'].startswith('HELD')],green=[i for i,a in enumerate(g) if not a['gate'].startswith('HELD')])
