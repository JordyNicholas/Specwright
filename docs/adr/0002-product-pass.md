# 0002. Product pass

Date: 2026-10-29
Status: Accepted
Sprint: 1

## Context

U0 described Specwright as a generator of a cited engineering SpecPack. The product goal is now a full pass: idea, brainstorm, proposal, architecture, requirements, team, a project folder, and one development cycle. The person accepts each stage. The history is a story, not a Git log.

## Decision

A run yields accepted pages, `history/story.md`, a team charter the user decided, and one cycle record. The founding pages are the specification. Specwright is the orchestrator of agents. It is not a language model.

Requirements R1–R14 in `docs/reference/requirements.md` are the acceptance conditions for that goal.

## Consequences

- README, architecture, charter, and the backlog describe this pass.
- Application code beyond the scaffold waits for Sprint 2.
- Stories cite requirement ids.

## Alternatives considered

- Keep the SpecPack as the whole product. It stops before a team, a folder, and a cycle.
- Let agents publish pages without acceptance. The user would not be the product owner of the run.
