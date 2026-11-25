#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun entry.

Writes one fortune cookie line to /output/entry.txt.
"""

import os

FORTUNE = "Your lucky numbers are 0, 0, 0, 0 \u2014 the market took the rest, but your sense of humour survived."

def main():
    words = FORTUNE.split()
    assert 1 <= len(words) <= 20, "fortune must be 1-20 words"
    assert 1 <= len(FORTUNE) <= 160, "fortune must be 1-160 characters"
    assert "\n" not in FORTUNE, "fortune must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)

if __name__ == "__main__":
    main()
