---
name: tidbx
description: Provision TiDB Cloud Serverless clusters and related resources. Use when creating, deleting, or listing clusters/branches, or managing SQL users.
---

# TiDB Cloud Provisioning (TiDB X)

Provision TiDB Cloud Serverless (now branded as TiDB X) clusters and related resources using the workflows below. Use the command patterns in the references file as implementation details, but keep the focus on the provisioning outcome and required inputs.

Note: TiDB Cloud Serverless has been renamed to TiDB X. Keep both terms in user-facing guidance for clarity.
Note: Many users say "instance" when they mean "cluster." Treat "instance" as a synonym for "cluster."

Reminder: This skill provides TiDB Cloud cluster CRUD operations (Create, Read/list, Update, Delete). Before any CRUD action, ensure the user completes ticloud setup and authentication (see Provisioning Setup below).

## Provisioning Setup

Complete setup before any provisioning or lifecycle operations.

Setup Status (TiDB Cloud component)  
- ○ ticloud installed  
- ○ authenticated  

When verifying setup, remind users to follow this order: install → login → verify with `ticloud auth whoami`.
Use the checklist to show users what they should do next and where they are in the setup flow.

Checklist template (update after each check, and reflect command results):

```
Setup Status (TiDB Cloud component)
- ○ ticloud installed
- ○ authenticated
```

After `command -v ticloud` succeeds, mark install complete:

```
Setup Status (TiDB Cloud component)
- ● ticloud installed
- ○ authenticated
```

After `ticloud auth whoami` succeeds, mark auth complete:

```
Setup Status (TiDB Cloud component)
- ● ticloud installed
- ● authenticated
```

### Install CLI

For macOS/Linux:

```bash
curl https://raw.githubusercontent.com/tidbcloud/tidbcloud-cli/main/install.sh | sh
```

After install, verify:

```bash
command -v ticloud
```

Use `command -v ticloud` to confirm installation before marking it complete.

Update checklist:

- ● ticloud installed

### Authenticate

Always check auth first:

```bash
ticloud auth whoami
```

If not logged in, run:

```bash
ticloud auth login --insecure-storage
```

Wait for the user to complete the browser flow, then re-check:

```bash
ticloud auth whoami
```

Update checklist:

- ● authenticated

### Network/DNS Issues

If `ticloud auth whoami` fails due to network/DNS (e.g., cannot reach `iam.tidbapi.com`):

- Explain that the environment needs network access for the CLI.
- Ask the user to enable network access for the agent environment, or run the command locally and share the output.

If setup errors persist, point the user to the official docs:

- https://docs.pingcap.com/tidbcloud/get-started-with-cli/

## Table Formatting (ASCII)

Use terminal-friendly ASCII tables for any list output (regions, projects, clusters, SQL users).

- Use ASCII borders with `+`, `-`, and `|`.
- Use fixed-width columns; left-align all text.
- Refine the table formatting so columns align cleanly and remain readable.
- Keep headers short and descriptive.
- Do not use Unicode box-drawing characters.
- Always emphasize command output that users should execute later.

Example format:

```
+----------------+-----------------------+---------------------------+--------+
| Display Name   | Cluster ID            | Region                    | State  |
+----------------+-----------------------+---------------------------+--------+
| test-skill     | 10913591479486949552  | alicloud-ap-southeast-1   | ACTIVE |
+----------------+-----------------------+---------------------------+--------+
```

## Auth Gate + Network Issues

- Always run `ticloud auth whoami` before any action.
- If not logged in, complete the setup steps in this document before proceeding.
- If auth fails due to network/DNS errors (e.g., cannot reach `iam.tidbapi.com`), tell the user:
  - The environment needs network access for the CLI to reach TiDB Cloud.
  - They must enable network access in their agent environment or run the command locally and share the output.

## Core Workflows

### Create a Cluster

