import argparse
from typing import List

def read_file(file_name:str) -> List[List[str]]:
    with open(file_name) as f:
        return [list(row) for row in f.read().strip().split('\n')]

DIRECTIONS = (
    (-1,-1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, 0),
    (1, -1),
    (1, 1),
)


def part_1(data: List[List[str]], max_x: int, max_y:int) -> int:
    count = 0
    for x, row in enumerate(data):
        for y, letter in enumerate(row):
            if letter != '@':
                continue

            adj = 0
            for dx, dy in DIRECTIONS:
                check_x, check_y = x + dx, y + dy
                if 0 > check_x or check_x >= max_x or 0 > check_y or check_y >= max_y: 
                    continue
                if data[check_x][check_y] == '@':
                    adj += 1

            if adj >= 4:
                continue
            count += 1
    return count

def part_2(data:List[List[str]], max_x: int, max_y: int) -> int:
    count = 0
    while True:
        tmp = 0
        for x, row in enumerate(data):
            for y, letter in enumerate(row):
                if letter != '@':
                    continue

                adj = 0
                for dx, dy in DIRECTIONS:
                    check_x, check_y = x + dx, y + dy
                    if 0 > check_x or check_x >= max_x or 0 > check_y or check_y >= max_y: 
                        continue
                    if data[check_x][check_y] == '@':
                        adj += 1
    
                if adj >= 4:
                    continue
                tmp += 1
                data[x][y] = '.'
        if tmp == 0:
            return count
        count += tmp


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', help="input file name", type=str)
    args = parser.parse_args()
    filename = args.file_name
    data = read_file(filename)
    max_x = len(data)
    max_y = len(data[0])

    print("Part 1:", part_1(data, max_x, max_y))
    print("Part 2:", part_2(data, max_x, max_y)) 
