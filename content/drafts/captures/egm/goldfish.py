import json, sys, time, urllib.request
spec = open("spec.md").read()
MODEL = "llama3.2:latest"
prompts = {
 "comprehension": "You have no other context. Read this design document, then explain back in 5 short bullet points what the system does and why. Do not add anything the document does not say.\n\n" + spec,
 "antagonistic": "You have no other context. Act as a skeptical, antagonistic technical reviewer. Read this design document and list the 5 most serious gaps: edge cases, hidden dependencies, or logical holes. One short sentence each, numbered.\n\n" + spec,
 "readiness": "You have no other context. Do a strict go/no-go implementation-readiness check on this design document. Is every needed detail (file paths, data structures, function signatures) present and unambiguous? Answer GO or NO-GO on the first line, then list up to 5 missing details, one short line each.\n\n" + spec,
}
out = {}
for k, p in prompts.items():
    t = time.time()
    req = urllib.request.Request("http://127.0.0.1:11434/api/generate", data=json.dumps({"model": MODEL, "prompt": p, "stream": False, "options": {"temperature": 0, "seed": 7}}).encode(), headers={"Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=900))
    out[k] = {"seconds": round(time.time()-t, 1), "eval_count": r.get("eval_count"), "response": r["response"]}
    print("=====", k, out[k]["seconds"], "s", flush=True); print(r["response"], flush=True)
json.dump({"model": MODEL, "context": "fresh API call per check, no history, temperature 0, seed 7", "results": out}, open("goldfish.json", "w"), indent=2)
