from utils.read import file


def part1(input):
    seats = getSeats(input)
    loop = False
    newSeats = seats.copy()

    while not loop:
        loop = True
        deepSeats = newSeats.copy()
        newSeats = {}

        for (x, y), character in deepSeats.items():
            adjSeats = [
                deepSeats.get((x - 1, y - 1), '.'),
                deepSeats.get((x, y - 1), '.'),
                deepSeats.get((x + 1, y - 1), '.'),
                deepSeats.get((x - 1, y), '.'),
                deepSeats.get((x + 1, y), '.'),
                deepSeats.get((x - 1, y + 1), '.'),
                deepSeats.get((x, y + 1), '.'),
                deepSeats.get((x + 1, y + 1), '.'),
            ]

            occupied = adjSeats.count('#')

            if character == '.':
                newSeats[(x, y)] = '.'
            elif character == 'L' and occupied == 0:
                newSeats[(x, y)] = '#'
                loop = False
            elif character == '#' and occupied >= 4:
                newSeats[(x, y)] = 'L'
                loop = False
            else:
                newSeats[(x, y)] = character

    return list(newSeats.values()).count('#')


def part2(input):
    seats = getSeats(input)
    loop = False
    newSeats = seats.copy()

    while not loop:
        loop = True
        deepSeats = newSeats.copy()
        newSeats = {}

        for (x, y), character in deepSeats.items():
            adjSeats = [
                seat_in_direction(x, y, -1, -1, deepSeats),
                seat_in_direction(x, y, 0, -1, deepSeats),
                seat_in_direction(x, y, 1, -1, deepSeats),
                seat_in_direction(x, y, -1, 0, deepSeats),
                seat_in_direction(x, y, 1, 0, deepSeats),
                seat_in_direction(x, y, -1, 1, deepSeats),
                seat_in_direction(x, y, 0, 1, deepSeats),
                seat_in_direction(x, y, 1, 1, deepSeats),
            ]

            occupied = adjSeats.count('#')

            if character == '.':
                newSeats[(x, y)] = '.'

            elif character == 'L' and occupied == 0:
                newSeats[(x, y)] = '#'
                loop = False

            elif character == '#' and occupied >= 5:
                newSeats[(x, y)] = 'L'
                loop = False

            else:
                newSeats[(x, y)] = character

    return list(newSeats.values()).count('#')


def getSeats(input):
    seats = {}
    for y, line in enumerate(input):
        for x, character in enumerate(line):
            seats[(x, y)] = character
    return seats


def seat_in_direction(startX, startY, dx, dy, _seats):
    seatX = startX
    seatY = startY

    while True:
        seatX += dx
        seatY += dy
        key = (seatX, seatY)
        if key not in _seats:
            return '.'

        char = _seats.get(key)
        if char == '.':
            continue
        if char == 'L':
            return 'L'
        if char == '#':
            return '#'


if __name__ == '__main__':
    input = file("day11", 0)
    exampleInput = ["L.LL.LL.LL",
                    "LLLLLLL.LL",
                    "L.L.L..L..",
                    "LLLL.LL.LL",
                    "L.LL.LL.LL",
                    "L.LLLLL.LL",
                    "..L.L.....",
                    "LLLLLLLLLL",
                    "L.LLLLLL.L",
                    "L.LLLLL.LL"]

    print("Example Part 1")
    check = part1(exampleInput)
    if check == 37:
        print(f"Correct value : {check}")
    else:
        print(f"Incorrect value : {check}")
    print("------------------------------------------------------")

    print("Part 1")
    check = part1(input)
    if check == 2303:
        print(f"Correct value : {check}")
    else:
        print(f"Incorrect value : {check}")
    print("------------------------------------------------------")

    print("Example Part 2")
    check = part2(exampleInput)
    if check == 26:
        print(f"Correct value : {check}")
    else:
        print(f"Incorrect value : {check}")
    print("------------------------------------------------------")

    print("Part 2")
    check = part2(input)
    if check == 2057:
        print(f"Correct value : {check}")
    else:
        print(f"Incorrect value : {check}")
    print("------------------------------------------------------")
