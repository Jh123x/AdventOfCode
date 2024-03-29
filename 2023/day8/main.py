# Start from AAA reach ZZZ
# Return number of steps required.
# R, go right, L go left, instructions loop on itself infinitely.
from typing import Tuple, Dict, List

FILE_NAME = "input.txt"
INSTRUCTIONS = str
Tree = Dict[str, Dict[str, str]]


def part1(data: str) -> int:
    """Returns the number of times it takes to reach the start"""
    curr, end, steps = "AAA", "ZZZ", 0
    insts, tree = parse_file(data=data)
    inst_len = len(insts)
    while curr != end:
        dir = insts[steps % inst_len]
        curr = tree.get(curr, {}).get(dir, "")
        if len(curr) == 0:
            raise Exception("Invalid path")
        steps += 1
    return steps


def parse_file(data: str) -> Tuple[INSTRUCTIONS, Tree]:
    inst, raw_tree = data.split("\n\n")
    tree: Tree = {}
    for line in raw_tree.split("\n"):
        if len(line) == 0:
            continue
        key, branches = line.split(" = ")
        left, right = branches[1:-1].replace(" ", "").split(",")
        tree[key] = {"L": left, "R": right}
    return inst.strip(), tree


if __name__ == "__main__":
    with open(FILE_NAME) as f:
        data = f.read()
    try:
        res = part1(data)
        print("Part 1:", res)
    except Exception as e:
        print("Part 1 (Skipped):", e)
