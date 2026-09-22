# Repo Layout — Specwright

Create the GitHub repo as **`specwright`** (public). Final tree:

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
│   ├── ARCHITECTURE.md
│   ├── STACK_PINNED.md
│   ├── adr/
│   │   ├── 0001-record-architecture-decisions.md
│   │   ├── 0002-langgraph-and-crewai-boundary.md
│   │   └── 0003-hybrid-rag.md
│   ├── charter/                 # copy of this pack
│   └── journal/
├── apps/
│   ├── api/
│   │   ├── pyproject.toml       # or workspace root pyproject — pick one in U0
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
│           └── features/assist/
├── packages/                    # optional; start without if simpler
│   └── schemas/                 # only if sharing JSON schema with web
├── prompts/
├── data/
│   └── kb/                      # markdown knowledge base (synthetic)
├── evals/
│   ├── cases/
│   ├── scorers/
│   └── reports/                 # gitignore contents except .gitkeep + sample
├── notebooks/                   # stretch only
├── infra/
│   ├── docker-compose.yml
│   └── aws/                     # U7 sketches
├── tests/
│   ├── unit/
│   └── component/
└── var/                         # local traces, sqlite checkpoints — gitignored
```

## Ownership by unit

| Path | First touched in |
|---|---|
| tooling, Makefile, empty package | U0 |
| `domain/`, `prompts/` | U1 |
| `adapters/rag/`, `data/kb/` | U2 |
| `adapters/crew/` | U3 |
| `adapters/graph/` | U4 |
| `evals/` | U5 (skeleton can start U1) |
| `apps/web/` | U6 |
| `infra/aws/` | U7 |

## Python packaging choice (locked)

**Single uv workspace at repo root** with package `specwright` under `apps/api/src/specwright`.

- Root `pyproject.toml` defines the project + dev deps.  
- `apps/web` remains separate (pnpm).  
- Avoid multiple Python packages until you need them.

## Knowledge base rules

- Synthetic, license-clean Markdown only.  
- Filename pattern: `data/kb/<area>/<slug>.md` with YAML front matter (`id`, `title`, `tags`).  
- No scraped copyrighted manuals.
