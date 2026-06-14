<!-- Keep PRs to one logical change. Commit format: <type>: <description> -->

## What & why
<!-- One or two lines. -->

## Type
- [ ] New rule / skill / hook / loop / agent
- [ ] Fix
- [ ] Docs
- [ ] Compliance content update

## Checklist
- [ ] Serves a stated goal (tokens / accuracy / truth-telling / speed / compliance)
- [ ] Compliance content is correct and sourced; nothing framed as legal advice
- [ ] If a hook changed: `python tests/test_hooks.py` passes (paste below)
- [ ] If a hook added: a test case added + fail mode stated in its docstring
- [ ] `INVENTORY.md` / `CHANGELOG.md` updated
- [ ] No inflated claims; anything I claim works, I actually ran

## Test output
```
<!-- paste `python tests/test_hooks.py` output -->
```
