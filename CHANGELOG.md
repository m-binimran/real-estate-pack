# Changelog

All notable changes to this project are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/). This project uses [SemVer](https://semver.org/).

## [Unreleased]

### Added
- **Per-skill slash commands** (`commands/` -> `.claude/commands/`): every skill is now directly callable as
  `/<skill-name>` (e.g. `/cma`, `/listing-description`), in addition to the workflow loops. Installer +
  uninstaller updated to copy/remove them.
- **Per-agent slash commands**: each review agent is callable as `/<agent-name>` (`/compliance-reviewer`,
  `/listing-reviewer`, `/contract-reviewer`).

## [0.1.0] - 2026-06-14
Initial pack. US residential real estate.

### Added
- **Hooks (7):** fair-housing-guard, pii-guard (fail-closed), secret-scan (fail-closed), claim-check-guard,
  superlative-guard, photo-disclosure-guard, review-gate.
- **Rules (8):** fair-housing, truth-telling, client-confidentiality, no-unlicensed-advice, ai-disclosure,
  professional-voice, review-before-publish, core-terse.
- **Skills (15):** listing-description, cma, buyer-consultation, seller-consultation, offer-analysis,
  market-report, lead-followup, open-house-plan, transaction-timeline, disclosure-checklist, social-content,
  objection-handling, negotiation-strategy, farming-prospecting, truthful-reporter.
- **Loops (6):** /list-it, /price-it, /new-lead, /offer-review, /close-it, /market-update.
- **Agents (3):** compliance-reviewer, listing-reviewer, contract-reviewer.
- MCP config (browser), templates (listing intake / CMA / transaction checklist / client brief), install +
  uninstall scripts (PowerShell + bash), committed test harness (`tests/test_hooks.py`, 16 cases), CI workflow,
  issue/PR templates, SECURITY.md, .env.example.

### Notes
- US-focused (Fair Housing Act, NAR, AI-photo disclosure). Not legal advice; guardrails reduce risk, not
  eliminate it. All 7 hooks verified by the committed test harness.
