from typing import List, Tuple, Set, Optional

# file_name = 'simple.txt'
# file_name = 'simple2.txt'
# file_name = 'test.txt'
file_name = 'input.txt'

Point = Tuple[int, int]

directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]


def is_valid(x: int, y: int, map: List[List[int]]):
    return 0 <= x < len(map) and 0 <= y < len(map[0])


def dfs(map: List[List[int]], start: Point, target: int, final_target: int, visited: Optional[Set[Point]] = None) -> int:
    if visited is not None and start in visited:
        return 0
    x, y = start

    if map[x][y] == final_target:
        if visited is not None:
            visited.add(start)
        return 1

    score = 0
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if not is_valid(new_x, new_y, map):
            continue
        if map[new_x][new_y] != target or map[new_x][new_y] > final_target:
            continue

        score += dfs(map, (new_x, new_y), target + 1, final_target, visited)

    return score


def part1(map: List[List[int]]) -> int:
    total = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] != 0:
                continue
            s = dfs(map, (x, y), 1, 9, set())
            total += s
    return total

def part2(map:List[List[int]]) -> int:
    total = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] != 0:
                continue
            s = dfs(map, (x, y), 1, 9)
            total += s
    return total

if __name__ == '__main__':
    with open(file_name) as f:
        matrix = list(map(lambda x: list(
            map(lambda x: int(x) if x != '.' else -1, x.strip())), f.readlines()))

    print(part1(matrix))
    print(part2(matrix))
