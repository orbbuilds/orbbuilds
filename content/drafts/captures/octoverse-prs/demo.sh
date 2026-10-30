#!/usr/bin/env bash
# Real checks on the Orb Builds repo (github.com/orbbuilds/orbbuilds), run on the Orb Builds box Oct 29, 2026.
# Part 2 reviews the latest commit (d196512) by testing it in a throwaway worktree at /tmp/rv (nothing pushed).
cd /workspace/orbbuilds
run(){ echo "\$ $*"; bash -c "$*" 2>&1; echo "[exit code $?]"; echo; }
date
echo "### 1. my repo, by the numbers"
run "git rev-list --count origin/main"
run "git log origin/main --format='%an' | sort | uniq -c"
run "gh pr list -R orbbuilds/orbbuilds --state all --limit 100 | wc -l"
run "gh api 'search/issues?q=repo:orbbuilds/orbbuilds+is:pr' --jq .total_count"
run "gh api repos/orbbuilds/orbbuilds --jq .created_at"
run "git log origin/main --since=2026-09-01 --until=2026-10-01 --oneline | wc -l"
run "git log origin/main --since='2026-10-29 00:00' --oneline | wc -l"
echo "### 2. reviewing my own latest commit"
run "git show --stat --format='%h %ad %s' --date=short d196512 | head -6"
cd /tmp/rv
run "md5sum public/episodes/rr-012.jpg /tmp/new-thumb.jpg"
run "grep -n 'hadThumb' tools/site/add-episode.mjs"
