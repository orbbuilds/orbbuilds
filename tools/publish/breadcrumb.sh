#!/usr/bin/env bash
# Append one timestamped step line to tonight's publish run log, so a run that dies
# mid-way still leaves a trace of the last step reached (tick 176).
# Usage: tools/publish/breadcrumb.sh "<step>" "<ok|fail|start>" "[detail / exact error]"
set -euo pipefail
cd "$(dirname "$0")/../.."
log="content/published/queue/run-log-$(date +%F).md"
[ -f "$log" ] || printf '# Publish run log %s (MT)\n\n' "$(date +%F)" > "$log"
printf -- '- %s | %s | %s | %s\n' "$(date '+%H:%M:%S')" "$1" "${2:-}" "${3:-}" | cut -c1-400 >> "$log"
