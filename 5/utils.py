"""Utilities for advent of code 2023."""
from os import isatty


def isDigit(c: str) -> str | bool:
    return c if c in "0123456789" else False


def oneInput() -> str:
    """Return a list with the first line in the input file."""
    with open("input") as file:
        for line in file:
            return [line.strip()]


def allInput() -> str:
    """Yield all lines in the input file."""
    with open("input") as file:
        for line in file:
            yield line.strip()


def example() -> str:
    """Yield all lines in the example file."""
    with open("example") as file:
        for line in file:
            yield line.strip()


def red(msg: str):
    """Return @msg with termcodes for a red fg color."""
    return "\033[1;31m" + str(msg) + "\033[0m"


def green(msg: str):
    """Return @msg with termcodes for a green fg color."""
    return "\033[1;32m" + str(msg) + "\033[0m"


def yellow(msg: str):
    """Return @msg with termcodes for a yellow fg color."""
    return "\033[1;33m" + str(msg) + "\033[0m"


def blue(msg: str):
    """Return @msg with termcodes for a blue fg color."""
    return "\033[1;34m" + str(msg) + "\033[0m"


def cyan(msg: str):
    """Return @msg with termcodes for a cyan fg color."""
    return "\033[1;35m" + str(msg) + "\033[0m"


def purple(msg: str):
    """Return @msg with termcodes for a purple fg color."""
    return "\033[1;36m" + str(msg) + "\033[0m"


def dim(msg: str):
    """Return @msg with termcodes for a dim fg color."""
    return "\033[2m" + str(msg) + "\033[0m"
