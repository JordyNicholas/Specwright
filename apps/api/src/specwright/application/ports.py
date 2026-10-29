from pathlib import Path
from typing import Protocol

from specwright.domain.page import PageFamily


class Wiki(Protocol):
    def accept(self, root: Path, name: str, family: PageFamily) -> Path:
        """Move `_pending/<name>` to `<family>/<name>` and return the new path."""
        ...

    def append_story(self, root: Path, paragraph: str) -> None:
        """Append one paragraph to history/story.md"""
        ...
