# Specwright — Stack policy

Defaults below match [ADR 0003](../adr/0003-orchestration.md) and [ADR 0005](../adr/0005-search-and-deferrals.md). Change them only with a newer ADR. Exact installed versions live in [docs/STACK_PINNED.md](../STACK_PINNED.md). Do not add a library until the sprint that imports it.

## Runtime

| Layer | Choice | Notes |
|---|---|---|
| Language (API) | Python 3.12 | Pin 3.12 |
| Language (UI) | TypeScript on Node 22 LTS | Screen is Sprint 8 |
| Python packages | uv, `pyproject.toml`, lockfile | One package, `specwright` |
| Node packages | pnpm | Only when the web app exists |
| Make | Root `Makefile` | `setup`, `check`, `test`, `run`, `eval`, `ingest` |

## Backend and agents

| Concern | Choice |
|---|---|
| HTTP API | FastAPI and Uvicorn |
| Validation and settings | Pydantic v2 and pydantic-settings |
| Orchestration | LangGraph: supervisor node, state, pause, SQLite checkpoint |
| Model and tools | LangChain (`langchain-core` and a provider package). Domain code does not import it |
| Chat, dev default | OpenAI via `langchain-openai`, model name from settings |
| Other providers | Adapter behind the LLM port: Anthropic, Bedrock, Ollama |
| Stage conversation | CrewAI inside one LangGraph node. It returns one pending page |
| Project record | Markdown and YAML in the run folder |
| Search | Full text over that folder. Refuse when nothing matches |
| Checkpoint | LangGraph SqliteSaver locally |
| Tracing | Structured logs always. LangSmith optional |
| CLI | Typer |

### Deferred

Chroma, pgvector, hybrid dense retrieval, harness hooks, fused ranking, and an external memory MCP adapter. See ADR 0005. They are not installed in Sprint 1.

### Version policy

At the sprint that adds a library: add it with uv, commit `uv.lock`, and refresh `docs/STACK_PINNED.md`. Do not float majors mid-sprint.

Families to target when that sprint arrives, checked on PyPI that day:

- `langgraph` 1.2.x
- `langchain` and `langchain-core` 1.x
- `crewai` current 1.x stable
- `fastapi` current stable already in the lockfile
- `pydantic` 2.x already in the lockfile

## Frontend

| Concern | Choice |
|---|---|
| Bundler | Vite |
| UI | React 19, or stable 18 if 19 blocks the sprint |
| Styling | CSS modules and CSS variables |
| Data | TanStack Query for the run endpoints |
| Lint | ESLint and Prettier |

One screen. It shows the story, the pending page, accept, and the handoff holder.

## Quality

| Concern | Choice |
|---|---|
| Python lint and format | Ruff |
| Types | mypy strict on `apps/api/src` |
| Tests | pytest and pytest-asyncio |
| CI | GitHub Actions runs `make check` |

## Secrets

`.env` is local and never committed. The example file lists every variable.

## Non-goals

- Specwright is not itself a model.
- No second orchestration framework beside LangGraph.
- No microservices in the study build.
- No fine-tuning on the critical path.
- The user is not taught Git in order to read a run.

## Model defaults

| Role | Default | Why |
|---|---|---|
| Orchestrator and classifiers | Small chat model | Cost. Temperature in the prompt file |
| Drafts that must keep ids and paths | Stronger chat model, temperature 0 | Residue |
| Embeddings | Not used until SW-32 | Full text comes first |

Read model names from settings.
