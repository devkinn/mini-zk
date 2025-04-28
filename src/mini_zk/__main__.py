import sys

from cyclopts import App, Parameter
from typing import Annotated
from pathlib import Path

from mini_zk import messages, note_utils, config

app = App(name="mini-zk")


# Cyclopts validators - throws error if conditions not met.


# validate_title - check if title is under MAX_TITLE_LENGTH and doesn't have markdown file extension.
def validate_title(type_, title):
    if len(title) > config.MAX_TITLE_LENGTH:
        raise ValueError(f"Max length of note title is {config.MAX_TITLE_LENGTH}.")
    elif title.lower().endswith(".md"):
        raise ValueError("Leave out the .md file extension.")


# validate_subfolder - check if subfolder is in SUBFOLDERS list in config file.
# mini-zk creates subfolders automatically so this prevents accidental subfolder creation.
def validate_subfolder(type_, subfolder):
    if subfolder != "ZK_ROOT":
        if subfolder not in config.SUBFOLDERS:
            raise ValueError(
                f"Subfolder {subfolder} not added to SUBFOLDERS in config file."
            )


@app.command
def new(
    title: Annotated[str, Parameter(validator=validate_title)],
    subfolder: Annotated[str, Parameter(validator=validate_subfolder)] = "ZK_ROOT",
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
    subfolder: str
        Provide a subfolder name that is defined within SUBFOLDERS list in config. mini-zk creates subfolders automatically if they don't exist. Can be used for more granular note organization. If not provided note will be created in ZK_ROOT directory.
    editor: bool
        Set to false to disable opening the editor after note creation.
    frontmatter: bool
        Set to false to disable frontmatter insertion at the top of the note.
    """

    path = Path(config.ZK_ROOT)
    # Join ZK_ROOT and subfolder and create it if it doesn't exist.
    if subfolder != "ZK_ROOT":
        path = path / Path(subfolder)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            messages.zk_info(f"Created subfolder: {subfolder}.")

    # Support for piping content.
    if not sys.stdin.isatty():
        content = sys.stdin.read()
    else:
        content = ""

    note_utils.create_note(title, content, path, editor, frontmatter)


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
