# Pipeline

A run is one pass. The user accepts every stage before the next stage starts. Agents write under `_pending/`. Accept moves the page and appends [the story](../explanation/history.md).

| Step | Pending path | Accepted path | Required content |
|---|---|---|---|
| Idea | `_pending/brief.md` | `concepts/brief.md` | Problem, who feels it, what they do today, what changes, what this is not |
| Brainstorm | `_pending/options.md` | `decisions/options.md` | Each option: existing alternatives, a real-world use, kept or discarded, and why. A non-market idea says so in one line |
| Proposal | `_pending/proposal.md` | `concepts/proposal.md` | Core idea, problem, scope, success |
| Architecture | `_pending/adr-NNNN.md` | `decisions/adr-NNNN.md` | Core workflow, system shape, and one decision per material stack choice |
| Requirements | `_pending/REQ-NNN.md` | `requirements/REQ-NNN.md` | Testable statement, link to the proposal, and a place in the roadmap |
| Team | `_pending/team-charter.md` | `procedures/team-charter.md` | Expertise for this project, duties, recommendation, user decision |
| Repository | — | The folder itself | Accepted pages plus `history/story.md`. No Git lesson |
| Cycle | `sessions/` notes stay episodic | Merge line on the requirement, paragraph in the story | One requirement, author, a different reviewer, user merge, drift note |

## Frontmatter

Accepted pages use Open Knowledge Format-style YAML. Unknown keys are kept.

| Key | Meaning |
|---|---|
| `type` | Concept, Decision, Requirement, Procedure, or Session Summary |
| `status` | `draft` while pending. `accepted` after the user accepts |
| `generated.by` | Model id on a draft. `human:<name>` on acceptance |
| `generated.at` | Timestamp of that write |
| `sources` | Upstream accepted page this one follows |
| `recommendation` | What the agents proposed |
| `decision` | What the user accepted. Both lines stay when they differ |
| `follows` | Path of the upstream page |
| `satisfies` | For a requirement, the proposal path |

Relations `causes`, `fixes`, and `contradicts` are the only typed edges. Traceability uses `follows` and `satisfies`, not new relation names.

## One cycle slice

| Moment | Who | Writes |
|---|---|---|
| Assign | Orchestrator | Work order citing requirement ids |
| Draft | Expertise named for that requirement | A pending change. A crew may talk only inside this step |
| Review | A role other than the author | Findings, or `contradicts` against an accepted decision |
| Merge | User | Merge line and a story paragraph |
| Watch | Monitor | Drift. No new requirement |

The work order fields are `stage`, `duty`, `requirement_ids`, `allowlist`, and `may_accept`.
