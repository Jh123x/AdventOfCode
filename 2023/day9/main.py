from typing import List,Tuple

FILE_NAME = "input.txt"


def process(sequences: List[List[int]], process_fn, res_idx: int) -> int:
    acc = 0
    for sequence in sequences:
        result = process_fn(sequence)
        acc += result[res_idx]
    return acc


def process_part1(sequence: List[int]) -> List[int]:
    if len(set(sequence)) == 1:
        sequence.append(sequence[0])
        return sequence

    seq2 = []
    for i in range(len(sequence)-1):
        seq2.append(sequence[i+1] - sequence[i])

    result = process_part1(seq2)
    seq2.append(sequence[-1] + result[-1])
    return seq2


def process_part2(sequence: List[int]) -> List[int]:
    if len(set(sequence)) == 1:
        sequence.append(sequence[0])
        return sequence

    seq2 = []
    for i in range(len(sequence)-1):
        seq2.append(sequence[i+1] - sequence[i])

    result = process_part2(seq2)
    return [sequence[0] - result[0]] +  sequence


if __name__ == "__main__":
    with open(FILE_NAME) as f:
        data = f.readlines()

    processed_data = list(map(lambda x: list(map(int, x.split(" "))), data))
    res = process(processed_data, process_part1, -1)
    print("Part 1:", res)
    res2 = process(processed_data, process_part2, 0)
    print("Part 2:", res2)
