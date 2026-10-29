# 0006. Documentation patterns

Date: 2026-10-29
Status: Accepted
Sprint: 1

## Context

Human readers and agents need different page shapes. The requested human pattern is Diátaxis. The requested agent patterns are Prompty or `.prompt.md` with YAML frontmatter, Zod schemas, and CO-STAR compiled into delimited blocks.

## Decision

- Human docs are tutorials, how-to guides, reference, or explanation. One page, one type. The map is `docs/README.md`.
- Agent prompts are `prompts/<name>/v<MAJOR>.prompt.md`. Frontmatter holds model, parameters, inputs, and a JSON Schema path. The body is CO-STAR as XML blocks: context, objective, style, tone, audience, response.
- The schema language is JSON Schema, implemented by Pydantic in `domain/` when the type is built. Zod is not a second source of truth. A TypeScript client derives types from the JSON Schema.

## Consequences

- The charter's old README outline and `meta.yaml` prompt layout are replaced by this decision.
- Prompt edits that change behavior create a new major version.

## Alternatives considered

- Zod in the frontmatter. It fits a TypeScript service. This API is Python, and two schema languages will diverge.
- Leave CO-STAR as prose labels with no delimiters. The checklist still helps the author, and the model does better with explicit blocks.
- One long handbook. It fails both a lookup and a lesson.
