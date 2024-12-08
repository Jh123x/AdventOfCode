from typing import Tuple, Dict, Set, List, Iterable, Callable
from collections import defaultdict

# file_name = 'test.txt'
file_name = 'input.txt'


#### Shared ####

Point = Tuple[int, int]


def is_valid_point(point: Point, max_x: int, max_y: int) -> bool:
    x, y = point
    return 0 <= x < max_x and 0 <= y < max_y


def print_map(mp: List[str], antinode_loc: Set[Point]):
    for i in range(len(mp)):
        for j in range(len(mp[0])):
            if (i, j) in antinode_loc and mp[i][j] == '.':
                print("#", end="")
            else:
                print(mp[i][j], end="")
        print()


def execute(
    freq_list: Dict[str, Set[Point]],
    max_x: int,
    max_y: int,
    get_antinode_fn: Callable[[List[Point], int, int], Iterable[Point]]
) -> int:
    antinode_loc: Set[Point] = set()
    for points in freq_list.values():
        antinode_loc.update(
            get_antinode_fn(
                list(points),
                max_x,
                max_y,
            ),
        )

    return len(antinode_loc)

#### Part 1 ####


def get_line_antinode(p1: Point, p2: Point, max_x: int, max_y: int) -> Iterable[Point]:
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]

    return filter(
        lambda x: is_valid_point(x, max_x, max_y),
        [(p1[0] + dx, p1[1] + dy), (p2[0] - dx, p2[1] - dy)],
    )


def get_antinode_points(
    points: List[Point],
    max_x: int,
    max_y: int,
) -> Set[Point]:
    n = len(points)
    antinode_points: Set[Point] = set()
    for i in range(n):
        for j in range(i+1, n):
            antinode_points.update(
                get_line_antinode(
                    points[i],
                    points[j],
                    max_x,
                    max_y,
                ),
            )

    return antinode_points


#### Part 2 ###


def get_empty_dir_points(p: Point, max_x: int, max_y: int, direction: Point) -> Iterable[Point]:
    x, y = p
    dx, dy = direction
    points = []
    while is_valid_point((x, y), max_x, max_y):
        points.append((x, y))
        x += dx
        y += dy

    return points


def get_line_antinode_2(p1: Point, p2: Point, max_x: int, max_y: int) -> Iterable[Point]:
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]

    points = []

    # Negative dir
    points.extend(get_empty_dir_points(p1, max_x, max_y, (-dx, -dy)))

    # Positive dir
    points.extend(get_empty_dir_points(p1, max_x, max_y, (dx, dy)))

    return points


def get_antinode_points_2(
    points: List[Point],
    max_x: int,
    max_y: int,
) -> Set[Point]:
    n = len(points)
    antinode_points: Set[Point] = set()
    for i in range(n):
        for j in range(i+1, n):
            antinode_points.update(
                get_line_antinode_2(
                    points[i],
                    points[j],
                    max_x,
                    max_y,
                ),
            )

    return antinode_points

#### Shared ####


if __name__ == '__main__':

    with open(file_name) as f:
        data = list(map(lambda x: x.strip(), f.readlines()))

    freq = defaultdict(set)
    for x, row in enumerate(data):
        for y, col in enumerate(row):
            if col == '.':
                continue
            freq[col].add((x, y))

    max_x = len(data)
    max_y = len(data[0])
    print(execute(freq, max_x, max_y, get_antinode_points))
    print(execute(freq, max_x, max_y, get_antinode_points_2))
