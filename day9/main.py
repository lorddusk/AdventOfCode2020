from utils.read import file


def part1(input, preamble):
    currentList = []
    start = 0
    toCheck = 0
    loop = True
    for i in range(start, preamble):
        currentList.append(input[i])

    while loop:
        toCheck = input[preamble]
        loop = checkPreamble(currentList, toCheck)
        currentList = []
        start += 1
        preamble += 1
        for i in range(start, preamble):
            currentList.append(input[i])
    return toCheck


def checkPreamble(list, check):
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            output = list[i] + list[j]
            if output == check:
                return True
    return False


def part2(input, final):
    start = 0
    numbers = 1
    currentList = [input[0]]
    loop = True
    while loop:
        output = sum(currentList)

        if output == final:
            loop = False

        elif output < final:
            currentList.append(input[numbers])
            numbers += 1

        elif output > final:
            start += 1
            numbers = start + 1
            currentList = [input[start]]

    output = min(currentList) + max(currentList)
    return output


if __name__ == '__main__':
    input = file("day9", 1)
    exampleInput = [35,
                    20,
                    15,
                    25,
                    47,
                    40,
                    62,
                    55,
                    65,
                    95,
                    102,
                    117,
                    150,
                    182,
                    127,
                    219,
                    299,
                    277,
                    309,
                    576]

    print("Example Part 1")
    check = part1(exampleInput, 5)
    if check == 127:
        print(f"Correct value : {check}")
    else:
        print(f"Incorrect value : {check}")
    print("------------------------------------------------------")

    print("Part 1")
    check = part1(input, 25)
    if check == 22406676:
        print(f"Correct value : {check}")
    else:
        print(f"Incorrect value : {check}")
    print("------------------------------------------------------")

    print("Example Part 2")
    check = part2(exampleInput, 127)
    if check == 62:
        print(f"Correct value : {check}")
    else:
        print(f"Incorrect value : {check}")
    print("------------------------------------------------------")

    print("Part 2")
    check = part2(input, 22406676)
    if check == 2942387:
        print(f"Correct value : {check}")
    else:
        print(f"Incorrect value : {check}")
    print("------------------------------------------------------")
