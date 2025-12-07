import argparse
from typing import List, Tuple


def read_file(file_name: str) -> List[Tuple[int]]:
    with open(file_name) as f:
        data = f.readlines()
    numbers_raw = data[:-1]
    opts_raw = data[-1]
    opts = list(filter(lambda x: len(x.strip()) > 0, opts_raw.strip().split(" ")))
    numbers = list(map(lambda x: list(map(int, list(filter(lambda x: len(x.strip()) > 0, x.strip().split(" "))))), numbers_raw))
    return list(zip(*numbers, opts))

def read_file_2(file_name:str) -> List[Tuple[int]]:
    with open(file_name) as f:
        data = f.readlines()
    numbers_raw = data[:-1]
    opts_raw = data[-1]
    opts = list(filter(lambda x: len(x.strip()) > 0, opts_raw.strip().split(" ")))
    numbers_str = list(map(lambda x: ''.join(x),zip(*numbers_raw)))

    grps = []
    tmp_grp = []
    idx = 0
    for letter_grp in numbers_str:
        cleaned_grp = letter_grp.strip()
        if len(cleaned_grp) == 0:
            tmp_grp.append(opts[idx])
            idx += 1
            grps.append(tmp_grp)
            tmp_grp = []
            continue
        tmp_grp.append(int(cleaned_grp))

    return grps

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type = str,help="input file to AoC")

    file_name = parser.parse_args().file_name
    result = read_file(file_name)

    acc = 0
    for row in result:
        res = 0
        if row[-1] == "+":
            res = sum(row[:-1]) 
        elif row[-1] == "*":
            res = 1
            for no in row[:-1]:
                res *= no
        acc += res
    print("Part 1:", acc)

    result = read_file_2(file_name)
    acc = 0
    for row in result: 
        res = 0
        if row[-1] == "+":
            res = sum(row[:-1])
        elif row[-1] == '*':
            res = 1
            for no in row[:-1]:
                res *= no
        else:
            raise ValueError(row)
        acc += res
    print("Part 2:", acc)
