from typing import Tuple, List, Dict, Set
from math import ceil
from tqdm import tqdm

file_name = 'test.txt'
# file_name = 'input.txt'

Point = Tuple[int, int]


class Case:
    def __init__(
        self,
        a: Point,
        b: Point,
        prize: Point,
        a_cost: int = 3,
        b_cost: int = 1,
        start: Point = (0, 0)
    ):
        self.a = a
        self.a_cost = a_cost
        self.b_cost = b_cost
        self.b = b
        self.prize = prize
        self.start = start

    def tokens_to_win(self) -> int:
        prize_x, prize_y = self.prize
        ax, ay = self.a
        bx, by = self.b

        for a_times in range(100):
            for b_times in range(100):
                if ax * a_times + bx * b_times != prize_x or ay * a_times + by * b_times != prize_y:
                    continue
                return a_times * self.a_cost + b_times * self.b_cost
        return 0

    def __repr__(self) -> str:
        return f"Case: {self.a} cost {self.a_cost}, {self.b} cost {self.b_cost}, prize {self.prize}"


def parse_btn(txt: str) -> Point:
    x, y = txt[9:].split(',')
    return (int(x[2:]), int(y[2:]))


def parse_prize(txt: str) -> Point:
    x, y = txt[7:].split(", ")
    return (int(x[2:]), int(y[2:]))


def parse_case(txt: str) -> Case:
    raw_a, raw_b, raw_prize = txt.split("\n")
    a = parse_btn(raw_a)
    b = parse_btn(raw_b)
    prize = parse_prize(raw_prize)

    return Case(a, b, prize)


def part1(cases: List[Case]) -> int:
    tokens = 0
    for case in cases:
        soln = case.tokens_to_win_1()
        tokens += soln
    return tokens


def update_prize_loc(case: Case) -> Case:
    case.prize = tuple(map(lambda x: x + 10000000000000, case.prize))
    return case


if __name__ == '__main__':
    with open(file_name) as f:
        cases = list(map(parse_case, f.read().split("\n\n")))

    print(part1(cases))
    # print(part2(list(map(update_prize_loc, cases))))
