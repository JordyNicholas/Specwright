# How the agents are orchestrated

Three libraries stay, and they do not share one job.

LangGraph is the orchestrator. It holds the stage order, the shared state, the branch chosen from a work order, the pause until you answer, and the SQLite checkpoint for that open gate.

An orchestrator node inside that graph is an agent. Its prompt reads accepted pages and must return a work order: stage, duty, requirement ids, tool allowlist, and the single role that may accept the handoff. A conditional edge follows that order. A specialist node has its own prompt and may write a pending page. The accept use case publishes the page and appends the story. No agent is given that use case.

LangChain is the call. `langchain-core` and a provider package supply messages, tools, and a reply that must match a schema. That code sits in the LLM adapter. Domain types do not import it.

CrewAI is the conversation inside one stage. The graph starts a crew and takes back one pending page. Brainstorm is the stage that wants this: a facilitator and a critic. The crew does not choose the next duty, pause the run, or publish an accepted page. If it did, the run would have two conductors, and a draft could move between roles without you.

During the development cycle the same charter works the roadmap. Interaction on a slice is assign, draft, review by someone else, your merge, and a story paragraph. A crew may debate inside the draft. The record is the handoff and the story.

This split is [ADR 0003](../adr/0003-orchestration.md). The charter already pointed here: LangGraph supervises, LangChain is the plumbing, CrewAI runs inside one node.
