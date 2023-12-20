#!/bin/env python3

import sys
from utils import allInput, oneInput, example, red, green, yellow, dim, blue, cyan, purple
from functools import reduce

colors = [red, green, yellow, blue, cyan, purple]


def color(n: int):
    return colors[n % (len(colors) - 1)](n)


class Range():
    """Represents a range from @start to @end."""

    def __init__(self, start, len):
        self.start = start
        self.end = start + len

    def contains(self, n: int) -> bool:
        return self.start < n < self.end

    def __repr__(self) -> str:
        return f"[{self.start:>3},{self.end:>3}]"


class Mapping():
    """Represents a mapping from one range onto another."""

    def __init__(self, string: str):
        lst = [int(x) for x in string.split(" ")]

        self.source = Range(lst[1], lst[2])
        self.dest = Range(lst[0], lst[2])

    def convert(self, n: int) -> int | bool:
        if self.source.contains(n):
            return self.dest.start - self.source.start + n
        else:
            return False

    def __repr__(self) -> str:
        diff = self.dest.start - self.source.start
        if diff > 0:
            return f"{self.source} -> {self.dest} {green(f"+{diff}"):>15}"
        else:
            return f"{self.source} -> {self.dest} {red(diff):>15}"


class Map(list[Mapping]):
    """Represents all mappings of one type."""

    def __init__(self, name: str):
        super().__init__(self)
        self.name = name
        self.source = name.split("-")[0]
        self.dest = name.split("-")[2].split(" ")[0]

    def append(self, string: str):
        if string and not string.__contains__(":"):
            super().append(Mapping(string))

    def convert(self, s: int):
        for mapping in self:
            if ret := mapping.convert(s):
                d = ret
                break
        else:
            d = s

        print(f"{self.source:>15}({color(s)}) -> {self.dest}({color(d)})")
        return d

    def __str__(self):
        string = f"{self.name}\n"
        for mapping in self:
            string += f"{mapping}\n"
        return string


with open("./example") as sys.stdin:
# with open("./input") as sys.stdin:
    seeds = [int(x) for x in input().split(" ")[1:]]
    input()

    seed2soil = Map(input())
    while (line := input()) != "":
        seed2soil.append(line)

    soil2fertilizer = Map(input())
    while (line := input()) != "":
        soil2fertilizer.append(line)

    fertilizer2water = Map(input())
    while (line := input()) != "":
        fertilizer2water.append(line)

    water2light = Map(input())
    while (line := input()) != "":
        water2light.append(line)

    light2temperature = Map(input())
    while (line := input()) != "":
        light2temperature.append(line)

    temperature2humidity = Map(input())
    while (line := input()) != "":
        temperature2humidity.append(line)

    humidity2location = Map(input())
    while (line := input()) != "":
        humidity2location.append(line)

    def seed2location(seed: int):
        soil = seed2soil.convert(seed)
        fertilizer = soil2fertilizer.convert(soil)
        water = fertilizer2water.convert(fertilizer)
        light = water2light.convert(water)
        temperature = light2temperature.convert(light)
        humidity = temperature2humidity.convert(temperature)
        location = humidity2location.convert(humidity)

        return location

    print(f"{seed2soil}")
    print(f"{soil2fertilizer}")
    print(f"{fertilizer2water}")
    print(f"{water2light}")
    print(f"{light2temperature}")
    print(f"{temperature2humidity}")
    print(f"{humidity2location}")

    locations = []
    for seed in seeds:
        print(f"Seed({color(seed)})")
        location = seed2location(seed)
        locations.append(location)
        print(f"Location({color(location)})\n")

    print(reduce(lambda a, b: a if a < b else b, locations))
