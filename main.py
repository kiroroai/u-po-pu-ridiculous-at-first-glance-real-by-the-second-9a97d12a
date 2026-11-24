#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes a single sentence (<=200 characters) to /output/entry.txt pitching
a bizarre startup that sounds like a joke until the business logic lands:
procrastinators pay a stranger to follow them around narrating their life
like a wildlife documentary, because being watched makes people behave.
Deterministic: the same bytes every run.
"""

import os
from pathlib import Path

# The pitch does its three jobs in one sentence: the odd thing being sold
# (a stranger narrating your life like a wildlife documentary), who pays
# (procrastinators, $99 a day), and why it holds together (being watched
# makes people behave, so the absurd service sells real accountability).
SENTENCE = (
    "Procrastinators pay $99 a day for a stranger to follow them around "
    "narrating their life like a wildlife documentary, because nobody "
    "slacks off while an audience is watching."
)


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, one sentence.
    assert 1 <= len(SENTENCE) <= 200, f"sentence is {len(SENTENCE)} characters"
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith(".")
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry = output_dir / "entry.txt"
    entry.write_text(SENTENCE, encoding="utf-8")
    print(f"wrote {entry} ({len(SENTENCE)} characters)")


if __name__ == "__main__":
    main()
