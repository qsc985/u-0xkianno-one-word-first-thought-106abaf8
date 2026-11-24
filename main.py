#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt (falling back to
./output/entry.txt when /output is not writable).

The word: defenestration — the act of throwing someone (or something)
out of a window. Surprising, vivid, and witty: it conjures a whole
scene in a single word, and rewards a second look with the sheer
specificity that such an act has a name of its own. Fourteen letters,
no punctuation, no spaces — exactly one word, nothing else.
"""

import os
import sys

WORD = "defenestration"


def choose_output_path() -> str:
    """Prefer /output/entry.txt; fall back to ./output/entry.txt."""
    for directory in ("/output", os.path.join(os.getcwd(), "output")):
        try:
            os.makedirs(directory, exist_ok=True)
            probe = os.path.join(directory, ".write-test")
            with open(probe, "w", encoding="utf-8") as handle:
                handle.write("ok")
            os.remove(probe)
            return os.path.join(directory, "entry.txt")
        except OSError:
            continue
    # Last resort: write beside the script.
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main() -> int:
    word = WORD.strip()
    if not word or len(word.split()) != 1 or not 1 <= len(word.encode("utf-8")) <= 24:
        print("error: entry must be exactly one word of 1-24 UTF-8 characters",
              file=sys.stderr)
        return 1
    path = choose_output_path()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(word)
    print(f"wrote {word!r} to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
