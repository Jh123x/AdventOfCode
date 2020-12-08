from os import read


def read_data(filename) -> tuple:
    with open(filename) as file:
        return tuple(map(lambda x: x.split('\n'), file.read().split("\n\n")))
    


def part_1(data:list) -> int:
    count = 0
    for grp in data:
        grp_set = set()
        for person in grp:
            grp_set = grp_set.union(person)
        count += len(grp_set)
    return count

def part_2(data:list) -> int:
    count = 0
    for grp in data:
        grp_set = set('abcdefghijklmnopqrestuvwxyz')
        for person in grp:
            grp_set = grp_set.intersection(person)
        count += len(grp_set)
    return count

if __name__ == '__main__':
    data = read_data('data.txt')
    print(part_1(data)) # Part 1
    print(part_2(data)) # Part 2