#!/usr/bin/env python3
"""
pii-guard.py  —  PreToolUse hook (Write|Edit|MultiEdit)

Blocks sensitive CLIENT personal data from being written to disk, where it can leak into a
listing, a shared doc, marketing copy, or version control. Targets the data agents handle:
SSNs, bank account / routing numbers, and credit-card numbers.

Fail policy: FAIL CLOSED. If this crashes it BLOCKS the write - a client-PII leak is worse
than a false block. (The only other fail-closed hook is secret-scan.)
Override for a legitimate redacted/example value: REAL_ESTATE_PACK_ALLOW_PII=1
"""
import json
import os
import re
import sys

PATTERNS = [
    ("SSN", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
    ("bank routing/account", re.compile(r"(?i)\b(routing|account|acct)\s*(number|no|#)?\s*[:#]?\s*\d{8,17}\b")),
    ("credit card", re.compile(r"\b(?:\d[ -]?){13,16}\b")),
]
# Obvious placeholders / redactions are fine.
SAFE = re.compile(r"(?i)(xxx|0000|1234-?5678|redacted|example|placeholder|\bN/?A\b|###)")


def extract(tool_name, ti):
    chunks = []
    if tool_name == "Write":
        chunks.append(ti.get("content", ""))
    elif tool_name == "Edit":
        chunks.append(ti.get("new_string", ""))
    elif tool_name == "MultiEdit":
        for e in ti.get("edits", []):
            chunks.append(e.get("new_string", ""))
    return ti.get("file_path", "") or "file", "\n".join(c for c in chunks if c)


def main():
    data = json.loads(sys.stdin.read())
    if os.environ.get("REAL_ESTATE_PACK_ALLOW_PII") == "1":
        sys.exit(0)
    path, text = extract(data.get("tool_name", ""), data.get("tool_input", {}) or {})

    for line in text.splitlines():
        if SAFE.search(line):
            continue
        for name, pat in PATTERNS:
            m = pat.search(line)
            if m:
                print(
                    f"[pii-guard] BLOCKED: looks like client {name} in {path}: "
                    f"\"{m.group(0).strip()[:20]}...\".\n"
                    f"Never store client SSNs / financial numbers in listing, marketing, or "
                    f"shared files. Keep them in your secure CRM only.",
                    file=sys.stderr,
                )
                sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # FAIL CLOSED
        print(f"[pii-guard] internal error, blocking to be safe: {e}", file=sys.stderr)
        sys.exit(2)
