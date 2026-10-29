# 0003. Orchestration

Date: 2026-10-29
Status: Accepted
Sprint: 1

## Context

The charter already assigned LangGraph to supervision, LangChain to model plumbing, and CrewAI to collaboration inside one node. A later draft of the design dropped CrewAI from the stack table and left LangChain unnamed. That read as if the orchestrator had no libraries.

## Decision

- LangGraph owns state, stage order, routing, human pause, and the SQLite checkpoint.
- The orchestrator is a graph node. It returns a work order. Conditional edges select the next agent.
- LangChain (`langchain-core` and a provider package) is how every agent node calls a model and binds tools. Domain code does not import it.
- CrewAI runs inside one graph node and returns one pending page. It does not assign duties, pause the run, or publish an accepted page.
- Accept, merge, and the story append are a use case, not an agent tool.

## Consequences

- Those libraries are added in the sprint that first imports them.
- Brainstorm is the first intended crew. The graph still waits for the user afterward.
- A second orchestrator is a defect.

## Alternatives considered

- CrewAI as the pipeline owner. Gates and the named handoff would sit inside a conversation the graph cannot pause cleanly.
- Direct HTTP to the provider with no LangChain. It duplicates tool-calling and schema handling that LangChain already provides for this stack.
