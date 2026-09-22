# Engineering Standards — Specwright

These rules apply from commit one. Teacher reviews against this checklist.

## 1. Architecture boundaries

```
apps/api          → HTTP, wiring, lifespan
src/specwright/    → application + domain (importable package)
  domain/         → pure models, errors (no FastAPI, no CrewAI, no LangGraph)
  application/    → use cases (orchestrate ports)
  adapters/       → LLM, vector DB, CrewAI, LangGraph, filesystem
  api/            → FastAPI routers (thin)
```

**Rules**

- `domain/` must not import FastAPI, LangChain, LangGraph, CrewAI, or DB drivers.  
- Adapters implement ports (Protocols / ABCs) defined in `application/ports.py` (or `domain/ports.py`).  
- Routers: validate → call use case → map response. No agent logic in routers.  
- Prefer one use case per flow (`GenerateSpecPack`, `IngestCorpus`, `RunEvalSuite`).

## 2. Naming

| Kind | Convention |
|---|---|
| Python modules/files | `snake_case.py` |
| Python classes | `PascalCase` |
| Python functions/vars | `snake_case` |
| React components | `PascalCase.tsx` |
| CSS modules | `ComponentName.module.css` |
| Env vars | `SPECWRIGHT_` prefix (e.g. `SPECWRIGHT_OPENAI_API_KEY`) |
| Prompts | `prompts/<name>/v<MAJOR>.md` + `meta.yaml` |

## 3. Types & errors

- Public functions annotated; mypy clean under `src/specwright`.  
- Domain failures: typed exceptions, e.g. `SpecwrightError` → `RetrievalEmptyError`, `SchemaValidationError`, `BudgetExceededError`.  
- Do not raise bare `Exception` from domain/application.  
- Prefer `Result`-like returns only if they stay readable; otherwise typed errors + HTTP mapping at the edge.

## 4. Async

- FastAPI routes `async`; blocking LLM/Crew calls run via `asyncio.to_thread` or native async clients.  
- Do not block the event loop with long sync CrewAI/LangGraph calls without offloading.

## 5. Config

- All config via `pydantic-settings` in one `Settings` object.  
- `.env.example` committed; `.env` gitignored.  
- Feature flags: `SPECWRIGHT_ENABLE_RERANK`, `SPECWRIGHT_ENABLE_LANGSMITH`, etc.

## 6. Prompts (first-class artifacts)

```
prompts/
  spec_normalize/
    v1.md
    meta.yaml    # model role, temperature, owner, changelog
  crew_researcher/
    v1.md
    meta.yaml
```

- No long system prompts buried only in Python strings (short glue OK).  
- Bumping a prompt = new `vN` (do not silently edit prod version).  
- Every prompt change that affects output quality requires an eval smoke run.

## 7. RAG standards

- Every answer that uses the KB must include **citations** (`source_id`, `chunk_id`, `span` or quote).  
- If retrieval confidence is below threshold → **refuse** with a clear message (no invented standards).  
- Chunking strategy documented in `docs/adr/0002-chunking.md` once chosen.  
- Ingest is idempotent and logged (doc count, chunk count, duration).

## 8. Agents

- **LangGraph** owns: state schema, edges, retries, HITL, persistence.  
- **CrewAI** owns: role collaboration for drafting content inside `run_crew`.  
- Do not invent a third orchestration framework.  
- Tools are small, typed, and side-effect documented (read-only vs write).  
- Agent nodes must be unit-testable with fakes (mock LLM / fake retriever).

## 9. Evals

- Golden cases live in `evals/cases/*.jsonl` (one concern per file OK).  
- Scorers in `evals/scorers/`; reports in `evals/reports/` (gitignored except a sample).  
- Minimum metrics for a “green” generate run: schema valid, ≥1 citation when KB hit expected, refusal when empty KB.  
- Never delete a failing case to go green — fix code or mark `xfail` with reason.

## 10. Logging & tracing

- Structured logs: `request_id`, `run_id`, `node`, `model`, `tokens_in`, `tokens_out`, `latency_ms`, `cost_usd_est`.  
- No secrets or full PII in logs. Redact API keys and emails.  
- LangSmith optional; local JSONL trace file always available under `var/traces/`.

## 11. Tests

| Layer | What |
|---|---|
| Unit | domain + pure functions; fake ports |
| Component | RAG retrieve with fixture corpus |
| Contract | API OpenAPI / schema snapshots where useful |
| Eval | separate from unit; `make eval` (may cost $) |

- Default `make test` = unit + component **without** paid LLM calls (use fakes).  
- `make eval` = real or recorded LLM (document which). Prefer recorded/cassettes later if cost hurts.

## 12. Git

- Branch: `main` protected; work on `feat/<unit>-short-name` or `study/u0-scaffold`.  
- Commits: imperative, scoped — `feat(rag): add bm25 hybrid merge`.  
- One logical concern per commit when possible.  
- Never commit: `.env`, keys, `var/`, large binaries, eval reports with secrets.  
- PR description (even solo): goal, how to test, charter rules touched.

## 13. Makefile targets (required)

```text
make setup      # install deps (uv + pnpm)
make check      # ruff + mypy + eslint + unit tests
make test       # pytest (no paid LLM)
make eval       # eval suite
make run        # api + web via compose or local
make ingest     # rebuild vector index from data/kb
```

## 14. Code style (Python)

- Ruff format is law; line length **100**.  
- No unused ignores; `# noqa` needs a reason comment.  
- Imports absolute from `specwright.*`.  

## 15. Code style (TypeScript)

- `strict: true` in tsconfig.  
- No `any` unless justified with comment.  
- Prefer function components; keep demo UI dumb.
