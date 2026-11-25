#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes a single joke about Monday mornings to /output/entry.txt.
Deterministic, stdlib only, no network, no input.

The joke's turn: you cannot ghost a weekday — Monday reads the
message and shows up at your desk anyway.
"""

import os

# SPDX-License-Identifier: MIT

JOKE = (
    "I tried to ghost Monday morning. "
    "It read my message at 6 a.m. and showed up at my desk anyway."
)


def main() -> None:
    line = JOKE.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert "\n" not in line, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
