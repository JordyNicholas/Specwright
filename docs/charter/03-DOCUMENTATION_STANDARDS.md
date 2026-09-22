# Documentation Standards — Specwright

Documentation is part of the curriculum. AI Engineering roles expect you to explain systems, not only ship demos.

## 1. Required docs (always present)

| Path | Purpose |
|---|---|
| `README.md` | What / why / quickstart / skills matrix / demo GIF or screenshots |
| `docs/charter/` | Copy of this charter pack (source of truth) |
| `docs/adr/` | Architecture Decision Records |
| `docs/journal/` | Per-unit learning journal |
| `docs/ARCHITECTURE.md` | Current system diagram + request lifecycle |
| `docs/STACK_PINNED.md` | Exact lockfile versions after U0 |
| `.env.example` | All env vars with comments |
| `CHANGELOG.md` | User-visible changes (Keep a Changelog style) |

## 2. README structure (fixed outline)

1. One-paragraph pitch  
2. Skills demonstrated (checklist mapped to GenAI tracks)  
3. Architecture diagram (mermaid)  
4. Quickstart (`make setup && make run`)  
5. Example SpecPack (short)  
6. Eval summary table (link to latest committed sample report)  
7. Project structure  
8. Roadmap / curriculum units  
9. License (MIT recommended for portfolio)

## 3. ADR format

File: `docs/adr/NNNN-title.md` (monotonic).

```markdown
# NNNN. Title

Date: YYYY-MM-DD
Status: Proposed | Accepted | Superseded by NNNN
Unit: Ux

## Context
## Decision
## Consequences
## Alternatives considered
```

**ADR triggers** (must write one before coding the change):

- New major dependency  
- Change to LangGraph vs CrewAI boundary  
- Chunking / retrieval strategy  
- Provider default change  
- Deploy topology change  

## 4. Learning journal

File: `docs/journal/U0X-short-name.md`

```markdown
# U0X — Title

## Goals
## What I built
## What confused me
## What I would do differently
## Commands / evidence
## Teacher review notes
```

Portuguese OK here. Keep it honest — this is study material, not marketing.

## 5. Code documentation

- **Modules**: one-liner at top if non-obvious.  
- **Public functions/classes**: Google-style or Sphinx docstrings stating Args / Returns / Raises.  
- **Do not** narrate obvious code (`i += 1  # increment i`).  
- Complex graph nodes: docstring must state inputs from state, side effects, failure modes.

## 6. API docs

- FastAPI auto OpenAPI is the contract.  
- Tag routes; set `response_model`.  
- Breaking response changes bump API version path (`/v1/...`) once you leave study MVP, or document as breaking in CHANGELOG.

## 7. Prompt docs

Each `prompts/<name>/meta.yaml` must include:

```yaml
name: spec_normalize
version: 1
owner: jordy
model_role: classifier  # classifier | synthesizer | judge
temperature: 0.0
changelog: "Initial normalize prompt"
eval_cases: ["evals/cases/normalize.jsonl"]
```

## 8. Diagrams

- Use **mermaid** in Markdown (ARCHITECTURE, ADRs, README).  
- Keep diagrams updated when graph nodes change (part of DoD for U4+).

## 9. Language & tone

- Repo English (README, ADRs, code comments aimed at employers).  
- Precise over hype (“hybrid RAG with citations” not “revolutionary AI”).  
- Never claim skills you did not implement.
