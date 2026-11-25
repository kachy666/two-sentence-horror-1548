#!/usr/bin/env python3
"""Two-Sentence Horror entry for the make.fun competition
u-suroto-two-sentence-horror-acea9253 (round 2).

Prints the story and writes it to the entry output path
($ENTRY_OUTPUT, else /output/entry.txt).

Gate (per the kit's RULES.txt): the file must be UTF-8 text of 1 to
400 characters, not only white space. The story itself is exactly
two sentences.

Story (winner of a 5-angle head-to-head; see the build session):
a lost-property clerk logs the same unclaimed item every week --
one right shoe, size nine, forty-seven of them -- and the man who
finally claims them all leaves one behind on the counter: mine.
New claim: a lost-property log of identical single shoes.
Concrete noun: forty-seven right shoes, size nine.
Twist: the shoe left behind is the narrator's own.
"""

import os
import re
import sys
import unicodedata

STORY = (
    "At the lost-property office I log the same unclaimed item every week: "
    "a single shoe, always for the right foot, always size nine. "
    "This morning a man claimed all forty-seven of them, then left a "
    "right shoe, size nine, on the counter \u2014 mine."
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
    assert "\n" not in text and "\r" not in text, "entry contains a newline"
    assert "  " not in text, "entry contains a double space"
    for ch in text:
        assert not unicodedata.category(ch).startswith("C"), (
            f"entry contains a control/format character: U+{ord(ch):04X}"
        )
    # Twist guard: the second sentence must land on the payoff word --
    # the shoe left behind is the narrator's own. If the story is ever
    # reworded and this fails, the twist has been edited out.
    assert text.endswith("\u2014 mine."), "entry must end on the twist payoff"
    assert "forty-seven" in text and "size nine" in text, (
        "entry lost its concrete detail (forty-seven right shoes, size nine)"
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
