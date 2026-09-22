# Specwright

Multi-agent system that turns messy product intent into a **cited engineering SpecPack** (requirements, architecture options, risks, implementation outline).

Study / portfolio project for AI Engineering (LangGraph, CrewAI, RAG, evals, LLMOps). Curriculum is teacher-managed; see `docs/charter/`.

## Status

**U0 — scaffold.** Tooling and `/health` only. Agents and RAG land in later units.

## Quickstart

Prerequisites: Python 3.12, [uv](https://docs.astral.sh/uv/), Make (WSL/Linux/macOS).

```bash
make setup
make check
make run
```

Then open `http://127.0.0.1:8000/health` → `{"status":"ok"}`.

## Skills demonstrated (roadmap)

| Skill | Unit |
|---|---|
| Project layout, FastAPI, quality gates | U0 (this) |
| Domain schemas, prompt registry | U1 |
| Hybrid RAG + citations | U2 |
| CrewAI multi-agent crew | U3 |
| LangGraph supervisor + HITL | U4 |
| Evals, tracing, guardrails | U5 |
| React demo UI | U6 |
| AWS deploy + portfolio narrative | U7 |

## License

MIT — see [LICENSE](LICENSE).
