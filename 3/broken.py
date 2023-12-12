#!/usr/bin/env python3


data = list()

try:
    while True:
        data.append(input())
except EOFError:
    pass

symbol_chars = "%-*$+/@=&#"


def peek(row: int, col: int):
    if not 0 <= row < len(data):
        return ""
    if not 0 <= col < len(data[0]):
        return ""

    return data[row][col]


def is_symbol(row: int, col: int):
    if c := peek(row, col):
        if c in symbol_chars:
            return c
    return False


def symbols_around(row: int, col_start: int, col_end: int):
    symbols = []
    for k in range(row - 1, row + 2):
        for v in range(col_start - 1, col_end + 2):
            if c := is_symbol(k, v):
                symbols.append(c)

    if symbols:
        return symbols
    return False


def is_digit(char: str):
    return char in "0123456789"


def main():
    # parts: dict[set] = { }
    # for s in symbol_chars:
    #     parts[s] = set()
    parts = []

    for i, line in enumerate(data):
        num = ""
        # print(line)
        for j, char in enumerate(line):
            if is_digit(char):
                num += char
                if j < len(data[0]) - 1:
                    continue

            if num:  # and char is not a digit
                if symbols := symbols_around(i, j - len(num), j - 1):
                    symbols.append(1)
                    parts.append(int(num))
                    # for s in symbols:
                    #     parts[s].add(int(num))
                    green(num)
                else:
                    red(num)
                num = ""
                if is_symbol(i, j):
                    yellow(peek(i, j))
                elif not is_digit(char):
                    print(peek(i, j), end="")
                continue

            if is_symbol(i, j):
                yellow(peek(i, j))
            else:
                print(peek(i, j), end="")
        print()

    return parts


def ble(*args):
    print("\033[0;34m", end="")
    print(*args, end="")
    print("\033[0m", end="")


def yellow(*args):
    print("\033[0;33m", end="")
    print(*args, end="")
    print("\033[0m", end="")


def green(*args):
    print("\033[0;32m", end="")
    print(*args, end="")
    print("\033[0m", end="")


def red(*args):
    print("\033[0;31m", end="")
    print(*args, end="")
    print("\033[0m", end="")


if __name__ == "__main__":
    parts = main()
    sum = 0
    for a in parts:
        sum += a
    # for s, part_nums in parts.items():
    #     print(f"Part {s} nums:")
    #     for part in part_nums:
    #         print(f"#{part} ", end="")
    #         sum += part
    #     print()
    print(sum)

    # print(reduce(lambda a, b: a + b, parts))
