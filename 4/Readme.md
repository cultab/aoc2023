
# Part 1:

```py
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
```
${\texttt{Card  \color{Goldenrod}{\\#4}\color{white} :}}$

${\texttt{ \color{springgreen}{ +1}\color{white}  because of  \color{Maroon}{84!}\color{white}  Matches now are worth  \color{Goldenrod}{1}\color{white} }}$

${\texttt{ \color{springgreen}{1}\color{white}  points from card  \color{Goldenrod}{\\#4}\color{white} }}$

${\texttt{Card  \color{Goldenrod}{\\#5}\color{white} :}}$

${\texttt{ \color{Maroon}{zero}\color{white}  points from card  \color{Goldenrod}{\\#5}\color{white} }}$

${\texttt{Card  \color{Goldenrod}{\\#6}\color{white} :}}$

${\texttt{ \color{Maroon}{zero}\color{white}  points from card  \color{Goldenrod}{\\#6}\color{white} }}$

${\texttt{In total we won  \color{Goldenrod}{13}\color{white}  points!}}$






# Part 2:

```py
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
```

${\texttt{We only have 1  \color{Goldenrod}{\\#1}\color{white} :}}$

${\texttt{ \color{springgreen}{ +1}\color{white}  cards of  \color{Goldenrod}{\\#2}\color{white}  because  \color{Maroon}{48}\color{white}  matched!}}$

${\texttt{ \color{springgreen}{ +1}\color{white}  cards of  \color{Goldenrod}{\\#3}\color{white}  because  \color{Maroon}{17}\color{white}  matched!}}$

${\texttt{ \color{springgreen}{ +1}\color{white}  cards of  \color{Goldenrod}{\\#4}\color{white}  because  \color{Maroon}{83}\color{white}  matched!}}$

${\texttt{ \color{springgreen}{ +1}\color{white}  cards of  \color{Goldenrod}{\\#5}\color{white}  because  \color{Maroon}{86}\color{white}  matched!}}$

${\texttt{We have 2  \color{Goldenrod}{\\#2s}\color{white} :}}$

${\texttt{ \color{springgreen}{ +2}\color{white}  cards of  \color{Goldenrod}{\\#3}\color{white}  because  \color{Maroon}{32}\color{white}  matched!}}$

${\texttt{ \color{springgreen}{ +2}\color{white}  cards of  \color{Goldenrod}{\\#4}\color{white}  because  \color{Maroon}{61}\color{white}  matched!}}$

${\texttt{We have 4  \color{Goldenrod}{\\#3s}\color{white} :}}$

${\texttt{ \color{springgreen}{ +4}\color{white}  cards of  \color{Goldenrod}{\\#4}\color{white}  because  \color{Maroon}{1}\color{white}  matched!}}$

${\texttt{ \color{springgreen}{ +4}\color{white}  cards of  \color{Goldenrod}{\\#5}\color{white}  because  \color{Maroon}{21}\color{white}  matched!}}$

${\texttt{We have 8  \color{Goldenrod}{\\#4s}\color{white} :}}$

${\texttt{ \color{springgreen}{ +8}\color{white}  cards of  \color{Goldenrod}{\\#5}\color{white}  because  \color{Maroon}{84}\color{white}  matched!}}$

${\texttt{We have 14  \color{Goldenrod}{\\#5s}\color{white} :}}$

${\texttt{We only have 1  \color{Goldenrod}{\\#6}\color{white} :}}$

${\texttt{In the end we got:}}$

${\texttt{      1 copies of card  \color{Goldenrod}{\\#1}\color{white} }}$

${\texttt{      2 copies of card  \color{Goldenrod}{\\#2}\color{white} }}$

${\texttt{      4 copies of card  \color{Goldenrod}{\\#3}\color{white} }}$

${\texttt{      8 copies of card  \color{Goldenrod}{\\#4}\color{white} }}$

${\texttt{      14 copies of card  \color{Goldenrod}{\\#5}\color{white} }}$

${\texttt{      1 copies of card  \color{Goldenrod}{\\#6}\color{white} }}$

${\texttt{or  \color{springgreen}{30}\color{white}  cards!}}$

This file was created with help from aha Ansi HTML Adapter. https://github.com/theZiz/aha
