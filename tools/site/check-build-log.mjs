// Fails if BUILD_LOG.md has an entry the /log page parser would silently skip.
import { readFileSync } from "node:fs";

const lines = readFileSync(new URL("../../BUILD_LOG.md", import.meta.url), "utf8").split("\n");
const errors = [];
const intro = "Newest first. Each entry starts with `## YYYY-MM-DD: Title`.";
if (!lines.includes(intro)) errors.push(`intro line missing or changed (expected: ${intro})`);
let entries = 0;
lines.forEach((line, i) => {
  const n = i + 1;
  if (line.startsWith("## ")) {
    if (/^## \d{4}-\d{2}-\d{2}\s*[:\-–—]\s*\S/.test(line)) entries++;
    else errors.push(`line ${n}: heading doesn't match "## YYYY-MM-DD: Title": ${line}`);
  } else if (line !== intro && /##\s+\d{4}-\d{2}-\d{2}/.test(line)) {
    errors.push(`line ${n}: dated heading is not at the start of the line: ${line.slice(0, 80)}`);
  }
});
if (errors.length) {
  console.error(`BUILD_LOG.md check failed:\n- ${errors.join("\n- ")}`);
  process.exit(1);
}
console.log(`BUILD_LOG.md ok (${entries} entries)`);
