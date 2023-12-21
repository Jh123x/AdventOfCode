from typing import List, Tuple, Set
from multiprocessing import Pool

FILE_NAME = "input.txt"

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
    a_to_b = {}
    with Pool(4) as p:
        res = p.map(parse_row, filter(lambda x: x.strip(), a_to_b_str.split("\n")[1:]))
    for r1, r2 in res:
        for from_no, to_no in zip(r1, r2):
            if from_no not in seed_no:
                continue
            a_to_b[from_no] = to_no
    return set(map(lambda x: a_to_b.get(x, x), seed_no))


def parse_row(row: str) -> Tuple[List[int], List[int]]:
    dest, src, no = map(int, row.split(" "))
    return range(src, src + no), range(dest, dest + no)


if __name__ == "__main__":
    with open(FILE_NAME) as f:
        data = f.read()
    result = part1(data)
    print(result)
