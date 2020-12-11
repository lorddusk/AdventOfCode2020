from utils.read import file


def part1(input, last_number):
    dif = []
    for n in input:
        dif.append(n - last_number)
        last_number = n
    dif.append(3)
    return dif


def part2(input):
    temp_list = []
    mult_list = []
    for n in input:
        if n != 3:
            temp_list.append(n)

        elif n == 3:
            if len(temp_list) > 3:
                mult_list.append((len(temp_list) - 1) * 2 + (len(temp_list) - 3))
            elif len(temp_list) > 1:
                mult_list.append((len(temp_list) - 1) * 2)
            temp_list = []

    r2 = 1
    for x in mult_list:
        r2 = r2 * x
    return r2


if __name__ == '__main__':
    input = sorted(file("day10", 1))
    exampleInput = sorted([16,
                           10,
                           15,
                           5,
                           1,
                           11,
                           7,
                           19,
                           6,
                           12,
                           4])

    exampleInput2 = sorted([28,
                            33,
                            18,
                            42,
                            31,
                            14,
                            46,
                            20,
                            48,
                            47,
                            24,
                            23,
                            49,
                            45,
                            19,
                            38,
                            39,
                            11,
                            1,
                            32,
                            25,
                            35,
                            8,
                            17,
                            7,
                            9,
                            4,
                            2,
                            34,
                            10,
                            3])

    print("Example Part 1")
    check = part1(exampleInput, 0)
    check = check.count(1) * check.count(3)
    if check == 35:
        print(f"Correct value : {check}")
    else:
        print(f"Incorrect value : {check}")

    check = part1(exampleInput2, 0)
    check = check.count(1) * check.count(3)
    if check == 220:
        print(f"Correct value : {check}")
    else:
        print(f"Incorrect value : {check}")
    print("------------------------------------------------------")

    print("Part 1")
    check = part1(input, 0)
    check = check.count(1) * check.count(3)
    if check == 2263:
        print(f"Correct value : {check}")
    else:
        print(f"Incorrect value : {check}")
    print("------------------------------------------------------")

    print("Example Part 2")
    check = part1(exampleInput, 0)
    check = part2(check)
    if check == 8:
        print(f"Correct value : {check}")
    else:
        print(f"Incorrect value : {check}")
    check = part1(exampleInput2, 0)
    check = part2(check)
    if check == 19208:
        print(f"Correct value : {check}")
    else:
        print(f"Incorrect value : {check}")
    print("------------------------------------------------------")

    print("Part 2")
    check = part1(input, 0)
    check = part2(check)
    if check == 396857386627072:
        print(f"Correct value : {check}")
    else:
        print(f"Incorrect value : {check}")
    print("------------------------------------------------------")
