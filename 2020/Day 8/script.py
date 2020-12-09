
def read_file(filename:str):
    with open(filename) as file:
        return tuple(map(lambda x: x.strip(), file.readlines()))

command_dict = {
    "jmp": lambda pc, acc, optval: (acc, pc+optval),
    "nop": lambda pc, acc, optval: (acc, pc+1),
    "acc": lambda pc, acc, optval: (acc + optval, pc+1)
}

def parse_command(command:str, acc:int, pc:int):
    cmd, val = tuple(map(lambda x: x.strip(), command.split(" ")))
    return command_dict[cmd](pc, acc, int(val))

def execute(data):
    pc = 0
    acc = 0
    executed_commands = set()

    while(pc < len(data)):
        if(pc in executed_commands):
            return False, acc
        cmd = data[pc] #Get current command
        executed_commands.add(pc)
        acc, pc = parse_command(cmd, acc, pc)

    return True, acc

def part1(data):
    _, acc = execute(data)
    return acc

def generate_combination(data):
    for index, value in enumerate(data):
        cmd, val = value.split(" ")
        if cmd == "nop":
            yield data[:index] + (f"jmp {val}",) + data[index+1:]
        elif cmd == 'jmp':
            yield data[:index] + (f"nop {val}",) + data[index+1:]

def part2(data):
    complete = False
    for d in generate_combination(data):
        complete, acc = execute(d)
        if(complete):
            break
        
    return acc

if __name__ == "__main__":
    data = read_file('data.txt')
    print(part1(data))
    print(part2(data))
