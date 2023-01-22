# part one;
with open(file="data.txt") as file:
    data = file.read().split("\n")
    horizontal_pos = horizontal_depth = 0

    for entry in data:
        direction, unit = entry.split(" ")
        if direction == "forward":
            horizontal_pos += int(unit)
        elif direction == "down":
            horizontal_depth += int(unit)
        else:
            horizontal_depth -= int(unit)

    print(horizontal_depth * horizontal_pos)


# part two;
with open(file="data.txt") as file:
    data = file.read().split("\n")
    aim = horizontal_pos = horizontal_depth = 0

    for entry in data:
        direction, unit = entry.split(" ")
        if direction == "forward":
            horizontal_pos += int(unit)
            horizontal_depth += (aim * int(unit))
        elif direction == "down":
            aim += int(unit)
        else:
            aim -= int(unit)

    print(horizontal_depth * horizontal_pos)
