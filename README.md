# mini-zk

A small Python CLI tool for creating notes in the zettelkasten workflow. Built with [cyclopts](https://github.com/BrianPugh/cyclopts) and [poetry](https://github.com/python-poetry/poetry).

There are many note taking tools out there but they often have a lot of features and require extensive configuration. For the sake of learning and keeping my configuration as minimal as possible I decided to create a tool tailored to my own needs.

**This project is actively developed and might change drastically.**

## Installation

To install mini-zk:

1. Clone this repository:

```bash
git clone https://github.com/devkinn/mini-zk.git && cd mini-zk
```

2. Install with pipx:

```bash
pipx install .
```

## Configuration

Config is stored in `config.py` file. Current options include changing default directory for note creation and the default text editor.

## Usage

Create a new note in default zettelkasten root specified in config file:

```bash
mini-zk new "Title of this note"
```

Specify directory for a note:

```bash
mini-zk new --dir="~/notes/" "Title of this note"
```

You can also **pipe**  content into new notes:

```bash
echo "This is some random content" | mini-zk new "Title of this note"
```

For all available commands and options append `-h` flag when executing mini-zk.

Check available commands:

```bash
mini-zk -h
```

Check available options for command `new`:

```bash
mini-zk new -h
```
