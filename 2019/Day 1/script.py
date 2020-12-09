with open("data.txt") as file:
    data = tuple(map(int, file.readlines()))


def calc(weight):
    return weight // 3 - 2


def calc_r(weight):
    res = calc(weight)
    if res <= 0:
        return 0
    else:
        return res + calc_r(res)

def part1(data):
    acc = 0
    for i in data:
        acc += calc(i)
    return acc

def part2(data):
    acc = 0
    for i in data:
        acc += calc_r(i)
    return acc

print(part2(data))

