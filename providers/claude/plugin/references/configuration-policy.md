# Configuration and activation policy

Apply this policy before searching the web or discovering SDK auth profiles. It
applies to both the `/sn-advisor` command and automatic skill routing.

## Resolve configuration

1. Read `${CLAUDE_PLUGIN_ROOT}/references/default-resources.json` as the baseline.
2. Use the first existing override: project `.sn-advisor.json`, then user
   `~/.sn-advisor/config.json`. Do not combine the project and user overrides.
3. Override only the fields present in that file. Merge nested objects with the
   baseline; replace arrays in full. An empty array remains empty.
4. Require both the baseline and selected override to be JSON objects, not arrays,
   strings, or `null`. If either file is unreadable, invalid JSON, or not an object,
   report the error and stop before external access. Do not silently fall back to
   a more permissive file.
5. Require a known mode, boolean enable flags, and positive integer record/result
   limits. Invalid values require correction before external access. No setting
   may authorize instance writes; allowed HTTP methods must remain `["GET"]`.

## Activation gates

Check `mode` before starting the advisory workflow:

- `disabled`: explain that the advisor is disabled and stop, even on explicit
  command invocation. Do not search or discover/connect to an instance.
- `manual`: run only when the user explicitly invokes `/sn-advisor` or the
  namespaced plugin command `/advisor:sn-advisor`.
- `advisor_first`: run for ServiceNow advisory/research/risk/troubleshooting
  requests. Direct implementation still belongs to the official SDK plugin.
- `passive`: run only when the user explicitly references SN Advisor or invokes
  `/sn-advisor` or `/advisor:sn-advisor`. Never activate proactively.

## Access gates

- If `web_search.enabled` is `false`, do not search or fetch external sources.
  Report that web research was disabled and label any unverified model knowledge.
- If `instance_readonly.enabled` is `false`, do not discover auth profiles,
  connect to an instance, or query it. Report that instance access was disabled.
- If both are disabled, work only from information already supplied by the user
  and clearly state the verification limits.
- Enforce `instance_readonly.max_records_per_query` for every query. Never use
  writes, scripts, or deployments as a fallback for unavailable read access.
- State that instance context was checked only if a read actually succeeded.
  Distinguish disabled, unavailable, failed, and successful access in the brief.
