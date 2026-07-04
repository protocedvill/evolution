#!/usr/bin/env python3
"""Print completion stats for the TODO.md backlog checklist."""

import argparse
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


def percent_complete(done, total):
    """Return the percentage of checklist items done, rounded to the nearest int.

    Returns 0 when there are no checklist items, to avoid dividing by zero.
    """
    if total == 0:
        return 0
    return round(100 * done / total)


def build_parser():
    parser = argparse.ArgumentParser(
        prog="todo_stats.py",
        description="Print completion stats for the TODO.md backlog checklist.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        help="path to the checklist file (default: TODO.md at repo root)",
    )
    parser.add_argument(
        "--remaining",
        action="store_true",
        help="print the text of each not-yet-done checklist item",
    )
    parser.add_argument(
        "--percent",
        action="store_true",
        help="print the percentage of checklist items done",
    )
    return parser


def main(argv):
    args = build_parser().parse_args(argv[1:])
    path = args.path or Path(__file__).resolve().parent.parent / "TODO.md"
    try:
        lines = path.read_text().splitlines()
    except FileNotFoundError:
        print(f"todo_stats.py: no such file: {path}", file=sys.stderr)
        return 1

    if args.remaining:
        for item in remaining_items(lines):
            print(item)
        return 0

    done, total = count_checklist_items(lines)

    if args.percent:
        print(f"{percent_complete(done, total)}%")
        return 0

    remaining = total - done
    print(f"{done}/{total} tasks done ({remaining} remaining)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
