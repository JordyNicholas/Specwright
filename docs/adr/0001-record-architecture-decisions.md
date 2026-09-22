# 0001. Record architecture decisions

Date: 2026-09-22
Status: Accepted
Unit: U0

## Context

Specwright needs a lightweight way to record stack and design choices so later units stay aligned with `docs/charter/`.

## Decision

Use Architecture Decision Records (ADRs) in `docs/adr/NNNN-title.md` as described in the documentation standards.

## Consequences

- Material stack or layout changes require an ADR before (or with) the code change.
- Readers can reconstruct why Python 3.12, LangGraph+CrewAI, etc. were chosen.

## Alternatives considered

- Wiki-only notes — easy to drift from the repo.
- Long README history — hard to scan decisions.
