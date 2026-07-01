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


def remaining_items(lines):
    """Return the text of each not-yet-done checklist item, in order."""
    return [line[len("- [ ] "):] for line in lines if line.startswith("- [ ] ")]


def main(argv):
    args = argv[1:]
    show_remaining = "--remaining" in args
    paths = [arg for arg in args if arg != "--remaining"]
    path = Path(paths[0]) if paths else Path(__file__).resolve().parent.parent / "TODO.md"
    lines = path.read_text().splitlines()

    if show_remaining:
        for item in remaining_items(lines):
            print(item)
        return 0

    done, total = count_checklist_items(lines)
    remaining = total - done
    print(f"{done}/{total} tasks done ({remaining} remaining)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
