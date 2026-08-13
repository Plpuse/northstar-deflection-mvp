#!/usr/bin/env bash
set -euo pipefail

OUT="docs/audit/commit-log.md"
REPO_URL=$(git config --get remote.origin.url | sed -E 's/\.git$//')

echo "# Commit Audit Log" > "$OUT"
echo "" >> "$OUT"
echo "Generated: $(date -u '+%Y-%m-%d %H:%M UTC')" >> "$OUT"
echo "" >> "$OUT"
echo "| Date | Author | Message | Issue Ref |" >> "$OUT"
echo "|------|--------|---------|-----------|" >> "$OUT"

git log --all --pretty=format:'%ad|%an|%s' --date=short | while IFS='|' read -r date author subject || [ -n "${date:-}" ]; do
  issue_ref=$(echo "$subject" | grep -oE '#[0-9]+' || true | tr '\n' ',' | sed 's/,$//')
  [ -z "$issue_ref" ] && issue_ref="—"
  echo "| $date | $author | $subject | $issue_ref |" >> "$OUT"
done

echo "" >> "$OUT"
echo "## Per-author commit counts" >> "$OUT"
echo "" >> "$OUT"
echo "| Author | Commits |" >> "$OUT"
echo "|--------|---------|" >> "$OUT"
git shortlog -sn --all | awk '{count=$1; $1=""; print "| "$0" | "count" |"}' >> "$OUT"

echo "Audit log written to $OUT"
