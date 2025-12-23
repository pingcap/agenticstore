#!/usr/bin/env python3
import argparse
import json
import os
import secrets
import string
import subprocess
import sys
from pathlib import Path


def generate_password(length: int = 16) -> str:
    alphabet = string.ascii_letters + string.digits + "!@#%^_+=-"
    return "".join(secrets.choice(alphabet) for _ in range(length))


def load_env(path: str) -> dict[str, str]:
    data: dict[str, str] = {}
    if not os.path.exists(path):
        return data
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            data[key] = value
    return data


def save_env(path: str, data: dict[str, str]) -> None:
    non_tidb = {k: v for k, v in data.items() if not k.startswith("TIDB_")}
    tidb = {k: v for k, v in data.items() if k.startswith("TIDB_")}

    lines: list[str] = []
    for key in sorted(non_tidb.keys()):
        lines.append(f"{key}={non_tidb[key]}")

    if tidb:
        lines.append("# TiDB connection settings")
        ordered_keys = [
            "TIDB_CLUSTER_ID",
            "TIDB_HOST",
            "TIDB_PORT",
            "TIDB_USERNAME",
            "TIDB_PASSWORD",
            "TIDB_DATABASE",
        ]
        for key in ordered_keys:
            if key in tidb:
                lines.append(f"{key}={tidb[key]}")
        for key in sorted(tidb.keys()):
            if key not in ordered_keys:
                lines.append(f"{key}={tidb[key]}")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def fetch_cluster_endpoints(cluster_id: str) -> tuple[str, str]:
    result = subprocess.run(
        ["ticloud", "serverless", "describe", "-c", cluster_id],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(result.stdout)
    public = data.get("endpoints", {}).get("public", {})
    host = public.get("host", "")
    port = str(public.get("port", ""))
    return host, port


def update_env(
    env_file: str,
    cluster_id: str,
    host: str,
    port: str,
    user: str,
    password: str,
    database: str | None,
) -> None:
    env_data = load_env(env_file)
    env_data.update(
        {
            "TIDB_CLUSTER_ID": cluster_id,
            "TIDB_HOST": host,
            "TIDB_PORT": port,
            "TIDB_USERNAME": user,
            "TIDB_PASSWORD": password,
        }
    )
    if database:
        env_data["TIDB_DATABASE"] = database
    save_env(env_file, env_data)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage TiDB Cloud SQL users and update .env.")
    parser.add_argument(
        "--env-file",
        default=str(Path.cwd() / ".env"),
        help="Path to .env file (defaults to .env in current directory).",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create", help="Create a SQL user.")
    create_parser.add_argument("--cluster-id", required=True, help="TiDB Cloud cluster ID.")
    create_parser.add_argument("--user", required=True, help="SQL username (accepts full name with prefix).")
    create_parser.add_argument(
        "--role",
        required=True,
        choices=["role_admin", "role_readwrite", "role_readonly"],
        help="SQL user role.",
    )
    create_parser.add_argument("--database", required=True, help="Database name for TIDB_DATABASE.")
    create_parser.add_argument(
        "--password",
        default=os.environ.get("TIDB_SQL_PASSWORD"),
        help="SQL user password (optional).",
    )

    update_parser = subparsers.add_parser("update", help="Update a SQL user password/role.")
    update_parser.add_argument("--cluster-id", required=True, help="TiDB Cloud cluster ID.")
    update_parser.add_argument("--user", required=True, help="SQL username (accepts full name with prefix).")
    update_parser.add_argument(
        "--role",
        required=True,
        choices=["role_admin", "role_readwrite", "role_readonly"],
        help="SQL user role.",
    )
    update_parser.add_argument("--database", help="Database name for TIDB_DATABASE.")
    update_parser.add_argument(
        "--password",
        default=os.environ.get("TIDB_SQL_PASSWORD"),
        help="New SQL user password (optional).",
    )

    return parser


def cmd_create(args: argparse.Namespace) -> None:
    password = args.password or generate_password(16)
    host, port = fetch_cluster_endpoints(args.cluster_id)

    result = subprocess.run(
        [
            "ticloud",
            "serverless",
            "sql-user",
            "create",
            "--user",
            args.user,
            "--password",
            password,
            "--role",
            args.role,
            "--cluster-id",
            args.cluster_id,
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    if result.stdout:
        print(result.stdout.rstrip())
    if result.stderr:
        print(result.stderr.rstrip(), file=sys.stderr)

    update_env(args.env_file, args.cluster_id, host, port, args.user, password, args.database)
    print(f"Saved connection settings to {args.env_file}.")


def cmd_update(args: argparse.Namespace) -> None:
    password = args.password or generate_password(16)
    host, port = fetch_cluster_endpoints(args.cluster_id)

    result = subprocess.run(
        [
            "ticloud",
            "serverless",
            "sql-user",
            "update",
            "--user",
            args.user,
            "--password",
            password,
            "--role",
            args.role,
            "--cluster-id",
            args.cluster_id,
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    if result.stdout:
        print(result.stdout.rstrip())
    if result.stderr:
        print(result.stderr.rstrip(), file=sys.stderr)

    update_env(args.env_file, args.cluster_id, host, port, args.user, password, args.database)
    print(f"Saved connection settings to {args.env_file}.")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "create":
        cmd_create(args)
    elif args.command == "update":
        cmd_update(args)
    else:
        parser.error("Unknown command")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
