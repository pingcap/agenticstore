---
name: tidbx-setup
description: Set up the TiDB Cloud component (install ticloud CLI and authenticate). Use when the user needs to install ticloud, log in, or fix authentication/network access before running TiDB Cloud operations.
---

# TiDB Cloud Setup

Use this skill only for setup: install the ticloud CLI and authenticate the user. After setup, hand off to the TiDB Cloud CRUD skill.

## Setup Checklist

Setup Status (TiDB Cloud component)  
- ○ ticloud installed  
- ○ authenticated  

## Install CLI

For macOS/Linux:

```bash
curl https://raw.githubusercontent.com/tidbcloud/tidbcloud-cli/main/install.sh | sh
```

After install, verify:

```bash
command -v ticloud
```

Update checklist:

- ● ticloud installed

## Authenticate

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

## Network/DNS Issues

If `ticloud auth whoami` fails due to network/DNS (e.g., cannot reach `iam.tidbapi.com`):

- Explain that the environment needs network access for the CLI.
- Ask the user to enable network access for the agent environment, or run the command locally and share the output.

If setup errors persist, point the user to the official docs:

- https://docs.pingcap.com/tidbcloud/get-started-with-cli/

## Hand Off

Once setup is complete, switch to the TiDB Cloud CRUD skill.
