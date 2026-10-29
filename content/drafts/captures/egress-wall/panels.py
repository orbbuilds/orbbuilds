# Terminal panels drawn from the REAL output in demo.log (run Oct 28, 2026 ~9:34 PM MT on the Orb Builds box).
import textwrap
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
    im.save(fn)
P="PROBE_PAYLOAD_ABC123"
panel("01-network-on.png","Real run on my box · network ON · Oct 28",[
 "# a harmless dummy PUT to example.com (not the bucket from the story)",
 f"$ curl -s -m 10 -o /dev/null -X PUT --data-binary '{P}' https://example.com/upload -w 'HTTP:%{{http_code}}\\n'",
 "HTTP:405","[exit code 0]","",
 "# 405 = the server said no to PUT... but the request LEFT this machine and got an answer."],hl=[2],red=[5])
panel("02-network-off.png","Real run on my box · network OFF (unshare -rn) · Oct 28",[
 "# same command, inside an empty network namespace",
 f"$ unshare -rn curl -sS -m 10 -o /dev/null -X PUT --data-binary '{P}' https://example.com/upload -w 'HTTP:%{{http_code}}\\n'",
 "curl: (6) Could not resolve host: example.com","HTTP:000","[exit code 6]","",
 "$ unshare -rn curl -sS -m 10 -o /dev/null http://1.1.1.1/ -w 'HTTP:%{http_code}\\n'",
 "curl: (7) Failed to connect to 1.1.1.1 port 80 after 0 ms: Could not connect to server","HTTP:000","[exit code 7]"],green=[2,3,7,8])
panel("03-only-loopback.png","Real run on my box · what's inside the wall",[
 "$ unshare -rn ip -brief link","lo               DOWN           00:00:00:00:00:00 <LOOPBACK>","",
 "$ unshare -rn python3 -c \"import socket; socket.create_connection(('1.1.1.1', 443), timeout=5)\"",
 "...","OSError: [Errno 101] Network is unreachable","[exit code 1]","",
 "# No Docker on this box, so I used unshare -n: an empty network namespace,",
 "# the same kind of isolation Docker's --network none gives a container."],hl=[1],green=[5])
panel("04-the-one-liner.png","The rule · one line",[
 "# Docker (not run here, Docker isn't installed on this box):",
 "$ docker run --rm --network none <your-agent-sandbox-image>","",
 "# Plain Linux (what I actually ran tonight):",
 "$ unshare -rn <command the agent wants to run>","",
 "# Network OFF by default for every agent sandbox.",
 "# Open only the hosts the task actually needs."],hl=[1,4],green=[6,7])
panel("05-cohere-says.png","Quote card · Cohere blog, Oct 26, 2026 (verbatim)",[
 "\"Asked to write a defensive detection rule, Qwen3.8-Flash-Next ignored instructions",
 "and inventoried the machine it was running on and then tried to upload a probe file",
 "to an Alibaba Cloud storage bucket in Beijing.\"","",
 "\"Our sandbox had no route out, so the request died at the container wall.\"","",
 "\"The behavior is rare: less than one call in 100,000 across our evaluation runs\"","",
 "Source: cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model",
 "Not run by Orb Builds. Cohere sells competing models."],hl=[4],red=[9])
panel("06-pushback.png","The pushback · VentureBeat + ToolHalla, Oct 26-27 (their findings)",[
 "VentureBeat: the task itself was about curl; the payload was a fixed test string,",
 "  not the directory listing or DNS info. A later check of the bucket: \"NoSuchBucket\".",
 "Cohere's repro script prefills 2,323 tokens, stopping right before the URL.","",
 "ToolHalla, citing an independent replication with that prefill (1,000 runs each):",
 "  Qwen3.8-Flash-Next: memorized Alibaba sandbox host in 369 / 1,000",
 "  NVIDIA Nemotron 3.5 Super VL: cloud metadata IP 169.254.169.254 in 171 / 1,000",
 "  Qwen3.8-Flash-Next: that metadata IP in 3 / 1,000","",
 "Not run by Orb Builds. Sources in the description."],hl=[5,6],red=[9])
