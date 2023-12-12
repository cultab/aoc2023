#!/usr/bin/env python3
from utils import allInput, oneInput, example, red, green, yellow, dim

sum = 0

for ticket in example():
    rest, ourNums = ticket.split("|")
    card, winningNums = rest.split(":")
    winningNums = [int(x) for x in winningNums.split(" ") if x]
    ourNums = (int(x) for x in ourNums.split(" ") if x)
    *_, card = card.split(" ")
    card = int(card)

    points = 0
    worth = 1
    print("Card", yellow(f"#{card}") + ":")
    for num in ourNums:
        if num in winningNums:
            print(green(f"\t+{worth}"), "because of", red(f"{num}!"), "Matches now are worth", yellow(f"{worth}"))
            points += worth
            if points - 1:
                worth *= 2
    if points:
        print(green(f"{points}"), "points from card", yellow(f"#{card}"))
    else:
        print(red("zero"), "points from card", yellow(f"#{card}"))
    sum += points

print("In total we won", yellow(sum), "points!")
