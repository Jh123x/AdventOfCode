from typing import List, Tuple

# file_name = 'test1.txt'
# file_name = 'test.txt'
file_name = 'input.txt'


def is_valid(map: List[str], x: int, y: int) -> bool:
    return 0 <= x < len(map) and 0 <= y < len(map[0])


def print_grid(map: List[str], x: int, y: int):
    printed_pts = [(x, y), (x-1, y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1)]
    for x in range(len(map)):
        for y in range(len(map[0])):
            if (x, y) in printed_pts:
                print(map[x][y], end="")
            else:
                print(".", end="")
        print()
    print()


directions = [
    [(-1, -1), (1, 1)],
    [(-1, 1), (1, -1)],
]

def is_x_mas(map: List[str], curr_x: int, curr_y: int) -> bool:
    for pairs in directions:
        s = set()
        for dx, dy in pairs:
            new_x = curr_x + dx
            new_y = curr_y + dy
            if not is_valid(map, new_x, new_y):
                return False
            s.add(map[new_x][new_y])
        if 'M' not in s or 'S' not in s:
            return False
    
    # print_grid(map, curr_x, curr_y)
    return True


def part2(map: List[str]) -> int:
    count = 0
    for x, row in enumerate(map):
        if x == 0:
            continue
        for y, letter in enumerate(row):
            if letter == 'A' and is_x_mas(map, x, y):
                count += 1

    return count


if __name__ == '__main__':
    with open(file_name) as f:
        rows = list(map(
            lambda x: x.strip(),
            f.readlines(),
        ))

    print(part2(rows))
