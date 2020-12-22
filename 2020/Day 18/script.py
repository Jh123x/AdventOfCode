import re

def find_matching_bracket(line:str, brackets:int = 0):
    for index,value in enumerate(line):
        if value == '(':
            brackets += 1
            continue
        if value != ')':
            continue
        if brackets == 0:
            return index

        brackets -= 1
    return None


def eval_exp(line:str, bracket:int = 0):
    acc = 0
    index = 0
    flag = False
    stack = []
    while index < len(line):
        
        value = line[index]
        index += 1

        if value == " ":
            continue

        if value == "(":
            end = index + find_matching_bracket(line[index:])
            value = eval_exp(line[index : end], bracket + 1)
            index += end - index + 1

        elif value in "+*":
            stack.append(value)
            continue
        
        if flag:
            acc = eval(f"{acc}{stack.pop()}{value}")
        else:
            flag = True
            acc = int(value)
        
    return acc


def part1(data:list):
    acc = 0
    for line in data:
        acc += eval_exp(line)
    return acc



if __name__ == "__main__":
    with open('data.txt') as file:
        data = file.read().split("\n")
    # print(part1(["1 + 2 * 3 + 4 * 5 + 6"]))
    # print(part1(["1 + (2 * 3) + (4 * (5 + 6))"]))
    # print(part1(["2 * 3 + (4 * 5)"]))
    # print(part1(data))

    print(part2(["1 + 2 * 3 + 4 * 5 + 6"]))
    # print(part2(["1 + (2 * 3) + (4 * (5 + 6))"]))
    # print(part2(["2 * 3 + (4 * 5)"]))
    # print(part2(data))