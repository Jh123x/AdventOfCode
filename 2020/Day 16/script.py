from intervaltree import IntervalTree, Interval

def parse(x:list):

    #Parse the ranges
    ranges_data = x[0].split("\n")
    ranges = {}
    for line in ranges_data:
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
    nearbytix = tuple(map(lambda y: tuple(map(int,y.split(','))), x[2].split('\n')[1:]))

    #Return the values
    return ranges, my_ticket, nearbytix    


def combine_ranges(ranges:tuple):
    ran = IntervalTree()
    for r in ranges:
        for start,end in r:
            ran.add(Interval(int(start), int(end) + 1))
    return ran


def part1(ranges:tuple, nearby_tickets:tuple):
    combined_range = combine_ranges(tuple(ranges.values()))
    invalid_acc = 0
    valid = []
    for ticket in nearby_tickets:
        for item in ticket:
            if(not combined_range.overlaps(item)):
                invalid_acc += item
                break
        else:
            valid.append(ticket)
    return invalid_acc, valid

def part2(ranges:tuple, my_ticket:tuple, nearby_tickets:tuple):
    
    #Get the valid tickets
    _, valid = part1(ranges, nearby_tickets)
    

#Read the file
with open('data.txt') as file:
    temp = file.read().split("\n\n")
    ranges, my_ticket, nearby_tickets = parse(temp)

test_input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
# test_range, test_tix, test_nearby = parse(test_input.split("\n\n"))
# print(part1(test_range, test_nearby))
print(part1(ranges, nearby_tickets)[0])
print(part2(ranges, my_ticket, nearby_tickets))