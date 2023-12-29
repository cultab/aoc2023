from enum import Enum, auto
from functools import reduce

from collections import OrderedDict
from utils import allInput, example, red, green, yellow, blue, cyan, purple, dim


# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456
class Type(Enum):
    High_Card = 0
    One_Pair = 1e6
    Two_Pairs = 2e6
    Three_of_a_Kind = 3e6
    Full_House = 4e6
    Four_of_a_Kind = 5e6
    Five_of_a_Kind = 6e6

    def __str__(self):
        return self._name_.replace("_", " ")


def cardToValue(card: str) -> int:  # base13
    return {
        "A": 12,
        "K": 11,
        "Q": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
        "J": 0,
    }[card]


class Hand:
    def __init__(self, hand: str, bid: int):
        self.bid = bid
        self.type, colors = getType(hand)

        self.repr = ""
        for card in hand:
            self.repr += colors[card](card)

        self.value = int(self.type._value_)
        print(
            f"{self} is a hand of {cyan(self.type)} worth {yellow(self.value)} points!"
        )
        for i, card in enumerate(hand):
            extra = cardToValue(card) * (13 ** (4 - i))
            self.value += extra
            print(f"    {colors[card](card)} is worth {green(f'+{extra}'):>18} points!")
        print(f"  It ends up with a worth of {yellow(self.value)} points!")
        # self.value = int(self.type._value_ + int(extra, base=16))

    def __str__(self):
        return self.repr


def getType(hand_str: str) -> (Type, dict[str, callable]):
    type: Type = Type.High_Card
    hand = OrderedDict()
    for card in hand_str:
        if hand.get(card):
            hand[card] += 1
        else:
            hand[card] = 1

    colors = {}

    # jokers = reduce(lambda jokers, card: jokers + 1 if card == "J" else jokers, hand_str, 0)

    no_jokers = (x for x in hand.items() if x[0] != "J")
    for card, count in no_jokers:
        colors[card] = purple
        match (count, type):
            case [5, _]:
                type = Type.Five_of_a_Kind
            case [4, _]:
                type = Type.Four_of_a_Kind
            case [3, Type.One_Pair]:
                colors[card] = cyan
                type = Type.Full_House
            case [3, _]:
                type = Type.Three_of_a_Kind
            case [2, Type.Three_of_a_Kind]:
                colors[card] = cyan
                type = Type.Full_House
            case [2, Type.One_Pair]:
                colors[card] = cyan
                type = Type.Two_Pairs
            case [2, _]:
                type = Type.One_Pair
            case [1, _]:
                colors[card] = dim

    colors["J"] = red
    card = "J"
    if count := hand.get(card):
        # only_jokers = (x for x in hand.items() if x[0] == "J")
        match (count, type):
            case [5, _]:
                type = type.Five_of_a_Kind
            case [4, Type.High_Card]:
                type = Type.Five_of_a_Kind
            case [3, Type.One_Pair]:
                type = Type.Five_of_a_Kind
            case [3, Type.High_Card]:
                type = Type.Four_of_a_Kind
            case [2, Type.Three_of_a_Kind]:
                type = Type.Five_of_a_Kind
            case [2, Type.One_Pair]:
                type = Type.Four_of_a_Kind
            case [2, Type.High_Card]:
                type = Type.Three_of_a_Kind
            case [1, Type.Four_of_a_Kind]:
                type = Type.Five_of_a_Kind
            case [1, Type.Three_of_a_Kind]:
                type = Type.Four_of_a_Kind
            case [1, Type.Two_Pairs]:
                type = Type.Full_House
            case [1, Type.One_Pair]:
                type = Type.Three_of_a_Kind
            case [1, Type.High_Card]:
                type = Type.One_Pair

    return type, colors


def parse():
    for line in allInput():
        # for line in example():
        hand, bid = line.split(" ")
        yield hand, int(bid)


hands = []

for hand, bid in parse():
    h = Hand(hand, int(bid))
    hands.append(h)

hands.sort(key=lambda a: a.value)

winnings = 0
for rank, hand in enumerate(hands, start=1):
    won = hand.bid * rank
    winnings += won
    print(
        f"{hand} ({cyan(hand.type)}) is worth {yellow(hand.value):>17} points with a bid of {green(f'$ {hand.bid}')}"
    )
    print(f"winning an additional {green(f'$ {won:>4}')}")

print(f"In the end we won {green(f'$ {winnings}')}!")

# 244889152
# 244434862
# 244848487
