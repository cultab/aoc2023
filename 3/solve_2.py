#!/usr/bin/env python3

from os import isatty
from collections import defaultdict
from functools import reduce


def isSymbol(c: str) -> bool:
    symbols = "!@#$%^&*()-=/+"
    return c in symbols


def isDigit(c: str) -> str | bool:
    return c if c in "0123456789" else False


def all_input() -> str:
    while True:
        try:
            yield input()
        except EOFError:
            break


def isSymbolAround(i, j) -> bool:
    for row in range(i - 1, i + 2):
        for col in range(j - 1, j + 2):
            if isSymbol(schematic[row, col]):
                return True

    return False


def numbersAround(i, j) -> dict[(int, int), str]:
    numbers = {}
    for row in range(i - 1, i + 2):
        skip = 0
        for col in range(j - 1, j + 2):
            if col < skip:  # we've gone over this number
                continue
            if isDigit(schematic[row, col]):
                number, pos, skip = parseNumber(row, col)
                numbers[pos] = number

    return numbers


def parseNumber(i, j) -> (str, (int, int), int):
    # search for number's start
    while digit := isDigit(schematic[i, j - 1]):
        j -= 1

    pos = (i, j)
    digits = ""
    while digit := isDigit(schematic[i, j]):
        digits += digit
        j += 1
    else:
        number = int(digits)

    return number, pos, j


def parseGear(i, j) -> int:
    numbers = numbersAround(i, j)
    if len(numbers) == 2:
        ratio = reduce(lambda a, b: a * b, numbers.values())
        return ratio

    return 0


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
            if char == "*":
                if ratio := parseGear(i, j):
                    print(green("*"), end="")
                    sum += ratio
                else:
                    print(red("*"), end="")
            else:
                print(char, end="")
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
