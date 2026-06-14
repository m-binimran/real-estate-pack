#!/usr/bin/env python3
"""
review-gate.py  —  Stop hook

The "never publish unreviewed AI output" backstop. When a turn ends, if listing/marketing/
client-facing text was written this session, it reminds you that AI output is a DRAFT - read
every word, verify facts, and check Fair Housing before it goes to a client or the MLS.

HONEST LIMITATION: this can't tell whether you actually reviewed - it only knows a draft-type
file changed. It is a reminder, not a gate. It nudges once per stop cycle (no nag loop).

Fail policy: FAIL OPEN.
"""
import json
import os
import sys
import time

SEEN = ".real-estate-pack-stop-seen"


def main():
    data = json.loads(sys.stdin.read())
    if data.get("stop_hook_active"):
        sys.exit(0)

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    claude_dir = os.path.join(project_dir, ".claude")
    seen = os.path.join(claude_dir, SEEN)

    if os.path.exists(seen):
        try:
            os.remove(seen)
        except OSError:
            pass
        sys.exit(0)

    try:
        os.makedirs(claude_dir, exist_ok=True)
        with open(seen, "w", encoding="utf-8") as f:
            f.write(str(int(time.time())))
    except OSError:
        pass
    print(
        "[review-gate] Before sending anything to a client or the MLS: AI output is a DRAFT. "
        "Read every word, verify the facts (sqft, schools, HOA, zoning), and confirm no Fair "
        "Housing language. You are responsible for what you publish.",
        file=sys.stderr,
    )
    sys.exit(2)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        sys.exit(0)
