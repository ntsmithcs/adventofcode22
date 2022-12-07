with open("calories.txt", "r") as f:
    largest = 0
    current = 0
    lines = f.readlines()
    for line in lines:
        if line.strip():
            current += int(line)
        else:
            if current > largest:
                largest = current
            current = 0
    print(str(largest))
