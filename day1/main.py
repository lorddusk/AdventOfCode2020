def part1(input):
    for i in range(0, len(input)):
        for j in range(0, len(input)):
            output = input[i] + input[j]
            if output == 2020:
                output = input[i] * input[j]
                print(f"{input[i]} x {input[j]} = {output}")
                return


def part2(input):
    for i in range(0, len(input)):
        for j in range(0, len(input)):
            for k in range(0, len(input)):
                output = input[i] + input[j] + input[k]
                if output == 2020:
                    output = input[i] * input[j] * input[k]
                    print(f"{input[i]} x {input[j]} x {input[k]} = {output}")
                    return


if __name__ == '__main__':
    input = []
    exampleInput = [1721, 979, 366, 299, 675, 1456]

    f = open('../inputs/day1.txt', 'r')
    for x in f:
        input.append(int(x))

    print("EXAMPLE PART 1")
    part1(exampleInput)
    print("------------------------------------------------------")
    print("PART 1")
    part1(input)
    print("------------------------------------------------------")
    print("EXAMPLE PART 2")
    part2(exampleInput)
    print("------------------------------------------------------")
    print("PART 2")
    part2(input)
    print("------------------------------------------------------")
