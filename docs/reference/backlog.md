# Product backlog

Product goal: a person can go from an idea prompt to a project folder and one completed development cycle, without using Git. Agents draft. The person accepts.

Success looks like this: a fixture idea yields the accepted pages, the story, the charter, and one cycle record; search cites a path or refuses; `make check` passes with a fake model.

The board fields are in [GitHub Project](github-project.md). Wording here wins if the board drifts.

## Roadmap

| When | Sprint | Goal |
|---|---|---|
| Now | 1, in review | A reader can see the product, the requirements, the prompt contract, and this backlog |
| Next | 2, ready | Accepting a fixture page publishes it and appends a story paragraph, with no model call |
| Later | 3 | An idea becomes a pending brief the user can accept or return |
| Later | 4 | Search cites an accepted page or refuses |
| Later | 5 | The charter blocks an author from reviewing their own work, and the handoff names one duty |
| Later | 6 | The founding stages pause for the user and resume |
| Later | 7 | Evals fail when traceability, residue, or a contradiction breaks |
| Later | 8 | One screen shows the story, the pending page, accept, and who holds the handoff |
| Later | 9 | The folder is created and one cycle finishes under the charter |

## Sprint 1 — Docs and decisions

**Goal:** the repository describes Specwright as an orchestrator, with Diátaxis pages, accepted ADRs, prompt contracts, and this backlog.

**Status:** In review.

| Id | Epic | Priority | Requirement | Story | Acceptance |
|---|---|---|---|---|---|
| SW-01 | Docs | Must | none | As a reader, I want the README to say Specwright orchestrates agents, so I do not look for a model | README states that, links the four Diátaxis types, and the health check still runs |
| SW-02 | Docs | Must | R1–R14 | As a product owner, I want the requirements written down, so later stories can cite them | `docs/reference/requirements.md` lists R1–R14 and the constraints |
| SW-03 | Docs | Must | none | As a contributor, I want ADRs for the product pass, orchestration, wiki, search, and docs, so code does not invent a second design | ADRs 0002–0006 are Accepted |
| SW-04 | Docs | Must | R12 | As an agent, I want prompt files with frontmatter and a delimited body, so the contract is separate from the instruction | Format page plus `prompts/idea-brief` and `prompts/brainstorm` |
| SW-05 | Docs | Must | none | As a scrum master, I want a backlog, a definition of ready, and a definition of done, so a sprint has a boundary | `backlog.md` and `scrum.md` exist and name Sprint 1 and Sprint 2 |
| SW-06 | Docs | Must | none | As a maintainer, I want the charter and the architecture page to match the product, so old SpecPack instructions are not followed | Charter, `ARCHITECTURE.md`, and the changelog agree with the ADRs |

## Sprint 2 — Page and story

**Goal:** accepting a fixture page writes it to the family folder and appends one story paragraph. No model is called.

**Status:** Ready. Pull only after Sprint 1 is Done.

| Id | Epic | Priority | Requirement | Story | Acceptance |
|---|---|---|---|---|---|
| SW-07 | Wiki | Must | R3, R4 | As a user, I want an accepted page to leave `_pending/`, so the folder shows what I decided | Accept moves a fixture page to its family path and removes it from pending |
| SW-08 | Wiki | Must | R4, R9 | As a user, I want a story paragraph in ordinary sentences, so I do not read a diff | The paragraph states the decision, the recommendation when it differs, and the page path |
| SW-09 | Wiki | Must | R5 | As a later stage, I want to read accepted pages only, so a draft cannot leak forward | A reader for accepted pages does not return `_pending/` paths |
| SW-10 | Wiki | Must | R14 | As a developer, I want this slice tested without a network, so `make check` stays cheap | Unit tests use no model and `make check` is green |

## Sprint 3 — Idea brief

**Goal:** an idea prompt becomes a pending brief in the fixed pattern. The user can accept it or return a note.

| Id | Epic | Priority | Requirement | Story | Acceptance |
|---|---|---|---|---|---|
| SW-11 | Idea | Must | R1, R2 | As a user, I want to submit an idea and receive a pending brief, so the run starts from my words | The pending brief has the five headings. The default test uses a fake model |
| SW-12 | Idea | Must | R3 | As a user, I want to return a note and see a revised draft, so acceptance is a decision | A second compile includes the note and does not publish the page |
| SW-13 | Idea | Must | R4 | As a user, I want acceptance to publish `concepts/brief.md` and the story line, so the idea is on record | Reuses the Sprint 2 accept path |

## Sprint 4 — Search

**Goal:** a question about the accepted folder cites a path, or refuses.

