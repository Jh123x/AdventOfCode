import argparse
from typing import List, Tuple

def read_file(file_name: str) -> List[Tuple[int, int]]:
    with open(file_name) as f:
        data = f.read()
    return list(map(lambda x: tuple(map(int,x.split('-'))), data.split(',')))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str, help="File to be processed")

    args = parser.parse_args()
    file_name = args.file_name
    
    ranges = read_file(file_name)
    invalid_id_sum = 0
    invalid_sum_2 = 0
    for start, end in ranges:
        for curr_no in range(start, end + 1):
            curr_no_str = str(curr_no)
            str_len = len(curr_no_str)
            half_len = str_len // 2
            if str_len > 0 and str_len % 2 == 0 and curr_no_str[:half_len] == curr_no_str[half_len:]:
                invalid_id_sum += curr_no

            acc = ''
            for idx, letter in enumerate(curr_no_str):
                if idx + 1 > half_len:
                    break
                acc += letter

                if str_len % len(acc) > 0:
                    continue

                if curr_no_str == acc * (str_len // len(acc)):
                    invalid_sum_2 += curr_no
                    break

    print("Part 1 Result:", invalid_id_sum)
    print("Part 2 Result:", invalid_sum_2) # 20077276822

