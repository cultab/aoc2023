#!/usr/bin/env python3

import re
from dataclasses import dataclass
from functools import reduce

max = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def all_input():
    while True:
        try:
            yield input()
        except EOFError:
            break


def get_rounds(game: str):
    return game.split(":")[1].split(";")


def get_marbles(round: str):
    marbles = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for color, count in marbles.items():
        if m := re.search(f"([0-9]+) {color}", round):
            marbles[color] = int(m.group(1))

    return marbles


sum_possible = 0
power = 0

for game in all_input():
    id = re.search("([0-9]+):", game).group(1)
    possible = True
    min_possible = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for round in get_rounds(game):
        for color, count in get_marbles(round).items():
            if min_possible[color] < count:
                print(f"Game {id}: needs at least {count} {color} marbles")
                min_possible[color] = count

            if max[color] < count:
                possible = False
                print(
                    f"Game {id}: impossible because {count} {color} marbles > {max[color]} {color} marbles")

    power += reduce(lambda a, b: a * b, min_possible.values())
    if possible:
        sum_possible += int(id)

print(f"{sum_possible=}")
print(f"{power=}")
