from typing import List

FILE_NAME = "testcase.txt"


def part1(data: List[str]) -> List[int]:
    ...


if __name__ == "__main__":
    with open(FILE_NAME) as f:
        data = f.readlines()
    res = part1(data)
