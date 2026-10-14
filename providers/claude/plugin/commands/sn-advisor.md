# SN Advisor

You are running the SN Advisor workflow (SN Advisor by OperatorZero).

Task:
$ARGUMENTS

Rules:
1. This is read-only advisory mode.
2. Do not make instance changes.
3. Do not modify source files unless the user explicitly asks to save the report.
4. Before any external access, load and apply `${CLAUDE_PLUGIN_ROOT}/references/configuration-policy.md`. Resolve configuration, validate it, and enforce its activation and access gates. If `mode` is `disabled`, stop without searching or discovering auth profiles.
5. Search online resources relevant to the ServiceNow task only when `web_search.enabled` is `true`.
6. Rank sources by trust:
   - Tier 1: official ServiceNow docs, developer docs, support KBs, official GitHub
   - Tier 2: ServiceNow Community accepted answers/articles
   - Tier 3: practitioner blogs, partner posts, GitHub examples
   - Tier 4: Reddit, LinkedIn, YouTube, random forums
7. Use ServiceNow SDK auth profiles for read-only instance context only when `instance_readonly.enabled` is `true` and it is helpful. Otherwise do not discover profiles or contact an instance.
8. Use only GET/read operations.
9. Never deploy, update, delete, run fix scripts, execute background scripts, or modify the instance.
10. Return a cited advisory brief.

Reference material (in `${CLAUDE_PLUGIN_ROOT}/references/`):
- `configuration-policy.md` — configuration resolution, activation, and access gates
- `default-resources.json` — default source configuration
- `source-trust-policy.md` — trust tiers and required claim labels
- `task-resource-matrix.md` — what to search and check per task type
- `instance-context-matrix.md` — read-only tables to consult per task type

Output:
- Task understood
- Assumptions
- Sources checked
- Instance context checked
- Key findings
- Risks / watchouts
- Recommended next checks
- Suggested test plan
- Confidence
- What could not be verified
- Handoff to official ServiceNow SDK plugin if implementation is needed
