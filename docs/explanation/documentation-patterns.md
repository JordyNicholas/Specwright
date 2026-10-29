# Documentation patterns

Two audiences read this repository, and they do not want the same shape of page.

## People: Diátaxis

[Diátaxis](https://diataxis.fr/) splits human docs into tutorials, how-to guides, reference, and explanation. Mixing them makes a page that is too slow for a lookup and too thin for a lesson.

Specwright uses that split directly. The tutorial runs the scaffold that exists today. How-to guides assume you already know the product and need a procedure. Reference holds requirements, the pipeline, the stack, the backlog, and the prompt contract, with no narrative. Explanation holds why the product, the libraries, and these patterns are shaped this way. The charter remains the working agreement. ADRs remain the decision log. The learning journal remains a personal record and is not one of the four types.

A fact has one home. The README points at the four types. It does not restate the requirements.

## Agents: Prompty-shaped files

A prompt file has two parts, matching the [Prompty](https://prompty.ai/) idea. YAML frontmatter is the infrastructure contract: model, parameters, inputs, and the output schema. The body is the instruction. Keeping them apart means a temperature change does not hide inside a paragraph, and a reviewer can diff the contract without rereading the prose.

The schema in that contract is JSON Schema. Pydantic models in `domain/` implement it when the sprint builds them. Zod is the same kind of contract for TypeScript, and this API is Python. A second hand-written Zod schema would drift from the Pydantic model. When a web client needs types, it should derive them from the JSON Schema. The research that suggested Zod is right about separating the contract from the body, and wrong about Zod as the source of truth in this repository.

## Authors: CO-STAR, then delimiters

CO-STAR (context, objective, style, tone, audience, response) is a checklist for writing an instruction so a piece is not forgotten. The file the model receives is those six parts as XML blocks, in that order. The mnemonic itself is for the author. Delimiters are for the model, which follows a bounded block more reliably than a label it must reinterpret.

Style and tone stay short. The response block points at the schema and forbids extra fields. That is what keeps requirement ids and paths from being paraphrased away.

Worked files live under `prompts/`. The lookup table is the [prompt format](../reference/prompt-format.md). The decision is [ADR 0006](../adr/0006-documentation-patterns.md).
