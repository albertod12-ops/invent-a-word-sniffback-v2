#!/usr/bin/env python3
"""Invent a Word We Need — entry program (v2: sniffback).

Writes one newly coined English word and its one-line definition to
/output/entry.txt. Deterministic: the same bytes on every run.
"""

import os

ENTRY = "sniffback — a smell that throws you years into the past in a single breath."

def main() -> None:
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == ENTRY.encode("utf-8"), "written bytes differ from entry"

if __name__ == "__main__":
    main()
