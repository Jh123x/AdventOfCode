from typing import List, Tuple

# file_name = "small.txt"
file_name = "test.txt"
# file_name = 'input.txt'

Point = Tuple[int, int]


class Map:
    def __init__(self, warehouse_map: str):
        self.map, self.robot_pos = self.__parse_map(warehouse_map)

    def __parse_map(self, warehouse_map: str) -> Tuple[List[List[str]], Point]:
        map_val = []
        robot_point = None
        for row in warehouse_map.split("\n"):
            map_val.append(list(row))
            idx = row.find("@")
            if idx == -1:
                continue
            robot_point = (len(map_val) - 1, idx)
        return map_val, robot_point

    def get_checksum(self) -> int:
        checksum = 0
        for x, row in enumerate(self.map):
            for y, letter in enumerate(row):
                if letter != 'O':
                    continue
                checksum += 100 * x + y
        return checksum

    def __repr__(self) -> str:
        return f"{"\n".join(map(lambda x: "".join(x), self.map))}\nRobot at: {self.robot_pos}"

    def process_move(self, move: str):
        match (move):
            case "<":
                self.process_dir((0, -1))
            case ">":
                self.process_dir((0, 1))
            case "^":
                self.process_dir((-1, 0))
            case "v":
                self.process_dir((1, 0))

    def process_dir(self, direction: Point):
        dx, dy = direction
        x, y = self.robot_pos
        ori_x, ori_y = self.robot_pos
        while True:
            if self.map[x][y] == '#':
                return
            if self.map[x][y] == '.':
                break
            x += dx
            y += dy

        if x != ori_x + dx or y != ori_y + dy:
            self.map[x][y] = 'O'

        robot_pos = (ori_x + dx, ori_y + dy)
        self.map[ori_x][ori_y] = '.'
        self.map[robot_pos[0]][robot_pos[1]] = '@'
        self.robot_pos = robot_pos


def parse_moves(robot_moves: str) -> str:
    return "".join(robot_moves.split("\n"))


def part1(map_val: Map, moves: str):
    for m in moves:
        map_val.process_move(m)
    return map_val.get_checksum()


def expand_map(raw_map: str) -> str:
    return raw_map.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")


if __name__ == '__main__':
    with open(file_name) as f:
        raw_map, raw_moves = f.read().split("\n\n")

    moves = parse_moves(raw_moves)
    expanded_map = expand_map(raw_map)
    map_val_2 = Map(expanded_map)

    print(part1(map_val_2, moves))
