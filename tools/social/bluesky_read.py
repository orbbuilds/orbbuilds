#!/usr/bin/env python3
"""Read-only Bluesky metrics for @orbbuilds.bsky.social (public AppView, no auth).

Usage: python3 tools/social/bluesky_read.py [--limit N] [--actor HANDLE] [--who]
Prints profile counts and, per recent own post: time (MT), likes, reposts,
quotes, replies, has-video, and the first 60 chars. Never posts anything.
Note: Bluesky exposes no impression or view counts; engagement is the signal.
--who also lists each liker/reposter and new followers, flagging likely
mass-engagers (follows 0 or follower/follow ratio >1000 with 10K+ posts), which
should NOT count toward the #22 win rule (tick 145).
"""
import argparse, json, urllib.request, urllib.parse
from datetime import datetime
from zoneinfo import ZoneInfo

API = "https://public.api.bsky.app/xrpc/"
MT = ZoneInfo("America/Denver")

def get(method, **params):
    url = API + method + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=20) as r:
        return json.load(r)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--actor", default="orbbuilds.bsky.social")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--who", action="store_true", help="list engagers + mass-engager flag")
    a = ap.parse_args()
    p = get("app.bsky.actor.getProfile", actor=a.actor)
    print(f"profile {p['handle']}: followers={p.get('followersCount')} "
          f"follows={p.get('followsCount')} posts={p.get('postsCount')}")
    feed = get("app.bsky.feed.getAuthorFeed", actor=a.actor, limit=a.limit,
               filter="posts_no_replies")["feed"]
    now = datetime.now(MT)
    for item in feed:
        post = item["post"]
        if post["author"]["did"] != p["did"]:
            continue  # skip reposts of others
        ts = datetime.fromisoformat(post["record"]["createdAt"].replace("Z", "+00:00")).astimezone(MT)
        age_min = int((now - ts).total_seconds() // 60)
        emb = post.get("embed", {}).get("$type", "")
        rkey = post["uri"].rsplit("/", 1)[-1]
        text = post["record"].get("text", "").replace("\n", " ")[:60]
        print(f"{ts:%b %d %I:%M %p} MT (T+{age_min} min) likes={post.get('likeCount',0)} "
              f"reposts={post.get('repostCount',0)} quotes={post.get('quoteCount',0)} "
              f"replies={post.get('replyCount',0)} video={'video' in emb} "
              f"url=https://bsky.app/profile/{p['handle']}/post/{rkey} | {text}")
        if a.who:
            for kind, meth, key in (("like", "app.bsky.feed.getLikes", "likes"),
                                    ("repost", "app.bsky.feed.getRepostedBy", "repostedBy")):
                for row in get(meth, uri=post["uri"], limit=50).get(key, []):
                    print("    " + kind + " " + describe(row.get("actor", row)))
    if not feed:
        print("no posts yet")
    if a.who:
        for f in get("app.bsky.graph.getFollowers", actor=a.actor, limit=50).get("followers", []):
            print("  follower " + describe(f))

def describe(actor):
    q = get("app.bsky.actor.getProfile", actor=actor["did"])
    fo, fl, po = q.get("followersCount", 0), q.get("followsCount", 0), q.get("postsCount", 0)
    mass = po >= 10000 and (fl == 0 or fo / max(fl, 1) > 1000)
    return (f"@{q['handle']} followers={fo} follows={fl} posts={po}"
            f"{'  [MASS-ENGAGER: exclude]' if mass else '  [counts]'}")

if __name__ == "__main__":
    main()
