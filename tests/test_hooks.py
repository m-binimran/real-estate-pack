#!/usr/bin/env python3
"""
test_hooks.py - self-contained test harness for the real-estate-pack hooks.

No third-party deps. Runs each hook as a subprocess with sample JSON on stdin and asserts the
exit code (0 = allow, 2 = block/warn). Run locally or in CI:

    python tests/test_hooks.py

Exit 0 if all pass, 1 if any fail.
"""
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOOKS = os.path.join(ROOT, "hooks")
PY = sys.executable


def run_hook(name, payload, env=None):
    e = dict(os.environ)
    if env:
        e.update(env)
    p = subprocess.run([PY, os.path.join(HOOKS, name)],
                       input=json.dumps(payload), capture_output=True, text=True, env=e)
    return p.returncode


def wp(tool, file_path, content=None):
    ti = {"file_path": file_path}
    if content is not None:
        ti["content"] = content
    return {"tool_name": tool, "tool_input": ti}


def write_file(d, name, body):
    p = os.path.join(d, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(body)
    return p


CASES = []
def case(name, expected, fn): CASES.append((name, expected, fn))

# fair-housing-guard
case("fair-housing blocks 'perfect for families'", 2,
     lambda d: run_hook("fair-housing-guard.py", wp("Write", "listing.md", "Lovely home, perfect for families.")))
case("fair-housing blocks 'no children'", 2,
     lambda d: run_hook("fair-housing-guard.py", wp("Write", "listing.md", "Quiet unit, no children please.")))
case("fair-housing allows property-focused copy", 0,
     lambda d: run_hook("fair-housing-guard.py", wp("Write", "listing.md", "Spacious 4-bedroom home with a large fenced yard and updated kitchen.")))

# pii-guard (fail-closed)
case("pii blocks SSN", 2,
     lambda d: run_hook("pii-guard.py", wp("Write", "client.md", "Buyer SSN 123-45-6789 on file.")))
case("pii allows redacted placeholder", 0,
     lambda d: run_hook("pii-guard.py", wp("Write", "client.md", "Buyer SSN xxx-xx-xxxx (redacted).")))
case("pii allows normal copy", 0,
     lambda d: run_hook("pii-guard.py", wp("Write", "listing.md", "3 bed, 2 bath, listed at 450000.")))

# secret-scan (fail-closed)
case("secret-scan blocks live key", 2,
     lambda d: run_hook("secret-scan.py", wp("Write", "config.txt", 'crm_key = "sk_live_abcdefghijklmnop1234"')))
case("secret-scan allows env ref", 0,
     lambda d: run_hook("secret-scan.py", wp("Write", "config.txt", "crm_key = process.env.CRM_KEY")))

# claim-check-guard (PostToolUse, real file)
case("claim-check flags sqft claim", 2,
     lambda d: run_hook("claim-check-guard.py", wp("Write", write_file(d, "l1.md", "Stunning home, 2,400 sq ft of living space."))))
case("claim-check allows claim-free copy", 0,
     lambda d: run_hook("claim-check-guard.py", wp("Write", write_file(d, "l2.md", "Bright, move-in ready home with a modern kitchen."))))

# superlative-guard
case("superlative flags 'guaranteed'", 2,
     lambda d: run_hook("superlative-guard.py", wp("Write", write_file(d, "s1.md", "This home is guaranteed to appreciate."))))
case("superlative allows factual copy", 0,
     lambda d: run_hook("superlative-guard.py", wp("Write", write_file(d, "s2.md", "Recently updated roof and HVAC."))))

# photo-disclosure-guard
case("photo-disclosure flags undisclosed AI edit", 2,
     lambda d: run_hook("photo-disclosure-guard.py", wp("Write", write_file(d, "p1.md", "Living room photos are AI-enhanced for brightness."))))
case("photo-disclosure allows disclosed staging", 0,
     lambda d: run_hook("photo-disclosure-guard.py", wp("Write", write_file(d, "p2.md", "Photos are virtually staged (disclosed)."))))

# review-gate (Stop) - isolate CLAUDE_PROJECT_DIR so the once-per-cycle marker is deterministic
case("review-gate nudges at stop", 2,
     lambda d: run_hook("review-gate.py", {"stop_hook_active": False}, env={"CLAUDE_PROJECT_DIR": d}))
case("review-gate no loop when active", 0,
     lambda d: run_hook("review-gate.py", {"stop_hook_active": True}, env={"CLAUDE_PROJECT_DIR": d}))


def main():
    passed = failed = 0
    with tempfile.TemporaryDirectory() as d:
        for name, expected, fn in CASES:
            try:
                got = fn(d)
            except Exception as e:
                print(f"ERROR {name}: {e}"); failed += 1; continue
            ok = got == expected
            print(f"{'PASS' if ok else 'FAIL'}  {name}  (expected {expected}, got {got})")
            passed += ok; failed += not ok
    print(f"\n{passed} passed, {failed} failed")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
