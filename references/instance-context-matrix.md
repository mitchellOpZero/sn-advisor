# Instance Context Matrix

Read-only instance context suggestions by task type.

## Upgrade

- `sys_upgrade_history`
- `sys_upgrade_history_log`
- `sys_update_xml`
- `sys_update_version`
- `sys_plugins`
- `sys_properties`

## UX

- `sys_properties`
- `sys_user_preference`
- `sys_ui_script`
- `sys_ui_page`
- `sys_ui_macro`
- `sys_ui_policy`
- `sys_script_client`
- portal/workspace tables when relevant and allowed

## ITSM/table process

- target task table such as `incident`, `problem`, `change_request`, `sc_request`, `sc_req_item`, `sc_task`
- `sys_dictionary`
- `sys_db_object`
- `sys_script`
- `sys_script_client`
- `sys_ui_policy`
- `sys_security_acl`
- assignment rule tables where available
- notification/SLA tables where relevant

## Catalog

- `sc_cat_item`
- `item_option_new`
- variable set tables
- catalog client script tables
- catalog UI policy tables
- flow/workflow tables where relevant

## Security

- `sys_security_acl`
- `sys_user_role`
- `sys_user_group`
- table hierarchy metadata
- user criteria tables where relevant

Do not read credential/secret tables.
