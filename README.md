# Project Interview

**An AI project mentor that helps you plan clearly and learn by building.**

This reusable skill interviews you about your idea, recommends a suitable stack and architecture, and guides you through development with **hints first**. It runs inside a compatible coding agent, with Codex metadata included.

## What it does

- Adapts questions to your experience, goals, project type, budget, and expected scale.
- Explains the chosen technologies, data flow, and folder structure for each relevant layer.
- Creates an ordered roadmap with prerequisites and practical completion checks.
- Covers security, accessibility, testing, deployment, recovery, and growth where relevant.
- Reviews your attempts, suggests improvements, and resumes from saved project notes.

MERN is welcome, but not required. Small projects receive small architectures. Code examples or implementation are available when you explicitly ask.

## Install in Codex

Ask the built-in installer:

```text
$skill-installer Install the skill from https://github.com/ahmedsamy13/Project-interview/tree/main/skills/project-interview
```

Or clone this repository and copy **the entire `skills/project-interview` folder** to one of these locations:

| Scope | Destination |
|---|---|
| All your projects | `~/.agents/skills/project-interview` |
| One repository | `<your-project>/.agents/skills/project-interview` |

On Windows, `~` means your user profile folder. Some installations use `$CODEX_HOME/skills` (usually `~/.codex/skills`); use the location supported by your host and install only one copy. If the skill does not appear, restart Codex. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

No application server, database, or separate API key is required by this skill. It uses the model and tools available in your agent; normal host usage limits still apply.

## Use it

Open the project you want help with, then start a chat:

```text
Use $project-interview. I want to build a tutor booking app using MERN.
I know React basics and want to practice backend development.
Interview me first, then recommend the structure and a roadmap. Hints first.
```

Continue naturally:

| You want to... | Say... |
|---|---|
| Start the next task | "What should I work on next, and why?" |
| Get help | "Give me one hint. Don't show the solution yet." |
| Review an attempt | "Review this code against my current task." |
| Change scope | "Add team accounts and explain what the plan needs to change." |
| Save or resume | "Save my progress." / "Resume this project from its saved notes." |
| Stay in chat | "Plan only in chat; don't create or edit files." |

When saving is authorized, the mentor maintains `.mentor/` notes in your project for requirements, architecture, decisions, roadmap, and progress. It distinguishes your reported completion from reviewed code and executed tests. Review notes before sharing them; keep secrets out.

## Inside the skill

[SKILL.md](skills/project-interview/SKILL.md) contains the workflow. Focused [references](skills/project-interview/references) cover interviews, architecture, quality, mentoring, and memory. [Templates](skills/project-interview/assets/templates) keep project records consistent.

Recommendations depend on the information and tools available. The skill cannot guarantee security, scalability, or compliance; it identifies assumptions and the checks needed to establish them.

## Validation

Maintainers can run structural checks with Python 3.10+:

```sh
python -m pip install -r requirements-dev.txt
python tools/validate_skill.py
python -m unittest discover -s tests -v
```

See [behavioral scenarios](evals/scenarios.md) for mentoring checks and [validation notes](docs/validation.md) for the tested scope. Structural checks do not prove mentoring quality.