- Do not present a setup checklist for cluster creation steps (region/project/cluster name). If a status is needed, label it as "Create Flow" rather than "Setup Status."
- Run `ticloud serverless region` and present the full list in a terminal-friendly ASCII bordered table (fixed-width columns in a code block) with selectable option numbers before asking for a region.
- If the user doesn’t know the project ID, run `ticloud project list` and present the results in the same ASCII bordered table format before asking. Keep the project ID as a third column.
- Ask in this order: region (after listing options). Do not ask for project ID or cluster name until the region is chosen. After region selection, ask for project ID (after listing projects if needed). Only after project selection, ask for the cluster display name as the final confirmation step.
- Confirm the required parameters (region, project, cluster name).
- This action can also save or update database connection strings in `.env` when the user requests it.
- Use the serverless create command pattern from `references/ticloud.md`.
- When creating a cluster, do not run the create command twice. Wait up to 60 seconds for completion before returning control.
- Verify creation by listing clusters and present results in an ASCII bordered table rather than raw JSON. If the environment is non-interactive, use `ticloud serverless list -p <project-id> -o json` and render a table from the JSON.

### Delete a Cluster

- Require explicit user confirmation before delete operations.
- Use the serverless delete command pattern from `references/ticloud.md`.
- After deletion, list the remaining clusters and present results in an ASCII bordered table rather than raw JSON. If the environment is non-interactive, use `ticloud serverless list -p <project-id> -o json` and render a table from the JSON.

### List Clusters

- If the user doesn’t know the available projects, list projects first, then ask which project to use.
- Ask which project the user wants to list before running `ticloud serverless list`.
- If the user doesn’t know the project ID, run `ticloud project list` and present results in the ASCII bordered table format.
- For non-interactive environments, use `ticloud serverless list -p <project-id> -o json` and render a table from the JSON.

### Describe a Cluster

- Confirm the target cluster (name or cluster ID).
- Use `ticloud serverless list -p <project-id> -o json` and filter by cluster ID or display name.
- Present details in a two-column ASCII table (Field, Value) with refined alignment.

### Create or Delete a Branch

- Confirm the target cluster and branch name.
- Use the branch commands from `references/ticloud.md`.
- List branches to verify changes.

### List Branches

- Follow the hierarchy: project → cluster → branch.
- If the user doesn’t know the available projects, list projects first.
- If the user doesn’t know the project ID, run `ticloud project list` and present results in the ASCII bordered table format.
- If the user doesn’t know the cluster ID, list clusters for the selected project and present results in the ASCII bordered table format.
- Ask which cluster the user wants to list before running `ticloud serverless branch list`.
- For non-interactive environments, use `ticloud serverless branch list --cluster-id <cluster-id> -o json` and render a table from the JSON.

### Manage SQL Users

- Use serverless SQL user commands from `references/ticloud.md`.
- Prefer generating the command for the user rather than executing it, unless the user explicitly asks you to run it.
- Do not generate passwords in scripts. Guide users to create/manage SQL users in the TiDB Cloud console and download the `.env` there.
- Use this console URL pattern (fill in IDs): `https://tidbcloud.com/clusters/<cluster-id>/overview?orgId=<org-id>&projectId=<project-id>`.
- Never read or display stored passwords (do not cat `.env`).
- When listing SQL users, present results in an ASCII bordered table rather than raw JSON.
- Default to `role_readwrite` unless the user requests a different role. When prompting, explicitly state that `role_readwrite` is the default.
- For SQL usernames, accept the exact value the user provides (including prefixed names like `2Q3h2gvr6xKRBhn.killer`).
- For password refresh, `--database` is optional; do not require it when updating a user.
- When creating or updating SQL users, wait 60 seconds for completion before returning control.
- When creating a SQL user, use a checklist and ask for these inputs one by one: username → database → role. When asking for role, list all available options first.
- Before executing SQL user create/update, print all collected inputs (cluster ID, username, database, role, env file) and ask for explicit approval to run the command.
- Use this exact approval summary format (add cluster name if known):
  - Cluster name: `<cluster-name>`
  - Cluster ID: `<cluster-id>`
  - Username: `<user>`
  - Database: `<database>`
  - Role: `<role>`
  - Env file: `<env-file>`


## Safety Checks

- Always run `ticloud auth whoami` before any action.
- Require explicit user confirmation before delete operations.
- For `ticloud` operations that take time, wait 60 seconds before returning control.

## References

- Command patterns and placeholders: `references/ticloud.md`
