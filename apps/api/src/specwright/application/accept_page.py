from pathlib import Path

from specwright.application.ports import Wiki
from specwright.domain.page import PageFamily


def accept_page(wiki: Wiki, root: Path, page_name: str, family: PageFamily) -> Path:
    return wiki.accept(root, page_name, family)
