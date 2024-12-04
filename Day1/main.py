from helpers import read_lines,abs
from collections import defaultdict

lines = read_lines("input.txt")

list1 = []
list2 = []

for line in lines:
    a,b = line.split("   ")
    list1.append(int(a))
    list2.append(int(b))

list1.sort()
list2.sort()

def part1():
    total = 0
    for a,b in zip(list1, list2):
        difference = abs(a - b)
        total += difference
    return total

print(f"Part 1 {part1()}")

def part2():
    count = defaultdict(lambda: 0)
    for n in list2:
        count[n] += 1

    total = 0
    for n in list1:
        total += (n * count[n])
    return total

print(f"Part 2 {part2()}")