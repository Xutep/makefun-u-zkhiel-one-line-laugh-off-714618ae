#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.

Deterministic, standard library only: no network, no randomness,
no input files. The joke is a single line, well under the 200
character limit.
"""

import os

JOKE = "My alarm clock dumped me. It said I kept hitting snooze on our relationship."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
