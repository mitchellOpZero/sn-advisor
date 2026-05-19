---
name: sn-output-templates
description: Output templates for ServiceNow advisor briefs, risk reviews, test plans, and SDK handoffs.
---

# ServiceNow Advisor Output Templates

## Standard advisory brief

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

## Finding format

```text
Finding:
Severity:
Evidence:
Why it matters:
Recommended check:
Source tier:
Confidence:
```

## Handoff format

```text
Implementation handoff to official ServiceNow SDK plugin:
- Task:
- Relevant artifact types:
- Instance findings to consider:
- Recommended SDK explain topics:
- Tests/checks to run after implementation:
```
