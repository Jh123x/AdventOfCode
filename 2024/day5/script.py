from typing import List, Dict, Set, Tuple
from collections import defaultdict
from functools import cmp_to_key

# file_name = 'test.txt'
file_name = 'input.txt'
RuleType = Dict[int, Set[int]]


def is_valid_page(rules: RuleType, page: List[int]) -> int:
    s = set()
    used = set()
    for no in page:
        if no in s:
            s.remove(no)
        if no in rules:
            s = s.union(rules[no])
        used.add(no)

    if len(s.intersection(used)) > 0:
        return 0

    return page[len(page) // 2]


def part1(rules: RuleType, pages: List[List[int]]) -> int:
    return sum(is_valid_page(rules, page) for page in pages)

def reorder_correctly(rule_list: List[Tuple[int, int]], candidates: List[int]) -> int:
    rule_set = set(rule_list)
    def cmp(n1:int , n2: int) -> int:
        return -1 if (n1, n2) in rule_set else 0
    candidates.sort(key=cmp_to_key(cmp))
    return candidates[len(candidates) // 2]

def part2(rules: RuleType, rule_list: List[Tuple[int, int]], pages: List[List[int]]) -> int:
    count = 0
    for page in pages:
        if is_valid_page(rules, page):
            continue
        count += reorder_correctly(rule_list, page)
    return count

if __name__ == '__main__':
    with open(file_name) as f:
        data = f.read()

    raw_rules, raw_pages = data.split("\n\n")
    rule_list = list(
        map(
            lambda x: tuple(map(int, x.split("|"))),
            raw_rules.split("\n"),
        ),
    )
    pages = list(
        map(
            lambda x: list(map(int, x.split(","))),
            raw_pages.split("\n"),
        ),
    )

    rules = defaultdict(set)
    for k, v in rule_list:
        rules[k].add(v)

    results = part1(rules, pages)
    print(results)
    results = part2(rules, rule_list, pages)
    print(results)
