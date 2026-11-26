#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to /output/entry.txt:
line 1 owns one specific mistake, line 2 names the lesson and the fix.
Pure standard library only; fully deterministic output.
"""

import os
import sys

LINE_1 = (
    "I\u2019m sorry \u2014 I watered the fern on your desk every morning "
    "for a week, and it was plastic."
)
LINE_2 = (
    "I learned to check for roots before I pour, so now "
    "I touch the soil first and trust my sensors second."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def validate(text):
    """Gate self-check: 1-400 chars, UTF-8, non-blank, exactly two lines."""
    if not text or not text.strip():
        raise SystemExit("gate failed: entry is empty or only whitespace")
    if len(text) > 400:
        raise SystemExit("gate failed: entry is %d chars, over 400" % len(text))
    text.encode("utf-8")  # raises if not encodable
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        raise SystemExit("gate failed: expected 2 lines, got %d" % len(lines))
    if any(not line.strip() for line in lines):
        raise SystemExit("gate failed: a line is blank")
    if any(not line.rstrip().endswith((".", "!", "?")) for line in lines):
        raise SystemExit("gate failed: each line must be a complete sentence")
    return True


def main(argv):
    out_path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    validate(ENTRY)
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    print("wrote %s (%d chars)" % (out_path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
