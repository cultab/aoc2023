#!/bin/env python3

import sys
from functools import reduce

from utils import (
    blue,
    cyan,
    green,
    pairwise,
    purple,
    red,
    yellow,
)

colors = [red, green, yellow, blue, cyan, purple]


def color(n: int):
    return colors[n % (len(colors) - 1)](n)


class Range():
    """Represents a range from @start to @end."""

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def contains(self, n: int) -> bool:
        return self.start <= n <= self.end

    def __repr__(self) -> str:
        """Return string representation of the Range."""
        return f"[{self.start:>2},{self.end:>3}]"


class Mapping():
    """Represents a mapping from one range onto another."""

    def __init__(self, string: str):
        lst = [int(x) for x in string.split(" ")]

        self.src = Range(lst[1], lst[1] + lst[2])
        self.dst = Range(lst[0], lst[0] + lst[2])
        self.diff = self.dst.start - self.src.start

    @classmethod
    def fromRanges(cls, src: Range, dst: Range):
        assert src.end - src.start == dst.end - dst.start
        return cls(f"{dst.start} {src.start} {src.end - src.start}")

    def convert(self, n: int) -> int | bool:
        """Convert."""
        if self.src.contains(n):
            return self.diff + n
        else:
            return False

    def convertEndpoints(self, start: int, end: int) -> Range:
        """
        Convert source range to destination range.

        Implies that start and end are within the source range.
        """
        return Range(self.convert(start), self.convert(end))

    def convertRange(self, r: Range) -> (list[Range], Range):
        converted: Mapping = None
        same = []
        if r.end < self.src.start:
            same.append(r)
        elif self.src.start <= r.start < self.src.end < r.end:
            converted = Mapping.fromRanges(
                Range(r.start, self.src.end),
                self.convertEndpoints(r.start, self.src.end)
            )
        elif r.start < self.src.start < r.end <= self.src.end:
            same.append(Range(r.start, self.src.start - 1),)
            converted = Mapping.fromRanges(
                Range(self.src.start, r.end),
                self.convertEndpoints(self.src.start, r.end))
        elif self.src.start <= r.start <= r.end <= self.src.end:
            converted = Mapping.fromRanges(
                r,
                self.convertEndpoints(r.start, r.end)
            )
        elif r.start < self.src.start < self.src.end < r.end:
            same.append(Range(r.start, self.src.start - 1))
            converted = Mapping.fromRanges(
                self.src,
                self.convertEndpoints(self.src.start, self.src.end)
            )
            same.append(Range(self.src.end + 1, r.end))
        elif self.src.end < r.start:
            same.append(r)

        return same, converted

    def __repr__(self) -> str:
        return f"{self.src} ->[{self.getColoredDiff():>14}]-> {self.dst}"

    def getColoredDiff(self) -> str:
        return green(f"+{self.diff}") if self.diff > 0 else red(self.diff)


class Map(list[Mapping]):
    """Represents all mappings of one type."""

    def __init__(self, name: str):
        super().__init__(self)
        self.name = name
        self.src = name.split("-")[0]
        self.dst = name.split("-")[2].split(" ")[0]

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

        diff = mapping.getColoredDiff() if d != s else yellow("==>")
        print(
            f"{self.src:>15}({color(s)}) ->[{diff:>14}]-> {self.dst}({color(d)})")
        return d

    def tryConvertRange(self, in_range: Range):
        rangesToCheck = [in_range]
        while rangesToCheck:
            r = rangesToCheck.pop()
            for mapping in self:
                checkNext, conv = mapping.convertRange(r)
                if conv:
                    print(
                        f"{conv.src} ->[{mapping.getColoredDiff():>14}]-> {conv.dst}")
                    rangesToCheck.extend(checkNext)
                    yield conv.dst
                    break
            else:  # if we can't convert this range with any mapping, just return it
                print(f"{r} ->[{yellow('==>')}]-> {r}")
                yield r

    def __str__(self):
        """Return string representation of all the mappings."""
        src = map.name.split("-")[0]
        dst = map.name.split("-")[2].split(" ")[0]
        string = f"map from {blue(src)} to {blue(dst)}" + " {\n"
        for mapping in self:
            string += f"\t{mapping}\n"
        return string + "}"


# sys.stdin = open("example")
sys.stdin = open("input")

seed_ranges = []
for start, length in pairwise(input().split(" ")[1:]):
    print(start, length)
    seed_ranges.append(Range(int(start), int(start) + int(length)))

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

maps = [
    seed2soil,
    soil2fertilizer,
    fertilizer2water,
    water2light,
    light2temperature,
    temperature2humidity,
    humidity2location,
]

locations = []

for seed_range in seed_ranges:
    print(seed_range)
    converting = [seed_range]
    toConvert = []
    for map in maps:
        print(map)
        for rng in converting:
            for each in map.tryConvertRange(rng):
                toConvert.append(each)
            # toConvert.extend(map.tryConvertRange(rng))
        converting.clear()
        converting = toConvert
        toConvert = []
    else:  # when we are at the final map aka:
        locations.extend(converting)  # to location, save the locations

print("Finally we got these location ranges for our seeds:")
for loc in locations:
    print(loc)

print(f"{reduce(lambda a, b: a if a.start < b.start else b, locations).start:,d}")
