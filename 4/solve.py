#!/usr/bin/env python3
from utils import allInput, oneInput, example, red, green, yellow, dim

sum = 0

for ticket in allInput():
    rest, ourNums = ticket.split("|")
    card, winningNums = rest.split(":")
    winningNums = [int(x) for x in winningNums.split(" ") if x]
    ourNums = (int(x) for x in ourNums.split(" ") if x)
    points = 0
    worth = 1
    print(card + ":")
    for num in ourNums:
        if num in winningNums:
            print(green(f"\t+{worth}") + f" because of {num}!\t" + yellow(f"{worth=}"))
            points += worth
            if points - 1:
                worth *= 2
    print(green(f"{points=}") if points else red(f"{points=}"))
    sum += points

print(yellow(sum))
