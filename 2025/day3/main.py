import argparse
from typing import List

def read_file(file_name: str) -> List[List[int]]:
    result = []
    with open(file_name) as f:
        for row in f.readlines():
            row = row.strip()
            result.append(list(map(int, row)))

    return result

def part1(data: List[List[int]]) -> int:
    total = 0
    for row in data:
        curr_max = 0
        for start_idx, no in enumerate(row):
            for end_idx in range(start_idx+1, len(row)):
                curr_max = max(curr_max, no * 10 + row[end_idx])
        total += curr_max
    return total

def part2(data: List[List[int]]) -> int:
    ...

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Day 3 of AoC")
    parser.add_argument("input_file", type=str, help="Input file name")
    
    args = parser.parse_args()
    filename = args.input_file

    data = read_file(filename)
    print("Part 1:", part1(data))
