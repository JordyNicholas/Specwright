# GitHub Project

The board is [SpecWright](https://github.com/users/JordyNicholas/projects/8).

Each story in [the product backlog](backlog.md) is an issue on that board. The backlog wording is the source of truth.

| Field | Meaning |
|---|---|
| Status | Product backlog, Ready, In progress, In review, Done |
| Sprint | Sprint 1 through Sprint 9, or Unscheduled |
| Priority | Must, Should, Could |
| Requirement | The requirement ids the story proves |
| Epic | Docs, Wiki, Idea, Search, Charter, Graph, Evals, Screen, Cycle, Later |

The Board view groups by Status. Sprint 1 is In review. Sprint 2 is Ready. Later sprints are in the product backlog. An item is Done when the [definition of done](scrum.md) is met and its pull request is merged.

A pull request that uses a closing keyword (`Closes #n`) against `main` moves that story to **In review**. When the pull request merges, the story moves from **In review** to **Done**. The workflow is `.github/workflows/project-status.yml`.
