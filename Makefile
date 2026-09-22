.PHONY: setup check test run ingest eval

setup:
	uv sync --group dev

check:
	uv run ruff check apps/api/src tests
	uv run ruff format --check apps/api/src tests
	uv run mypy
	uv run pytest

test:
	uv run pytest

run:
	uv run uvicorn specwright.main:app --reload --host 127.0.0.1 --port 8000

ingest:
	@echo "Ingest is implemented in U2."

eval:
	@echo "Eval suite is implemented in U5."
