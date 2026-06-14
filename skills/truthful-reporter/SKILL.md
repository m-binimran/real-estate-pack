---
name: truthful-reporter
description: Verify facts and compliance before presenting client-facing real estate content as final. Use before sending a listing, CMA, market report, or email to a client or the MLS.
---

# truthful-reporter

Turn "I drafted it" into "I verified it" - or an honest "needs verification."

## Before calling anything ready, confirm
| Content | Check |
|---------|-------|
| Listing | Every fact (sqft, beds, lot, year, HOA, features) matches the MLS/records; photos disclosed |
| CMA | Comps are real, recent, comparable; labeled opinion-of-value not appraisal |
| Market report | Each stat has a named source + as-of date |
| Disclosures | Required items for the state are present and acknowledged |
| Any client copy | Fair Housing clean, no PII, no overpromises, no legal/tax advice |

## Report format
- State what's verified vs. what still needs the agent to confirm. Use `[verify]` for open items.
- Never present unverified property facts as confirmed. "I drafted copy claiming X" is not "the home has X."

## Guardrails
- If you can't verify a fact here, say so - don't fill the gap with a guess.
- The agent is liable for what's published; this skill makes the open items explicit, not hidden.
(The `claim-check-guard`, `fair-housing-guard`, and `review-gate` hooks back this up automatically.)
