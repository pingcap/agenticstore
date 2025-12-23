---
name: data-table-formatter
description: Format structured data into clean terminal-friendly ASCII tables. Use when you need readable tables for CLI outputs or when presenting lists of resources without raw JSON.
---

# Data Table Formatter

Format structured data into readable, terminal-friendly ASCII tables.

## When to Use

Use this skill to render lists of up to 50 rows from CLI outputs into plain-text tables.

## Table Style

- Use ASCII borders with `+`, `-`, and `|`.
- Use fixed-width columns; left-align all text.
- Column widths must be at least 2 spaces wider than the longest value in that column.
- Keep headers short and descriptive.
- Do not use Unicode box-drawing characters.

## Workflow

1. Identify columns and extract values.
2. Compute max width per column (including header).
3. Add 2 spaces of padding to each max width.
4. Render header row and separator.
5. Render data rows.

## Example

Input rows:

- displayName, clusterId, regionId, state

Output format:

```
+----------------+-----------------------+---------------------------+--------+
| Display Name   | Cluster ID            | Region                    | State  |
+----------------+-----------------------+---------------------------+--------+
| test-skill     | 10913591479486949552  | alicloud-ap-southeast-1   | ACTIVE |
+----------------+-----------------------+---------------------------+--------+
```
