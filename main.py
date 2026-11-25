#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username, one word and nothing else
(1-30 characters), to /output/entry.txt. Pure standard library.
"""

import os

ENTRY = "solana-hits"

MAX_CHARS = 30


def main():
    # Fail loudly instead of submitting a gate-violating entry.
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if len(ENTRY.split()) != 1:
        raise SystemExit("entry must be exactly one word")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
