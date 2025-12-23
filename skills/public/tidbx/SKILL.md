---
name: tidbx
description: Manage TiDB Cloud resources via the ticloud CLI. Use when creating, deleting, or listing TiDB Cloud clusters/branches, managing SQL users, or importing/exporting data via ticloud.
---

# TiDB Cloud CLI

Use the ticloud CLI to manage TiDB Cloud Serverless clusters and branches, and to import/export data. Follow the workflows below and use the exact command patterns in the references file.

## Prerequisite

The TiDB Cloud component setup (CLI install + auth) is required before any cluster/branch/data operations. This skill assumes setup is already complete.

## Table Formatting

Use the `data-table-formatter` skill for any table output (regions, projects, clusters, SQL users).

## Auth Gate + Network Issues

- Always run `ticloud auth whoami` before any action.
- If not logged in, point the user to the TiDB Cloud setup skill and stop (do not attempt setup here).
- If auth fails due to network/DNS errors (e.g., cannot reach `iam.tidbapi.com`), tell the user:
  - The environment needs network access for the CLI to reach TiDB Cloud.
  - They must enable network access in their agent environment or run the command locally and share the output.

## Core Workflows

### Create a Cluster

- Do not present a setup checklist for cluster creation steps (region/project/cluster name). If a status is needed, label it as "Create Flow" rather than "Setup Status."
- Run `ticloud serverless region` and present the full list in a terminal-friendly bordered table (fixed-width columns in a code block) with selectable option numbers before asking for a region.
- If the user doesn’t know the project ID, run `ticloud project list` and present the results in the same bordered table format before asking. Keep the project ID as a third column.
- Ask in this order: region (after listing options), project ID (after listing projects if needed), then cluster display name as the final confirmation step.
- Confirm the required parameters (region, project, cluster name).
- Use the serverless create command pattern from `references/ticloud.md`.
- When creating a cluster, wait 60 seconds for completion before returning control.
- Verify creation by listing clusters and present results in a bordered table rather than raw JSON. If the environment is non-interactive, use `ticloud serverless list -p <project-id> -o json` and render a table from the JSON.

### Delete a Cluster

- Require explicit user confirmation before delete operations.
- Use the serverless delete command pattern from `references/ticloud.md`.
- List clusters to confirm removal and present results in a bordered table rather than raw JSON. If the environment is non-interactive, use `ticloud serverless list -p <project-id> -o json` and render a table from the JSON.

### List Clusters

- If the user doesn’t know the available projects, list projects first, then ask which project to use.
- Ask which project the user wants to list before running `ticloud serverless list`.
- If the user doesn’t know the project ID, run `ticloud project list` and present results in the bordered table format.
- For non-interactive environments, use `ticloud serverless list -p <project-id> -o json` and render a table from the JSON.

### Create or Delete a Branch

- Confirm the target cluster and branch name.
- Use the branch commands from `references/ticloud.md`.
- List branches to verify changes.

### Import or Export Data

- Confirm source/target, file format, and target database/schema.
- Use the serverless import/export commands from `references/ticloud.md`.
- Verify completion in CLI output or by listing relevant resources.

### Manage SQL Users

- Use serverless SQL user commands from `references/ticloud.md`.
- Prefer generating the command for the user rather than executing it, unless the user explicitly asks you to run it.
- For password handling and execution, use `scripts/sql_user_manage.py` to generate a strong password, fetch host/port, create/update the SQL user, and update connection vars in `.env`.
- Never read or display stored passwords (do not cat `.env`).
- When listing SQL users, present results in a bordered table rather than raw JSON.
- Default to `role_readwrite` unless the user requests a different role.
- For SQL usernames, accept the exact value the user provides (including prefixed names like `2Q3h2gvr6xKRBhn.killer`).
- For password refresh, `--database` is optional; do not require it when updating a user.
- When creating or updating SQL users, wait 60 seconds for completion before returning control.

## Safety Checks

- Always run `ticloud auth whoami` before any action.
- Require explicit user confirmation before delete operations.
- For `ticloud` operations that take time, wait 60 seconds before returning control.

## References

- Command patterns and placeholders: `references/ticloud.md`
