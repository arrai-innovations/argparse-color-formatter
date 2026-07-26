# argparse-color-formatter

An ANSI-aware [`formatter_class` for `argparse`](https://docs.python.org/3/library/argparse.html#formatter-class).
It calculates layout using the visible width of help text, without counting ANSI
escape sequences as displayed characters.

![That script's help text is so cool...](https://docs.arrai.dev/argparse-color-formatter/readme/acf.png "That script's help text is so cool...")

[![PYPI](https://img.shields.io/pypi/v/argparse-color-formatter?style=for-the-badge)](https://pypi.org/project/argparse-color-formatter/)

![Tests](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/python314.svg) [![Coverage](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/python314.coverage.svg)](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/htmlcov_python314/)

![Tests](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/python313.svg) [![Coverage](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/python313.coverage.svg)](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/htmlcov_python313/)

![Tests](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/python312.svg) [![Coverage](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/python312.coverage.svg)](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/htmlcov_python312/)

![Tests](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/python311.svg) [![Coverage](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/python311.coverage.svg)](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/htmlcov_python311/)

![Tests](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/python310.svg) [![Coverage](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/python310.coverage.svg)](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/htmlcov_python310/)

![Tests](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/python39.svg) [![Coverage](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/python39.coverage.svg)](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/htmlcov_python39/)

![Ruff](https://docs.arrai.dev/argparse-color-formatter/artifacts/main/ruff.svg)

## Install

```shell
$ pip install argparse-color-formatter
```

## What it does

This package does not decide which text to colour. Your application supplies the
ANSI-coloured program names, metavars, descriptions, help strings, or epilogues.
`ColorHelpFormatter` then:

- wraps descriptions, help strings, and usage text at their visible width;
- aligns option and positional argument labels correctly; and
- preserves ANSI sequences in the formatted output.

Without an ANSI-aware formatter, invisible escape sequences can make `argparse`
wrap text too early or misalign help columns.

## Do I need this on Python 3.14?

Python 3.14 added [native colour support to `argparse`](https://docs.python.org/3.14/library/argparse.html#color).
If you only want the standard `argparse` colour theme, you do not need this
package.

This package is still useful when your application embeds its own ANSI sequences
in descriptions, help strings, program names, or metavars. Python 3.14 accounts
for its own theme in some layout calculations, but still wraps arbitrary
application-coloured descriptions and help strings using their encoded length.
`ColorHelpFormatter` handles those sequences by their visible width and preserves
the native Python 3.14 theme alongside them.

## Python 3.9 to 3.13

These Python versions do not add colours to `argparse` help. Use a library such
as [`ansicolors`](https://pypi.org/project/ansicolors/) or generate ANSI
sequences directly, then use `ColorHelpFormatter` to keep the resulting output
aligned and wrapped correctly.

## Usage

Pass `ColorHelpFormatter` to an argument parser as `formatter_class`. The example
uses `ansicolors`, which is installed as a dependency of this package.

```python
import argparse

from colors import bold

from argparse_color_formatter import ColorHelpFormatter

output = bold("FILE")
parser = argparse.ArgumentParser(
    description=f"Write the generated report to {output}.",
    formatter_class=ColorHelpFormatter,
)
parser.add_argument(
    "--output",
    metavar=output,
    help=f"save the report as {output}",
)
```

## Development

### Setup

```shell
pipenv install --dev
pre-commit install
pre-commit install --hook-type commit-msg
```

### Build

```shell
pipenv run build
```

### Test

```shell
pipenv run test
```

## After and before

ANSI colour escapes using this library's `ColorHelpFormatter`:

![after screenshot](https://docs.arrai.dev/argparse-color-formatter/readme/after.png)

ANSI colour escapes using the default `HelpFormatter`:

![before screenshot](https://docs.arrai.dev/argparse-color-formatter/readme/before.png)
