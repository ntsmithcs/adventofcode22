def main():
    sums = to_sums("Day1/calories.txt")
    total = get_total(sums, 3)
    print(sums)
    print(total)


def to_sums(filename):
    sums = []
    with open(filename, "r") as f:
        lines = f.readlines()
        current = 0
        for line in lines:
            if line.strip():
                current += int(line)
            else:
                sums.append(current)
                current = 0
        sums.append(current)
    return sorted(sums, reverse=True)


def get_total(arr, n):
    total = 0
    for i in range(n):
        total += arr[i]
    return total


if __name__ == "__main__":
    main()