| Id | Epic | Priority | Requirement | Story | Acceptance |
|---|---|---|---|---|---|
| SW-14 | Search | Must | R11 | As an agent, I want search to return a page path, so answers point at the folder | A known phrase returns the fixture page path |
| SW-15 | Search | Must | R5, R11 | As a user, I want a miss to refuse, so the agent does not invent a decision | An empty or irrelevant query returns a refusal and no path |

## Sprint 5 — Charter and handoff

**Goal:** the team charter records both the recommendation and the decision, and a handoff has one acceptor.

| Id | Epic | Priority | Requirement | Story | Acceptance |
|---|---|---|---|---|---|
| SW-16 | Charter | Must | R7 | As a user, I want the author and the reviewer to be different roles, so review is real | A charter where they are the same role is rejected |
| SW-17 | Charter | Must | R7 | As a user, I want both the recommendation and my decision kept, so a change of mind is visible | The stored charter keeps both lines |
| SW-18 | Charter | Must | R8 | As a scrum master, I want the wrong role to be refused, so the baton cannot be taken by whoever runs next | Accepting a handoff as another duty fails |

## Sprint 6 — Founding graph

**Goal:** LangGraph walks the founding stages, pauses for the user, and resumes from the checkpoint.

| Id | Epic | Priority | Requirement | Story | Acceptance |
|---|---|---|---|---|---|
| SW-19 | Graph | Must | R2, R3 | As a user, I want the run to wait at each founding stage, so I see every draft | The graph interrupts with a pending page and does not start the next stage |
| SW-20 | Graph | Must | R3 | As a user, I want to resume after the process stops, so an open gate is not lost | A new process loads the SQLite checkpoint and is still on that gate |
| SW-21 | Graph | Must | R6 | As a user, I want discarded options to remain written, so a later stage cannot revive them silently | The options page still lists them after a later stage runs |
| SW-22 | Graph | Must | R6 | As a developer, I want each requirement to cite the proposal, so the roadmap has a source | A requirement without `satisfies` is rejected |

## Sprint 7 — Evals

**Goal:** the suite fails when traceability, residue, or a contradiction is broken.

| Id | Epic | Priority | Requirement | Story | Acceptance |
|---|---|---|---|---|---|
| SW-23 | Evals | Must | R6 | As a product owner, I want an eval to catch a requirement that does not cite the proposal | The case fails on a broken fixture and passes on a good one |
| SW-24 | Evals | Must | R12 | As a product owner, I want an eval to catch a compiled page that dropped ids or paths | The case fails when those tokens are absent |
| SW-25 | Evals | Must | R13 | As a user, I want the cycle to stop on `contradicts` until I reconcile it | The graph will not offer merge while the contradiction is open |

## Sprint 8 — Screen

**Goal:** one screen shows the story, the pending page, accept, and who holds the handoff.

| Id | Epic | Priority | Requirement | Story | Acceptance |
|---|---|---|---|---|---|
| SW-26 | Screen | Must | R3, R4, R9 | As a user, I want to read the story and accept the pending page in the browser, so I do not use Git or a raw folder | The screen renders a fixture run, accept updates the story, and the handoff holder is visible |

## Sprint 9 — Cycle

**Goal:** the project folder exists and one requirement goes through draft, review, user merge, and a drift note.

| Id | Epic | Priority | Requirement | Story | Acceptance |
|---|---|---|---|---|---|
| SW-27 | Cycle | Must | R9 | As a user, I want the tool to create the project folder from accepted pages, so I am not asked to commit | The folder contains the trail and `history/story.md`, and the UI does not show Git commands |
| SW-28 | Cycle | Must | R7, R10 | As a user, I want one requirement implemented and reviewed by someone else, so the charter is real | Author and reviewer differ. Merge waits for the user |
| SW-29 | Cycle | Must | R10 | As a user, I want drift recorded and scope left alone, so the monitor cannot add a requirement | The cycle record cites the requirement id and adds none |

## Unscheduled

| Id | Epic | Priority | Requirement | Story | Acceptance |
|---|---|---|---|---|---|
| SW-30 | Later | Should | R2 | As a user, I want brainstorm to be a facilitator and a critic in one crew, so that stage is a conversation | The graph calls one CrewAI node and receives one pending options page |
| SW-31 | Later | Could | R11 | As a developer, I want an MCP adapter to an external ai-memory server, so pages can be indexed there | The wiki port has a second adapter. The folder remains the source of truth |
| SW-32 | Later | Could | R11 | As a user, I want vector search when full text misses, so recall can improve without replacing the story | An eval shows a miss that vectors find, and accepted pages are still cited by path |
