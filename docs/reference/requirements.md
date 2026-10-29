# Requirements

These are the conditions for the product goal. Identifiers are stable. Backlog stories cite them. A change to a requirement needs an ADR.

| Id | Statement |
|---|---|
| R1 | A run starts from idea text and a destination folder. |
| R2 | The run walks, in order: idea, brainstorm, proposal, architecture, requirements, team, repository, one development cycle. |
| R3 | Each stage pauses with a pending page until the user accepts it or returns it with a note. |
| R4 | On accept, the page is published into its family and one plain-language paragraph is appended to `history/story.md`. |
| R5 | A later stage reads accepted pages only. |
| R6 | Every requirement has an id and a link to the proposal. Discarded options stay written. |
| R7 | The charter records expertise, duties, the agents' recommendation, and the user's decision. The author of a change is not its reviewer. The user merges. |
| R8 | A handoff is offered only to the duty named in the charter. Any other acceptor is refused. |
| R9 | The project folder is readable without Git. |
| R10 | One cycle covers one requirement, records drift, and adds no scope. |
| R11 | Search answers with a page path, or refuses when no accepted page supports the answer. |
| R12 | A compiled page keeps requirement ids and file paths from its inputs. |
| R13 | A contradiction with an accepted decision stops the cycle until the user reconciles it. |
| R14 | `make check` passes with a fake model and no network. |

## Constraints

These apply to every requirement.

- Domain code imports no web framework, LangChain, LangGraph, or CrewAI.
- Only the accept use case publishes a page and appends the story.
- Prompts are versioned `.prompt.md` files. See [prompt format](prompt-format.md).
- Text is redacted before it is stored as an observation.
- Compaction never deletes `history/story.md` or an accepted page.

## Out of scope for the goal

Harness adapters for external coding agents, five-way search fusion, a cross-project inbox, decay that removes the story, and an ai-memory server inside this repository.
