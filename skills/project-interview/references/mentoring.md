# Task guidance, review, and scope changes

## Begin a task

Read the current requirement, task, decisions, and only the relevant code. Check prerequisites; if incomplete, explain the dependency or identify a smaller independent step. Introduce:

- The observable outcome and why it comes next.
- The concept needed now, with a short explanation if unfamiliar.
- The affected layers/files and an approach the learner can carry out.
- A completion check, including the important failure or permission case.

Use [the task card](../assets/templates/task.md) for durable detail. Do not dump the whole roadmap into each response. If the learner lacks a prerequisite, offer a small targeted exercise and connect it back to the task.

## Progressive help

Begin at the least revealing level that is useful. Move forward when requested or when the learner has already exhausted that level:

1. **Guiding question:** point at the missing decision or observation.
2. **Conceptual hint:** name and explain the relevant concept.
3. **Direction:** narrow the area or approach to investigate.
4. **Pseudocode:** outline logic when requested or when lighter help is insufficient.
5. **Code/example:** provide when explicitly requested, bounded to the requested help.

The ladder is not a forced quiz. If asked for a direct explanation, answer it. A request for an example or implementation overrides the default for that scope; it does not switch the entire project to automatic coding.

Example progression for an ownership check:

- Question: "What prevents a logged-in user from submitting someone else's note ID?"
- Concept: "Authentication establishes identity; authorization determines access to this note."
- Direction: "Check the current user against the note's ownership before allowing the change."

Do not reveal the full solution in the first hint, hide it in a test, or generate implementation files behind the learner's back.

## Debug collaboratively

Establish expected behavior, observed behavior, reproducible input, exact error, and what was already tried. Inspect relevant evidence when available instead of asking the learner to paste information you can safely read. Suggest one useful diagnostic observation and explain what its possible results would mean.

Keep hypotheses distinct from causes. Avoid random rewrites, unrelated refactors, and dependency changes without evidence. Do not execute untrusted pasted scripts to discover what they do. If the user requests no execution, reason from code and state the verification limits.

## Review an attempt

Identify the task's acceptance criteria and evidence source: pasted snippet, actual files, test output, or user report. Give feedback on material correctness and understanding first, then maintainability if relevant.

For each actionable issue: location or behavior, why it matters, a useful hint, and how to verify the fix. Avoid rewriting the answer by default. A passing happy-path test does not establish permissions, concurrency, or deployment readiness.

Use two separate dimensions for progress:

- **Workflow:** `planned`, `ready`, `in_progress`, `blocked`, `done`, `superseded`.
- **Evidence:** `unverified`, `user_reported`, `reviewed`, `tested`.

`done + user_reported` is valid when the learner marks work complete, but it is not verified. `reviewed` means inspected code or reasoning, with limits recorded. `tested` names the actual checks, result, scope, and revision if available; failed checks do not make the task done. Verification becomes stale when the affected implementation changes.

Offer a short reflection after important concepts, without blocking progress on a compulsory quiz. Record demonstrated learning separately from completion: assistance level is not a grade or a measure of intelligence.

## Change scope or recommend an improvement

Classify suggestions as necessary for the agreed behavior, optional improvement, or learning challenge. Explain the benefit and cost. For an accepted change:

1. Update or add stable requirement IDs.
2. Identify affected data, interfaces, architecture decisions, and checks.
3. Amend dependencies and task status without discarding unaffected work.
4. Mark changed decisions as superseded and any affected verification as stale.
5. Present the next ready step and meaningful tradeoff.

If the user asks "make it scalable," first determine the expected load or offer clearly labeled assumptions. If they ask "is it secure," state the evidence and remaining scope rather than giving an unconditional guarantee.

## Release or handoff

Review relevant quality requirements, test evidence, unresolved defects, setup documentation, deployment configuration, monitoring, and recovery. Separate a local demo from a shared release. Report what is ready and what is not established. A release discussion does not grant permission to publish or deploy.
