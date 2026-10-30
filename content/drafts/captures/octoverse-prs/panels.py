# Panels drawn from the REAL output in demo.log / review-test.log (Oct 29, 2026 ~9:37-9:45 PM MT, Orb Builds box)
# and verbatim quotes from GitHub's Octoverse post (Oct 28, 2026) and Visual Studio Magazine (Oct 29, 2026).
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
panel("01-github-says.png","Quote card · GitHub Octoverse 2026, Oct 28 (verbatim)",[
 "\"By September 2026, more than 40% of pull requests on GitHub started with an",
 "agent's first draft, up from 17% in March. That is 110 million in September alone,\"","",
 "\"In February, 83% of agent-involved pull requests merged within two weeks, a touch",
 "behind the roughly 86% for pull requests without detected agent involvement.",
 "By September, agent pull requests were at 90%, while the comparison group held at about 86%.\"","",
 "Agent signal: \"It is a floor, since not all agent use may be detected.\"","",
 "Source: github.blog (Octoverse 2026). GitHub's own telemetry."],hl=[0,1,5],red=[9])
panel("02-the-catch.png","The catch · Visual Studio Magazine, Oct 29 (verbatim)",[
 "\"These are GitHub's platform measurements and should not be taken as proof",
 "that agent-written changes are more reliable.\"","",
 "On the 8x-more-commits stat for new repos with an agent config file:",
 "\"a correlation that does not establish causation.\"","",
 "My note: merged fast  !=  correct.",
 "GitHub also sells the agents (Copilot) and the review tools."],hl=[0,1,4],red=[6])
panel("03-my-repo.png","Real run on my box · github.com/orbbuilds/orbbuilds · Oct 29",[
 "$ git rev-list --count origin/main","454","",
 "$ git log origin/main --format='%an' | sort | uniq -c","    453 Orb Builds","      1 OrbBuilds","",
 "$ gh api 'search/issues?q=repo:orbbuilds/orbbuilds+is:pr' --jq .total_count","0","",
 "$ git log origin/main --since=2026-09-01 --until=2026-10-01 --oneline | wc -l","0",
 "# repo created Oct 9. Every commit pushed straight to main. Zero pull requests."],hl=[1,4,5],red=[9,12],green=[])
panel("04-my-review.png","Real run on my box · reviewing my own latest commit (d196512)",[
 "# an old thumbnail already sits at public/episodes/rr-012.jpg  (test worktree, nothing pushed)",
 "$ node tools/site/add-episode.mjs --number 12 ... --thumb /tmp/new-thumb.jpg",
 "episodes.ts ok (10 episodes)",
 "Added Episode 12 (2026-10-29) with thumbnail public/episodes/rr-012.jpg.","",
 "$ md5sum public/episodes/rr-012.jpg /tmp/new-thumb.jpg",
 "e0c049b9e5e9f331d2280bafa2db1838  public/episodes/rr-012.jpg   <- still the OLD file",
 "71658058159a5cf3818fc5fb0e2aa9be  /tmp/new-thumb.jpg","",
 "94: if (!hadThumb) copyFileSync(thumbSrc, thumbDest);",
 "# says \"Added\", silently keeps the old thumbnail. A reviewer would have caught it."],green=[3],red=[6,10],hl=[9])
