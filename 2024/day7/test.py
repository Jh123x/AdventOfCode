from typing import Tuple, List, Callable
from tqdm import tqdm

file_name = 'test.txt'
file_name = 'input.txt'

operators = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    "|": lambda x, y: int(str(x) + str(y))
}


def is_possible(target: int, nos: List[int], curr_idx: int, curr: int, opts: str) -> Tuple[bool, str]:
    if curr_idx == len(nos):
        return target == curr, opts

    curr_elem = nos[curr_idx]
    for k, fn in operators.items():
        if k == '|':
            continue
        is_pos, opt_res = is_possible(target, nos, curr_idx + 1, fn(curr, curr_elem), opts + k)
        if not is_pos:
            continue

        return True, opt_res

    return False, ""


def evaluate(eqns: Tuple[int, List[int]], pos_fn: Callable[[int, List[int], int, str], Tuple[bool, str]]) -> int:
    total = 0
    for target, lst in tqdm(eqns, total=len(eqns)):
        is_pos, opts = pos_fn(target, lst, 1, lst[0], "")
        if not is_pos:
            continue

        eqn_str, eval_res = get_eqn(lst, opts)
        if debug:
            print(f"{target} = {eqn_str}")
        assert eval_res == target
        total += target

    return total


def is_possible_2(target: int, nos: List[int], curr_idx: int, curr: int, opts: str) -> Tuple[bool, str]:
    if curr_idx == len(nos):
        return target == curr, opts

    curr_elem = nos[curr_idx]
    for k, fn in operators.items():
        is_pos, opt_res = is_possible_2(target, nos, curr_idx + 1, fn(curr, curr_elem), opts + k)
        if not is_pos:
            continue

        return True, opt_res

    return False, ""


def get_eqn(lst: List[int], opts: str) -> Tuple[str, int]:
    builder = [str(lst[0])]
    acc = lst[0]

    for no, op in zip(lst[1:], opts):
        builder.append(op)
        builder.append(str(no))

        if op == '+':
            acc += no
        if op == '*':
            acc *= no
        if op == '|':
            acc = int(str(acc) + str(no))

    return ''.join(builder), acc


if __name__ == '__main__':
    debug = False
    with open(file_name) as f:
        rows = f.readlines()
    size = len(rows)
    eqns = []
    for row in rows:
        total, others = row.strip().split(": ")
        numbers = list(map(int, others.split(" ")))
        eqns.append((int(total), numbers))

    results = evaluate(eqns, is_possible)
    print(results)

    results = evaluate(eqns, is_possible_2)
    print(results)
