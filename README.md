# Project Interview

**A reusable AI skill for project planning and ongoing development mentoring.**

Project Interview turns a software idea into a practical build plan. It asks about your requirements and experience, recommends technologies and an application structure, then guides you through one task at a time. Its default teaching style is **hints first**: you write the code, and the mentor helps you understand and check your work.

## Requirements

- A coding agent that supports `SKILL.md` skills. Codex installation is documented below.
- Access to your project folder if you want code review and saved progress.
- Browsing tools for checking current documentation, when available.

The skill does not run a website or require its own server, database, or API key. It uses your agent's model and tools, with the host's normal usage limits.

## Installation

In Codex, send this message:

```text
$skill-installer Install the skill from https://github.com/ahmedsamy13/Project-interview/tree/main/skills/project-interview
```

For manual installation, clone this repository or download its ZIP. Copy **the entire `skills/project-interview` folder**, including its references and templates, to one of these locations:

| Scope | Destination |
|---|---|
| All your projects | `~/.agents/skills/project-interview` |
| One repository | `<your-project>/.agents/skills/project-interview` |

On Windows, `~` means your user profile folder. Some hosts and installers use `$CODEX_HOME/skills`, usually `~/.codex/skills`. Use the location supported by your installation and keep only one copy. If the skill does not appear, restart Codex. [Official installation reference](https://learn.chatgpt.com/docs/build-skills).

## Quick start

Open the project folder you want to work on, then send:

```text
Use $project-interview. I want to build a tutor booking app using MERN.
I know React basics and want to practice backend development.
Interview me first, then recommend the structure and a roadmap. Hints first.
```

You can use MERN or another stack. For an existing project, ask the mentor to inspect the current structure before recommending changes.

## Workflow and outputs

| Stage | What the skill does | Output |
|---|---|---|
| Interview | Clarifies users, features, learning goals, budget, and constraints | Project brief with requirements and open questions |
| Architecture | Explains technology choices, data flow, responsibilities, and folder structure | Technical plan with reasons and tradeoffs |
| Roadmap | Chooses a starting point and orders features by their dependencies | Tasks with prerequisites and completion checks |
| Mentoring | Explains concepts, gives progressive hints, and reviews attempts | Guidance for the current task |
| Continuation | Records decisions, tracks evidence, and adjusts to changed requirements | Saved progress and the next useful step |

Planning also covers security, accessibility, performance, testing, deployment, and recovery where they apply. The depth matches the project: a local CLI should not receive the architecture of a large hosted service.

## Common requests

```text
Use $project-interview to resume this project's saved plan.
Explain why this feature should come before the others.
Give me one hint without showing the solution.
Review my attempt against the current task's completion checks.
Show a small code example for this concept; don't edit files.
Add team accounts and explain which requirements and tasks change.
Save my progress and record what I should do next.
```

These are ordinary chat requests, not a fixed command syntax. To work without saving files, add: `Keep everything in chat; do not create or edit files.`

## Saved project state

When persistent mentoring is authorized, the skill maintains notes in your project's `.mentor/` folder, or reuses existing planning documents:

| File | Contents |
|---|---|
| `brief.md` | Requirements, learning goals, scope, and assumptions |
| `architecture.md` | Stack, structure, data model, and research notes |
| `roadmap.md` | Task order, dependencies, status, and evidence |
| `progress.md` | Latest result, blockers, and next action |
| `decisions.md` | Important decisions and their reasons |
| `tasks/` | Detailed task notes when needed |

Files are created as needed. Project history stays with the project, not inside the installed skill. In a chat without file access, the mentor can provide a handoff to copy, but cannot save it for you.

## Behavior and limits

- Hints come before solutions; code examples and implementation require your request.
- Reported completion, reviewed code, and executed tests are recorded separately.
- Recommendations identify assumptions and checks; they do not guarantee security, scale, or compliance.
- Research and code inspection depend on available tools. Publishing or deployment requires authorization.
- Review saved notes before sharing them, and keep credentials and private data out.

## Skill files and validation

The entry point is [SKILL.md](skills/project-interview/SKILL.md). Supporting [references](skills/project-interview/references) provide focused guidance; [templates](skills/project-interview/assets/templates) define the project records.

For maintainers, run the package checks with Python 3.10+:

```sh
python -m pip install -r requirements-dev.txt
python tools/validate_skill.py
python -m unittest discover -s tests -v
```

See [behavioral scenarios](evals/scenarios.md) for mentoring checks and [validation notes](docs/validation.md) for the tested scope. Structural checks do not prove mentoring quality.
