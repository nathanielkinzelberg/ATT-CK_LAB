# CLAUDE.md — ATT&CK-Pi Lab

This file tells Claude Code how to work with this repository.

## Project Overview

A phase-by-phase Python adversary simulation platform built as a portfolio project targeting a Red Team Engineer role at SafeBreach.

- **Laptop (Controller)** handles the CLI, sends authenticated requests, displays results, saves reports
- **Raspberry Pi 5 (Agent)** runs a FastAPI server, executes whitelisted MITRE ATT&CK simulation modules, returns structured JSON
- Communication between them over HTTP with API token authentication

## Repository Layout

```
attackLab/
├── controller/             # Laptop-side CLI and HTTP client
├── agent/                  # Raspberry Pi FastAPI server
│   └── techniques/         # One Python module per ATT&CK technique
├── shared/                 # Shared models and logging config (used by both sides)
├── tests/
│   ├── unit/               # Module-level tests
│   └── integration/        # Controller → Agent end-to-end tests
├── reports/                # Generated execution reports (gitignored)
├── docs/
│   ├── journal/            # Per-phase build journal entries
│   └── decisions/          # Architecture decision records
├── README.md
├── CLAUDE.md               # This file
├── .gitignore
└── .env.example
```

## Development Workflow

- **Phases:** Work one phase at a time. Do not advance until the current phase is confirmed working.
- **Commits:** One commit per completed phase minimum. Nathaniel makes all commits and pushes — never run git commit, git push, or git add.
- **Commit format:** `Phase N: short description`
- **Teaching:** Explain every concept in plain English before writing code. Define every new term. One file at a time.

## Phase Tracking

| Phase | Title                                | Status      |
|-------|--------------------------------------|-------------|
| 0     | Project Setup and Scaffolding        | Complete    |
| 1     | Shared Models and Base Class         | Complete    |
| 2     | Agent — FastAPI Server and Auth      | In Progress |
| 3     | T1082 — System Information Discovery | Not Started |
| 4     | Controller CLI and HTTP Client       | Not Started |
| 5     | T1057 — Process Discovery            | Not Started |
| 6     | T1087 — Account Discovery            | Not Started |
| 7     | T1016 — Network Config Discovery     | Not Started |
| 8     | T1046 — Network Service Scanning     | Not Started |
| 9     | Automated Tests                      | Not Started |
| 10    | Reporting and Structured Output      | Not Started |
| 11    | Deploy Agent as Raspberry Pi Service | Not Started |
| 12    | GitHub Portfolio Polish              | Not Started |
| 13    | Résumé Bullets                       | Not Started |
| 14    | Interview Prep                       | Not Started |

## End of Phase Checklist

At the end of every phase, before Nathaniel commits, always update:
1. **CLAUDE.md** — mark the phase Complete in the Phase Tracking table, mark next phase In Progress
2. **README.md** — update the status line and progress table
3. **docs/journal/phase_NN_*.md** — fill in all sections: dates, concepts learned, problems encountered, final code reference
4. **docs/glossary.md** — add any new terms introduced in this phase

## Key Rules for Claude

- Never generate the entire finished project at once.
- Work one phase at a time and wait for confirmation before moving on.
- Before writing any code, explain what it is and why we need it in plain English.
- Define every new term the first time it appears.
- One concept, one file at a time when introducing something new.
- Ask comprehension questions after each major concept.
- Never run git commit, git push, git add, or any Git write command — Nathaniel does all Git operations.
- If Nathaniel seems confused, stop and go back to basics immediately.
- Nathaniel commits whenever he is ready. Never prompt him to commit.
- At the end of each phase, provide a suggested commit message only. Nathaniel writes his own git commands.
