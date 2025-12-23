# AgenticStack

AgenticStack is a repo for designing and curating SKILLS for code agents. It focuses on full-stack app-builder AI agent stacks, including databases, object storage, runtimes, authentication services, API design patterns, and codebase hosting. Components are added incrementally and documented as the stack grows.

## Goals

- Provide reusable SKILLS for common full-stack building blocks
- Offer opinionated, composable tech stacks for AI app builders
- Keep guidance practical, concise, and easy to apply in real projects

## Scope (Planned Components)

- Database (SQL/NoSQL selection, migration flows, ORM patterns)
- Object storage (providers, upload flows, access control)
- Runtime (server runtime, job/queue, edge functions where applicable)
- Authentication (service selection, session/token strategy)
- API design (REST/GraphQL conventions, versioning, error patterns)
- Codebase hosting (repo layout, CI/CD, deployment handoff)

## Structure (Suggested)

This repo starts empty and grows over time. A typical layout will look like:

- `skills/` - skill definitions and instructions
- `stacks/` - curated stack blueprints
- `templates/` - starter code or reference templates
- `examples/` - sample apps that use the stacks

## How to Use

- Browse the `skills/` directory for capability-specific instructions.
- Combine skills into a stack from `stacks/`.
- Use `templates/` and `examples/` to scaffold new projects.

## Contributing

Contributions are welcome. If you add a new component, include:

- A short rationale
- Clear prerequisites
- Step-by-step usage
- Known trade-offs

## Roadmap

- Add database skill and stack
- Add object storage skill and stack
- Add runtime and auth stack
- Add API design conventions
- Add codebase hosting guidelines

