from typing import List
from collections import defaultdict


file_name = "input.txt"

def part1(a1: List[int], a2: List[int]) -> int:
    a1.sort()
    a2.sort()
    
    return sum(map(lambda x: abs(x[0] - x[1]), zip(a1, a2)))

def part2(a1: List[int], a2: List[int]) -> int:
    score = 0
    freq_list_1 = defaultdict(int)
    freq_list_2 = defaultdict(int)
    for no in a1:
        freq_list_1[no] += 1

    for no in a2:
        freq_list_2[no] += 1

    for k, v in freq_list_1.items():
        score += v * (k * freq_list_2[k])
        
    return score
    

if __name__ == '__main__':
    a1, a2 = [], []
    with open(file_name) as f:
        for r in f.readlines():
            v1, v2 = r.split("   ")
            a1.append(int(v1))
            a2.append(int(v2))
    print(part1(a1, a2))
    print(part2(a1, a2))
    