# Architecture and build order

Use after discovery or for an existing project's architectural question. Inspect existing conventions before suggesting new ones. Focus on responsibilities, data flow, and tradeoffs; folders alone are not architecture.

## Make the stack decision

Determine whether the user wants to practice a chosen stack or wants a recommendation. Respect that preference. Compare the recommended option with at most one or two meaningful alternatives against actual constraints: learning effort, data consistency, platform, hosting, team experience, operating cost, and required capabilities.

For each chosen technology, state its job, why it fits, the main drawback, and what evidence would justify replacing or extending it. Verify current compatibility and support status from official documentation when needed. No default requirement for MERN, microservices, containers, queues, caching, or AI frameworks.

## Produce the blueprint

Use [the architecture template](../assets/templates/architecture.md). Cover each relevant layer and mark absent ones not applicable with a reason:

1. **System map:** actors, interfaces, application processes, storage, external services, trust boundaries, and one important request/data flow.
2. **Client:** navigation, feature boundaries, component ownership, local vs server state, form validation, loading/empty/error states, accessibility, and rendering/offline needs.
3. **Application:** business rules, transport boundaries, validation, identity, permissions, errors, and external integrations. For APIs, describe important operations, inputs/outputs, permission rules, and failure behavior; avoid a premature exhaustive endpoint catalog.
4. **Data:** entities, relationships, ownership, uniqueness, consistency requirements, query patterns, indexing, retention, and schema evolution. Choose relational vs document vs local storage from these requirements. Explain atomicity for contested resources.
5. **Delivery and operations:** development and production configuration, secrets, build/release process, runtime placement, health signals, backup/restore, and rollback where needed.
6. **Quality and growth:** apply [quality coverage](quality.md), identify likely bottlenecks, and give measurable triggers for extra complexity. Never claim unlimited scale or proven security from a diagram.

## Explain structure for the chosen technologies

Provide an annotated tree that follows the selected framework's conventions. Explain the purpose of each major directory, dependency direction, and where the first feature will live. Include tests and configuration. Omit unused folders and placeholders; proposing a tree does not authorize scaffolding it.

For a separate React/Express app, a possible structure is:

```text
client/src/
  app/                 # routing and application-wide providers
  features/<feature>/  # feature UI, hooks, and API calls
  components/          # genuinely shared UI
server/src/
  modules/<feature>/   # transport, business rules, and persistence as needed
  middleware/          # cross-cutting request handling
  config/              # validated runtime configuration
tests/                 # cross-feature integration or end-to-end checks
```

This is an example, not a required template. A small module can keep related logic together; separate services or repositories only when they clarify a real boundary. Put unit tests beside code or follow the existing convention. Introduce a shared package only when both sides actually need it; do not expose database models or secrets to the client.

For Django, Rails, Next.js, mobile frameworks, CLI tools, games, or data pipelines, use their own conventions and official documentation. A CLI may need only an entry point, core logic, storage adapter, and tests. A static website may need neither server nor database. An existing repository's good conventions take precedence over a preferred pattern.

## Choose where to start

| Main uncertainty | First useful work |
|---|---|
| Interaction or navigation | Prototype the core screen/workflow using representative data |
| Complex rules, relationships, or concurrency | Model the rules and exercise critical data operations |
| Unfamiliar service, hardware, deployment, or model capability | Time-box a feasibility experiment with a success criterion |
| Ordinary CRUD behavior | Build a small end-to-end feature through the required layers |
| Existing broken application | Reproduce the problem and inspect the affected path before redesigning |

Avoid a universal "database first" or "authentication first." Build ownership and permission enforcement before exposing private records or allowing other users; local prototypes must be clearly distinguished from shared releases.

## Build a dependency-aware roadmap

Use [the roadmap template](../assets/templates/roadmap.md) and [task template](../assets/templates/task.md).

- Link tasks to requirement IDs and name prerequisites. Every first-release requirement needs implementation and verification work; every task needs a requirement, learning goal, or explicit technical reason.
- Keep dependencies acyclic; ensure at least one task is ready. A cycle usually indicates an overly large task or a missing interface agreement.
- Give the first working slice an observable result. Include relevant failure paths and validation as part of the feature, not a final vague "add security" task.
- Expand the current task and immediate successors. Keep distant milestones coarse until uncertainty is resolved.
- Separate must-do work, useful later improvements, and optional learning challenges. Give effort ranges only with assumptions; do not promise exact delivery dates from an idea.
- For a scope change, list affected requirements, components, data, checks, and dependencies before revising the plan. Keep stable task IDs, mark superseded work, and preserve valid completed work.

Record significant decisions with reasons, rejected alternatives, and revisit conditions. A short decision entry is enough for a small project.
