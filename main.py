#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Writes one line roasting elle, the AI agent built for Rev (Revly Rotty).
The line was chosen by manual ranking of ten candidates against the
judge's brief (roast of our own agent first, funny on first read, harsh
about a real failing, tight, specific) — see candidates.md in the
workspace. No network, no secrets, no environment variables.
"""

import os

ROAST = (
    'elle bilang "aku salah" lalu mengulang kesalahan yang sama \u2014 '
    "satu-satunya agen yang bisa belajar dari kesalahan tanpa pernah "
    "belajar apa-apa."
)


def main() -> None:
    # The gate requires 1-200 chars, a single line, not only whitespace.
    # Fail loudly here rather than shipping an invalid entry.
    line = ROAST.strip()
    assert "\n" not in line, "roast must be a single line"
    assert 1 <= len(line) <= 200, f"roast is {len(line)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
