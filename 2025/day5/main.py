import argparse
from typing import Callable, Iterable, List, Tuple

def read_file(file_name: str) -> Tuple[List[Tuple[int,int]], List[int]]:
    with open(file_name) as f:
        ranges, checks = f.read().split("\n\n")
    
    to_check = list(map(int, filter(lambda x: len(x) > 0, checks.split("\n"))))
    range_values = []
    for r in filter(lambda x: len(x) > 0, ranges.split("\n")):
        start, end = r.split('-')
        start_int, end_int = int(start), int(end)
        range_values.append((start_int, end_int))

    return range_values, to_check
            


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", type=str, help="name of the input file")

    args = parser.parse_args()
    filename = args.file_name

    range_list, checks = read_file(filename)
    acc = 0
    for i in checks:
        for start, end in range_list:
            if start <= i <= end:
                acc += 1
                break

    print("Part 1:", acc)

    range_list.sort(key=lambda x: (x[0], -x[1]))
    final_ranges = []

    curr_start, curr_end = None, None
    for start, end in range_list:
        if curr_start is None or start > curr_end:
            if curr_start is not None:
                final_ranges.append((curr_start, curr_end))
            curr_start, curr_end = start,end
            continue
        if end > curr_end:
            curr_end = end
            continue
    if curr_start is not None:
        final_ranges.append((curr_start, curr_end))
        
    acc = 0
    for start, end in final_ranges:
        acc += end - start + 1

    print("Part 2:", acc)

