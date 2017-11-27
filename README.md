# argparse-color-formatter
a [`formatter_class` for `argparse`](https://docs.python.org/3/library/argparse.html#formatter-class) that knows how to
 deal with ansi color escapes. specifically, this formatter does not count ansi color escape characters as displayed
 characters when wrapping argparse's help text into the terminal.

> ![That script's help text is so cool...](/acf.png "That script's help text is so cool...")

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
Ansi color escapes using the default `HelpFormatter`:
[before screenshot](/before.png)

Ansi color escapes using this libraries new `ColorHelpFormatter`:
[after screenshot](/after.png)
