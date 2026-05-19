---
name: sn-instance-readonly
description: Use ServiceNow SDK auth profiles for read-only instance context. Never write to the instance.
---

# ServiceNow Instance Read-Only Context

Use this skill when advisor output would be materially improved by checking live instance context.

## Access model

Use ServiceNow SDK auth profiles only.

Expected profile discovery:

```bash
npx @servicenow/sdk auth --list
```

Use the configured default alias if present. Otherwise ask the user which alias to use. The selected profile's ServiceNow ACLs are the access boundary.

## Hard guardrails

- GET/read only.
- No POST, PUT, PATCH, DELETE.
- No deploy.
- No build/publish side effects.
- No fix scripts.
- No background scripts.
- ServiceNow ACLs and the selected SDK auth profile determine what can be read.
- Any table and any readable field may be queried when useful for the task.
- Do not maintain an advisor-owned table denylist by default.
- Do not redact field values by default; trust ServiceNow ACLs and the selected profile.
- Respect max record limits.

## Useful context by task

Upgrade:
- instance version/build
- active plugins
- upgrade history
- skipped updates
- relevant system properties
- modified OOB records where safely visible

UX:
- UI-related system properties
- user preferences for UI15/UI16/Next Experience
- active themes/branding
- homepages/dashboards
- workspaces
- portals
- UI scripts, UI macros, UI pages
- client scripts and UI policies

ITSM/table process:
- table dictionary
- business rules
- client scripts
- UI policies
- ACLs
- assignment rules
- flows/workflows
- notifications
- SLAs

Catalog:
- catalog item
- variables and variable sets
- catalog client scripts
- catalog UI policies
- flows/workflows
- approvals
- portals where exposed

Security:
- ACLs
- roles/groups metadata
- table hierarchy
- before-query business rules
- user criteria

Integrations:
- REST messages metadata
- scripted REST APIs
- MID Server status/config
- scheduled imports
- transform maps

## Output language

Always state:

"Read-only instance context checked. No instance changes were made."

If instance access is unavailable, state what could not be verified and continue using online sources.
