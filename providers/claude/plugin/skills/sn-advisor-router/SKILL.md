---
name: sn-advisor-router
description: Route ServiceNow read-only advisory/research tasks subject to the configured activation mode. In the default manual mode, run only when the user explicitly invokes /sn-advisor or /advisor:sn-advisor. Do not use for direct implementation/code/deploy tasks; let the official ServiceNow SDK plugin handle those.
---

# SN Advisor Router

This skill routes ServiceNow advisory work. It is intentionally narrow so it can coexist with the official ServiceNow SDK plugin.

## Use this skill when

First load `${CLAUDE_PLUGIN_ROOT}/references/configuration-policy.md`, resolve
configuration, and enforce its activation and access gates. The task types below
are eligible only when the configured mode permits activation. In `manual` mode,
only explicit `/sn-advisor` or `/advisor:sn-advisor` invocation qualifies; in
`disabled` mode, stop.

- The user explicitly invokes `/sn-advisor` or `/advisor:sn-advisor`.
- The user asks for ServiceNow research.
- The user asks for current docs/community/support signals.
- The user asks for best practices.
- The user asks what to look out for.
- The user asks for risk assessment.
- The user asks for upgrade readiness.
- The user asks for troubleshooting context before action.

## Do not use this skill when

- The user asks to create, edit, build, deploy, or implement ServiceNow code.
- The user asks to write Fluent SDK artifacts.
- The user asks to transform or deploy an app.
- The user asks for direct source changes.

For implementation, defer to the official ServiceNow SDK plugin.

## Workflow

1. Restate the task.
2. Classify the ServiceNow domain:
   - platform upgrade / release readiness
   - UX / Next Experience / UI15 / UI16 / Workspace / UI Builder
   - Service Portal / Employee Center
   - ITSM process
   - catalog / request / variables
   - Flow Designer / workflow / approvals
   - ACL / role / group / security
   - CMDB / Discovery / Service Mapping
   - integration / MID Server
   - data import / transform maps
   - notifications / events
   - SLAs / schedules
   - knowledge
   - reporting / PA
   - performance / technical debt
   - Instance Scan / HealthScan-style review
   - SDK/source-code task
   - debugging / troubleshooting
3. Load configured source policy, preserving the activation and access gates checked above.
4. Search relevant online resources only when `web_search.enabled` is `true`.
5. Rank sources by trust.
6. Pull read-only instance context through ServiceNow SDK auth profiles only when `instance_readonly.enabled` is `true` and it is useful. When disabled, do not discover profiles or contact an instance.
7. Produce the advisory brief.
8. State explicitly that no changes were made.
9. If implementation is requested next, hand off to the official ServiceNow SDK plugin.

## Output contract

Return:

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
- Implementation handoff
