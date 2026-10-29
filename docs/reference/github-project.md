# GitHub Project

The board is the Scrum view of [the product backlog](backlog.md). Creating it is a [how-to](../how-to/create-the-github-project.md). The backlog remains the wording. The board does not get a parallel description of the work.

## Project

| Field | Value |
|---|---|
| Title | Specwright |
| Repository | `jordynicholas/specwright` |
| Views | Board by Status, Table by Sprint, Roadmap by Sprint |

## Fields

| Field | Options |
|---|---|
| Status | Product backlog, Ready, In progress, In review, Done |
| Sprint | Sprint 1 … Sprint 9, or Unscheduled |
| Priority | Must, Should, Could |
| Requirement | R1 … R14, or none |
| Epic | Docs, Wiki, Idea, Search, Charter, Graph, Evals, Screen, Cycle, Later |

## How items move

1. New work lands in **Product backlog** with the backlog id.
2. Planning moves a ready story to **Ready**.
3. Implementation moves it to **In progress**, then **In review** when the pull request is open.
4. **Done** requires the [definition of done](scrum.md) and a merged pull request.

Sprint 1 rows are **In review** for the documentation pull request. All **Must** rows below Sprint 1 stay in **Product backlog** except Sprint 2, which is **Ready**.
