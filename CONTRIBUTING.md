# Contributing

Thanks for improving real-estate-pack. Keep the bar high and the scope tight (US residential real estate).

## Principles
- Every item must serve a stated goal: fewer tokens, accuracy, truth-telling, speed, or compliance/quality.
- **Compliance accuracy matters most.** Fair Housing, disclosure, and advertising rules must be correct and
  sourced. When in doubt, cite the guidance. Don't add a phrase to a guard without a documented basis.
- **Hooks must be tested.** Add a case to `tests/test_hooks.py` and run it: `python tests/test_hooks.py`.
  State the fail mode (open/closed) in the hook docstring.
- **No legal advice** in any rule/skill/agent - frame as "confirm with broker/attorney."
- Keep rule/skill files short - they cost tokens every turn.

## Adding a hook
1. Read JSON from stdin, decide, exit 0 (allow) or 2 (block/warn, reason on stderr).
2. Fail-closed only where a miss is worse than a false block (PII, secrets). Otherwise fail-open.
3. Wire it in `hooks/settings.json` with the right event + matcher. Add a test case. Update `INVENTORY.md`.

## Adding a skill / loop / agent
- Skill: a folder under `skills/` with `SKILL.md` (frontmatter `name` + `description`).
- Loop: a `.md` under `loops/` with a `description` frontmatter (installs as a slash command).
- Agent: a `.md` under `agents/` with frontmatter (`name`, `description`, `tools`, `model`).
- Update `INVENTORY.md` and `CHANGELOG.md`. Don't reference a skill/agent you didn't add.

## PRs
- One logical change per PR. Commit format: `<type>: <description>`. Note what you tested + paste the result.
