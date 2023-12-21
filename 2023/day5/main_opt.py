from typing import Tuple, Set

FILE_NAME = "input.txt"


class LazyDict:
    def __init__(self: "LazyDict") -> None:
        self.curr_fn = lambda x: x

    def register(self: "LazyDict", src: int, dest: int, range_no: int) -> None:
        fn = self.curr_fn
        def wrapper(value: int) -> int:
            if src <= value <= src + range_no:
                return dest + (value - src)
            return fn(value)

        self.curr_fn = wrapper

    def calc(self: "LazyDict", value: int) -> int:
        return self.curr_fn(value)


def part1(data: str) -> int:
    for idx, row in enumerate(data.split("\n\n")):
        if idx == 0:
            res_seed = parse_seed(row)
            continue
        res_seed = parse_map(row, res_seed)
    return min(res_seed)


def parse_seed(seed_str: str) -> Set[int]:
    return set(map(int, filter(lambda x: x.strip(), seed_str.split(":")[1].split(" "))))


def parse_map(a_to_b_str: str, seed_no: Set[int]) -> Set[int]:
    a_to_b = LazyDict()
    res = map(parse_row, filter(lambda x: x.strip(), a_to_b_str.split("\n")[1:]))
    for dst, src, range_no in res:
        a_to_b.register(src, dst, range_no)
    return set(map(lambda x: a_to_b.calc(x), seed_no))


def parse_row(row: str) -> Tuple[int]:
    return tuple(map(int, row.split(" ")))


if __name__ == "__main__":
    with open(FILE_NAME) as f:
        data = f.read()
    result = part1(data)
    print(result)
