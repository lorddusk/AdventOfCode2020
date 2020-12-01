def examplepart1(input):
    print("EXAMPLE PART 1")
    for i in range(0, len(input)):
        for j in range(0, len(input)):
            output = input[i] + input[j]
            if output == 2020:
                output = input[i] * input[j]
                print(f"{input[i]} x {input[j]} = {output}")
                print("------------------------------------------------------")
                return


def part1(input):
    print("PART 1")
    for i in range(0, len(input)):
        for j in range(0, len(input)):
            output = input[i] + input[j]
            if output == 2020:
                output = input[i] * input[j]
                print(f"{input[i]} x {input[j]} = {output}")
                print("------------------------------------------------------")
                return


def examplepart2(input):
    print("EXAMPLE PART 2")
    for i in range(0, len(input)):
        for j in range(0, len(input)):
            for k in range(0, len(input)):
                output = input[i] + input[j] + input[k]
                if output == 2020:
                    output = input[i] * input[j] * input[k]
                    print(f"{input[i]} x {input[j]} x {input[k]} = {output}")
                    print("------------------------------------------------------")
                    return


def part2(input):
    print("PART 2")
    for i in range(0, len(input)):
        for j in range(0, len(input)):
            for k in range(0, len(input)):
                output = input[i] + input[j] + input[k]
                if output == 2020:
                    output = input[i] * input[j] * input[k]
                    print(f"{input[i]} x {input[j]} x {input[k]} = {output}")
                    print("------------------------------------------------------")
                    return


if __name__ == '__main__':
    input = []
    exampleInput = [1721, 979, 366, 299, 675, 1456]

    f = open('../inputs/day1.txt', 'r')
    for x in f:
        input.append(int(x))
    examplepart1(exampleInput)
    part1(input)
    examplepart2(exampleInput)
    part2(input)
