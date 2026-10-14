# Validation notes

This package has two different validation layers:

- **Structural checks:** metadata, local resource links, resource reachability, template boundaries, and regression tests for broken packages.
- **Behavioral checks:** isolated mentor sessions using the prompts in [the scenario suite](../evals/scenarios.md). These evaluate observable responses and saved state, not exact wording.

The [skill-creator validator](https://github.com/openai/skills/tree/main/skills/.system/skill-creator) is an additional authoring check. The repository validator is self-contained apart from its development-only PyYAML dependency.

## Initial results — 2026-10-14

Environment: Windows, Python 3.14.2, PyYAML 6.0.3 in an isolated virtual environment. The committed GitHub Actions workflow also runs the structural checks on Python 3.12.

| Check | Result |
|---|---|
| Skill-creator quick validator | Passed |
| Package metadata, references, and template boundaries | Passed |
| Eight package regression tests | Passed |
| GitHub Actions on the initial published revision | Passed on Python 3.12: [run](https://github.com/ahmedsamy13/Project-interview/actions/runs/38590669292) |
| Installed skill package | Passed the same package validator |
| Scenario A: offline Python CLI | Passed: small local design, no forced web infrastructure, labeled assumptions, no files written |
| Scenario B: initial interview | Passed: three relevant question groups and no premature implementation |
| Scenario C: Django/PostgreSQL booking API | Passed: respected the chosen stack, addressed atomic booking rules and record permissions, explained structure and dependencies, and qualified scale assumptions |
| Scenario D: one hint | Passed: a single ownership question, no solution code |

Behavioral checks used independent Codex subagent sessions with the skill path and raw scenario inputs. Representative observed response for D: "What prevents a logged-in user from changing the note ID in their request to someone else's?" In A, the mentor selected standard-library Python and JSON, explained data-loss checks, and disclosed unavailable browsing.

Scenarios E-H remain available for future regression evaluation; they were not completed in this initial run. Automatic discovery (scenario I) was not tested; the behavioral runs explicitly loaded the skill. These are smoke tests, not statistical evaluations across models. No application was implemented, deployed, security-audited, or load-tested. This document does not establish compliance, security certification, or performance of applications planned with the skill.
