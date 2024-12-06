from typing import List, Tuple, Set
from copy import deepcopy
from tqdm import tqdm


# file_name = 'test.txt'
file_name = 'input.txt'

change = {
    ">": "v",
    "v": "<",
    "<": "^",
    "^": ">"
}


def part1(curr_map: List[List[str]], guard_pos: Tuple[int, int], direction: str) -> int:
    x, y = guard_pos
    max_x = len(curr_map)
    max_y = len(curr_map[0])
    visited = set([(x, y)])

    while 0 <= x < max_x and 0 <= y < max_y:
        if curr_map[x][y] == '.':
            visited.add((x, y))

        if curr_map[x][y] == '#':
            dx, dy = get_dir_change(direction)
            x -= dx
            y -= dy
            direction = change[direction]
            continue

        curr_map[x][y] = 'X'
        dx, dy = get_dir_change(direction)
        x += dx
        y += dy

    return len(visited), visited

def part2(positions: Set[Tuple[int, int]], curr_map: List[List[str]], guard_pos: Tuple[int, int], direction: str) -> int:
    total = 0
    for (x, y) in tqdm(positions):
        curr_map[x][y] = '#'
        result = is_loop(curr_map, guard_pos, direction)
        curr_map[x][y] = '.'
        if not result:
            continue
        total += 1
    return total


def is_loop(curr_map: List[List[str]], guard_pos: Tuple[int, int], direction: str) -> int:
    x, y = guard_pos
    max_x = len(curr_map)
    max_y = len(curr_map[0])
    visited2 = set()

    while 0 <= x < max_x and 0 <= y < max_y:
        if (x,y,direction) in visited2:
            return True

        if curr_map[x][y] == '#':
            # Backtrack + change dir
            dx, dy = get_dir_change(direction)
            x -= dx
            y -= dy
            direction = change[direction]
            continue

        visited2.add((x, y, direction))
        dx, dy = get_dir_change(direction)
        x += dx
        y += dy

    return False


def get_dir_change(direction: str) -> Tuple[int, int]:
    if direction == ">":
        return 0, 1
    if direction == "<":
        return 0, -1
    if direction == "^":
        return -1, 0
    if direction == "v":
        return 1, 0


if __name__ == '__main__':
    with open(file_name) as f:
        curr_map = list(map(lambda x: list(x.strip()), f.readlines()))

    for x, row in enumerate(curr_map):
        for y, col in enumerate(row):
            if col in set('^v><'):
                guard_pos = (x, y)
                direction = col

    p1_map = deepcopy(curr_map)
    results, visited = part1(p1_map, guard_pos, direction)
    print(results)
    results = part2(visited, deepcopy(curr_map), guard_pos, direction)
    print(results)
