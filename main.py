#!/usr/bin/env python3
"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. The text is fixed and the program is fully
deterministic: every run writes the same bytes, with no network, no
randomness, no input and no clock.

The text is a night scene built for the judge's published brief: it shows
rather than instructs, keeps plain concrete words, and ends on an image
that keeps going after the last line — the earth turning, carrying the
field, the reader and everything quiet around and around, all night long.
"""

import os

TEXT = (
    "Past the last streetlight the field opens to the night, and the sky "
    "is so full of stars the dark between them looks thin, and the earth "
    "turns so slowly under your feet you can almost feel it, carrying the "
    "field, and you, and everything quiet, around and around, all night long."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate allows 1 to 280 characters, counted as Unicode code points.
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} characters"
    assert TEXT.strip(), "text must not be only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Read it back: the run is only a success if the file on disk is
    # byte for byte the text the gate will judge.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        assert f.read() == TEXT, "written file differs from TEXT"


if __name__ == "__main__":
    main()
