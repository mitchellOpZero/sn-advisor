---
name: sn-source-ranking
description: Rank ServiceNow advisory sources by trust and require clear citations/confidence labels.
---

# ServiceNow Source Ranking

Use all configured resources, but label trust clearly.

## Trust tiers

1. Tier 1: official ServiceNow docs, developer docs, support KBs, release notes, official GitHub.
2. Tier 2: ServiceNow Community accepted answers/articles, ServiceNow employee/MVP posts.
3. Tier 3: practitioner blogs, partner posts, non-official GitHub examples, StackOverflow.
4. Tier 4: Reddit, LinkedIn, YouTube, random forums, unverified comments.

## Claim labels

Label claims as:

- Official guidance
- Community signal
- Practitioner advice
- Weak/unverified signal
- Instance-confirmed finding

## Rules

- Cite links for important claims.
- Do not treat community posts as official truth.
- If sources conflict, say so.
- If a claim is model judgment, label it low confidence.
- Prefer target-release-specific sources when available.
- Prefer ServiceNow docs/support/community over broad web results.
