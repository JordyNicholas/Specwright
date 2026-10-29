from pathlib import Path

from specwright.application.ports import Wiki
from specwright.domain.page import PageFamily
from specwright.domain.story import story_paragraph


def accept_page(
    wiki: Wiki, root: Path, page_name: str, family: PageFamily, decision: str, recommendation: str
) -> Path:
    accepted = wiki.accept(root, page_name, family)
    wiki.append_story(root, story_paragraph(decision, recommendation, accepted, root))
    return accepted
