<p align="center">
  <img src="public/logo.svg" alt="AgenticStack logo" width="120" height="120" />
</p>

# AgenticStack

AgenticStack is a repo for designing and curating SKILLS for code agents. It focuses on storage- and database-related capabilities for agentic apps, such as database provisioning, object storage access, and data lifecycle workflows. Components are added incrementally and documented as the stack grows.

## Goals

- Provide reusable SKILLS for storage and database building blocks
- Offer opinionated, composable storage/database workflows for AI app builders
- Keep guidance practical, concise, and easy to apply in real projects

## Scope (Planned Components)

- Database (SQL/NoSQL selection, provisioning, migration flows, ORM patterns)
- Object storage (providers, upload flows, access control)
- Data lifecycle (backup/restore, retention, export/import)

## Structure (Suggested)

This repo starts empty and grows over time. A typical layout will look like:

- `skills/` - skill definitions and instructions
- `references/` - deeper docs used by skills

## How to Use

- Browse the `skills/` directory for capability-specific instructions.
- Use skills to provision or manage storage/database resources.

## Contributing

Contributions are welcome. If you add a new component, include:

- A short rationale
- Clear prerequisites
- Step-by-step usage
- Known trade-offs

## Roadmap

- Add more database provisioning skills (managed SQL/NoSQL)
- Add object storage skills (S3-compatible and cloud-specific)
- Add data lifecycle skills (backup/restore, export/import)
