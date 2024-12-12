from typing import List, Dict, Set, Tuple
from collections import defaultdict
from copy import copy

file_name = 'test_simple.txt'
file_name = 'test_e.txt'
file_name = 'test_2_example.txt'
file_name = 'test_edge.txt'
file_name = 'test_example.txt'
file_name = 'input.txt'

Point = Tuple[int, int]
x_dir = ((1, 0), (-1, 0))
y_dir = ((0, 1), (0, -1))
directions = x_dir + y_dir


class Plot:
    def __init__(self, symbol: str, points: List[Tuple]):
        self.symbol = symbol
        self.points = points
        self.area = len(points)
        self.perimeter = get_perimeter(points)
        self.sides = get_sides(points)

    def __repr__(self):
        return f"Plot {self.symbol}: Area={self.area} Perimeter={self.perimeter} Sides={self.sides}"

    def get_price(self) -> int:
        return self.area * self.perimeter

    def get_price_bulk(self) -> int:
        return self.area * self.sides


def get_sides(points: List[Point]) -> int:
    side_dict = defaultdict(set)
    points = set(copy(points))
    for x, y in points:
        for dx, dy in directions:
            if (x+dx, y + dy) in points:
                continue
            side_dict[(x, y)].add((dx, dy))

    sides = 0
    for (x, y) in list(side_dict.keys()):
        if (x, y) not in side_dict:
            continue
        for d in side_dict.pop((x, y)):
            for dx, dy in get_adj_dirs(d):
                new_x, new_y = x + dx, y + dy
                while (new_x, new_y) in side_dict and d in side_dict[(new_x, new_y)]:
                    side_dict[(new_x, new_y)].remove(d)
                    new_x, new_y = new_x + dx, new_y + dy

            sides += 1
    return sides


def get_adj_dirs(direction: Point) -> Tuple[Point, Point]:
    if direction in x_dir:
        return y_dir
    return x_dir


def get_perimeter(points: List[Point]) -> int:
    perimeter = 0
    points = set(copy(points))
    for x, y in points:
        for dx, dy in directions:
            if (x+dx, y + dy) in points:
                continue
            perimeter += 1
    return perimeter


def is_valid(matrix: List[List[str]], x: int, y: int):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def get_plot_points(matrix: List[List[str]], visited: List[List[bool]], x: int, y: int) -> List[Point]:
    if visited[x][y]:
        return []

    visited[x][y] = True
    current_points = [(x, y)]
    current_symbol = matrix[x][y]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if not is_valid(matrix, new_x, new_y) or matrix[new_x][new_y] != current_symbol:
            continue
        points = get_plot_points(matrix, visited, new_x, new_y)
        current_points.extend(points)

    return current_points


def to_plots(matrix: List[List[str]]) -> List[Plot]:
    visited = [[False for _ in range(len(matrix[0]))]
               for _ in range(len(matrix))]
    plots = []
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if visited[x][y]:
                continue
            points = get_plot_points(matrix, visited, x, y)
            plot = Plot(matrix[x][y], points)
            plots.append(plot)

    return plots


def part1(plots: List[Plot]) -> int:
    return sum(p.get_price() for p in plots)


def part2(plots: List[Plot]) -> int:
    return sum(p.get_price_bulk() for p in plots)


if __name__ == '__main__':
    with open(file_name) as f:
        matrix = list(map(lambda x: list(x.strip()), f.readlines()))

    plots = to_plots(matrix)
    print(part1(plots))
    print(part2(plots))
