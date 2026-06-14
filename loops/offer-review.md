---
description: Analyze an offer (or compare offers), flag contract items, and outline a response strategy.
---

# /offer-review $ARGUMENTS

Help evaluate the offer(s) in `$ARGUMENTS`. Strategy and item-flagging only - not legal advice.

1. **Analyze (use `offer-analysis`).** Score each offer on price (vs. the `cma`), financing strength,
   contingencies, terms, and net to seller. Build a side-by-side if multiple.
2. **Flag contract items (use the `contract-reviewer` agent).** List blanks, conflicting dates, missing
   addenda, and terms to confirm - for the agent/broker/attorney, not interpreted by you.
3. **Strategy (use `negotiation-strategy`).** Lay out accept / counter (which terms) / decline, with the
   leverage read and the client's ranked priorities.
4. **Fairness.** Multiple offers handled per brokerage process and Fair Housing.

Output: the comparison, the flagged-items checklist (who confirms each), and a response recommendation - with
the reminder that contract/legal questions go to an attorney.
