# Tutorial: run the scaffold

This lesson runs the repository as it exists today. You will install the pinned Python dependencies, pass the quality gates, and see a healthy API. You will not start an agent run. That behavior is specified and not built yet.

You need Python 3.12, [uv](https://docs.astral.sh/uv/), and Make.

## 1. Install

From the repository root:

```bash
make setup
```

uv creates the environment from `uv.lock`.

## 2. Check

```bash
make check
```

The command finishes with exit code 0. It runs Ruff, mypy, and pytest. It does not call a model.

## 3. Serve

```bash
make run
```

In a browser or another terminal, open `http://127.0.0.1:8000/health`.

You should see:

```json
{"status":"ok"}
```

Stop the server with Ctrl+C.

## What you have

A FastAPI application with one route. The packages `domain/`, `application/`, and `adapters/` are empty on purpose. The next increment is [Sprint 2 in the backlog](../reference/backlog.md): accepting a page and appending the story.

To read why the tool exists, use [What Specwright is](../explanation/product.md). To look up requirements, use [Requirements](../reference/requirements.md).
