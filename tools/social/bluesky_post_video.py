#!/usr/bin/env python3
"""Post one vertical MP4 (or a text-only post) to Bluesky via ATProto.

Writes hashtag + link facets (UTF-8 byte offsets) so #tags are clickable and
show in tag feeds, and refuses text over the 300-grapheme cap.

Default is dry-run: createSession + getServiceAuth + file probe. Pass --post
to upload and create the feed record. Never prints passwords or JWTs.

Creds file format (space-separated labels):
  bluesky <handle> email <email> password <app-password>
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import requests

CRED_DEFAULT = Path("/home/box/secrets/bluesky.txt")
PDS = "https://bsky.social"
VIDEO_HOST = "https://video.bsky.app"
LABELS = {
    "handle",
    "user",
    "username",
    "identifier",
    "password",
    "pass",
    "email",
    "app",
    "app_password",
    "app-password",
    "pw",
    "bluesky",
}


# --- rich-text facets (hashtags + links) --------------------------------
# Bluesky does not auto-link #tags or URLs in raw text: the client must send
# app.bsky.richtext.facet entries with UTF-8 *byte* offsets. Without them tags
# are not clickable and the post does not show up in tag feeds.
import re
import unicodedata

TAG_RE = re.compile(r"(?:^|\s)(#[^\d\s\W][\w]*)", re.UNICODE)
URL_RE = re.compile(r"(?:^|\s|\()(https?://[^\s)]+)")
MAX_GRAPHEMES = 300


def grapheme_len(text: str) -> int:
    """Approximate grapheme count: code points minus combining marks / ZWJ / VS."""
    n = 0
    for ch in text:
        if unicodedata.combining(ch) or ch in "\u200d\ufe0f\ufe0e":
            continue
        n += 1
    return n


def _byte_span(text: str, start: int, end: int) -> tuple[int, int]:
    b0 = len(text[:start].encode("utf-8"))
    b1 = b0 + len(text[start:end].encode("utf-8"))
    return b0, b1


def build_facets(text: str) -> list[dict]:
    facets: list[dict] = []
    for m in URL_RE.finditer(text):
        url = m.group(1).rstrip(".,;:!?")
        start = m.start(1)
        b0, b1 = _byte_span(text, start, start + len(url))
        facets.append({
            "index": {"byteStart": b0, "byteEnd": b1},
            "features": [{"$type": "app.bsky.richtext.facet#link", "uri": url}],
        })
    for m in TAG_RE.finditer(text):
        tag = m.group(1).rstrip(".,;:!?")
        if len(tag) > 65:  # lexicon: tag maxGraphemes 64 (without '#')
            continue
        start = m.start(1)
        b0, b1 = _byte_span(text, start, start + len(tag))
        facets.append({
            "index": {"byteStart": b0, "byteEnd": b1},
            "features": [{"$type": "app.bsky.richtext.facet#tag", "tag": tag[1:]}],
        })
    facets.sort(key=lambda f: f["index"]["byteStart"])
    return facets


def load_creds(path: Path) -> tuple[str, str]:
    parts = path.read_text().strip().split()
    kv: dict[str, str] = {}
    i = 0
    while i < len(parts):
        key = parts[i].lower().rstrip(":")
        if key in LABELS and i + 1 < len(parts):
            kv[key] = parts[i + 1]
            i += 2
        else:
            i += 1
    ident = kv.get("handle") or kv.get("identifier") or kv.get("user") or kv.get("username")
    if parts and parts[0].lower() == "bluesky" and len(parts) > 1 and parts[1].endswith(".bsky.social"):
        ident = parts[1]
    password = (
        kv.get("password")
        or kv.get("pass")
        or kv.get("pw")
        or kv.get("app_password")
        or kv.get("app-password")
    )
    if not ident or not password:
        raise SystemExit(f"could not parse handle/password from {path}")
    return ident, password


def create_session(identifier: str, password: str) -> dict:
    r = requests.post(
        f"{PDS}/xrpc/com.atproto.server.createSession",
        json={"identifier": identifier, "password": password},
        timeout=60,
    )
    if r.status_code != 200:
        try:
            err = r.json()
            msg = f"{err.get('error')}: {err.get('message', '')[:160]}"
        except Exception:
            msg = f"HTTP {r.status_code}"
        raise SystemExit(f"createSession failed: {msg}")
    return r.json()


def pds_host_from_session(session: dict) -> str:
    from urllib.parse import urlparse

    did_doc = session.get("didDoc") or {}
    services = did_doc.get("service") or []
    for svc in services:
        sid = svc.get("id") or ""
        if sid.endswith("#atproto_pds"):
            return urlparse(svc["serviceEndpoint"]).hostname or ""
    # Fallback: PLC directory
    did = session["did"]
    doc = requests.get(f"https://plc.directory/{did}", timeout=30).json()
    for svc in doc.get("service") or []:
        if (svc.get("id") or "").endswith("#atproto_pds"):
            return urlparse(svc["serviceEndpoint"]).hostname or ""
    raise SystemExit("could not resolve PDS host for getServiceAuth aud")


def get_service_auth(access_jwt: str, pds_host: str) -> str:
    exp = int(time.time()) + 60 * 30
    r = requests.get(
        f"{PDS}/xrpc/com.atproto.server.getServiceAuth",
        params={
            "aud": f"did:web:{pds_host}",
            "lxm": "com.atproto.repo.uploadBlob",
            "exp": str(exp),
        },
        headers={"Authorization": f"Bearer {access_jwt}"},
        timeout=60,
    )
    if r.status_code != 200:
        try:
            err = r.json()
            msg = f"{err.get('error')}: {err.get('message', '')[:160]}"
        except Exception:
            msg = f"HTTP {r.status_code}"
        raise SystemExit(f"getServiceAuth failed: {msg}")
    token = r.json().get("token")
    if not token:
        raise SystemExit("getServiceAuth returned no token")
    return token


def upload_video(did: str, service_token: str, video_path: Path) -> dict:
    url = f"{VIDEO_HOST}/xrpc/app.bsky.video.uploadVideo"
    params = {"did": did, "name": video_path.name}
    data = video_path.read_bytes()
    r = requests.post(
        url,
        params=params,
        headers={
            "Authorization": f"Bearer {service_token}",
            "Content-Type": "video/mp4",
            "Content-Length": str(len(data)),
        },
        data=data,
        timeout=300,
    )
    try:
        body = r.json()
    except Exception:
        raise SystemExit(f"uploadVideo non-JSON HTTP {r.status_code} len={len(r.content)}")
    # JobStatus may be nested or top-level depending on server version
    job = body.get("jobStatus") or body
    if r.status_code >= 400 and not (job.get("blob") or job.get("jobId")):
        raise SystemExit(
            f"uploadVideo failed HTTP {r.status_code}: "
            f"{body.get('error') or body.get('message') or str(body)[:200]}"
        )
    return job


def poll_job(job_id: str, timeout_s: int = 300) -> dict:
    deadline = time.time() + timeout_s
    last = {}
    while time.time() < deadline:
        r = requests.get(
            f"{VIDEO_HOST}/xrpc/app.bsky.video.getJobStatus",
            params={"jobId": job_id},
            timeout=60,
        )
        body = r.json()
        status = body.get("jobStatus") or body
        last = status
        state = status.get("state") or ""
        blob = status.get("blob")
        print(
            f"job {job_id[:12]}… state={state} progress={status.get('progress', '')} "
            f"blob={'yes' if blob else 'no'}",
            flush=True,
        )
        if blob:
            return status
        if state in ("JOB_STATE_FAILED", "failed", "FAILED"):
            raise SystemExit(f"video job failed: {status.get('error') or status.get('message') or state}")
        # already_exists path: blob may still be present on error responses
        if status.get("error") == "already_exists" and blob:
            return status
        time.sleep(2)
    raise SystemExit(f"video job timed out after {timeout_s}s; last={json.dumps(last)[:300]}")


def create_post(access_jwt: str, did: str, text: str, blob: dict | None, width: int, height: int) -> dict:
    record = {
        "$type": "app.bsky.feed.post",
        "text": text,
        "createdAt": time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime()),
        "langs": ["en"],
        "facets": build_facets(text),
    }
    if blob is not None:
        record["embed"] = {
            "$type": "app.bsky.embed.video",
            "video": blob,
            "aspectRatio": {"width": width, "height": height},
        }
    r = requests.post(
        f"{PDS}/xrpc/com.atproto.repo.createRecord",
        headers={"Authorization": f"Bearer {access_jwt}"},
        json={
            "repo": did,
            "collection": "app.bsky.feed.post",
            "record": record,
        },
        timeout=60,
    )
    if r.status_code != 200:
        try:
            err = r.json()
            msg = f"{err.get('error')}: {err.get('message', '')[:200]}"
        except Exception:
            msg = f"HTTP {r.status_code}"
        raise SystemExit(f"createRecord failed: {msg}")
    return r.json()


def probe_video(path: Path) -> tuple[int, int, float]:
    import subprocess

    out = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=width,height",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            str(path),
        ],
        text=True,
    )
    data = json.loads(out)
    stream = data["streams"][0]
    dur = float(data["format"]["duration"])
    return int(stream["width"]), int(stream["height"]), dur


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--creds", type=Path, default=CRED_DEFAULT)
    ap.add_argument("--file", type=Path, default=None, help="vertical MP4; omit for a text-only post (B-text drops)")
    ap.add_argument("--text", required=True)
    ap.add_argument("--width", type=int, default=0)
    ap.add_argument("--height", type=int, default=0)
    ap.add_argument(
        "--post",
        action="store_true",
        help="Actually upload + create the post. Without this flag, dry-run only.",
    )
    args = ap.parse_args()

    w = h = 0
    if args.file is not None:
        if not args.file.is_file():
            raise SystemExit(f"missing video: {args.file}")
        size = args.file.stat().st_size
        w, h, dur = probe_video(args.file)
        if args.width:
            w = args.width
        if args.height:
            h = args.height
        print(f"file ok: {args.file} ({size} bytes, {w}x{h}, {dur:.1f}s)")
    else:
        print("no --file: text-only post")

    glen = grapheme_len(args.text)
    facets = build_facets(args.text)
    tags = [f["features"][0].get("tag") for f in facets if f["features"][0]["$type"].endswith("#tag")]
    links = [f["features"][0].get("uri") for f in facets if f["features"][0]["$type"].endswith("#link")]
    print(f"text ok: {glen}/{MAX_GRAPHEMES} graphemes; tags={tags} links={links}")
    if glen > MAX_GRAPHEMES:
        raise SystemExit(f"text is {glen} graphemes, over Bluesky's {MAX_GRAPHEMES} cap; shorten it")

    ident, password = load_creds(args.creds)
    session = create_session(ident, password)
    did = session["did"]
    handle = session.get("handle", ident)
    print(
        f"session ok: handle={handle} did={did[:16]}… "
        f"emailConfirmed={session.get('emailConfirmed')}"
    )
    pds_host = pds_host_from_session(session)
    print(f"pds host: {pds_host}")
    token = get_service_auth(session["accessJwt"], pds_host)
    print(f"service auth ok: token_len={len(token)}")

    if not args.post:
        print("dry-run complete (pass --post to upload + publish)")
        return

    if args.file is None:
        result = create_post(session["accessJwt"], did, args.text, None, 0, 0)
        rkey = result.get("uri", "").rsplit("/", 1)[-1]
        print(f"posted uri={result.get('uri','')}")
        print(f"public https://bsky.app/profile/{handle}/post/{rkey}")
        return

    print("uploading to video.bsky.app …")
    job = upload_video(did, token, args.file)
    blob = job.get("blob")
    job_id = job.get("jobId")
    if not blob:
        if not job_id:
            raise SystemExit(f"uploadVideo returned neither blob nor jobId: {json.dumps(job)[:300]}")
        print(f"processing jobId={job_id}")
        job = poll_job(job_id)
        blob = job.get("blob")
    if not blob:
        raise SystemExit("no blob after processing")

    result = create_post(session["accessJwt"], did, args.text, blob, w, h)
    uri = result.get("uri", "")
    cid = result.get("cid", "")
    # Public URL from at://did/.../app.bsky.feed.post/rkey
    rkey = uri.rsplit("/", 1)[-1] if uri else ""
    public = f"https://bsky.app/profile/{handle}/post/{rkey}" if rkey else ""
    print(f"posted uri={uri}")
    print(f"posted cid={cid}")
    print(f"public {public}")


if __name__ == "__main__":
    main()
