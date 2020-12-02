def part1(input):
    valid = 0
    for password in input:
        policies = password.split(" ")
        min, max = policies[0].split("-")
        policy = policies[1][0]
        password = policies[2]
        occurrences = password.count(policy)
        if int(min) <= occurrences <= int(max):
            valid += 1
    print(f"Valid number of passwords in file: {valid}")


def part2(input):
    valid = 0
    for password in input:
        policies = password.split(" ")
        checkA, checkB = policies[0].split("-")
        policy = policies[1][0]
        password = policies[2]
        checkA = int(checkA) - 1
        checkB = int(checkB) - 1

        if password[checkA] == policy:
            posA = True
        else:
            posA = False

        if password[checkB] == policy:
            posB = True
        else:
            posB = False

        if posA == True and posB == False:
            valid += 1
        elif posB == True and posA == False:
            valid += 1

    print(f"Valid number of passwords in file: {valid}")


if __name__ == '__main__':
    input = []
    exampleInput = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

    f = open('../inputs/day2.txt', 'r')
    for x in f:
        input.append(x.rstrip())

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
