import argparse
from typing import List, Tuple


Coord = Tuple[int,int]


def read_file(file_name: str) -> List[Coord]:
    result = []
    with open(file_name) as f:
        for row in f.readlines():
            x, y = row.strip().split(',')
            result.append((int(x),int(y)))
    return result

def form_rect(pt: Coord, pt2: Coord) -> int:
    x, y = pt
    x2, y2 = pt2

    return (abs(x-x2) + 1) * (abs(y - y2) + 1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Input file path")

    args = parser.parse_args()
    file_name = args.input_file

    points = read_file(file_name)
    
    max_area = 0
    for idx,pt in enumerate(points):
        for idx2 in range(idx + 1, len(points)):
            max_area = max(max_area, form_rect(pt, points[idx2]))

    print("Part 1:", max_area)
