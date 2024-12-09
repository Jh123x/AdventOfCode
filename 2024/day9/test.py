from typing import List, Any, Dict, Tuple
from copy import copy
from tqdm import tqdm

# file_name = 'small_test.txt'
# file_name = 'test.txt'
file_name = 'input.txt'


def gen_space_and_sector(blocks: List[int]) -> Tuple[List[int], List[Tuple[int, int]], List[Tuple[int, int]]]:
    space = []
    free_list = []
    sectors = []
    is_free = False

    for no in blocks:
        if is_free:
            free_list.append([len(space), no])
            space.extend([None] * no)
        else:
            sectors.append((len(space), no))
            space.extend([len(sectors) - 1] * no)
        is_free = not is_free

    return space, free_list, sectors


def get_checksum(space: List[int]) -> int:
    checksum = 0
    for idx, no in enumerate(space):
        if no is None:
            continue
        checksum += idx * no

    return checksum


def part1(space: List[int]) -> int:
    start, end = 0, len(space) - 1

    while end > start:
        while space[start] is not None:
            start += 1
        while space[end] is None:
            end -= 1

        space[start], space[end] = space[end], space[start]
        start += 1
        end -= 1

    return get_checksum(filter(lambda x: x is not None, space))


def populate_space(space: List[int], start_idx: int, sec_no: int, length: int):
    for i in range(length):
        space[start_idx + i] = sec_no


def part2(space: List[int], free_list: List[List[int]], sectors: List[List[int]]) -> int:
    for s_idx, (sec_idx, length) in tqdm(enumerate(reversed(sectors)),total=len(sectors)):
        sec_no = len(sectors) - s_idx - 1
        for f_idx, (idx, f_len) in enumerate(free_list):
            if length > f_len or idx > sec_idx:
                continue
            populate_space(space, idx, sec_no, length)
            populate_space(space, sec_idx, None, length)
            if length == space:
                free_list.remove([idx, f_len])
            else:
                free_list[f_idx] = [idx + length, f_len - length]
            break

    return get_checksum(space)


if __name__ == '__main__':
    with open(file_name) as f:
        blocks = list(map(int, f.read().strip()))

    space, free_list, sectors = gen_space_and_sector(blocks)
    print(part1(copy(space)))
    result = part2(space, free_list, sectors)
    assert result != 8623254343177
    print(result)
