#!/usr/bin/env python3
"""
superlative-guard.py  —  PostToolUse hook (Write|Edit|MultiEdit)

Flags absolute / guarantee-style claims in marketing copy that create misrepresentation
liability: "guaranteed", "best price in town", "won't last", "perfect", "flawless",
"as-is with no issues", "will appreciate". These promise outcomes you can't promise.

Advisory only. Fail policy: FAIL OPEN.
"""
import json
import os
import re
import sys

RISKY = re.compile(
    r"(?i)\b(guarantee[ds]?|guaranteed (to|return)|best (price|deal|value) (in|on the)"
    r"|won'?t last|priced to (sell|move) fast|flawless|perfect (home|condition|property)"
    r"|no (issues|problems|defects)|will (appreciate|increase in value)|risk[- ]free"
    r"|once[- ]in[- ]a[- ]lifetime|must sell)\b"
)
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

    hits = sorted(set(m.group(0).strip().lower() for m in RISKY.finditer(text)))
    if not hits:
        sys.exit(0)
    print(
        "[superlative-guard] Misrepresentation risk - these promise outcomes you can't "
        f"guarantee: {', '.join(hits)}. Soften to verifiable, factual language before publishing.",
        file=sys.stderr,
    )
    sys.exit(2)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        sys.exit(0)
