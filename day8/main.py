from utils.read import file


def part1(instructions):
    seen = []
    accu = 0
    i = 0
    for _ in instructions:
        seen.append(False)

    while True:
        if seen[i] == True:
            break

        seen[i] = True
        opcode, acc = instructions[i].split(" ")
        if opcode == "nop":
            i = _nop(i)

        if opcode == "acc":
            i, accu = _acc(i, acc, accu)

        if opcode == "jmp":
            i = _jmp(i, acc)

    print(f"Accumulator value, before looping: {accu}")
    return accu


def part2(instructions):
    for ind, ins in enumerate(instructions):
        accu = 0
        i = 0

        opcode, acc = ins.split(" ")
        if opcode == "nop":
            opcode = "jmp"
        if opcode == "jmp":
            opcode = "nop"

        patch_n = ind
        patch = f'{opcode} {acc}'

        seen = []
        for _ in instructions:
            seen.append(False)

        try:
            while True:
                if seen[i]:
                    break
                seen[i] = True
                ins = instructions[i]
                if i == patch_n:
                    ins = patch

                opcode, acc = ins.split(" ")
                if opcode == "nop":
                    i = _nop(i)

                if opcode == "acc":
                    i, accu = _acc(i, acc, accu)

                if opcode == "jmp":
                    i = _jmp(i, acc)
        except:
            print(f"Accumulator value, after terminating: {accu}")
            return accu


def _nop(i):
    i += 1
    return i


def _acc(i, acc, accu):
    accu += int(acc)
    i += 1
    return i, accu


def _jmp(i, acc):
    i += int(acc)
    return i


def debug(i, tp, accu, step, alreadyChanged):
    print(f"Step: {i} - {tp} - Next Step: {i + accu} - Changed: {step} - Loop Changed: {alreadyChanged}")


if __name__ == '__main__':
    input = file("day8")
    exampleInput = ["nop +0",
                    "acc +1",
                    "jmp +4",
                    "acc +3",
                    "jmp -3",
                    "acc -99",
                    "acc +1",
                    "jmp -4",
                    "acc +6"]

    print("Example Part 1")
    check = part1(exampleInput)
    if check == 5:
        print("Correct value")
    else:
        print("Incorrect value")
    print("------------------------------------------------------")

    print("Part 1")
    check = part1(input)
    if check == 1420:
        print("Correct value")
    else:
        print("Incorrect value")
    print("------------------------------------------------------")

    print("Example Part 2")
    check = part2(exampleInput)
    if check == 8:
        print("Correct value")
    else:
        print("Incorrect value")
    print("------------------------------------------------------")

    print("Part 2")
    check = part2(input)
    if check == 1245:
        print("Correct value")
    else:
        print("Incorrect value")
    print("------------------------------------------------------")
