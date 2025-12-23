# TiDB Cloud CLI Command Patterns

Use these patterns and replace placeholders in <> with user-provided values.

## Cluster Operations (Serverless)

```bash
ticloud serverless create --display-name <cluster-name> --region <region> --project-id <project-id>
ticloud serverless list
ticloud serverless delete --cluster-id <cluster-id>
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
ticloud auth login
ticloud auth whoami
```
## SQL User Operations (Serverless)

```bash
ticloud serverless sql-user create --user <user-name> --password <password> --role <role> --cluster-id <cluster-id>
ticloud serverless sql-user list --cluster-id <cluster-id>
ticloud serverless sql-user update --user <user-name> --password <password> --role <role> --cluster-id <cluster-id>
ticloud serverless sql-user delete --user <user-name> --cluster-id <cluster-id>
```
