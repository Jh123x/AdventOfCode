from typing import List, Tuple
from tqdm.auto import tqdm


class Program:
    def __init__(self, a: int, b: int, c: int, program: List[int]):
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.idx = 0

    def run_program(self) -> List[int]:
        results = []
        while self.idx < len(self.program):
            inst = self.next_value()
            match inst:
                case 0:
                    self.parse_adv()
                case 1:
                    self.parse_bxl()
                case 2:
                    self.parse_bst()
                case 3:
                    self.parse_jnz()
                case 4:
                    self.parse_bxc()
                case 5:
                    result = self.parse_out()
                    results.append(result)
                case 6:
                    self.parse_bdv()
                case 7:
                    self.parse_cdv()
                case _:
                    break
        return results

    def next_value(self) -> int:
        if self.idx >= len(self.program):
            return -1
        v = self.program[self.idx]
        self.idx += 1
        return v

    def parse_combo(self) -> int:
        combo = self.next_value()
        match combo:
            case 0 | 1 | 2 | 3:
                return combo
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
            case _:
                raise Exception("unexpected operand")

    def parse_adv(self) -> None:
        """adv instruction"""
        self.a = self.parse_dv()

    def parse_dv(self) -> int:
        combo = self.parse_combo()
        return self.a // (2 ** combo)

    def parse_bxl(self) -> None:
        literal = self.next_value()
        self.b = self.b ^ literal

    def parse_bst(self) -> None:
        combo = self.parse_combo()
        self.b = combo % 8

    def parse_jnz(self) -> None:
        literal = self.next_value()
        if self.a == 0:
            return
        self.idx = literal

    def parse_bxc(self) -> None:
        self.next_value()
        self.b = self.b ^ self.c

    def parse_out(self) -> int:
        return self.parse_combo() % 8

    def parse_bdv(self) -> None:
        self.b = self.parse_dv()

    def parse_cdv(self) -> None:
        self.c = self.parse_dv()


def parse_reg(raw_reg: str) -> Tuple[int, int, int]:
    acc = []
    for reg in raw_reg.strip().split("\n"):
        acc.append(int(reg[12:]))
    return acc


def parse_prog(raw_prog: str) -> List[str]:
    return list(map(int, raw_prog.strip()[9:].split(",")))


def generator():
    a = 0
    while True:
        yield a
        a += 1


if __name__ == '__main__':
    # file_name = 'tc.txt'
    # file_name = 'test.txt'
    file_name = 'input.txt'

    with open(file_name) as f:
        raw = f.read()

    raw_reg, prog = raw.split("\n\n")
    a, b, c = parse_reg(raw_reg)
    prog = parse_prog(prog)

    # Part 1
    program = Program(a, b, c, prog)
    output = program.run_program()
    print(','.join(map(str, output)))

    # Part 2 (Incomplete)
    # start = 34493631492869
    # end = 45991503855616
    # start = 3449363149286
    # end = 45991503855616
    a = 25300847102451
    prog_len = len(prog)
    while True:
        p = Program(a, b, c, prog)
        output = p.run_program()
        if output == prog:
            break
        a += 1
    print(output, prog)
    i = 7
    while True:
        p = Program(a, b, c, prog)
        output = p.run_program()
        if output[-i:] == prog[-i:]:
            break
        print(a, output, bin(a))
        a += 100

    print(output, prog)
    print(a)
