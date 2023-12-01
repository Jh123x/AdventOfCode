from typing import Tuple


FILE_PATH = 'input.txt'
WINDOW_SIZE = 5


def parse_word(word: str) -> Tuple[int, bool]:
    if word.startswith("one"):
        return "1", True
    if word.startswith("two"):
        return "2", True
    if word.startswith("three"):
        return "3", True
    if word.startswith("four"):
        return "4", True
    if word.startswith("five"):
        return "5", True
    if word.startswith("six"):
        return "6", True
    if word.startswith("seven"):
        return "7", True
    if word.startswith("eight"):
        return "8", True
    if word.startswith("nine"):
        return "9", True
    return word[0], False

def parse_line(line: str) -> int:
    """parse each line from the file"""
    no = ["", ""]
    for i, char in enumerate(line):
        char, isNo = parse_word(line[i: i+ WINDOW_SIZE])
        if not isNo and not char.isdigit():
            continue
        if no[0] == "":
            no[0] = char
        no[1] = char
    return int("".join(no))




if __name__ == '__main__':
    with open(FILE_PATH, 'r') as f:
        lines = f.readlines()
    sum_val = 0
    for line in lines:
        sum_val += parse_line(line)
    print(sum_val)