#!/usr/bin/env python3
from utils import allInput, oneInput, example, red, green, yellow, dim
from functools import reduce


cards: dict[int, int] = {}
for ticket in example():
    rest, ourNums = ticket.split("|")
    id, winningNums = rest.split(":")
    winningNums = set(int(x) for x in winningNums.split(" ") if x)
    ourNums = set(int(x) for x in ourNums.split(" ") if x)
    *_, id = id.split(" ")
    id = int(id)

    if cards.get(id):
        cards[id] += 1
        print(f"We have {cards[id]}", yellow(f"#{id}s") + ":")
    else:
        cards[id] = 1
        print("We only have 1", yellow(f"#{id}") + ":")

    matches = winningNums & ourNums

    for copy, match in enumerate(matches, start=id + 1):
        if cards.get(copy):
            cards[copy] += cards[id]
        else:
            cards[copy] = cards[id]
        print(green(f"\t+{cards[id]}"), "cards of", yellow(f"#{copy}"), "because", red(f"{match}"), "matched!")

sum = 0
print("In the end we got:")
for card, copies in cards.items():
    sum += copies
    print(f"\t{copies} copies of card", yellow(f"#{card}"))

print("or", green(f"{sum}"), "cards!")
