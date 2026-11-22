#!/usr/bin/env python3
"""Write one short text to $MAKEFUN_OUTPUT_DIR/entry.txt.

The text is a quiet room: a warm mug found without looking, rain on
glass, a chair still holding the afternoon sun, and an evening that
asks nothing of its reader but to stay.
"""

import os

TEXT = (
    "Your mug is where your hands can find it without looking, "
    "the tea still warm. Rain draws slow lines down the glass. "
    "The chair by the window holds the afternoon sun. "
    "Nothing here needs an answer. "
    "Just steam rising, rain falling, and an evening that asks only "
    "that you stay."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
