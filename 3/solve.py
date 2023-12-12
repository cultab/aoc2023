#!/usr/bin/env python3

from os import isatty
from collections import defaultdict


def isSymbol(c: str) -> bool:
    symbols = "!@#$%^&*()-=/+"
    return c in symbols


def isDigit(c: str) -> str | bool:
    return c if c in "0123456789" else False


def all_input():
    while True:
        try:
            yield input()
        except EOFError:
            break


def isSymbolAround(i, j):
    for row in range(i - 1, i + 2):
        for col in range(j - 1, j + 2):
            if isSymbol(schematic[row, col]):
                return True

    return False


def parsePartNumber(i, j):
    digits = ""
    is_part = False
    while digit := isDigit(schematic[i, j]):
        if isSymbolAround(i, j):
            is_part = True
        digits += digit
        j += 1
    else:
        number = int(digits)

    # print(f"{number=}")
    return number, is_part, j


schematic = defaultdict(lambda: ".")


def main():
    global schematic
    data: list[str] = [x for x in all_input()]

    for i, line in enumerate(data):
        for j, letter in enumerate(line):
            schematic[i, j] = letter

    sum = 0

    for i, line in enumerate(data):
        j = 0
        while j < len(line):
            char = schematic[i, j]
            if isDigit(char):
                number, isPartNumber, newJ = parsePartNumber(i, j)
                j = newJ
                if isPartNumber:
                    sum += number
                    print(green(number), end="")
                else:
                    print(red(number), end="")
            else:
                if isSymbol(char):
                    print(yellow("Σ"), end="")
                else:
                    print(dim("·"), end="")
                j += 1

        print(sum)

    print(sum)


def red(msg: str):
    return "\033[0;31m" + str(msg) + "\033[0m" if isatty(1) else msg


def green(msg: str):
    return "\033[0;32m" + str(msg) + "\033[0m" if isatty(1) else msg


def yellow(msg: str):
    return "\033[0;33m" + str(msg) + "\033[0m" if isatty(1) else msg


def dim(msg: str):
    return "\033[2m" + str(msg) + "\033[0m" if isatty(1) else msg


if __name__ == "__main__":
    main()
