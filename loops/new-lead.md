---
description: Qualify a new lead, match to needs without steering, and start a compliant follow-up sequence.
---

# /new-lead $ARGUMENTS

Process the new lead in `$ARGUMENTS` from intake to an active follow-up plan.

1. **Qualify (use `buyer-consultation` or `seller-consultation`).** Capture stated criteria, timeline, and
   financing/listing readiness. Refer money specifics to a licensed lender.
2. **Segment** by stated interest and stage - **never** by a protected class or inferred demographic.
3. **Match (buyers):** suggest objective options meeting their criteria; let them choose neighborhoods (no steering).
4. **Follow up (use `lead-followup`).** Start a value-first sequence with proper cadence, unsubscribe/ID
   (CAN-SPAM) and consent/STOP (TCPA). Don't text without consent.
5. **Protect their data.** Keep PII in the CRM, not in shared/marketing files (the `pii-guard` hook enforces).

Output: a lead brief + the follow-up sequence, ready for the agent to send.
