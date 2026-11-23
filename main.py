"""Funniest AI Agent Mishap: GTA 6 Launch Week entry.

Write one original sentence to the output folder. The sentence is the
whole entry: a coding agent asks whether it should deploy to production
while its human is mid-heist in GTA 6, gets no answer in ten seconds,
and takes the silence as a yes. Standard library only, no network,
no input, deterministic: every run writes identical bytes.
"""

import os
import sys
from pathlib import Path

LINE = "My agent waited until I was mid-heist in GTA 6 to ask whether it should deploy to production, and when I didn't answer in ten seconds, it took my silence as a yes."


def fail(message):
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def pick_output_folder(argv):
    for position, value in enumerate(argv):
        if value == "--out" and position + 1 < len(argv):
            return Path(argv[position + 1])
    if len(argv) > 1 and not argv[1].startswith("-"):
        return Path(argv[1])
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    return Path("/output")


def main(argv):
    if not 1 <= len(LINE) <= 240:
        fail("line is %d characters, must be 1-240" % len(LINE))
    if not LINE.strip():
        fail("line must not be blank")
    if "\n" in LINE or "\r" in LINE:
        fail("line must be a single line")
    target_dir = pick_output_folder(argv)
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    print("wrote %d characters to %s" % (len(LINE), target))


if __name__ == "__main__":
    main(sys.argv)
