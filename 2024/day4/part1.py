from typing import List, Tuple

# file_name = 'test1.txt'
# file_name = 'test.txt'
file_name = 'input.txt'

directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

def is_valid(map: List[str], x: int, y: int) -> bool:
    return 0 <= x < len(map) and 0 <= y < len(map[0])

def print_grid(map: List[str], x: int, y:int, direction: Tuple[int, int]):
    printed_pts = [(x, y)]
    dx, dy = direction
    for _ in range(3):
        x += dx
        y += dy
        printed_pts.append((x, y))
    
    for x in range(len(map)):
        for y in range(len(map[0])):
            if (x, y) in printed_pts:
                print(map[x][y], end="")
            else:
                print(".", end ="")
        print()
    print()
        

def find_m(map: List[str], curr_x: int, curr_y: int) -> int:
    count = 0
    for dx, dy in directions:
        new_x = curr_x + dx
        new_y = curr_y + dy
        if not is_valid(map, new_x, new_y) or map[new_x][new_y] != "M":
            continue
        if not find_as(map, new_x, new_y, (dx, dy)):
            continue
        print_grid(map, curr_x, curr_y, (dx, dy))
        count += 1
    return count

def find_as(map: List[str], curr_x: int, curr_y: int, direction: Tuple[int, int]) -> bool:
    dx, dy = direction
    for letter in 'AS':
        curr_x += dx
        curr_y += dy
        if not is_valid(map, curr_x, curr_y) or map[curr_x][curr_y] != letter:
            return 0
        
    return 1

def part1(map: List[str]) -> int:
    count = 0
    for x, row in enumerate(map):
        for y, letter in enumerate(row):
            if letter == 'X':
                count += find_m(map, x, y)

    return count


if __name__ == '__main__':
    with open(file_name) as f:
        rows = list(map(
            lambda x: x.strip(),
            f.readlines(),
        ))
        
    print(part1(rows))
