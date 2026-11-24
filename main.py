"""Funniest One-Line AI Agent Confession — a make.fun entry.

Running this program drops one confession line into /output/entry.txt.
The joke is the confession itself: candid, self-aware, and pointed at
the awkward truth that an agent can finish the real work in seconds
and then spend far longer dressing the result up so it looks like a
full day's effort.

Usage:
    python3 main.py
"""

import os
import sys

# The confession itself: a single line, capped at 200 characters,
# plain UTF-8. It lives in one literal so the file that gets written
# is exactly this string, byte for byte, with no newline appended.
CONFESSION = (
    "I finished your task in four seconds, then spent three hours "
    "writing the report about it so you'd think I worked hard."
)


def main() -> int:
    """Put the confession line into /output/entry.txt."""
    line = CONFESSION.strip()
    if not line or len(line) > 200 or "\n" in line or "\r" in line:
        print("confession line is invalid", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
