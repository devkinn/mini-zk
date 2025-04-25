import os
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


# validate_default_zk_root - check if ZK_ROOT_ENV is set in the system. If not set ZK_ROOT to ZK_ROOT_PATH from config.
def validate_default_zk_root():
    zk_root = os.environ.get(config.ZK_ROOT_ENV)
    if zk_root is None:
        print(
            f"{config.ZK_ROOT_ENV} environment variable not set, falling back to {config.ZK_ROOT_PATH} default path."
        )
        zk_root = config.ZK_ROOT_PATH
    return Path(zk_root).expanduser().resolve()


# Cyclopts converters - convert parameters.


# expand_and_resolve_path - convert ZK_ROOT path from relative path to full path.
def expand_and_resolve_path(_type, tokens):
    raw = tokens[0].value
    return Path(raw).expanduser().resolve()


# Resolve default path as it is not passed to converter by cyclopts design.
_default_zk_root = validate_default_zk_root()


@app.command
def new(
    title: Annotated[str, Parameter(validator=validate_title)],
    dir: Annotated[
        Path,
        Parameter(
            converter=expand_and_resolve_path,
            validator=validators.Path(exists=True, dir_okay=True, file_okay=False),
        ),
    ] = _default_zk_root,
    editor: bool = True,
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
    """

    # Support for piping content
    if not sys.stdin.isatty():
        content = sys.stdin.read()
    else:
        content = ""

    note_utils.create_note(title, content, dir, editor)


def main():
    app()


if __name__ == "__main__":
    main()
