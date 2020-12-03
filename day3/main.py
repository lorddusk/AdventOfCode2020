def part1(input):
    dupe, loc, loop, matrix, open, tree = start(input)

    while loop:
        try:
            posLoc = matrix[loc[0]][loc[1]]
            if posLoc == ".":
                open += 1
            if posLoc == "#":
                tree += 1
            loc[0] += 1
            loc[1] += 3
            if loc[0] >= len(matrix):
                loop = False
        except IndexError:
            dupe += 1
            matrix = createMatrix(input, dupe)

    print(f"Open spaces: {open}, Trees {tree}")


def part2(input, paths):
    totalTrees = 1
    for path in paths:
        incX = path[0]
        incY = path[1]
        dupe, loc, loop, matrix, open, tree = start(input, path)
        while loop:
            try:
                posLoc = matrix[loc[0]][loc[1]]
                if posLoc == ".":
                    open += 1
                if posLoc == "#":
                    tree += 1
                loc[0] += incX
                loc[1] += incY
                if loc[0] >= len(matrix):
                    loop = False
            except IndexError:
                dupe += 1
                matrix = createMatrix(input, dupe)

        print(f"For path {incX},{incY} - Open spaces: {open}, Trees {tree}")
        totalTrees = totalTrees * tree
    print(f"Total Trees: {totalTrees}")


def start(input, loc=None):
    dupe = 1
    matrix = createMatrix(input, dupe)
    open = 0
    tree = 0
    # x,y
    if loc is None:
        loc = [1, 3]
    loop = True
    return dupe, loc, loop, matrix, open, tree


def createMatrix(input, amount):
    matrix = []
    for row in input:
        newRow = []
        for i in range(0, amount):
            for char in row:
                newRow.extend(char)
        matrix.append(newRow)
    return matrix


if __name__ == '__main__':
    input = []
    exampleInput = ["..##.......",
                    "#...#...#..",
                    ".#....#..#.",
                    "..#.#...#.#",
                    ".#...##..#.",
                    "..#.##.....",
                    ".#.#.#....#",
                    ".#........#",
                    "#.##...#...",
                    "#...##....#",
                    ".#..#...#.#"]

    f = open('../inputs/day3.txt', 'r')
    for x in f:
        input.append(x.rstrip())

    print("EXAMPLE PART 1")
    part1(exampleInput)
    print("------------------------------------------------------")
    print("PART 1")
    part1(input)
    print("------------------------------------------------------")
    print("EXAMPLE PART 2")
    paths = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
    part2(exampleInput, paths)
    print("------------------------------------------------------")
    print("PART 2")
    paths = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
    part2(input, paths)
    print("------------------------------------------------------")
