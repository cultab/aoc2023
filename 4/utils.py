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
    return "\033[0;31m" + str(msg) + "\033[0m" if isatty(1) else msg


def green(msg: str):
    """Return @msg with termcodes for a green fg color."""
    return "\033[0;32m" + str(msg) + "\033[0m" if isatty(1) else msg


def yellow(msg: str):
    """Return @msg with termcodes for a yellow fg color."""
    return "\033[0;33m" + str(msg) + "\033[0m" if isatty(1) else msg


def dim(msg: str):
    """Return @msg with termcodes for a dim fg color."""
    return "\033[2m" + str(msg) + "\033[0m" if isatty(1) else msg
