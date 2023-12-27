import sys
from functools import reduce
from math import sqrt, ceil, floor

from utils import (
    blue,
    cyan,
    green,
    pairwise,
    purple,
    red,
    yellow,
)

sys.stdin = open("./input")
# sys.stdin = open("./example")

duration = int(input().split(":")[1].replace(" ", ""))
record = int(input().split(":")[1].replace(" ", ""))

# We want distance > record
#
# distance = speed * time
# speed = hold time
# time = race duration - hold time
#
# distance = hold time * (race duration -  hold time)
#          = hold time *  race duration - (hold time)²
#
# distance > record
#
# find ∀ integer h where f(h) = - h² + (h * d) > r
# where h = hold time,
#       d = race duration,
#       r = record
#
# g(h) = -h² + (h * d) - r > 0
# g'(h) = -2h + d
# g"(h) = -2 => g(h) is always concave
#
# find roots, where g(h) = 0 => h² - h⋅d - r = 0
#
# quadratic formula for a = 1, b = -d, c = r
#
#     d ± √(d² - 4r)
# h = --------------
#           2
# without loss of generallity  assume h₁ < h₂
#
# solution = floor(h₂) - ceil(h₁) + 1

root1 = (duration + sqrt(duration**2 - 4 * record)) / 2
root2 = (duration - sqrt(duration**2 - 4 * record)) / 2
# root1 must be always smaller than root2
if root1 > root2:
    root1, root2 = root2, root1

# account for root being integer,
# we want numbers inside the range, exclusive of the endpoints
if root1 == int(root1):
    root1 += 1
if root2 == int(root2):
    root2 -= 1

print(f"{root1=}")
print(f"{root2=}")
start = ceil(root1)
end = floor(root2)
print(f"[{start},{end}]")
print(end - start + 1)
