from pathlib import Path
from specwright.domain.page import PageFamily

class FileWiki:
  def accept(self, root: Path, name: str, family: PageFamily) -> Path:
    source = root / "_pending" / name
    target_dir = root / family.value
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / name
    source.replace(target)

    return target
