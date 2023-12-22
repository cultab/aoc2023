#!/bin/env python3

import sys

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

    # def __iand__(s, o):
    #     ret = []
    #
    #     if o < s:
    #         ret.append(o)
    #
    #     if s < o:
    #         ret.append(o)
    #
    #     if o.start >= s.start and o.end <= s.start:
    #         ret.append(o)
    #
    #     if o.start < o.end < s.end:
    #         ret.append(Range[o.start, s.start - 1])
    #         ret.append(Range[s.start, o.end])
    #
    #     if s.start < o.start < o.end < s.end:
    #         ret.append(o)
    #
    #     if s.start < o.start < s.end < o.end:
    #         ret.append(Range[o.start, s.end - 1])
    #         ret.append(Range[s.end, o.end])
    #
    #
    #
    # def __lt__(self, other):
    #     return self.end < other.start
    #
    # def __gt__(self, other):
    #     return self.start > other.end

    def __repr__(self) -> str:
        return f"[{self.start:>3},{self.end:>3}]"


class Mapping():
    """Represents a mapping from one range onto another."""

    def __init__(self, string: str):
        lst = [int(x) for x in string.split(" ")]

        self.src = Range(lst[1], lst[1] + lst[2])
        self.dst = Range(lst[0], lst[0] + lst[2])
        self.diff = self.dst.start - self.src.start

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
        ret = Range(self.convert(start), self.convert(end))
        if self.convert(start) == 53:
            print("============================")
            print(f"{end=}")
            print(f"{ret=}")
        return ret

    def convertRange(self, r: Range) -> (list[Range], Range):
        converted: Range = None
        same = []
        if r.end < self.src.start:
            same.append(r)
        elif self.src.start < r.start < self.src.end < r.end:
            converted = self.convertEndpoints(r.start, self.src.end)
            same.append(Range(self.src.end + 1, r.end))
        elif r.start < self.src.start < r.end < self.src.end:
            same.append(Range(r.start, self.src.start - 1),)
            converted = self.convertEndpoints(self.src.start, r.end)
        elif self.src.start < r.start < r.end < self.src.end:
            converted = self.convertEndpoints(r.start, r.end)
        elif r.start < self.src.start < self.src.end < r.end:
            same.append(Range(r.start, self.src.start-1))
            converted = self.convertEndpoints(self.src.start, self.src.end)
            same.append(Range(self.src.end + 1, r.end))
        elif self.src.end < r.start:
            same.append(r)

        # print(f"{same=}\n{converted=}")
        return same, converted

    def __repr__(self) -> str:
        diff = self.dst.start - self.src.start
        if diff > 0:
            return f"{self.src} -> {self.dst} {green(f'+{diff}'):>15}"
        else:
            return f"{self.src} -> {self.dst} {red(diff):>15}"

    def getDiff(self) -> str:
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

        print(f"{self.src:>15}({color(s)}) -> {self.dst}({color(d)})")
        return d

    def convertRange(self, r: Range) -> list[Range]:
        check = [r]
        converted = []
        while check:
            rng = check.pop()
            for mapping in self:
                checkNext, conv = mapping.convertRange(rng)
                if conv:
                    print(f"          {mapping.getDiff()}")
                    print(f"{rng} -> {conv}")
                    check.extend(checkNext)
                    converted.append(conv)
                    break
            else:
                if check:
                    print(f"          {yellow('~')}")
                    print(f"{r} -> {check[0]}...")
                    converted.extend(check)
                else:
                    print(f"          {yellow('~')}")
                    print(f"{r} == {rng}...")
                    converted.append(rng)
                break

        return converted

    def __str__(self):
        string = f"{self.name}\n"
        for mapping in self:
            string += f"{mapping}\n"
        return string


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


def seed2location(seed: int):
    soil = seed2soil.convert(seed)
    fertilizer = soil2fertilizer.convert(soil)
    water = fertilizer2water.convert(fertilizer)
    light = water2light.convert(water)
    temperature = light2temperature.convert(light)
    humidity = temperature2humidity.convert(temperature)
    location = humidity2location.convert(humidity)

    return location


# print(f"{seed2soil}")
# print(f"{soil2fertilizer}")
# print(f"{fertilizer2water}")
# print(f"{water2light}")
# print(f"{light2temperature}")
# print(f"{temperature2humidity}")
# print(f"{humidity2location}")

maps = [
    seed2soil,
    soil2fertilizer,
    fertilizer2water,
    water2light,
    light2temperature,
    temperature2humidity,
    humidity2location,
]

last = []

for seed_range in seed_ranges:
    print(seed_range)
    converting = [seed_range]
    toConvert = []
    for m in maps:
        print("using the", m)
        print("\tconverting", converting)
        for rng in converting:
            # print("->>>", rng)
            toConvert.extend(m.convertRange(rng))
            print("up next", toConvert)
            # print(rng, " becomes: \n")
            # for c in toConvert:
            #     print(f"\t{c}")
        converting.clear()
        converting = toConvert
        last = converting
        toConvert = []


m = last[0].start
for r in last:
    if r.start < m:
        m = r.start

print("====================================")
print(m)
print("====================================")
# locations = []
# for seed in seeds:
#     print(f"Seed({color(seed)})")
#     location = seed2location(seed)
#     locations.append(location)
#     print(f"Location({color(location)})\n")
#
# print(reduce(lambda a, b: a if a < b else b, locations))
