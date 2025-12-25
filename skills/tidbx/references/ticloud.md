# TiDB Cloud CLI Command Patterns

Use these patterns and replace placeholders in <> with user-provided values.

## Cluster Operations (Serverless)

```bash
ticloud serverless create --display-name <cluster-name> --region <region> --project-id <project-id>
ticloud serverless list
ticloud serverless list -p <project-id>
ticloud serverless list -p <project-id> -o json
ticloud serverless describe
ticloud serverless describe -c <cluster-id>
ticloud serverless delete
ticloud serverless delete -c <cluster-id>
```

## Branch Operations (Serverless)

```bash
ticloud serverless branch create --cluster-id <cluster-id> --name <branch-name>
ticloud serverless branch list --cluster-id <cluster-id>
ticloud serverless branch delete --cluster-id <cluster-id> --branch-id <branch-id>
```

## Import / Export (Serverless)

```bash
ticloud serverless import start --cluster-id <cluster-id> --local.file-path <file-path> --file-type <file-type> --local.target-database <database> --local.target-table <table>
ticloud serverless export create --cluster-id <cluster-id> --target-type <target-type>
```

## Supporting Commands

```bash
ticloud serverless region
ticloud project list
ticloud auth login
ticloud auth whoami
```
## SQL User Operations (Serverless)

```bash
ticloud serverless sql-user list --cluster-id <cluster-id>
ticloud serverless sql-user update --user <user-name> --password <password> --role <role> --cluster-id <cluster-id>
ticloud serverless sql-user delete --user <user-name> --cluster-id <cluster-id>
```

Create a SQL user

Usage:
  ticloud serverless sql-user create [flags]

Examples:
  Create a SQL user in interactive mode:
  $ ticloud serverless sql-user create

  Create a SQL user in non-interactive mode:
  $ ticloud serverless sql-user create --user <user-name> --password <password> --role <role> --cluster-id <cluster-id>

Flags:
  -c, --cluster-id string   The ID of the cluster.
  -h, --help                help for create
      --password string     The password of the SQL user.
      --role strings        The role(s) of the SQL user, supported roles ["role_admin" "role_readwrite" "role_readonly"]
  -u, --user string         The name of the SQL user, user prefix will be added automatically.

Global Flags:
  -D, --debug            Enable debug mode
      --no-color         Disable color output
  -P, --profile string   Profile to use from your configuration file
