# Prompt file format

Prompt files are the contract an agent loads. Human discussion of why this shape was chosen is in [documentation patterns](../explanation/documentation-patterns.md).

## Path

```text
prompts/<name>/v<MAJOR>.prompt.md
prompts/<name>/output.schema.json
```

A behavior change is a new major file. Do not edit a version that a run has already used. Short glue in Python is allowed. A system prompt is not.

## Frontmatter

The frontmatter is [Prompty](https://prompty.ai/)-shaped. It holds the infrastructure contract. The body holds the instruction.

| Key | Role |
|---|---|
| `name`, `version`, `description` | Identity |
| `model.api` | `chat` |
| `model.configuration` | Provider type and model name. Prefer `${SPECWRIGHT_CHAT_MODEL}` |
| `model.parameters` | Temperature and token limits |
| `inputs` | Name, type, and description of each template variable |
| `outputs.<name>.schema` | Path to a JSON Schema file |

The output schema is JSON Schema. The domain model that implements it is Pydantic, written in the sprint that introduces the type. Zod is not a second contract. A TypeScript client derives types from the same JSON Schema.

## Body

The body is the CO-STAR map as delimited XML blocks, in this order: `context`, `objective`, `style`, `tone`, `audience`, `response`. Template variables use Prompty's `{{name}}` form. The `response` block names the schema fields the model must fill and no others.

CO-STAR is how the author checks that the instruction is complete. The model receives the delimited blocks, not a worksheet about the mnemonic.

## Worked examples

- [Idea brief](../../prompts/idea-brief/v1.prompt.md)
- [Brainstorm](../../prompts/brainstorm/v1.prompt.md)
