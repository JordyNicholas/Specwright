# Scrum working agreement

Specwright is built as one product with a single ordered backlog. A sprint is one increment. It ends when its sprint goal's acceptance criteria pass. It has no calendar length.

## Roles

| Role | Who | Accountable for |
|---|---|---|
| Product owner | Jordy | Order of the backlog, and accepting an increment |
| Developer | Jordy | The increment, including tests |
| Scrum master | This agreement, checked in review | Definition of ready, definition of done, and that the sprint goal is the only scope |

The teacher review checks the increment against the definition of done. It does not add scope mid-sprint.

## Definition of ready

A story can enter a sprint when all of these are true:

- It has the user-story sentence and acceptance criteria in [the backlog](backlog.md).
- It cites the requirements it proves.
- No open product question would change those criteria.
- The test that demonstrates it is named, and that test uses a fake model unless the story is an eval.
- It belongs to the current sprint goal.

## Definition of done

- Acceptance criteria met.
- `make check` is green.
- User-facing behavior is updated in the matching Diátaxis page, not in a second copy.
- A prompt change is a new `vN.prompt.md`, with an eval note when it changes output.
- `CHANGELOG.md` mentions user-visible changes.
- A study sprint adds a journal entry.

## Ceremonies

| Ceremony | What happens |
|---|---|
| Planning | The product owner pulls ready stories that fit the sprint goal. Nothing else enters the sprint. |
| Review | The increment is shown against the acceptance criteria. Failed criteria stay in the sprint. |
| Retrospective | One note in the journal: what to change in the working agreement. |

## Current sprint

Sprint 1 is in review. Its goal and stories are in [the backlog](backlog.md). Sprint 2 is ready to pull after Sprint 1 is done.
