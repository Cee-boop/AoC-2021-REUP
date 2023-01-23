from copy import deepcopy


# part one;
with open(file="data.txt") as file:
    data = file.read().split("\n")
    gamma = epsilon = ""

    for i in range(len(data[0])):
        binary_string = ""
        for j in range(len(data)):
            binary_string += data[j][i]

        zero_count, one_count = binary_string.count("0"), binary_string.count("1")
        if zero_count > one_count:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    print(int(gamma, 2) * int(epsilon, 2))


# part two;
with open(file="data.txt") as file:
    data = file.read().split("\n")
    oxygen, scrubber = deepcopy(data), deepcopy(data)
    
    def check_index(lst, char, index):
        for k in range(len(lst) - 1, -1, -1):
            if len(lst) == 1:
                return lst
            if lst[k][index] != char:
                del lst[k]

        return lst

    for i in range(len(oxygen[0])):
        binary_string = ""
        for j in range(len(oxygen)):
            binary_string += oxygen[j][i]

        zero_count, one_count = binary_string.count("0"), binary_string.count("1")
        if zero_count == one_count:
            oxygen = check_index(oxygen, "1", i)
        elif zero_count > one_count:
            oxygen = check_index(oxygen, "0", i)
        else:
            oxygen = check_index(oxygen, "1", i)

    for i in range(len(scrubber[0])):
        binary_string = ""
        for j in range(len(scrubber)):
            binary_string += scrubber[j][i]

        zero_count, one_count = binary_string.count("0"), binary_string.count("1")
        if zero_count == one_count:
            scrubber = check_index(scrubber, "0", i)
        elif zero_count > one_count:
            scrubber = check_index(scrubber, "1", i)
        else:
            scrubber = check_index(scrubber, "0", i)

    print(int(oxygen[0], 2) * int(scrubber[0], 2))
