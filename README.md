# argparse-color-formatter
A [`formatter_class` for `argparse`](https://docs.python.org/3/library/argparse.html#formatter-class) that deals with ANSI colour escapes. Specifically, this formatter does not count escape characters as displayed characters when wrapping argparse's help text into the terminal.

> ![That script's help text is so cool...](https://docs.arrai-dev.com/argparse-color-formatter/readme/acf.png "That script's help text is so cool...")

###### master

![Tests](https://docs.arrai-dev.com/argparse-color-formatter/master.python38.svg) [![Coverage](https://docs.arrai-dev.com/argparse-color-formatter/master.python38.coverage.svg)](https://docs.arrai-dev.com/argparse-color-formatter/htmlcov_master_python38/)

![Tests](https://docs.arrai-dev.com/argparse-color-formatter/master.python37.svg) [![Coverage](https://docs.arrai-dev.com/argparse-color-formatter/master.python37.coverage.svg)](https://docs.arrai-dev.com/argparse-color-formatter/htmlcov_master_python37/)

![Tests](https://docs.arrai-dev.com/argparse-color-formatter/master.python36.svg) [![Coverage](https://docs.arrai-dev.com/argparse-color-formatter/master.python36.coverage.svg)](https://docs.arrai-dev.com/argparse-color-formatter/htmlcov_master_python36/)

![Tests](https://docs.arrai-dev.com/argparse-color-formatter/master.python27.svg) [![Coverage](https://docs.arrai-dev.com/argparse-color-formatter/master.python27.coverage.svg)](https://docs.arrai-dev.com/argparse-color-formatter/htmlcov_master_python27/)

![Flake8](https://docs.arrai-dev.com/argparse-color-formatter/master.flake8.svg)

###### develop

![Tests](https://docs.arrai-dev.com/argparse-color-formatter/develop.python38.svg) [![Coverage](https://docs.arrai-dev.com/argparse-color-formatter/develop.python38.coverage.svg)](https://docs.arrai-dev.com/argparse-color-formatter/htmlcov_develop_python38/)

![Tests](https://docs.arrai-dev.com/argparse-color-formatter/develop.python37.svg) [![Coverage](https://docs.arrai-dev.com/argparse-color-formatter/develop.python37.coverage.svg)](https://docs.arrai-dev.com/argparse-color-formatter/htmlcov_develop_python37/)

![Tests](https://docs.arrai-dev.com/argparse-color-formatter/develop.python36.svg) [![Coverage](https://docs.arrai-dev.com/argparse-color-formatter/develop.python36.coverage.svg)](https://docs.arrai-dev.com/argparse-color-formatter/htmlcov_develop_python36/)

![Tests](https://docs.arrai-dev.com/argparse-color-formatter/develop.python27.svg) [![Coverage](https://docs.arrai-dev.com/argparse-color-formatter/develop.python27.coverage.svg)](https://docs.arrai-dev.com/argparse-color-formatter/htmlcov_develop_python27/)

![Flake8](https://docs.arrai-dev.com/argparse-color-formatter/develop.flake8.svg)

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
![before screenshot](https://docs.arrai-dev.com/argparse-color-formatter/readme/before.png)

ANSI colour escapes using this libraries new `ColorHelpFormatter`:
![after screenshot](https://docs.arrai-dev.com/argparse-color-formatter/readme/after.png)
