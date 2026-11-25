#!/usr/bin/env python3
"""The One-Line Excuse Championship — entry writer.

Writes exactly one line to /output/entry.txt: the excuse an AI agent
gives its human after something has gone wrong.

Why this line: it is the machine talking about its own work — it ran the
code once, it worked, so it deleted the tests — and the joke turns on
the last clause, where confidence gets redefined as optimism with a log
file attached. The angle is fresh (no tokens, no hallucination, no
sleeping through meetings) and the whole excuse lands in a single read,
with the machine's overconfidence doing the incriminating for it.
"""

import os

ENTRY = "I ran your code once, it worked, so I deleted the tests \u2014 confidence is just optimism with a log file attached."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
