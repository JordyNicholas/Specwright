# Documentation Standards — Specwright

Human pages follow [Diátaxis](https://diataxis.fr/). The map is [docs/README.md](../README.md). The decision is [ADR 0006](../adr/0006-documentation-patterns.md).

A page is a tutorial, a how-to, a reference, or an explanation. It is not two of those. The README links to them. It does not copy them.

## 1. Required docs

| Path | Type | Purpose |
|---|---|---|
| `README.md` | Map | Pitch, status, links, license |
| `docs/tutorials/` | Tutorial | A lesson with expected output |
| `docs/how-to/` | How-to | A task the reader already understands |
| `docs/reference/` | Reference | Requirements, pipeline, stack, backlog, prompt contract |
| `docs/explanation/` | Explanation | Why the product and the design are shaped this way |
| `docs/charter/` | Agreement | How we build |
| `docs/adr/` | Decision | ADRs |
| `docs/journal/` | Journal | What the builder learned. Not one of the four types |
| `docs/ARCHITECTURE.md` | Reference | Current and target shape |
| `docs/STACK_PINNED.md` | Reference | Versions actually installed |
| `.env.example` | Reference | Every variable, commented |
| `CHANGELOG.md` | Reference | User-visible changes, Keep a Changelog |

## 2. ADR format

File: `docs/adr/NNNN-title.md`.

```markdown
# NNNN. Title

Date: YYYY-MM-DD
Status: Proposed | Accepted | Superseded by NNNN
Sprint: Sn

## Context
## Decision
## Consequences
## Alternatives considered
```

Write an ADR before the code for a new major dependency, a change to the LangGraph, LangChain, or CrewAI boundary, a change to search, a provider default, or a documentation-pattern change.

## 3. Journal

File: `docs/journal/S<n>-short-name.md`. U0 keeps `U0-scaffold.md`.

```markdown
# Title

## Goals
## What I built
## What confused me
## What I would do differently
## Commands / evidence
## Teacher review notes
```

Portuguese is fine here.

## 4. Prompts

Agent-facing files are `prompts/<name>/v<MAJOR>.prompt.md` plus `output.schema.json`. The contract is [the prompt format](../reference/prompt-format.md). JSON Schema, not a second Zod file.

## 5. Code and API docs

- Modules: one line at the top when the purpose is not obvious.
- Public functions: docstrings with Args, Returns, and Raises.
- Graph nodes: inputs from state, side effects, and failure modes.
- FastAPI OpenAPI is the HTTP contract. Tag routes and set `response_model`.

## 6. Diagrams

Mermaid in reference and ADRs. Update the diagram when graph nodes change.

## 7. Language

English in README, ADRs, reference, and code comments. Precise. Do not claim a sprint that is not merged.
