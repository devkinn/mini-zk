# This file contains functions for message handling - errors, warning, info.

import sys

from rich.console import Console


def zk_error(message: str):
    Console().print(format_message(message, "Error", "red"))
    sys.exit(1)


def zk_warning(message: str):
    Console().print(format_message(message, "Warning", "yellow"))


def zk_info(message: str):
    Console().print(format_message(message, "Info", "blue"))


# format_message - format the displayed message. Design taken from Cyclopts source code to match the aesthetic.
def format_message(message: str, title: str, style: str):
    from rich import box
    from rich.panel import Panel
    from rich.text import Text

    panel = Panel(
        Text(message, "default"),
        title=title,
        box=box.ROUNDED,
        expand=True,
        title_align="left",
        style=style,
    )
    return panel
