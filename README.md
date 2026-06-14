# real-estate-pack

**Compliance guardrails, skills, loops & review agents for US residential real estate agents on Claude Code.**

Most "AI for real estate" resources are copy-paste prompt packs. This one is **enforced**: the guarantees
come from **hooks** (deterministic - they run every time), with rules, skills, loops, and review agents on top.
It is built around the two things that get agents in trouble with AI: **Fair Housing** and **fabricated facts**.

Every item serves at least one goal:

| Icon | Goal |
|------|------|
| 🪙 | Fewer tokens |
| 🎯 | Accuracy (verified facts) |
| ✅ | Truth-telling (no hallucinated property details) |
| ⚡ | Speed |
| 💎 | Quality / compliance standard |

---

## ⚠️ Important - read first
- **This is not legal advice.** It is a drafting + guardrail tool. You, the licensed agent, are responsible
  for everything you publish or send.
- **US residential focus.** Fair Housing (federal), NAR, and disclosure references are US-based. Outside the
  US, swap in your jurisdiction's law.
- **Hooks are guardrails, not guarantees.** `fair-housing-guard` catches common, documented phrases - not every
  possible violation. Always run the `compliance-reviewer` and read every word before publishing.
- **State and brokerage rules vary** (disclosures especially). Confirm with your broker/attorney.

---

## What's inside
| Folder | Contents | Layer |
|--------|----------|-------|
| `rules/` | Advisory `CLAUDE.md` fragments (Fair Housing, truth-telling, confidentiality, no-advice, disclosure) | Advisory |
| `skills/` | Listing, CMA, consults, offers, market reports, lead follow-up, etc. | On-demand |
| `hooks/` | **Deterministic enforcement** (fair-housing, PII, fact-check, superlative, photo disclosure, review) + `settings.json` | **Enforced** |
| `loops/` | Multi-step slash commands (`/list-it`, `/price-it`, `/offer-review`, ...) | Workflow |
| `agents/` | Review subagents (compliance / listing / contract) | Review |
| `mcp/` | Browser MCP for verifying public property/market facts | Tooling |
| `templates/` | Listing intake, CMA, transaction checklist, client brief | Docs |
| `tests/` | `test_hooks.py` - runs every hook against sample inputs | Proof |

See [`INVENTORY.md`](INVENTORY.md) for the full table of every item and why it exists.

---

## Install
**Windows (PowerShell):**
```powershell
./install.ps1 -ProjectPath "C:\path\to\your\workspace"
```
**macOS / Linux:**
```bash
./install.sh /path/to/your/workspace
```
The installer copies `hooks/` into `<project>/.claude/hooks/`, merges `hooks/settings.json` into
`<project>/.claude/settings.json`, appends `rules/` into `<project>/CLAUDE.md`, and copies skills ->
`.claude/skills/`, loops -> `.claude/commands/`, agents -> `.claude/agents/`. (`mcp/` and `templates/` are for
reference - wire them in per the folder READMEs.)

**Requires:** Python 3.8+ on PATH (the hooks are Python; they run on Windows/macOS/Linux).

**Verify the pack itself:** `python tests/test_hooks.py` (16 cases across all 7 hooks).

**Uninstall** (removes only what it installed, restores your CLAUDE.md):
```powershell
./uninstall.ps1 -ProjectPath "C:\path\to\your\workspace"   # Windows
./uninstall.sh /path/to/your/workspace                      # macOS / Linux
```

---

## Honest scope
- New repo - starts at **0 stars**. No inflated claims.
- Inspired by the dev-pack methodology ([github.com/m-binimran/dev-pack](https://github.com/m-binimran/dev-pack))
  and grounded in published Fair Housing advertising guidance and 2026 real-estate-AI compliance writing.
- The guardrails reduce risk; they do not eliminate it. Compliance is the licensed agent's responsibility.

## License
MIT - see [LICENSE](LICENSE).
