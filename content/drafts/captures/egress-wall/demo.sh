#!/usr/bin/env bash
# Real egress demo run on the Orb Builds box (no Docker installed here; unshare -n gives the
# process an empty network namespace, the same isolation `docker run --network none` uses).
P='PROBE_PAYLOAD_ABC123'
run(){ echo "\$ $*"; bash -c "$*" 2>&1; echo "[exit code $?]"; echo; }
echo "### 1. network ON (normal shell)"; run "curl -s -m 10 -o /dev/null -X PUT --data-binary '$P' https://example.com/upload -w 'HTTP:%{http_code}\n'"
echo "### 2. network OFF (unshare -rn = new empty network namespace)"
run "unshare -rn curl -sS -m 10 -o /dev/null -X PUT --data-binary '$P' https://example.com/upload -w 'HTTP:%{http_code}\n'"
run "unshare -rn curl -sS -m 10 -o /dev/null http://1.1.1.1/ -w 'HTTP:%{http_code}\n'"
run "unshare -rn ip -brief link"
run "unshare -rn python3 -c \"import socket; socket.create_connection(('1.1.1.1', 443), timeout=5)\""
echo "### versions"; run "curl --version | head -1; unshare --version; uname -sr; which docker || echo 'docker: not installed on this box'"
