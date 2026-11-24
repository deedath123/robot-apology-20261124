#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty entry.

Writes a two-line robot apology to /output/entry.txt.
Line 1: one sentence, the robot apologizing for one specific mistake.
Line 2: one sentence, the lesson and the changed behaviour.
Standard library only, deterministic.
"""

from pathlib import Path

ENTRY = (
    "I'm sorry I watered your grandmother's orchid with yesterday's cold coffee "
    "instead of the fern beside it, and it wilted overnight.\n"
    "I learned to read the label on every pot before I pour, so from now on "
    "I will check the tag twice and water only the plant it names.\n"
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    assert text.strip(), "entry must not be only whitespace"
    lines = text.strip().split("\n")
    assert len(lines) == 2, "entry must be exactly 2 lines"
    assert all(line.strip().endswith(".") for line in lines), "each line must be one sentence"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
