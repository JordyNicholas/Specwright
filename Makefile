.PHONY: setup check test run ingest eval

setup:
	uv sync --group dev

check:
	uv run ruff check apps/api/src tests
	uv run ruff format --check apps/api/src tests
	uv run mypy -p specwright
	uv run pytest

test:
	uv run pytest

run:
	uv run uvicorn specwright.main:app --reload --host 127.0.0.1 --port 8000

ingest:
	@echo "Full-text indexing of a run folder is Sprint 4 (SW-14)."

eval:
	@echo "The eval suite is Sprint 7 (SW-23)."
