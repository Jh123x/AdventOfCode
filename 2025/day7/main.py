import argparse
from typing import List

def read_file(filename:str) -> List[str]:
    with open(filename) as f:
        return list(map(lambda x: x.strip(), f.readlines()))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name',type=str, help="input file name")
    filename = parser.parse_args().file_name
    data = read_file(filename)
    curr_s = [0 for _ in range(len(data))]
    start_idx = -1
    split_count = 0
    for row in data:
        if start_idx < 0:
            start_idx = row.index('S')
            curr_s[start_idx] += 1
            continue

        for idx, l in enumerate(row):
            if l != '^': 
                continue
            split_count += 1
            curr_s[idx] = 0
            if idx > 0:
                curr_s[idx-1] += 1
            if idx < len(data) - 1:
                curr_s[idx+1] += 1

    print("Part 1:", split_count)

    curr_table = [0 for _ in range(len(data))]
    curr_table[start_idx] += 1
    for row in data:
        tmp = [0 for _ in range(len(data))]
        for idx, l in enumerate(row):
            if l != '^' or curr_table[idx] == 0:
                if curr_table[idx] > 0:
                    tmp[idx] += curr_table[idx]
                continue
            if idx >= 0:
                tmp[idx-1] += curr_table[idx]
            if idx <= len(data) - 1:
                tmp[idx+1] += curr_table[idx]
        curr_table = tmp

    print("Part 2:", sum(curr_table))
