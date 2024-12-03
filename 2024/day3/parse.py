import re


file_name = 'input.txt'
# file_name = 'test.txt'
detect_regex = re.compile(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))")

def part1(line:str) -> int:
    results = detect_regex.findall(line)
    acc = 0
    is_enabled = True
    for mul, do, dont in results:
        if len(mul) > 0 and is_enabled:
            n1, n2 = mul[4:-1].split(",")
            acc += int(n1) * int(n2)
        if len(do) > 0:
            is_enabled = True
        if len(dont) > 0:
            is_enabled = False
    return acc
    
if  __name__ == '__main__':
    with open(file_name) as f:
        line = f.read()
    print(part1(line))
