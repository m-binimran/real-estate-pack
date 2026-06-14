#!/usr/bin/env python3
"""
claim-check-guard.py  —  PostToolUse hook (Write|Edit|MultiEdit)

Flags specific factual claims in listing/marketing text that AI commonly gets wrong or
hallucinates - square footage, lot size, year built, school ratings, HOA fees, flood/zoning -
and reminds you to verify each against the MLS / county / source before publishing.

Advisory only (PostToolUse exit 2 feeds the note back; the write already happened).
Fail policy: FAIL OPEN.
"""
import json
import os
import re
import sys

CLAIMS = [
    ("square footage", re.compile(r"(?i)\b[\d,]{3,}\s*(sq\.?\s*ft|square feet|sqft)\b")),
    ("lot size", re.compile(r"(?i)\b[\d.]+\s*(acre|acres)\b|\blot size\b")),
    ("year built", re.compile(r"(?i)\b(built in|year built|constructed in)\s*\d{4}\b")),
    ("school rating/name", re.compile(r"(?i)\b(top[- ]rated|#?\s*\d+\s*(rated|ranked)|blue ribbon|\d(\.\d)?\s*/\s*10)\s+schools?\b|\bschool district\b")),
    ("HOA fee", re.compile(r"(?i)\bhoa\b.*\$\s?\d+|\$\s?\d+\s*(/|per)\s*(mo|month|year|yr)\b")),
    ("flood / zoning", re.compile(r"(?i)\b(no flood|not in a flood|flood zone|zoned (for )?\w+|rezone)\b")),
    ("tax amount", re.compile(r"(?i)\b(property tax|taxes)\b.*\$\s?\d+")),
]
ONLY_EXT = {".md", ".txt", ".mdx", ".html"}


def main():
    data = json.loads(sys.stdin.read())
    ti = data.get("tool_input", {}) or {}
    path = ti.get("file_path") or ti.get("path") or ""
    _, ext = os.path.splitext(path)
    if ext.lower() not in ONLY_EXT or not os.path.isfile(path):
        sys.exit(0)
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    found = [name for name, pat in CLAIMS if pat.search(text)]
    if not found:
        sys.exit(0)
    print(
        "[claim-check-guard] This contains factual claims AI often gets wrong: "
        + ", ".join(sorted(set(found)))
        + ". Verify each against the MLS / county records / source before publishing - "
          "you (not the AI) are liable for accuracy.",
        file=sys.stderr,
    )
    sys.exit(2)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # FAIL OPEN
        print(f"[claim-check-guard] internal error, skipping: {e}", file=sys.stderr)
        sys.exit(0)
