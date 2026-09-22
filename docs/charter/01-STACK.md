# Specwright — Locked Stack

Decisions below are **defaults**. Change only via an ADR in `docs/adr/`.

## Runtime & package managers

| Layer | Choice | Notes |
|---|---|---|
| Language (AI/API) | **Python 3.12** | CrewAI supports ≤3.13; pin 3.12 for stability |
| Language (UI) | **TypeScript 5.x** on **Node 22 LTS** | Matches your React experience |
| Python packages | **uv** + `pyproject.toml` + lockfile | Reproducible; faster than raw pip |
| Node packages | **pnpm** + lockfile | Strict, fast; commit the lockfile |
| Containers | **Docker** + **Docker Compose** | One-command local demo |
| Make | **Makefile** at repo root | Standard entrypoints: `make setup check test eval run` |

## Backend / AI

| Concern | Choice |
|---|---|
| HTTP API | **FastAPI** + **Uvicorn** |
| Validation / settings | **Pydantic v2** + **pydantic-settings** |
| Orchestration | **LangGraph** (supervisor, state, HITL, checkpoints) |
| Multi-agent collaboration | **CrewAI** (invoked *inside* one LangGraph node) |
| LLM plumbing / tools | **LangChain** + **langchain-core** (+ provider packs) |
| Embeddings / chat (dev default) | **OpenAI** API via `langchain-openai` |
| Alternate providers | Interface `LLMProvider`; adapters later: Anthropic, Bedrock, Ollama |
| Vector store (local) | **Chroma** |
| Vector store (Compose/prod-shaped) | **pgvector** on **PostgreSQL 16** |
| Keyword / hybrid search | **BM25** (e.g. `rank_bm25`) + dense; merge + optional rerank |
| Rerank (optional MVP+) | Cross-encoder or provider rerank — behind a flag |
| Checkpointing | LangGraph **SqliteSaver** (local) → Postgres checkpointer later |
| Tracing | **LangSmith** (optional key) + structured logs always |
| HTTP client | **httpx** |
| CLI | **Typer** (e.g. `sw ask`, `sw ingest`, `sw eval`) |

### Version policy (Python AI libs)

Ecosystem moves fast. Do **not** hardcode patch versions in this charter forever.

At scaffold time (U0):

1. Create the project with `uv`.  
2. Add dependencies **without** floating majors beyond what you install that day.  
3. Commit `uv.lock`.  
4. Record exact resolved versions in `docs/STACK_PINNED.md` (generated once per lock refresh).

**Baseline families to target when installing (verify on PyPI that day):**

- `langgraph` 1.2.x  
- `langchain` / `langchain-core` 1.x  
- `crewai` 1.15.x (or current 1.x stable)  
- `fastapi` 0.115+ / current stable  
- `pydantic` 2.x  

Refresh lockfiles intentionally (lesson or ADR), not mid-feature.

## Frontend

| Concern | Choice |
|---|---|
| Bundler | **Vite** |
| UI library | **React 19** (or current stable 18+ if 19 friction) |
| Styling | **CSS modules** + CSS variables (no UI kit required for MVP) |
| Data fetching | **TanStack Query** for `/assist` calls |
| Lint/format | **ESLint** + **Prettier** |

Keep the UI thin: one demo screen. No design-system sprawl in study mode.

## Tooling (quality gates)

| Concern | Choice |
|---|---|
| Python lint/format | **Ruff** (format + lint) |
| Python types | **mypy** (strict for `apps/api/src`) |
| Python tests | **pytest** + **pytest-asyncio** |
| Coverage (soft) | **pytest-cov**; gate later if useful |
| Pre-commit | **pre-commit** hooks: ruff, mypy (api), eslint, prettier |
| CI | **GitHub Actions**: `make check` on PR/main |

## Cloud & secrets (from U7)

| Concern | Choice |
|---|---|
| Primary cloud | **AWS** (leverage your CCP) |
| Secrets | `.env` local (never committed); AWS SSM/Secrets Manager in deploy |
| Observability MVP | Structured JSON logs + LangSmith; CloudWatch when on AWS |

## Explicit non-goals (stack)

- No NestJS / Spring in Specwright (keep AI path in Python).  
- No microservices split in study mode (one API process).  
- No fine-tuning in the critical path (notebook stretch only).  
- No Flux / fiscal / Pix domain code.

## Model defaults (study budget)

| Role | Default | Rationale |
|---|---|---|
| Classifier / router | Small/cheap chat model | Cost |
| Main synthesis | Stronger chat model | Quality for SpecPack |
| Embeddings | `text-embedding-3-small` (or current OpenAI small) | Cost/quality |
| Local free path | **Ollama** adapter (optional lesson) | Practice offline on your GPU laptop |

Always read model names from config — never hardcode in business logic.
