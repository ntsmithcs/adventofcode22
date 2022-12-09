
import string
sumOfPriorities = 0
with open("Day3/puzzleInput.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        half = int(len(line)/2)
        first = line[0:half]
        second = line[half: len(line)]
        common = set(first).intersection(second).pop()
        priority = string.ascii_letters.index(common) + 1
        sumOfPriorities += priority
print(sumOfPriorities)
