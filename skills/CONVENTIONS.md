# Skill Conventions

This directory stores Codex skills for the AgenticStore repo.

## Layout

- `skills/` - publishable skills

Each skill lives in its own folder named after the skill.

## Naming

- Use lowercase letters, digits, and hyphens only.
- Keep names short and action-oriented (e.g., `db-postgres`, `object-storage-s3`).

## Required Files

Every skill must include:

- `SKILL.md` with YAML frontmatter containing `name` and `description`.

Optional directories:

- `scripts/` - executable helpers
- `references/` - detailed docs loaded on demand
- `assets/` - templates or files used in outputs

## Creation Workflow

Prefer the `init_skill.py` helper to scaffold new skills:

```bash
scripts/init_skill.py <skill-name> --path skills --resources scripts,references,assets
```

Package when ready:

```bash
scripts/package_skill.py <path/to/skill-folder>
```

## Style

- Keep `SKILL.md` concise and action-oriented.
- Move deep reference material into `references/`.
- Avoid extra docs inside skill folders (no README or changelog).
