# U0 — Scaffold

Historical record. On 2026-10-29 the product goal became the full project pass. This entry stays as the record of the scaffold. See `docs/explanation/product.md`.

## Goals

- Establish repo layout and quality tooling (`make check`).
- Ship a minimal FastAPI `/health` endpoint.

## What I built

- Initial `uv` project (student), then completed U0 scaffold with teacher assistance on PR #1:
  - `apps/api/src/specwright` hexagonal stubs
  - FastAPI health, Makefile, tests, charter copy, placeholders

## What confused me

- Mapping `uv init` default `src/` layout to Specwright’s `apps/api/src/` tree.
- Windows/WSL path choices for the working copy.

## What I would do differently

- Start from the charter tree checklist before running `uv init`.

## Commands / evidence

```bash
make setup
make check
make run
```

## Teacher review notes

_Filled after review._
