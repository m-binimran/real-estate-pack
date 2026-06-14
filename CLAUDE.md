# CLAUDE.md - working ON real-estate-pack

This is the repo for the pack itself. (To use the pack in your workspace, run an installer - see README.)

## What this repo is
A curated, **enforced** Claude Code pack for US residential real estate agents. Layers: `rules/` (advisory) ·
`skills/` (on-demand) · `hooks/` (deterministic) · `loops/` (slash commands) · `agents/` (review subagents) ·
`mcp/` · `templates/`. Full list in [INVENTORY.md](INVENTORY.md).

## House rules for changing this repo
- Every item serves a goal: fewer tokens, accuracy, truth-telling, speed, compliance/quality.
- **Compliance content must be correct and sourced.** Fair Housing / disclosure / advertising law is the point
  of this pack - get it right, cite it, and never frame anything as legal advice.
- **Hooks must be tested:** add a case to `tests/test_hooks.py` and run `python tests/test_hooks.py`. State the
  fail mode (open/closed) in the docstring.
- Keep rule/skill files short - they cost tokens every turn.
- **No inflated claims.** Anything documented as working must actually have been run. New repo = 0 stars.
- Update `INVENTORY.md` and `CHANGELOG.md` when adding/removing items.

## Verify
```bash
python tests/test_hooks.py        # all hook behavior (16 cases)
python -c "import json;json.load(open('hooks/settings.json'))"
```

## Conventions
- Commit format: `<type>: <description>`. Hooks are Python 3.8+ (cross-platform). One logical change per PR.
- This is a drafting/guardrail tool, not legal advice - keep that framing everywhere.
