from typing import List, Tuple

file_name = 'input.txt'
# file_name = 'test.txt'

def is_safe_report(rpt: List[int]) -> bool:
    if len(rpt) == 0:
        return True
    total_diff = 0
    prev = rpt[0]
    for i in range(1, len(rpt)):
        no = rpt[i]
        diff, prev = prev - no, no
        if abs(diff) < 1 or abs(diff) > 3 or diff < 0 and total_diff > 0 or diff > 0 and total_diff < 0:
            return False

        total_diff += diff

    return True

def part1(reports: List[List[int]]) -> int:
    safe_reports = 0
    for rpt in reports:
        if not is_safe_report(rpt):
            continue
        safe_reports += 1
            
    return safe_reports

def part2(reports: List[List[int]]) -> int:
    safe_reports = 0
    for rpt in reports:
        if not is_kinda_safe_report(rpt):
            continue
        safe_reports += 1

    return safe_reports

def is_kinda_safe_report(rpt: List[int]) -> int:
    # If any chopped up ones are true, it is true
    for i in range(len(rpt)):
       if is_safe_report(rpt[:i] + rpt[i+1:]):
           return True
    return False
    
if __name__ == '__main__':
    reports = []
    with open(file_name) as f:
        for row in f.readlines():
            report = list(map(int, row.split()))
            reports.append(report)

    print(part1(reports))
    print(part2(reports))