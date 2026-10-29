# How to run the quality gates

Run this before you open a pull request.

```bash
make check
```

That target runs Ruff, mypy on the `specwright` package, and pytest. It must pass without a network call to a model provider.

Useful slices:

```bash
make test
uv run ruff format apps/api/src tests
```

`make eval` and `make ingest` are reserved. They print a pointer until the search and eval backlog items exist. Do not add a paid model call to `make test`.
