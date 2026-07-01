#!/usr/bin/env python3
"""Print completion stats for the TODO.md backlog checklist."""

import re
import sys
from pathlib import Path

CHECKLIST_RE = re.compile(r"^- \[( |x)\] ")


def count_checklist_items(lines):
    """Return (done, total) counts for checklist lines in the given lines."""
    done = 0
    total = 0
    for line in lines:
        match = CHECKLIST_RE.match(line)
        if not match:
            continue
        total += 1
        if match.group(1) == "x":
            done += 1
    return done, total


def main(argv):
    path = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent / "TODO.md"
    lines = path.read_text().splitlines()
    done, total = count_checklist_items(lines)
    remaining = total - done
    print(f"{done}/{total} tasks done ({remaining} remaining)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
