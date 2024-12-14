from typing import List, Set, Dict, Tuple
from tqdm import tqdm


# file_name = "test.txt"
file_name = 'input.txt'
Point = Tuple[int, int]


class Robot:
    def __init__(self, pos: Point, velocity: Point) -> int:
        """"""
        self.start_pos = pos
        self.v = velocity

    def pos_after_x(self, width: int, height: int, x: int) -> Point:
        dx = (self.start_pos[0] + self.v[0] * x) % width
        dy = (self.start_pos[1] + self.v[1] * x) % height
        return (dx, dy)

    def __repr__(self) -> str:
        return f"Robot at {self.start_pos} moving at {self.v}"


def parse_point(pt: str) -> Point:
    return tuple(map(int, pt.strip().split(",")))


def parse_robot_lines(line: str) -> Robot:
    p, v = line.strip().split(" ")
    start_p = parse_point(p[2:])
    velocity = parse_point(v[2:])
    return Robot(start_p, velocity)


def get_middle(no: int) -> int:
    return no // 2


def visualize(positions: List[Point], width: int, height: int) -> None:
    matrix = [[0 for _ in range(width)] for _ in range(height)]
    for x, y in positions:
        matrix[y][x] += 1

    print(
        *list(
            map(
                lambda x: ''.join(
                    map(
                        str,
                        map(lambda x: '.' if x == 0 else x, x),
                    ),
                ),
                matrix,
            ),
        ),
        sep="\n",
    )


def get_quad_vals(positions: List[Point], width: int, height: int) -> Tuple[int, int, int, int]:
    mid_width = get_middle(width)
    mid_height = get_middle(height)
    arr = [0, 0, 0, 0]
    for x, y in positions:
        if x == mid_width or y == mid_height:
            continue
        idx = 0
        if x > mid_width:
            idx += 1
        if y > mid_height:
            idx += 2
        arr[idx] += 1
    return tuple(arr)


def prod(*x: List[int]) -> int:
    if len(x) == 0:
        return 0

    start = x[0]
    for i in range(1, len(x)):
        start *= x[i]
    return start


def part_1(robots: List[Robot], width: int, height: int) -> int:
    x = 100
    points = [robot.pos_after_x(width, height, x) for robot in robots]
    q_val = get_quad_vals(points, width, height)
    return prod(*q_val)


directions = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1)
]


def is_ff_high(points: List[Point]) -> bool:
    visited = set()
    for p in points:
        if p in visited:
            continue
        s = [p]
        idx = 0
        while idx < len(s):
            visited.add(p)
            p = s[idx]
            x, y = p
            for dx, dy in directions:
                new_p = (x + dx, y + dy)
                if new_p not in points or new_p in visited:
                    continue
                s.append(new_p)

            idx += 1
        if len(s) > 50:
            return True
    return False


def part_2(robots: List[Robot], width: int, height: int) -> int:
    for i in tqdm(range(10404)):
        points = [robot.pos_after_x(width, height, i) for robot in robots]
        if not is_ff_high(points):
            continue

        print(chr(27) + "[2J")
        print('iteration:', i)
        visualize(points, width, height)
        print("-" * width)

        v: str = input()
        if v == 'q':
            break
        if v.isnumeric():
            i = int(v) - 1
        i += 1


if __name__ == '__main__':
    with open(file_name) as f:
        robots = tuple(map(parse_robot_lines, f.readlines()))
    # print(part_1(robots, 101, 103))
    print(part_2(robots, 101, 103))
