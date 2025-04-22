import subprocess
import random
import string

from pathlib import Path
from mini_zk import config


def create_note(title: str, content: str, dir: Path):
    filename = create_filename(title)
    path = dir / filename
    path.write_text(content)
    open_in_editor(path)
    print(f"Created note: {path}")


def open_in_editor(path: Path):
    subprocess.run([config.EDITOR, str(path)])


def create_filename(title: str) -> str:
    id = "".join(
        random.choices(string.ascii_lowercase + string.digits, k=config.ID_LENGTH)
    )
    filename = (
        id
        + "-"
        + title.replace(
            " ",
            "-",
        ).lower()
        + ".md"
    )
    return filename
