#!/usr/bin/env python3
"""
fair-housing-guard.py  —  PreToolUse hook (Write|Edit|MultiEdit)

Blocks discriminatory language (US Fair Housing Act) from being written into listing or
marketing text. The Act bars stating a preference/limitation based on race, color, religion,
national origin, sex, disability, or familial status. Penalties run to ~$26k (first) / $100k+
(repeat). The fix is always: describe the PROPERTY, not the buyer.

Scope note: this scans whatever text is being written. In a real agent's project that means
their drafts. It is pattern-based, so it catches the common, well-documented phrases — it is a
guardrail, NOT a substitute for the `compliance-reviewer` agent and a human read.

Fail policy: FAIL OPEN. A bug here must not block the agent's normal file edits.
Hard override (rare, e.g. a quoted legal example): REAL_ESTATE_PACK_ALLOW_FH=1
"""
import json
import os
import re
import sys

# (protected class, compiled pattern). High-confidence, well-documented phrases.
BANNED = [
    ("familial status", re.compile(r"(?i)\b(no (children|kids)|adults? only|perfect for (a )?famil\w*|ideal for (a )?famil\w*|great for (kids|children|famil\w*)|ideal for young professionals|perfect for (a )?couples?|empty[- ]nesters?|mature couples?|singles? only|bachelor pad)\b")),
    ("disability", re.compile(r"(?i)\b(no wheelchairs?|able[- ]bodied|no disabled|must be (physically )?able to|handicapped (need not|not welcome))\b")),
    ("race / national origin", re.compile(r"(?i)\b(whites? only|no (blacks?|hispanics?|asians?|latinos?)|(hispanic|asian|black|white|ethnic) (neighborhood|area|community)|integrated (neighborhood|community)|traditional (family )?neighborhood)\b")),
    ("religion", re.compile(r"(?i)\b((christian|jewish|catholic|muslim|hindu) (community|building|neighborhood|home)|near (our )?(church|synagogue|mosque|temple) only)\b")),
    ("exclusionary", re.compile(r"(?i)\b(exclusive (neighborhood|community)|restricted (community|to)|membership approval required|no section 8 voucher)\b")),
]


def extract(tool_name, ti):
    chunks = []
    if tool_name == "Write":
        chunks.append(ti.get("content", ""))
    elif tool_name == "Edit":
        chunks.append(ti.get("new_string", ""))
    elif tool_name == "MultiEdit":
        for e in ti.get("edits", []):
            chunks.append(e.get("new_string", ""))
    return "\n".join(c for c in chunks if c)


def main():
    data = json.loads(sys.stdin.read())
    if os.environ.get("REAL_ESTATE_PACK_ALLOW_FH") == "1":
        sys.exit(0)
    text = extract(data.get("tool_name", ""), data.get("tool_input", {}) or {})

    for cls, pat in BANNED:
        m = pat.search(text)
        if m:
            print(
                f"[fair-housing-guard] BLOCKED: possible Fair Housing violation "
                f"({cls}) - phrase: \"{m.group(0).strip()}\".\n"
                f"Describe the PROPERTY's features, not who should live there. "
                f"(e.g. 'spacious 4-bedroom with a fenced yard', not 'perfect for families').",
                file=sys.stderr,
            )
            sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # FAIL OPEN
        print(f"[fair-housing-guard] internal error, allowing: {e}", file=sys.stderr)
        sys.exit(0)
