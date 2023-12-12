#!/usr/bin/env python3

import re

DEBUG = True
# DEBUG = False

def printd(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def is_digit(char):
    if char in [str(x) for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]:
        return int(char)
    else:
        return None


def all_input():
    while True:
        try:
            yield input()
        except EOFError:
            break


look = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def parse(line):
    while line:
        if digit := is_digit(line[0]):
            yield int(digit)
        else:
            for pattern, value in look.items():
                if re.match(pattern, line):
                    yield value
                    break  # not really needed, just saves cycles

        line = line[1:]


sum = 0

for line in all_input():
    first = ''
    second = ''
    printd(f"{line} -> ", end="")
    for digit in parse(line):
        printd(digit, end="")
        if not first:
            first = digit

        second = digit
    printd()

    # print(f"{first}{second}")
    sum += int(f"{first}{second}")

print(sum)
