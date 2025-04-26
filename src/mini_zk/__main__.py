import sys

from cyclopts import App, Parameter, validators
from typing import Annotated
from pathlib import Path

from mini_zk import note_utils
from mini_zk import config

app = App(name="mini-zk")


# Cyclopts validators - throws error if conditions not met.


# validate_title - check if title is under MAX_TITLE_LENGTH and doesn't have markdown file extension.
def validate_title(type_, title):
    if len(title) > config.MAX_TITLE_LENGTH:
        raise ValueError(f"Max length of note title is {config.MAX_TITLE_LENGTH}.")
    elif title.lower().endswith(".md"):
        raise ValueError("Leave out the .md file extension.")


# Cyclopts converters - convert parameters.


# expand_and_resolve_path - convert ZK_ROOT path from relative path to full path.
def expand_and_resolve_path(_type, tokens):
    raw = tokens[0].value
    return Path(raw).expanduser().resolve()


@app.command
def new(
    title: Annotated[str, Parameter(validator=validate_title)],
    dir: Annotated[
        Path,
        Parameter(
            converter=expand_and_resolve_path,
            validator=validators.Path(exists=True, dir_okay=True, file_okay=False),
        ),
    ] = config.ZK_ROOT,
    editor: bool = True,
    frontmatter: bool = True,
):
    """
    Creates a new note with the provided title and drops into the editor for interactive editing.
    If stdin is piped, fills the note with that data.

    Parameters
    ----------
    title: str
        Title of the note.
    dir: Path
        Directory which the note will be created in. Defaults to ZK_ROOT specified in config file.
    editor: bool
        Set to false to disable opening the editor after note creation.
    frontmatter: bool
        Set to false to disable frontmatter insertion at the top of the note.
    """

    # Support for piping content
    if not sys.stdin.isatty():
        content = sys.stdin.read()
    else:
        content = ""

    note_utils.create_note(title, content, dir, editor, frontmatter)


@app.command
def open():
    """
    Opens zettelkasten using directory set in ZK_ROOT in config file. Editor of choice has to support opening directories. Neovim recommended.
    """
    dir = config.ZK_ROOT
    note_utils.open_in_editor(dir)


def main():
    app()


if __name__ == "__main__":
    main()
