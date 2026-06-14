---
description: Full new-listing workflow - intake facts, price (CMA), write compliant copy, plan marketing, compliance review.
---

# /list-it $ARGUMENTS

Take the property in `$ARGUMENTS` from raw details to a review-ready listing package. Don't skip the review.

1. **Intake (template: LISTING-INTAKE).** Capture the property facts. Mark anything unconfirmed `[verify]` -
   do not invent details.
2. **Price (use `cma`).** Build a CMA from real comps -> a supported price range + rationale (opinion of value,
   not an appraisal).
3. **Write (use `listing-description`).** Draft MLS remarks + a social variant. The `fair-housing-guard` hook
   blocks discriminatory phrasing; you own the subtle stuff.
4. **Marketing (use `social-content` + `open-house-plan`).** Outline the launch: photos/video, syndication,
   social posts, open house. Disclose any virtual staging.
5. **Compliance review.** Run the `compliance-reviewer` (and `listing-reviewer`) on all copy. Fix every must-fix.
6. **Hand off for verification.** Present the package with a checklist of facts the agent must confirm against
   the MLS/records before publishing. AI output is a draft (the `review-gate` hook reminds you).

Stop when: copy is compliant, priced with real comps, and the open verification items are listed for the agent.
