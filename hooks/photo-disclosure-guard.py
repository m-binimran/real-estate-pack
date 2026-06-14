#!/usr/bin/env python3
"""
photo-disclosure-guard.py  —  PostToolUse hook (Write|Edit|MultiEdit)

If listing text references virtually-staged / AI-enhanced / rendered images, reminds you that
AI-altered photos must be DISCLOSED (NAR Code of Ethics Art. 2 & 12; most MLSs require a
"Virtually Staged" label; CA AB 723 makes undisclosed AI-altered listing photos a misdemeanor
as of Jan 2026).

Advisory only. Fail policy: FAIL OPEN.
"""
import json
import os
import re
import sys

EDITED = re.compile(r"(?i)\b(virtual(ly)? stag\w*|digitally (stag|enhanc|alter)\w*|ai[- ]?(enhanc|generat|edit)\w*|rendered|photoshopp?ed|computer[- ]generated)\b")
DISCLOSED = re.compile(r"(?i)(virtually staged|digitally staged|disclosed|disclosure|photo (is|are) (virtually|digitally))")
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

    if EDITED.search(text) and not DISCLOSED.search(text):
        print(
            "[photo-disclosure-guard] This references altered/AI/staged imagery but no "
            "disclosure label. Add a clear 'Virtually Staged' / AI-edited disclosure on the "
            "photos and in the listing (NAR Art. 2 & 12; MLS rules; CA AB 723).",
            file=sys.stderr,
        )
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        sys.exit(0)
