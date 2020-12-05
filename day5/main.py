import math
from utils.read import file


def sortThroughBoardingPasses(input):
    seatList = []
    highestSeatId = 0
    for board in input:
        min = 0
        max = 127
        row = 0
        for i in range(0, 7):
            diff = max - min
            if board[i] == "F":
                max -= math.ceil(diff / 2)
            if board[i] == "B":
                min += math.floor(diff / 2)
        min += 1
        if min == max:
            row = min
        else:
            print(f"ERROR in ROW, {min} - {max}, {board}")
            break

        min = 0
        max = 7
        column = 0
        for i in range(7, 10):
            diff = max - min
            if board[i] == "L":
                max -= math.ceil(diff / 2)
            if board[i] == "R":
                min += math.floor(diff / 2)
        min += 1
        if min == max:
            column = min
        elif board[-3:] == "LLL" and min == 1 and max == 0:
            column = 0
        else:
            print(f"ERROR in COLUMN, {min} - {max}, {board}")
            break
        seatId = row * 8 + column
        if seatId > highestSeatId:
            highestSeatId = seatId
        seatList.append(seatId)
    seatList.sort()
    print(f"Highest ID: {highestSeatId}")
    print(f"Missing Seat Id: {sorted(set(range(seatList[0], seatList[-1] + 1)).difference(seatList))[0]}")


if __name__ == '__main__':
    input = file("day5")
    exampleInput = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

    print("PART 1 & 2")
    sortThroughBoardingPasses(input)
    print("------------------------------------------------------")
