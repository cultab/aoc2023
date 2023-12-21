"""Utilities for advent of code 2023."""
# from os import isatty
from typing import Iterable


def pairwise(it: Iterable[any]):
    """
    Return pairs from iterable.

    s -> (s0, s1), (s2, s3), (s4, s5), ..."
    """
    a = iter(it)
    return zip(a, a)


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


def red(msg: object, bold=True):
    """Return @msg with termcodes for red text."""
    return _termEncoded(msg, 1 if bold else 0, 31)


def green(msg: object, bold=True):
    """Return @msg with termcodes for green text."""
    return _termEncoded(msg, 1 if bold else 0, 32)


def yellow(msg: object, bold=True):
    """Return @msg with termcodes for yellow text."""
    return _termEncoded(msg, 1 if bold else 0, 33)


def blue(msg: object, bold=True):
    """Return @msg with termcodes for blue text."""
    return _termEncoded(msg, 1 if bold else 0, 34)


def purple(msg: object, bold=True):
    """Return @msg with termcodes for purple text."""
    return _termEncoded(msg, 1 if bold else 0, 35)


def cyan(msg: object, bold=True):
    """Return @msg with termcodes for cyan text."""
    return _termEncoded(msg, 1 if bold else 0, 36)


def dim(msg: object):
    """Return @msg with termcodes for a dim fg color."""
    return _termEncoded(msg, 2, None)


def _termEncoded(msg: any, one: int, two: int) -> str:
    return f"\033[{one}{';' if two else ''}{two if two else ''}m{msg}\033[0m"
