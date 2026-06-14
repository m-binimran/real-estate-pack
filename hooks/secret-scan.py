#!/usr/bin/env python3
"""
secret-scan.py  —  PreToolUse hook (Write|Edit|MultiEdit)

Blocks hardcoded API keys/tokens from being written to disk. Agents integrate CRMs, MLS/IDX
feeds, mail, and lead tools - those keys belong in environment variables, not in files.

Fail policy: FAIL CLOSED. A crash blocks the write so a secret can't slip past on error.
"""
import json
import re
import sys

PATTERNS = [
    ("Private key block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("JWT / service token", re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
    ("Generic key assignment", re.compile(
        r"""(?ix)(api[_-]?key|secret|token|passwd|password|client[_-]?secret|access[_-]?token)
        \s*[:=]\s*['"]([^'"\s]{12,})['"]""")),
    ("AWS access key id", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("Stripe live key", re.compile(r"sk_live_[0-9a-zA-Z]{16,}")),
    ("Google API key", re.compile(r"AIza[0-9A-Za-z_-]{30,}")),
]
PLACEHOLDER = re.compile(
    r"(?i)(process\.env|os\.environ|getenv|import\.meta\.env|\$\{?[A-Z_]+\}?"
    r"|your[_-]?(api[_-]?key|secret|token)|xxx+|placeholder|example|changeme|<[^>]+>)")


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
    path, content = extract(data.get("tool_name", ""), data.get("tool_input", {}) or {})
    if path.endswith(".env.example") or path.endswith(".env.template"):
        sys.exit(0)
    for line in content.splitlines():
        if PLACEHOLDER.search(line):
            continue
        for name, pat in PATTERNS:
            if pat.search(line):
                print(
                    f"[secret-scan] BLOCKED: hardcoded secret ({name}) in {path}.\n"
                    f"Move it to an environment variable (e.g. process.env.X) and reference it.",
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
        print(f"[secret-scan] internal error, blocking to be safe: {e}", file=sys.stderr)
        sys.exit(2)
