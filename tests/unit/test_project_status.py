import importlib.util
from pathlib import Path


def _status():
    path = Path(__file__).resolve().parents[2] / ".github" / "scripts" / "sync_project_status.py"
    spec = importlib.util.spec_from_file_location("sync_project_status", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_merge_moves_in_review_to_done() -> None:
    assert _status().desired_status("In review", True) == "Done"


def test_merge_leaves_work_that_is_not_in_review() -> None:
    status = _status()
    assert status.desired_status("Ready", True) is None
    assert status.desired_status("Product backlog", True) is None
    assert status.desired_status("Done", True) is None


def test_open_pull_request_moves_unreviewed_work_into_review() -> None:
    status = _status()
    assert status.desired_status("Product backlog", False) == "In review"
    assert status.desired_status("Ready", False) == "In review"
    assert status.desired_status("In progress", False) == "In review"
    assert status.desired_status("In review", False) is None
    assert status.desired_status("Done", False) is None
