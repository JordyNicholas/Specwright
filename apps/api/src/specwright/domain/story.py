from pathlib import Path


def story_paragraph(decision: str, recommendation: str, page: Path, root: Path) -> str:
    location = page.relative_to(root).as_posix()
    sentences = [f"You decided: {decision}"]
    if recommendation != decision:
        sentences.append(f"The draft had recommended: {recommendation}")
    sentences.append(f"Page: {location}.")
    return " ".join(sentences) + "\n"


def append_story(self, root: Path, paragraph: str) -> None:
    """Append one paragraph to history/story.md."""
    ...
