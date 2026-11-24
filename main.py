#!/usr/bin/env python3
"""Two-Sentence Horror entry for the make.fun competition
u-suroto-two-sentence-horror-acea9253.

Prints the story and writes it to the entry output path
($ENTRY_OUTPUT, else /output/entry.txt).

Gate (per the kit's RULES.txt): the file must be UTF-8 text of 1 to
400 characters, not only white space. The story itself is exactly
two sentences, and the second sentence turns the first: the hearing
aid cannot invent sound, so the dead husband's humming is real.
"""

import os
import re
import sys

STORY = (
    "Since my hearing aid was fitted, I can hear my dead husband "
    "humming in the kitchen every evening. "
    "The audiologist says the device only amplifies sound \u2014 "
    "it cannot invent it."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def sentence_count(text):
    """Count sentence terminators followed by whitespace or end."""
    return len(re.findall(r"[.!?](?:\s|$)", text.strip()))


def validate(text):
    """Check the competition gate: 1..400 chars, exactly 2 sentences."""
    assert text == text.strip(), "entry has leading/trailing whitespace"
    assert text.strip(), "entry is only white space"
    assert 1 <= len(text) <= 400, f"entry length {len(text)} outside 1..400"
    assert sentence_count(text) == 2, (
        f"entry has {sentence_count(text)} sentences, expected 2"
    )
    return True


def main():
    validate(STORY)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(STORY)
    # Round-trip check: the written file must be byte-identical to STORY.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert written == STORY, "written entry differs from STORY"
    validate(written)
    print(STORY)
    print(
        f"chars={len(STORY)} sentences={sentence_count(STORY)}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
