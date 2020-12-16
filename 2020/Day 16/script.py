def parse(x:list):

    #Parse the ranges
    ranges_data = x[0].split("\n")
    print(ranges_data)
    ranges = {}
    for line in ranges_data:
        print(line)
        key, value = line.split(': ')
        value = value.split(" or ")
        acc = []
        for r in value:
            start,end = r.split('-')
            acc.append((start,end))
        ranges[key] = acc

    #Parse my ticket
    my_ticket = tuple(map(int, x[1].split("\n")[1].split(",")))

    #Parse the remaining tickets
    nearbytix = tuple(map(lambda y: y.split(','), x[2].split('\n')[1:]))

    #Return the values
    return ranges, my_ticket, nearbytix


def part1():
    pass

def part2():
    pass

#Read the file
with open('data.txt') as file:
    temp = file.read().split("\n\n")
    print(len(temp))
    ranges, my_ticket, nearby_ticket = tuple(map(parse, temp))

print(ranges)

# print(part1(data))
# print(part2(data))