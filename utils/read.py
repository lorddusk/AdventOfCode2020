def file(day):
    input = []
    f = open(f'../inputs/{day}.txt', 'r')
    for x in f:
        input.append(x.rstrip())
    return input