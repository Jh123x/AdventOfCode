import argparse
from os import WCOREDUMP
from typing import List, Tuple, Dict
from heapq import heappush, heappop
from collections import defaultdict

Coord = Tuple[int,int,int]

def read_file(file_name: str) -> List[Coord]:
    with open(file_name) as f:
        return [tuple(map(int,row.strip().split(','))) for row in f.readlines()]

def euclid_dist(pt1: Coord, pt2: Coord) -> int:
    return sum(abs(pt1[i] - pt2[i])**2 for i in range(3))

def get_parent(ufds: Dict[Coord, Coord], pt: Coord) -> Coord:
    if pt not in ufds:
        return pt
    curr_pt = pt
    while ufds[curr_pt] != curr_pt:
        curr_pt = ufds[curr_pt]

    ufds[pt] = curr_pt
    return curr_pt

def has_parent(ufds: Dict[Coord, Coord], pt: Coord) -> bool:
    return pt in ufds

def set_parent(ufds: Dict[Coord, Coord], pt:Coord, parent_pt: Coord) -> None:
    ufds[pt] = parent_pt

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", type=str, help="Input file name")
    parser.add_argument("--edges", type=int, help="edges to choose")
    args = parser.parse_args()
    file_name = args.file_name

    data = read_file(file_name)
   
    edge_list = []
    for idx, coord in enumerate(data):
        for idx2 in range(idx+1, len(data)):
            coord2 = data[idx2]
            dist = euclid_dist(coord, coord2)
            heappush(edge_list, (dist, coord, coord2))
    ufds = {coord: coord for coord in data}

    edge_list_cpy = edge_list.copy()
    ufds_cpy = ufds.copy()

    # Kruskals Algo with max of x
    ctr = args.edges
    while ctr > 0:
        ctr -=1
        _, coord1, coord2 = heappop(edge_list)
        top1 = get_parent(ufds, coord1)
        top2 = get_parent(ufds, coord2)
        if top1 == top2:
            continue
        set_parent(ufds, top1, top2)

    grp_counter = defaultdict(int)
    for c in data:
        grp_counter[get_parent(ufds, c)] += 1

    results = sorted(map(lambda x: x[1], grp_counter.items()), reverse=True)

    acc = 1
    for i in results[:3]: 
        acc *= i

    print("Part 1:", acc)

    edge_list = edge_list_cpy
    ufds = ufds_cpy

    c1, c2 = (0,0,0),(0,0,0)
    while len(edge_list) > 0:
        _, coord1, coord2 = heappop(edge_list)
        top1 = get_parent(ufds, coord1)
        top2 = get_parent(ufds, coord2)
        if top1 == top2:
            continue
        set_parent(ufds, top1, top2)
        c1, c2 = coord1, coord2

    print("Part 2:", c1[0] * c2[0])

