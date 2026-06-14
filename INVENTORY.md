# Inventory - every item, what it does, why we need it

Goals: 🪙 tokens · 🎯 accuracy · ✅ truth-telling · 💎 quality/compliance · ⚡ speed

## Hooks (`hooks/` -> `.claude/hooks/`, wired by `settings.json`) - the enforced backbone
| Hook (event) | What it does | Fail mode | Goals |
|--------------|--------------|-----------|-------|
| `fair-housing-guard` (PreToolUse Write/Edit) | Blocks documented Fair Housing violations in listing/marketing text | open | 💎✅ |
| `pii-guard` (PreToolUse Write/Edit) | Blocks client SSN/financial numbers from hitting disk | closed | 💎 |
| `secret-scan` (PreToolUse Write/Edit) | Blocks hardcoded CRM/MLS API keys | closed | 💎 |
| `claim-check-guard` (PostToolUse Write/Edit) | Flags unverified facts (sqft/schools/HOA/flood) -> verify with MLS | open | 🎯✅ |
| `superlative-guard` (PostToolUse Write/Edit) | Flags misrepresentation ("guaranteed/won't last/flawless") | open | ✅ |
| `photo-disclosure-guard` (PostToolUse Write/Edit) | Flags AI/virtually-staged imagery missing a disclosure | open | 💎 |
| `review-gate` (Stop) | Reminds: AI output is a draft - review before sending to client/MLS | open | ✅ |

## Rules (`rules/` -> appended to CLAUDE.md)
| File | What it does | Goals |
|------|--------------|-------|
| `fair-housing.md` | Describe the property not the buyer; banned framing; steering; 55+ nuance | 💎✅ |
| `truth-telling.md` | Never invent property facts/comps; mark `[verify]`; cite sources | ✅🎯 |
| `client-confidentiality.md` | Keep client PII out of shared/marketing files | 💎 |
| `no-unlicensed-advice.md` | No legal/tax/appraisal advice; refer to professionals | 💎 |
| `ai-disclosure.md` | Disclose AI/virtually-staged photos (NAR/MLS/AB 723) | 💎 |
| `professional-voice.md` | No guarantees/superlatives; features over promises | ✅💎 |
| `review-before-publish.md` | AI output is a draft; checklist before publishing | ✅ |
| `core-terse.md` | Client-ready, concise output | 🪙⚡ |

## Skills (`skills/` -> `.claude/skills/`)
| Skill | What it does | Goals |
|-------|--------------|-------|
| `listing-description` | MLS-ready, Fair-Housing-clean, fact-checked listing copy | 💎✅ |
| `cma` | Comparative Market Analysis (real comps, adjustments, range) | 🎯💎 |
| `buyer-consultation` | Needs analysis, process map, no steering | 💎 |
| `seller-consultation` | Pricing, prep, marketing, net sheet outline | 💎🎯 |
| `offer-analysis` | Score/compare offers on price, financing, terms, net | 🎯💎 |
| `market-report` | Sourced neighborhood/market update narrative | 🎯✅ |
| `lead-followup` | CAN-SPAM/TCPA-compliant nurture sequences, no steering | 💎 |
| `open-house-plan` | Promo, prep, lead capture, safety, follow-up | ⚡💎 |
| `transaction-timeline` | Contract-to-close milestones + deadlines | ⚡🎯 |
| `disclosure-checklist` | Required disclosures + state-specific flags | 💎 |
| `social-content` | Compliant just-listed/market/brand posts | 💎 |
| `objection-handling` | Honest, evidence-based objection scripts | 💎 |
| `negotiation-strategy` | Interests, leverage, trades, walk-away | 🎯💎 |
| `farming-prospecting` | Compliant farm/sphere plan + cadence | 💎 |
| `truthful-reporter` | Verify facts + compliance before "final" | ✅ |

## Loops (`loops/` -> `.claude/commands/`)
| Command | What it does | Goals |
|---------|--------------|-------|
| `/list-it` | Intake -> CMA -> compliant copy -> marketing -> compliance review | 💎✅ |
| `/price-it` | Build a defensible CMA from real comps | 🎯 |
| `/new-lead` | Qualify -> match (no steering) -> compliant follow-up | 💎 |
| `/offer-review` | Analyze offer -> flag contract items -> response strategy | 🎯💎 |
| `/close-it` | Transaction timeline + disclosure checklist | ⚡💎 |
| `/market-update` | Sourced market report for newsletter/briefing | 🎯✅ |

## Agents (`agents/` -> `.claude/agents/`)
| Agent | What it does | Goals |
|-------|--------------|-------|
| `compliance-reviewer` | Fair Housing + disclosures + advice + PII + misrepresentation review | 💎✅ |
| `listing-reviewer` | Listing quality + factual accuracy + Fair Housing | 💎✅ |
| `contract-reviewer` | Flags missing/ambiguous contract terms (NOT legal advice) | 💎 |

## Supporting
| Item | What it does | Goals |
|------|--------------|-------|
| `mcp/.mcp.json` | Browser MCP to verify public property/market facts | ✅🎯 |
| `templates/` | Listing intake, CMA, transaction checklist, client brief | 💎 |
| `tests/test_hooks.py` | Runs every hook against sample inputs (16 cases) | ✅ |
| `.github/` | CI (tests hooks on 3 Python versions) + issue/PR templates | ✅💎 |
| `install.*` / `uninstall.*` | One-command setup + clean removal | ⚡ |
