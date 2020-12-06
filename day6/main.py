import collections
import itertools

from utils.read import file


def part1(input):
    groupNum = 1
    totalAnswers = 0
    input = createGroupedInput(input)
    for group in input:
        groupAnswers = []
        for person in group:
            for answer in person:
                if answer not in groupAnswers:
                    groupAnswers.append(answer)
        totalAnswers += len(groupAnswers)
        groupNum += 1
    print(f"Sum of all groups: {totalAnswers}")


def part2(input):
    input = createGroupedInput(input)
    totalAnswers = 0
    for group in input:
        group_length = len(group)
        group_answers = list(itertools.chain.from_iterable(group))
        answers_counter = collections.Counter(group_answers)
        for y in answers_counter:
            if answers_counter[y] == group_length:
                totalAnswers += 1
    print(f"Sum of all groups: {totalAnswers}")


def createGroupedInput(input):
    groups = [[]] * len(input)
    current = 0
    for line in input:
        if line == "":
            current += 1
        else:
            if groups[current] == []:
                groups[current] = [line]
            else:
                groups[current].append(line)
    filtered = list(filter(None, groups))
    return filtered


if __name__ == '__main__':
    input = file("day6")
    exampleInput = ["abc",
                    "",
                    "a",
                    "b",
                    "c",
                    "",
                    "ab",
                    "ac",
                    "",
                    "a",
                    "a",
                    "a",
                    "a",
                    "",
                    "b"]

    print("Example Part 1")
    part1(exampleInput)
    print("------------------------------------------------------")
    print("Part 1")
    part1(input)
    print("------------------------------------------------------")
    print("Example Part 2")
    part2(exampleInput)
    print("------------------------------------------------------")
    print("Part 2")
    part2(input)
    print("------------------------------------------------------")
