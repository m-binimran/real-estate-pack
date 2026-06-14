# Security & compliance policy

## Scope
real-estate-pack ships shell-invoked Python hooks that run inside your Claude Code sessions. Treat them as code
that executes on your machine - read a hook before trusting it. Each hook documents its **fail mode** in its docstring.

## Design stance
- `pii-guard` and `secret-scan` fail **closed**: if they error, they block the write, so client PII / secrets
  can't slip past on a crash.
- All other guards fail **open**: a bug in a guard must not block your normal work.
- **Guards are defense-in-depth, not a guarantee.** `fair-housing-guard` matches documented phrases - it will
  miss novel or subtle violations; `claim-check-guard` flags common claim shapes, not every fact. They do not
  replace the `compliance-reviewer` agent or a human read. Compliance is the licensed agent's responsibility.

## Handling client data
- Never commit client PII. `.gitignore` excludes `.env*`; keep SSNs/financials in your secure CRM, not in repo files.
- This pack does not transmit anything anywhere - hooks read stdin and write to stderr/stdout only.

## Reporting
- If a guard can be trivially bypassed in a way that matters (an obvious Fair Housing phrase it misses, a clear
  PII pattern it lets through), open an issue with a minimal example. We'll add a regression test to
  `tests/test_hooks.py`.

## Not legal advice
This project is a drafting and guardrail tool, not legal counsel. Fair Housing, disclosure, and advertising law
vary by jurisdiction and change over time. Confirm requirements with your broker and attorney.
