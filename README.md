# ServiceNow Advisor for Claude Code

Read-only ServiceNow task advisor for Claude Code.

This plugin is intended to run alongside the official ServiceNow SDK Claude Code plugin. The official SDK plugin remains responsible for implementation, Fluent/SDK code generation, builds, deploys, and SDK documentation lookups. This advisor plugin is responsible for research, risk assessment, source ranking, and read-only instance context.

## TL;DR

Use `/advisor ...` when you want a grounded advisory pass before doing ServiceNow work.

Examples:

```text
/advisor what should I look out for before changing ServiceNow user experience during an upgrade?
/advisor assess risk before changing Incident assignment rules
/advisor research docs/community and check instance context for catalog cleanup
/advisor what should we test before enabling Next Experience?
```

The advisor:

- Pulls online resources relevant to the ServiceNow task.
- Lets users configure which sources/domains are allowed.
- Ranks sources by trust.
- Uses ServiceNow SDK auth profiles for read-only instance context.
- Produces risks, watchouts, checklists, citations, and test plans.
- Makes no instance changes.
- Hands off implementation to the official ServiceNow SDK plugin.

## Relationship to the official ServiceNow SDK plugin

Both plugins can be active together.

Use this split:

| Need | Use |
|---|---|
| Research, current docs, community signals, risk assessment, best practices, upgrade readiness, troubleshooting context | `/advisor` |
| Create/edit Fluent code, build, deploy, transform, implement ServiceNow changes | Official ServiceNow SDK plugin |

Do not make the advisor trigger on every ServiceNow mention. That will fight the SDK plugin. The safest default is manual invocation through `/advisor`.

## Default operating mode

Default mode should be:

```json
{
  "mode": "manual"
}
```

Supported modes:

- `manual`: only runs when the user invokes `/advisor`.
- `advisor_first`: runs before implementation for research/risk/best-practice/upgrade/troubleshooting prompts.
- `passive`: available if referenced, but does not proactively run.
- `disabled`: installed but inactive.

Recommended MVP: `manual` only.

## Advisor-first trigger policy

If users later enable `advisor_first`, it should trigger for prompts like:

- "what should I look out for"
- "best practices"
- "research this"
- "check docs/community"
- "assess risk"
- "upgrade readiness"
- "before we implement"
- "troubleshoot with docs/community"

It should not trigger for direct implementation prompts like:

- "create a Business Rule"
- "write Fluent code"
- "deploy this app"
- "update this table"
- "generate SDK code"
- "build the package"

For those, the official ServiceNow SDK plugin should run first.

## Configurable resources

Users should be able to configure the resources the advisor can pull from.

Config lookup order:

1. Project: `.servicenow-advisor.json`
2. User: `~/.servicenow-advisor/config.json`
3. Plugin defaults: `references/default-resources.json`

Example:

```json
{
  "mode": "manual",
  "default_instance_alias": "dev",
  "web_search": {
    "enabled": true,
    "max_results_per_tier": 5,
    "include_low_confidence_sources": true,
    "require_citations": true
  },
  "sources": {
    "tier_1_official": [
      "https://www.servicenow.com/docs",
      "https://developer.servicenow.com",
      "https://servicenow.github.io/sdk",
      "https://github.com/ServiceNow",
      "https://support.servicenow.com"
    ],
    "tier_2_community": [
      "https://www.servicenow.com/community"
    ],
    "tier_3_practitioner": [
      "https://www.servicenow.com/blogs",
      "https://nowlearning.servicenow.com",
      "https://github.com"
    ],
    "tier_4_weak_signals": [
      "https://reddit.com",
      "https://stackoverflow.com",
      "https://medium.com",
      "https://linkedin.com",
      "https://youtube.com"
    ]
  },
  "blocked_domains": [],
  "preferred_domains": [
    "servicenow.com",
    "developer.servicenow.com",
    "support.servicenow.com"
  ],
  "instance_readonly": {
    "enabled": true,
    "table_access_policy": "service_now_acl_only",
    "max_records_per_query": 100,
    "http_methods_allowed": ["GET"],
    "redaction": "none"
  }
}
```

## Source trust tiers

The advisor should use all configured sources, but label confidence clearly.

1. Tier 1: official ServiceNow docs, developer docs, support KBs, release notes, official GitHub.
2. Tier 2: ServiceNow Community accepted answers/articles, ServiceNow employee/MVP posts.
3. Tier 3: practitioner blogs, partner posts, non-official GitHub examples, StackOverflow.
4. Tier 4: Reddit, LinkedIn, YouTube, random forums, unverified comments.

Output should label claims as:

- Official guidance
- Community signal
- Practitioner advice
- Weak/unverified signal
- Instance-confirmed finding

## Read-only instance context

Use ServiceNow SDK auth profiles only.

Expected behavior:

- List or use configured SDK auth profiles.
- Query instance context only when helpful for the task.
- Enforce read-only behavior.
- Use only GET/read operations.
- Read any table/field the selected ServiceNow SDK auth profile can read under ServiceNow ACLs, subject to max record limits.
- Do not apply advisor-owned table denylists or field redaction by default.
- Never deploy, update, delete, run fix scripts, execute background scripts, or modify source.

Potential helper script:

```text
scripts/sn-readonly-query.mjs
```

Guardrails:

- HTTP GET only.
- ServiceNow ACLs and the selected SDK auth profile determine what can be read.
- Any table and any readable field may be queried, subject to ACLs and max record limits.
- No advisor-maintained table denylist or field redaction by default.
- No background script execution.
- No deploy/build/update commands.

## Output template

The advisor should return:

```text
ServiceNow Advisor Brief

Task understood:

Assumptions:

Sources checked:
- Official:
- Community:
- Practitioner/other:

Instance context checked:

Key findings:

Instance-specific observations:

Risks / watchouts:

Recommended next checks:

Suggested test plan:

Confidence:

Could not verify:

Action boundary:
Read-only advisory only. No instance changes were made.

Implementation handoff:
If implementation is needed, use the official ServiceNow SDK plugin next.
```

## Proposed Claude Code plugin structure

```text
servicenow-advisor/
  .claude-plugin/
    marketplace.json
  providers/
    claude/
      plugin/
        skills/
          sn-advisor-router/
            SKILL.md
          sn-source-ranking/
            SKILL.md
          sn-instance-readonly/
            SKILL.md
          sn-output-templates/
            SKILL.md
  skills/
    sn-advisor-router/
      SKILL.md
    sn-source-ranking/
      SKILL.md
    sn-instance-readonly/
      SKILL.md
    sn-output-templates/
      SKILL.md
  commands/
    advisor.md
  references/
    default-resources.json
    source-trust-policy.md
    task-resource-matrix.md
    instance-context-matrix.md
  scripts/
    sn-readonly-query.mjs
```

## MVP build order

1. Claude Code plugin shell.
2. `/advisor` command.
3. `sn-advisor-router` skill.
4. Configurable source policy.
5. Source trust/ranking reference.
6. Instance read-only policy reference.
7. Advisory output template.
8. Optional read-only SDK helper script.

## Success criteria

The plugin is successful if it:

- Produces task-specific resources, not generic ServiceNow advice.
- Cites sources.
- Separates official docs from community/weak signals.
- Uses live instance data when an SDK auth profile is available.
- Stays read-only.
- Says what it could not verify.
- Gives practical next checks and test plans.
- Hands implementation to the official ServiceNow SDK plugin.
