# SN Advisor by OperatorZero

Read-only ServiceNow task advisor for Claude Code.

`/advisor` researches a ServiceNow task across official docs, support KBs, and community sources, ranks every source by trust, optionally checks **read-only** instance context through your ServiceNow SDK auth profiles, and returns a cited advisory brief: key findings, risks and watchouts, recommended next checks, and a test plan. It never changes your instance.

It is designed to run alongside the official ServiceNow SDK plugin for Claude Code: SN Advisor handles research, risk assessment, and grounding; the official SDK plugin handles implementation, Fluent/SDK code generation, builds, and deploys.

## Install

```bash
claude plugin marketplace add mitchellOpZero/sn-advisor
claude plugin install advisor@sn-advisor
```

Restart your Claude Code session and `/advisor` is available.

## Use

```text
/advisor what should I look out for before changing ServiceNow user experience during an upgrade?
/advisor assess risk before changing Incident assignment rules
/advisor research docs/community and check instance context for catalog cleanup
/advisor what should we test before enabling Next Experience?
```

Every brief includes:

- Task understood and assumptions
- Sources checked, separated by trust tier
- Read-only instance context checked (when an SDK auth profile is available)
- Key findings and instance-specific observations
- Risks / watchouts
- Recommended next checks and a suggested test plan
- Confidence, and what could not be verified
- An implementation handoff to the official ServiceNow SDK plugin when changes are needed

## Source trust tiers

The advisor uses all configured sources but labels confidence clearly:

1. **Tier 1 — Official**: ServiceNow docs, developer docs, support KBs, release notes, official GitHub.
2. **Tier 2 — Community**: ServiceNow Community accepted answers/articles, ServiceNow employee/MVP posts.
3. **Tier 3 — Practitioner**: practitioner blogs, partner posts, non-official GitHub examples, StackOverflow.
4. **Tier 4 — Weak signals**: Reddit, LinkedIn, YouTube, unverified forums.

Claims are labeled as official guidance, community signal, practitioner advice, weak/unverified signal, or instance-confirmed finding. See [source-trust-policy.md](providers/claude/plugin/references/source-trust-policy.md).

## Read-only instance context

When useful, the advisor reads live instance context through your existing **ServiceNow SDK auth profiles** (`npx @servicenow/sdk auth --list`). Guardrails:

- HTTP GET only — no POST/PUT/PATCH/DELETE, no deploys, no fix or background scripts.
- ServiceNow ACLs and the selected auth profile are the access boundary; the advisor adds no credentials of its own.
- Record limits are enforced (default 100 per query).

If no profile is available, the advisor says what it could not verify and continues with online sources only.

## Configuration

Config lookup order:

1. Project: `.sn-advisor.json`
2. User: `~/.sn-advisor/config.json`
3. Plugin defaults: [default-resources.json](providers/claude/plugin/references/default-resources.json)

See [examples/sn-advisor.config.example.json](examples/sn-advisor.config.example.json) for the full shape — allowed source tiers, blocked/preferred domains, web search options, instance read-only limits, and the operating mode:

- `manual` (default, recommended): runs only on `/advisor`.
- `advisor_first`: runs before implementation for research/risk/upgrade/troubleshooting prompts.
- `passive`: available if referenced, never proactive.
- `disabled`: installed but inactive.

## Relationship to the official ServiceNow SDK plugin

Both plugins can be active together. Use this split:

| Need | Use |
|---|---|
| Research, current docs, community signals, risk assessment, best practices, upgrade readiness, troubleshooting context | `/advisor` |
| Create/edit Fluent code, build, deploy, transform, implement ServiceNow changes | Official ServiceNow SDK plugin |

The advisor does not trigger on every ServiceNow mention; manual invocation through `/advisor` is the default.

## Repository layout

```text
.claude-plugin/marketplace.json        # marketplace: sn-advisor
providers/claude/plugin/               # the installable Claude Code plugin
  .claude-plugin/plugin.json
  commands/advisor.md                  # /advisor
  skills/                              # router, source ranking, read-only instance, output templates
  references/                          # default sources, trust policy, task & instance matrices
examples/sn-advisor.config.example.json
```

## License

MIT © OperatorZero. Not affiliated with or endorsed by ServiceNow, Inc. ServiceNow is a trademark of ServiceNow, Inc.; it is used here only to describe compatibility.
