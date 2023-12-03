from typing import List, Optional, Set, Tuple

FILE_NAME = "input.txt"
DIRECTIONS = [
    [-1, -1],  # top left
    [-1, 0],  # top
    [-1, 1],  # top right
    [0, -1],  # left
    [0, 1],  # right
    [1, -1],  # bottom left
    [1, 0],  # bottom
    [1, 1],  # bottom right
]


def get_engine_nos(lines: List[str]) -> List[int]:
    nos = []
    for y, row in enumerate(lines):
        row = row.strip()
        for x, letter in enumerate(row):
            # ignore dots
            if letter == ".":
                continue
            if letter.isdigit():
                continue
            nos.extend(get_adj_no(lines, y, x))
    return nos


def get_gear_ratios(lines: List[str]) -> List[int]:
    nos = []
    for y, row in enumerate(lines):
        row = row.strip()
        for x, letter in enumerate(row):
            # ignore all except gears
            if letter != '*':
                continue
            gear_nos = get_adj_no(lines, y, x)
            if len(gear_nos) != 2:
                continue
            nos.append(gear_nos[0] * gear_nos[1])
    return nos


def get_adj_no(lines: List[str], y: int, x: int) -> List[int]:
    visited = set()
    nos = []
    for dx, dy in DIRECTIONS:
        y_loc = y + dy
        x_loc = x + dx
        if y_loc < 0 or y_loc >= len(lines) or x_loc < 0 or x_loc >= len(lines[0]):
            continue
        if not lines[y_loc][x_loc].isdigit():
            continue
        no = parse_no(lines, y_loc, x_loc, visited)
        if no is None:
            continue
        nos.append(no)
    return nos


def parse_no(lines: List[str], y: int, x: int, visited: Set[Tuple[int, int]]) -> Optional[int]:
    left_idx = x
    right_idx = x
    if (y, x) in visited:
        return None

    # Slide left
    while left_idx >= 0 and lines[y][left_idx].isdigit():
        left_idx -= 1

    # Slide right
    while right_idx < len(lines[0]) and lines[y][right_idx].isdigit():
        right_idx += 1

    for i in range(left_idx+1, right_idx):
        visited.add((y, i))

    return int(lines[y][left_idx+1:right_idx])


if __name__ == '__main__':
    with open(FILE_NAME) as f:
        lines = f.readlines()
    print("Part 1:", sum(get_engine_nos(lines)))
    print("Part 2:", sum(get_gear_ratios(lines)))
