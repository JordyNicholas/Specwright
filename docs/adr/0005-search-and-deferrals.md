# 0005. Search and deferrals

Date: 2026-10-29
Status: Accepted
Sprint: 1

## Context

The original stack specified Chroma, pgvector, and hybrid retrieval before the product folder existed. Memory engines such as a SQLite write lock, harness hooks, five-way ranking, a cross-project inbox, and decay do not by themselves explain a project to a person.

## Decision

- Search for the product goal is full text over the run folder. A hit returns a path. A miss refuses.
- The LangGraph checkpoint may use local SQLite. That file is not the story.
- Chroma, pgvector, fused ranking, external harness hooks, cross-project mail, decay of accepted pages, and an ai-memory MCP adapter are deferred until a backlog story needs them.
- Vector search (SW-32) requires an eval that shows full text missing a page a person needed.

## Consequences

- Sprint 4 builds the full-text behavior with fixtures.
- `make ingest` stays a stub until that sprint.
- The charter's vector-store rows are deferred, not deleted from history. This ADR supersedes them for the product goal.

## Alternatives considered

- Build hybrid RAG in the first increment. It indexes a corpus the product does not have yet.
- Copy ai-memory into this repository. It replaces the pipeline with a different product.
