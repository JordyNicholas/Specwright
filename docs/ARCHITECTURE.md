# Architecture

## Current (U0, done)

```mermaid
flowchart LR
  client[HTTP client] --> api[FastAPI]
  api --> health[GET /health]
```

- Package: `specwright` under `apps/api/src/specwright/`
- Layers, still empty: `domain/`, `application/`, `adapters/`, `api/`
- No model, graph, or wiki is installed

## Target

```mermaid
flowchart TD
  user[User] --> edge[CLI or API]
  edge --> cases[Use cases]
  cases --> graph[LangGraph]
  graph --> llm[LangChain adapter]
  graph --> crew[CrewAI inside one node]
  graph --> wiki[Wiki adapter]
  wiki --> folder[Run folder]
  folder --> story[history/story.md]
  graph --> search[Full-text search]
  search --> folder
```

The graph pauses for the user. Agents write `_pending/` pages. Only the accept use case publishes a page and appends the story. Domain types do not import FastAPI, LangChain, LangGraph, or CrewAI.

The stage table is [the pipeline reference](reference/pipeline.md). Why the libraries are split is [orchestration](explanation/orchestration.md).
