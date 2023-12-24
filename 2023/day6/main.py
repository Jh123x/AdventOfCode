from typing import List
from functools import reduce
from operator import mul

FILE_NAME = "input.txt"


def part1(data: str) -> int:
    """Return the result for part 1"""
    time_str, dist_str = data.split("\n")
    return reduce(
        mul,
        map(
            lambda time_dist: count_ways_to_win(*time_dist),
            zip(parse_values(time_str), parse_values(dist_str)),
        ),
        1,
    )


def part2(data: str) -> int:
    time_str, dist_str = data.split("\n")
    return count_ways_to_win(
        parse_part2_val(time_str),
        parse_part2_val(dist_str),
    )


def count_ways_to_win(time: int, dist: int) -> int:
    return sum(
        map(
            lambda speed: int(speed * (time - speed) > dist),
            range(time),
        ),
    )


def parse_values(time_str: str) -> List[int]:
    gen = filter(is_not_empty, time_str.split(" "))
    next(gen)
    return list(map(int, gen))


def parse_part2_val(time_str: str) -> int:
    gen = filter(is_not_empty, time_str.split(":"))
    _ = next(gen)
    return int("".join(gen).replace(" ", ""))


def is_not_empty(value: str) -> bool:
    return bool(len(value))


if __name__ == "__main__":
    with open(FILE_NAME) as f:
        data = f.read()
    res = part1(data)
    print("Part 1:", res)
    res2 = part2(data)
    print("Part 2:", res2)
