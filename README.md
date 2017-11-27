# argparse-color-formatter
A [`formatter_class` for `argparse`](https://docs.python.org/3/library/argparse.html#formatter-class) that deals with ANSI colour escapes. Specifically, this formatter does not count escape characters as displayed characters when wrapping argparse's help text into the terminal.

> ![That script's help text is so cool...](/acf.png "That script's help text is so cool...")

## Install

```shell
$ pip install argparse-color-formatter
```

## Usage

Pass in `argparse_color_formatter.ColorHelpFormatter` to a new argument parser as `formatter_class`

```python
import argparse
from argparse_color_formatter import ColorHelpFormatter

parser = argparse.ArgumentParser(
    formatter_class=ColorHelpFormatter
)
```

## Before & After
ANSI colour escapes using the default `HelpFormatter`:
![before screenshot](/before.png)

ANSI colour escapes using this libraries new `ColorHelpFormatter`:
![after screenshot](/after.png)
