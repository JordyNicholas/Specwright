# Stack

Installed versions are in [STACK_PINNED.md](../STACK_PINNED.md). This page is the target definition. Libraries are added in the sprint that first imports them, then the lockfile and `STACK_PINNED.md` are refreshed.

| Concern | Definition |
|---|---|
| Language | Python 3.12 |
| Packages | uv, one package `specwright` under `apps/api/src` |
| HTTP | FastAPI and Uvicorn |
| Records | Pydantic v2 |
| Orchestration | LangGraph: state, order, routing, pause, SQLite checkpoint |
| Model calls | `langchain-core` and a provider package such as `langchain-openai` |
| Stage conversation | CrewAI, inside one graph node, returning one pending page |
| Project files | Markdown with YAML frontmatter on disk |
| Search | Full text over the run folder. Index rebuilt from the files |
| Checkpoint | LangGraph SqliteSaver, same machine, not the story |
| CLI | Typer, before the React screen |
| UI | React, Vite, TypeScript. One screen after a run can pause and accept |
| Quality | Ruff, mypy strict, pytest. `make check` uses a fake model |

## Deferred until a requirement needs them

Chroma, pgvector, hybrid dense retrieval, harness hooks for other coding agents, fused ranking, and an MCP adapter to an external ai-memory server.

## Model settings

Model names come from settings (`SPECWRIGHT_CHAT_MODEL`). They are not hardcoded in domain code. Tests bind a fake. Temperature lives in the prompt file, not in business logic.
