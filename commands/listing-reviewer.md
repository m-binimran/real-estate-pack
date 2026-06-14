---
description: Reviews a listing description for quality, factual accuracy, and Fair Housing compliance. Use after drafting listing/MLS copy, and inside /list-it.
---

# /listing-reviewer $ARGUMENTS

Launch the `listing-reviewer` subagent to review: $ARGUMENTS

If no target is specified, review the most recent changes (run `git diff`). Relay the subagent's findings,
grouped by severity, with its verdict.
