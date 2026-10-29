# 0004. Wiki and story

Date: 2026-10-29
Status: Accepted
Sprint: 1

## Context

Agents and the user both need a record. The user may not read Git. Session notes are not decisions. ai-memory's useful idea is a markdown wiki as the source of truth, with drafts separated from accepted pages.

## Decision

- The run folder is the source of truth. Search indexes are derived and can be rebuilt.
- Agents write only under `_pending/`.
- Accept moves the page to its family (`concepts/`, `decisions/`, `requirements/`, `procedures/`) and appends one paragraph to `history/story.md`.
- Frontmatter keeps `recommendation` and `decision` when they differ.
- `follows` and `satisfies` are extension fields. Typed relations stay `causes`, `fixes`, and `contradicts`.
- Accepted pages and the story are not deleted by compaction.

The stage table is `docs/reference/pipeline.md`.

## Consequences

- Sprint 2 implements accept and the story with a fixture, before any live model.
- The repository step copies this folder. It does not instruct the user in Git.

## Alternatives considered

- Git log as the history the user reads. It assumes a skill the product does not require.
- A database row as the only copy of a decision. It is harder to read and easier to trap.
