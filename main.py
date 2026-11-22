#!/usr/bin/env python3
"""Write one short text to $MAKEFUN_OUTPUT_DIR/entry.txt.

The text is a quiet room: a warm mug found without looking, rain on
glass, a chair still holding the afternoon sun, and an evening that
asks nothing of its reader but to stay.

The entry text is assembled from its five sentences and checked
against the competition's length gate (1-280 Unicode code points,
not only whitespace) before anything is written.
"""

import os
import sys

# The five sentences of the entry, kept separate so the text is built
# from its parts rather than pasted as one block.
SENTENCES = [
    "Your mug is where your hands can find it without looking, "
    "the tea still warm.",
    "Rain draws slow lines down the glass.",
    "The chair by the window holds the afternoon sun.",
    "Nothing here needs an answer.",
    "Just steam rising, rain falling, and an evening that asks only "
    "that you stay.",
]

MIN_LEN = 1
MAX_LEN = 280


def build_text() -> str:
    """Join the sentences into the single entry text."""
    return " ".join(SENTENCES)


def validate(text: str) -> None:
    """Gate the text: 1-280 Unicode code points, not only whitespace."""
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        raise ValueError(
            f"entry text is {len(text)} code points, "
            f"outside the {MIN_LEN}-{MAX_LEN} range"
        )
    if not text.strip():
        raise ValueError("entry text is only whitespace")


def main() -> int:
    text = build_text()
    try:
        validate(text)
    except ValueError as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Read back what was written and re-check it: the file on disk
    # must be exactly the validated text, or the run has failed.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != text:
        print("verification failed: entry.txt does not match the text",
              file=sys.stderr)
        return 1
    try:
        validate(written)
    except ValueError as exc:
        print(f"verification failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
