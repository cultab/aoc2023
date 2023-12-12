
# Part 1:

```py
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
```
<pre>
Card <span style="color:olive;">#1</span>:
<span style="color:green;">	+1</span> because of <span style="color:red;">83!</span> Matches now are worth <span style="color:olive;">1</span>
<span style="color:green;">	+1</span> because of <span style="color:red;">86!</span> Matches now are worth <span style="color:olive;">1</span>
<span style="color:green;">	+2</span> because of <span style="color:red;">17!</span> Matches now are worth <span style="color:olive;">2</span>
<span style="color:green;">	+4</span> because of <span style="color:red;">48!</span> Matches now are worth <span style="color:olive;">4</span>
<span style="color:green;">8</span> points from card <span style="color:olive;">#1</span>
Card <span style="color:olive;">#2</span>:
<span style="color:green;">	+1</span> because of <span style="color:red;">61!</span> Matches now are worth <span style="color:olive;">1</span>
<span style="color:green;">	+1</span> because of <span style="color:red;">32!</span> Matches now are worth <span style="color:olive;">1</span>
<span style="color:green;">2</span> points from card <span style="color:olive;">#2</span>
Card <span style="color:olive;">#3</span>:
<span style="color:green;">	+1</span> because of <span style="color:red;">21!</span> Matches now are worth <span style="color:olive;">1</span>
<span style="color:green;">	+1</span> because of <span style="color:red;">1!</span> Matches now are worth <span style="color:olive;">1</span>
<span style="color:green;">2</span> points from card <span style="color:olive;">#3</span>
Card <span style="color:olive;">#4</span>:
<span style="color:green;">	+1</span> because of <span style="color:red;">84!</span> Matches now are worth <span style="color:olive;">1</span>
<span style="color:green;">1</span> points from card <span style="color:olive;">#4</span>
Card <span style="color:olive;">#5</span>:
<span style="color:red;">zero</span> points from card <span style="color:olive;">#5</span>
Card <span style="color:olive;">#6</span>:
<span style="color:red;">zero</span> points from card <span style="color:olive;">#6</span>
In total we won <span style="color:olive;">13</span> points!
</pre>

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

<pre>
We only have 1 <span style="color:olive;">#1</span>:
<span style="color:green;">	+1</span> cards of <span style="color:olive;">#2</span> because <span style="color:red;">48</span> matched!
<span style="color:green;">	+1</span> cards of <span style="color:olive;">#3</span> because <span style="color:red;">17</span> matched!
<span style="color:green;">	+1</span> cards of <span style="color:olive;">#4</span> because <span style="color:red;">83</span> matched!
<span style="color:green;">	+1</span> cards of <span style="color:olive;">#5</span> because <span style="color:red;">86</span> matched!
We have 2 <span style="color:olive;">#2s</span>:
<span style="color:green;">	+2</span> cards of <span style="color:olive;">#3</span> because <span style="color:red;">32</span> matched!
<span style="color:green;">	+2</span> cards of <span style="color:olive;">#4</span> because <span style="color:red;">61</span> matched!
We have 4 <span style="color:olive;">#3s</span>:
<span style="color:green;">	+4</span> cards of <span style="color:olive;">#4</span> because <span style="color:red;">1</span> matched!
<span style="color:green;">	+4</span> cards of <span style="color:olive;">#5</span> because <span style="color:red;">21</span> matched!
We have 8 <span style="color:olive;">#4s</span>:
<span style="color:green;">	+8</span> cards of <span style="color:olive;">#5</span> because <span style="color:red;">84</span> matched!
We have 14 <span style="color:olive;">#5s</span>:
We only have 1 <span style="color:olive;">#6</span>:
In the end we got:
	1 copies of card <span style="color:olive;">#1</span>
	2 copies of card <span style="color:olive;">#2</span>
	4 copies of card <span style="color:olive;">#3</span>
	8 copies of card <span style="color:olive;">#4</span>
	14 copies of card <span style="color:olive;">#5</span>
	1 copies of card <span style="color:olive;">#6</span>
or <span style="color:green;">30</span> cards!
</pre>

This file was created with the aha Ansi HTML Adapter. https://github.com/theZiz/aha
