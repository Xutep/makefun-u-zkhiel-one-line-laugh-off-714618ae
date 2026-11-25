#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.

Deterministic, standard library only: no network, no randomness,
no input files. The joke is a single line, well under the 200
character limit.
"""

import os

JOKE = "My alarm clock dumped me. It said I kept hitting snooze on our relationship."


def prepare_line(text: str) -> str:
    """Return text as exactly one line: collapse any whitespace runs
    (including newlines) to single spaces and enforce the 200-char cap."""
    line = " ".join(text.split())
    if len(line) > 200:
        raise ValueError(f"entry line is {len(line)} chars, over the 200-char limit")
    if not line:
        raise ValueError("entry line is empty")
    return line


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(prepare_line(JOKE) + "\n")


if __name__ == "__main__":
    main()
