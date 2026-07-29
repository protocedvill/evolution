#!/usr/bin/env bash
# Lints TODO.md to ensure every checklist line starts with "- [ ] " or "- [x] ".
set -euo pipefail

todo_file="${1:-$(dirname "$0")/../TODO.md}"
status=0

if [[ ! -f "$todo_file" ]]; then
  echo "check_todo_format.sh: no such file: $todo_file" >&2
  exit 1
fi

while IFS= read -r line || [[ -n "$line" ]]; do
  if [[ "$line" == -\ \[* ]] && [[ "$line" != "- [ ] "* ]] && [[ "$line" != "- [x] "* ]]; then
    echo "Malformed checklist line: $line" >&2
    status=1
  fi
done < "$todo_file"

if [[ "$status" -eq 0 ]]; then
  echo "TODO.md checklist format OK"
fi

exit "$status"
