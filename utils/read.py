def file(day, type=0):
    input = []
    f = open(f'../inputs/{day}.txt', 'r')
    if type == 0:
        for x in f:
            input.append(x.rstrip())
    else:
        for x in f:
            input.append(int(x.rstrip()))
    return input