---
name: sn-advisor-router
description: Use only for ServiceNow read-only advisory/research tasks, especially when the user explicitly invokes /advisor or asks for current online resources, best practices, risk assessment, upgrade readiness, troubleshooting context, or says “what should I look out for.” Do not use for direct implementation/code/deploy tasks; let the official ServiceNow SDK plugin handle those.
---

# SN Advisor Router

This skill routes ServiceNow advisory work. It is intentionally narrow so it can coexist with the official ServiceNow SDK plugin.

## Use this skill when

- The user explicitly invokes `/sn-advisor`.
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
3. Load configured source policy.
4. Search relevant online resources.
5. Rank sources by trust.
6. Pull read-only instance context through ServiceNow SDK auth profiles when useful.
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
