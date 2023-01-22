# part one;
with open(file="data.txt") as file:
    sonar_report = list(map(int, file.read().split("\n")))
    increases = 0
    for i in range(1, len(sonar_report)):
        if sonar_report[i] > sonar_report[i - 1]:
            increases += 1

    print(increases)


# part two;
with open(file="data.txt") as file:
    sonar_report = list(map(int, file.read().split("\n")))
    increases = 0
    start = 0
    current_sum = 0
    previous_sum = None

    for end, num in enumerate(sonar_report):
        current_sum += num
        if end - start + 1 == 3:
            if previous_sum is not None and current_sum > previous_sum:
                increases += 1

            previous_sum = current_sum
            current_sum -= sonar_report[start]
            start += 1

    print(increases)
