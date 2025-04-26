import subprocess
import random
import string
import datetime

from pathlib import Path
from textwrap import dedent

from mini_zk import config
from mini_zk import messages


def create_note(title: str, content: str, dir: Path, editor: bool, frontmatter: bool):
    filename = format_filename(title)
    path = dir / filename
    with path.open("a") as note:
        if frontmatter:
            note.write(insert_frontmatter(title))
        note.write(content)
    if editor:
        open_in_editor(path)
    messages.zk_info(f"Created note: {path}")


def open_in_editor(path: Path):
    try:
        subprocess.run([config.EDITOR, str(path)], check=True)
    except FileNotFoundError:
        messages.zk_warning(
            f"Editor [{config.EDITOR}] set in config not found and the note won't be opened. Make sure it is installed and in your PATH."
        )
    except subprocess.CalledProcessError as e:
        messages.zk_error(str(e))


# format_filename - formats title to match {id}-{kebab-case-title} template.
def format_filename(title: str) -> str:
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


def insert_frontmatter(title: str):
    frontmatter = f"""\
    ---
    title: {title}
    date: {datetime.date.today()}
    tags:
      -
    ---

    """
    return dedent(frontmatter)
