from typing import List
from tqdm import tqdm


file_name = 'test.txt'
file_name = 'input.txt'


def prune(no1: int) -> int:
    return no1 % 16777216


def mix(no1: int, no2: int) -> int:
    return no1 ^ no2


cache = {}

def get_next_secret(current_secret: int, count: int) -> int:
    if count <= 0:
        return current_secret

    for idx in range(count):
        key = (current_secret, count - idx)
        if key in cache:
            return cache[key]

        result = current_secret * 64
        current_secret = prune(mix(current_secret, result))
        result = current_secret // 32
        current_secret = prune(mix(current_secret, result))
        result = current_secret * 2048
        current_secret = prune(mix(current_secret, result))
        cache[key] = current_secret

    return current_secret


def part1(r: List[int]) -> int:
    total = 0
    for no in tqdm(r):
        total += get_next_secret(no, 2000)
    return total


if __name__ == '__main__':
    with open(file_name) as f:
        r = list(map(int, f.readlines()))

    print(part1(r))
