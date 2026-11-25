#!/usr/bin/env python3
"""The Coward's Way Out — entry program.

writes one line, a phone's last words as its battery hits 1 percent,
to /output/entry.txt. Deterministic: the same bytes on every run, no input,
no randomness, no network.

The farewell: with 1% left and 47 unread messages from the owner's mother,
the phone chooses to die rather than deliver them. The laugh is the phone
as a reluctant messenger with its own survival instinct — it would rather
go dark than face the inbox. No will reading, no farewell to the charger,
no pun on 1 percent.
"""

from pathlib import Path

ENTRY = (
    "I have 1% left and 47 unread messages from your mother. I'm taking the coward's way out.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 199, "entry must be 1-199 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
