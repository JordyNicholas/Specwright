# Repo Layout — Specwright

The GitHub repository is **`specwright`**. Tree:

```text
specwright/
├── README.md
├── CHANGELOG.md
├── LICENSE
├── Makefile
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── README.md                # Diátaxis map
│   ├── tutorials/
│   ├── how-to/
│   ├── reference/
│   ├── explanation/
│   ├── ARCHITECTURE.md
│   ├── STACK_PINNED.md
│   ├── adr/
│   │   ├── 0001-record-architecture-decisions.md
│   │   ├── 0002-product-pass.md
│   │   ├── 0003-orchestration.md
│   │   ├── 0004-wiki-and-story.md
│   │   ├── 0005-search-and-deferrals.md
│   │   └── 0006-documentation-patterns.md
│   ├── charter/                 # copy of this pack
│   └── journal/
├── apps/
│   ├── api/
│   │   ├── pyproject.toml       # unused; the package is the root pyproject.toml
│   │   ├── Dockerfile
│   │   └── src/
│   │       └── specwright/
│   │           ├── __init__.py
│   │           ├── main.py      # FastAPI app factory
│   │           ├── domain/
│   │           ├── application/
│   │           ├── adapters/
│   │           └── api/
│   └── web/
│       ├── package.json
│       ├── vite.config.ts
│       ├── index.html
│       └── src/
│           ├── main.tsx
│           ├── App.tsx
│           └── features/run/    # Sprint 8
├── packages/                    # optional; start without if simpler
│   └── schemas/                 # only if sharing JSON schema with web
├── prompts/
│   └── <name>/
│       ├── v1.prompt.md
│       └── output.schema.json
├── data/
│   └── kb/                      # unused until a story needs a sample corpus
├── evals/
│   ├── cases/
│   ├── scorers/
│   └── reports/                 # gitignore contents except .gitkeep + sample
├── notebooks/                   # stretch only
├── infra/
│   ├── docker-compose.yml
│   └── aws/                     # not part of the product goal
├── tests/
│   ├── unit/
│   └── component/
└── var/                         # local traces, sqlite checkpoints — gitignored
```

## Ownership by sprint

| Path | First touched in |
|---|---|
| Tooling, Makefile, health check | U0, done |
| Docs quadrants, ADRs, prompt contracts | Sprint 1 |
| `domain/`, `adapters/wiki/` | Sprint 2 |
| Idea-brief wiring | Sprint 3 |
| `adapters/search/` | Sprint 4 |
| Charter checks, `adapters/crew/` for brainstorm | Sprint 5, crew conversation may slip to SW-30 |
| `adapters/graph/` | Sprint 6 |
| `evals/` | Sprint 7 |
| `apps/web/` | Sprint 8 |

## Python packaging choice (locked)

**Single uv workspace at repo root** with package `specwright` under `apps/api/src/specwright`.

- Root `pyproject.toml` defines the project + dev deps.  
- `apps/web` remains separate (pnpm).  
- Avoid multiple Python packages until you need them.

## Run folder

A run writes a separate folder. It is not this repository. See [the pipeline](../reference/pipeline.md).

Fixture folders used by tests stay small, license-clean, and free of scraped manuals. `data/kb/` is unused until a story needs a sample corpus. Search for the product goal reads the run folder, not `data/kb/`.
