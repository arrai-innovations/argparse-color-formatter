# argparse-color-formatter
A [`formatter_class` for `argparse`](https://docs.python.org/3/library/argparse.html#formatter-class) that deals with ANSI colour escapes. Specifically, this formatter does not count escape characters as displayed characters when wrapping argparse's help text into the terminal.

![That script's help text is so cool...](https://docs.arrai.dev/argparse-color-formatter/readme/acf.png "That script's help text is so cool...")

[![PYPI](https://img.shields.io/pypi/v/argparse-color-formatter?style=for-the-badge)](https://pypi.org/project/argparse-color-formatter/)

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

## Usage

Pass in `argparse_color_formatter.ColorHelpFormatter` to a new argument parser as `formatter_class`

```python
import argparse
from argparse_color_formatter import ColorHelpFormatter

parser = argparse.ArgumentParser(
    formatter_class=ColorHelpFormatter
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

## After & Before
ANSI colour escapes using this library's new `ColorHelpFormatter`:
![after screenshot](https://docs.arrai.dev/argparse-color-formatter/readme/after.png)

ANSI colour escapes using the default `HelpFormatter`:
![before screenshot](https://docs.arrai.dev/argparse-color-formatter/readme/before.png)
