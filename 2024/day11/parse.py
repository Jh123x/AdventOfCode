from typing import List
from functools import cache
from tqdm import tqdm
from copy import copy

# file_name = 'test.txt'
file_name = 'input.txt'


@cache
def blink(no: int) -> List[int]:
    if no == 0:
        return [1]

    str_no = str(no)
    if len(str_no) % 2 == 0:
        l = len(str_no)
        no1 = int(str_no[:l//2])
        no2 = int(str_no[l//2:])
        return [no1, no2]
    return [no * 2024]


@cache
def blink_n(no: int, blinks: int) -> List[int]:
    if blinks == 0:
        return 1
    acc = 0
    for s in blink(no):
        acc += blink_n(s, blinks - 1)
    return acc


def answer(stones: List[int], blinks: int) -> int:
    acc = 0
    for s in tqdm(stones):
        acc += blink_n(s, blinks)
    return acc


if __name__ == '__main__':
    with open(file_name) as f:
        stones = sorted(list(map(int, f.read().split(" "))))

    print(answer(copy(stones), 25))
    print(answer(copy(stones), 75))
