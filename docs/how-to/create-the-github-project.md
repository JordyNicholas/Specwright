# How to create the GitHub Project

Create the Scrum board from [the board reference](../reference/github-project.md). The items and their fields already live in [the product backlog](../reference/backlog.md).

This environment cannot create the project. The available GitHub token cannot read or write Projects.

## 1. Create the project

On GitHub: **Projects → New project → Board**. Name it `Specwright`.

Or, with a token that has the `project` scope:

```bash
gh project create --owner JordyNicholas --title "Specwright" --format json
```

Link it to the `jordynicholas/specwright` repository.

## 2. Add the fields

Create the fields listed in the [board reference](../reference/github-project.md): Status, Sprint, Priority, Requirement, Epic.

Set Status options to: Product backlog, Ready, In progress, In review, Done.

## 3. Add one item per backlog id

For each row in the backlog, create a GitHub issue from [the user-story template](../../.github/ISSUE_TEMPLATE/user_story.md) and add it to the project. Copy the id, sprint, priority, requirement, and status from the backlog table. The issue body is the user story plus the acceptance criteria. Do not invent a second wording.

## 4. Open the board

- Board grouped by Status, so the sprint ceremony has a place to move work.
- Table filtered to the current sprint.
- Roadmap grouped by Sprint, ordered from Sprint 1 to Sprint 9.

Sprint 1 items are **In review** while the documentation pull request is open. Move them to **Done** when that pull request merges and `make check` is green. Pull Sprint 2 into **Ready** only after Sprint 1 is Done. The [definition of ready](../reference/scrum.md) is the gate.
