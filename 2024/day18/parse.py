from typing import Set, Tuple, List
from queue import Queue
from tqdm import tqdm


Point = Tuple[int, int]
directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]


def is_valid(point: Point, exit: Point):
    x, y = point
    tx, ty = exit

    return 0 <= x <= tx and 0 <= y <= ty


def part1(points: Set[Point], exit: Point) -> Set[Point]:
    q = Queue()
    q.put((0, 0, set()))
    visited = set([])

    while not q.empty():
        x, y, path = q.get()
        p = (x, y)

        if p == exit:
            path.add(p)
            return path

        if p in visited or p in points or not is_valid(p, exit):
            continue

        visited.add(p)

        for dx, dy in directions:
            new_p = (x + dx, y + dy)
            p2 = path.copy()
            p2.add(new_p)
            q.put((new_p[0], new_p[1], p2))

    return set()


def part2(points: Set[Point], exit: Point):
    for i in tqdm(range(2988, len(points))):
        if len(part1(points[:i], exit)) > 0:
            continue
        return i
    return -1


def print_sheets(points: List[Point], exit: Point, path: Set[Point] = set()):
    x, y = exit
    for i in range(x + 1):
        for j in range(y+1):
            pt = (i, j)
            if pt in path:
                print("o", end="")
                continue

            print("." if (i, j) not in points else "#", end="")
        print()


if __name__ == '__main__':
    file_name = 'input.txt'
    with open(file_name) as f:
        points = list(
            map(
                lambda x: tuple(map(int, x.strip().split(","))),
                f.readlines(),
            ),
        )

    target = (70, 70)
    path = part1(points[:1024], target)
    print_sheets(points[:1024], target, path)
    print(len(path))

    b = part2(points, target)
    print(points[b])
