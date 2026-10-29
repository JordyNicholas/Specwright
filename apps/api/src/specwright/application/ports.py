from pathlib import Path
from typing import Protocol

from specwright.domain.page import PageFamily

class Wiki(Protocol):
  def accept(self, root: Path, name: str, family: PageFamily) -> Path:
    """ Move `_pending/<name>` to `<family>/<name>` and return the new path. """
    return root