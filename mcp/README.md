# MCP config

One server that lets the agent **verify facts against real sources** instead of guessing - which is what makes
the truth-telling guardrails work.

| Server | What it gives the agent | Why it matters |
|--------|-------------------------|----------------|
| `playwright` | Drive a real browser to read public listing portals, county records, and market data | `cma`, `market-report`, and `truthful-reporter` can confirm sqft/comps/stats instead of hallucinating them |

## Setup
1. Copy `.mcp.json` to your project root (or merge into an existing one).
2. Use it to look up and confirm public facts; always cite the source + as-of date.

> The agent can read public data to *verify* - but you are still responsible for confirming material facts
> against the MLS and county records before publishing. The browser is for checking, not for republishing
> scraped data as your own.
