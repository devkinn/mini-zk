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

By default mini-zk uses directory set in `ZK_ROOT` environmental variable, but it will fall back to path set in config file if it is not set.

## Usage

The tool can be executed under two names: `mini-zk` and `zk` which is just faster to type.

### Commands

Create a new note in default zettelkasten root specified in config file:

```bash
zk new "Title of this note"
```

Specify directory for a note:

```bash
zk new --dir="~/notes/" "Title of this note"
```

Open the zettelkasten directory:

```bash
zk open
```

You can also **pipe** content into new notes:

```bash
echo "This is some random content" | zk new "Title of this note"
```

For all available commands and options append `-h` flag when executing mini-zk.

Check available commands:

```bash
zk -h
```

Check available options for command `new`:

```bash
zk new -h
```
