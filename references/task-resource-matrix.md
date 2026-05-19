# Task Resource Matrix

Map a ServiceNow task to web resources and instance context.

## General platform upgrade

Search:
- ServiceNow upgrade planning checklist
- ServiceNow upgrade tools and resources
- ServiceNow Upgrade Center
- ServiceNow Upgrade Console
- target release notes
- known issues for target release

Instance context:
- upgrade history
- skipped updates
- active plugins
- relevant system properties
- modified OOB records if safely visible

## UX / UI15 / UI16 / Next Experience / Workspace

Search:
- ServiceNow UI15 UI16 docs
- Next Experience docs
- target release UX known issues
- community posts on UI migration
- support KBs for UI preferences and UI switching

Instance context:
- UI system properties
- user preferences
- themes/branding
- workspaces
- portals
- UI scripts/macros/pages
- client scripts and UI policies

## ITSM process change

Search:
- product docs for Incident/Problem/Change/Request
- assignment rule best practices
- Flow Designer/workflow guidance
- community troubleshooting posts

Instance context:
- target table dictionary
- business rules
- client scripts
- UI policies
- ACLs
- assignment rules
- flows/workflows
- notifications
- SLAs

## Catalog / Request

Search:
- Service Catalog docs
- Employee Center / Service Portal docs if relevant
- Flow Designer approvals docs
- community posts for catalog item gotchas

Instance context:
- catalog item
- variables
- variable sets
- catalog client scripts
- catalog UI policies
- flows/workflows
- approvals
- portals

## Access / security

Search:
- ACL docs
- role/group docs
- ServiceNow security best practices
- GlideRecordSecure guidance if scripting involved

Instance context:
- ACLs
- roles/groups metadata
- table hierarchy
- user criteria
- before-query business rules

## Integrations / MID Server

Search:
- REST/SOAP docs
- IntegrationHub docs
- MID Server docs
- target release integration known issues

Instance context:
- REST messages metadata
- scripted REST APIs
- MID Server status/config
- scheduled imports
- transform maps
- recent integration error logs if safely accessible

## SDK / Fluent source task

Search:
- ServiceNow SDK docs
- `npx @servicenow/sdk explain --list --format=raw`
- relevant SDK explain topics
- ServiceNow/sdk-examples

Instance context:
- app scope
- table dictionary
- existing metadata if safely accessible

Handoff:
- official ServiceNow SDK plugin should implement changes.
