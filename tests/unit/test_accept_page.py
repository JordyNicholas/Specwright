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
    decision = "the decision."
    recommendation = "the recommendation."

    accepted = accept_page(
        FileWiki(), tmp_path, "brief.md", PageFamily.CONCEPTS, decision, recommendation
    )

    assert accepted == tmp_path / "concepts" / "brief.md"
    story = (tmp_path / "history" / "story.md").read_text(encoding="utf-8")
    assert "You decided: the decision." in story
    assert "The draft had recommended: the recommendation." in story
    assert "Page: concepts/brief.md" in story
    assert accepted.read_text(encoding="utf-8") == "problem: the brief\n"
    assert not source.exists()


def test_same_decision_and_recommendation(tmp_path: Path) -> None:
    pending = tmp_path / "_pending"
    pending.mkdir()
    source = pending / "brief.md"
    source.write_text("problem: the brief\n", encoding="utf-8")
    decision = "the same."
    recommendation = "the same."

    accepted = accept_page(
        FileWiki(), tmp_path, "brief.md", PageFamily.CONCEPTS, decision, recommendation
    )

    assert accepted == tmp_path / "concepts" / "brief.md"
    story = (tmp_path / "history" / "story.md").read_text(encoding="utf-8")
    assert "You decided: the same." in story
    assert "The draft had recommended: the recommendation." not in story
    assert "Page: concepts/brief.md" in story
    assert accepted.read_text(encoding="utf-8") == "problem: the brief\n"
    assert not source.exists()
