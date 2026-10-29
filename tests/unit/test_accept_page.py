"""Accepting a page files it under its family and removes the pending copy."""

from pathlib import Path

from specwright.adapters.wiki.filesystem import FileWiki
from specwright.application.accept_page import accept_page
from specwright.domain.page import PageFamily


def test_accept_page(tmp_path: Path) -> None:

    pending = tmp_path / "_pending"
    pending.mkdir()
    source = pending / "brief.md"
    source.write_text("problem: the brief\n", encoding="utf-8")

    accepted = accept_page(FileWiki(), tmp_path, "brief.md", PageFamily.CONCEPTS)

    assert accepted == tmp_path / "concepts" / "brief.md"
    assert accepted.read_text(encoding="utf-8") == "problem: the brief\n"
    assert not source.exists()
