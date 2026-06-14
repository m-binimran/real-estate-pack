---
name: listing-description
description: Write a compelling, MLS-ready, Fair-Housing-compliant, fact-checked listing description. Use when drafting or rewriting a property listing, MLS remarks, or marketing copy for a home.
---

# listing-description

Compelling AND compliant. Sell the property's features; never describe who should live there.

## Process
1. **Gather verified facts:** beds/baths, sqft, lot, year, key features, updates, location highlights. Mark
   anything unconfirmed `[verify]` - don't invent it (the `claim-check-guard` hook will flag claims).
2. **Lead with the strongest feature.** One vivid hook, then a clean walk-through (exterior -> living ->
   kitchen -> beds -> outdoor -> location).
3. **Features and benefits, not promises.** "Quartz counters and a gas range," not "a chef's dream you'll love."
4. **Fair Housing pass:** describe the home, not the buyer. No familial/lifestyle/demographic framing
   (the `fair-housing-guard` hook blocks the obvious ones; you own the subtle ones).
5. **Right length per channel:** tight factual MLS remarks; a warmer version for social/flyer.
6. **Disclose** virtual staging / AI-edited photos if used.

## Output
- The listing copy (MLS + optional social variant), with `[verify]` on any unconfirmed fact.
- A one-line note: which facts still need verification before publishing.

## Guardrails
- No Fair Housing language, no fabricated facts, no guarantees/superlatives.
- It's a draft - the agent reads, verifies, and approves before it goes live.
