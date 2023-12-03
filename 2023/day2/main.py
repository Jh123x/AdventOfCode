from typing import Tuple

FILE_NAME = "input.txt"

def parse_line(line: str) -> Tuple[int, int, int]:
    """Parse a line of the input file."""
    groups = line.split(";")
    color_acc = {"red": 0, "blue": 0, "green": 0}
    for grp in groups:
        for entry in grp.split(", "):
            entry = entry.strip()
            count, color = entry.split(" ")
            count = int(count)
            color_acc[color] = max(count,color_acc[color])
    print(color_acc)
    return color_acc["red"],  color_acc["green"], color_acc["blue"]

if __name__ == '__main__':
    # Red, Green, Blue
    max_counts = [12, 13, 14]
    with open(FILE_NAME, 'r') as f:
        lines = f.readlines()
        
    id_sum = 0
    pow_sum = 0
    for idx, line in enumerate(lines):
        game_count, game_line = line.split(":")
        game_no = int(game_count.split(" ")[1])
        r,b,g = parse_line(game_line)
        pow_sum += r * b * g
        if r > max_counts[0] or b > max_counts[1] or g > max_counts[2]:
            continue
        id_sum += game_no
    print("Part 1:", id_sum)
    print("Part 2:", pow_sum)