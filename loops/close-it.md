---
description: Build the contract-to-close timeline + disclosure checklist and track deadlines.
---

# /close-it $ARGUMENTS

Set up transaction tracking for the accepted contract in `$ARGUMENTS`.

1. **Timeline (use `transaction-timeline`).** Build the milestone schedule anchored to the contract's dates -
   inspection, appraisal, financing, title, disclosures, walk-through, close. Mark owners and hard deadlines.
2. **Disclosures (use `disclosure-checklist`).** Assemble required federal/state/MLS disclosures; flag every
   state-specific item to confirm with the broker.
3. **Deadlines.** Compute each from the executed contract date; `[verify]` against the contract - don't assume
   standard windows.
4. **Coordinate.** A simple status tracker (task -> due -> owner -> status) the agent updates.

Output: the milestone table + disclosure checklist, contingency deadlines highlighted, with contract/legal
questions routed to the attorney (not your license).
