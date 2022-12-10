from itertools import islice
import string

filename = "Day3/puzzleInput.txt"
N = 3
sumPriorities = 0

with open(filename, 'r') as f:
    while True:
        group = [x.rstrip('\n') for x in islice(f, N)]
        if not group:
            break
        badge = set(group[0]) & set(group[1]) & set(group[2])
        priority = string.ascii_letters.index(badge.pop()) + 1
        sumPriorities += priority

print(sumPriorities)
