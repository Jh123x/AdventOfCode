
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

def part1(data):
    pc = 0
    acc = 0
    executed_commands = set()

    while(pc < len(data)):
        if(pc in executed_commands):
            break
        cmd = data[pc] #Get current command
        executed_commands.add(pc)
        acc, pc = parse_command(cmd, acc, pc)

    return acc

def part2(data):
    pc = 0
    acc = 0
    executed_commands = set()

    while(pc < len(data)):
        cmd = data[pc] #Get current command
        if(pc in executed_commands):
            if("jmp" in cmd):
                print("jmp swap")
                cmd = cmd.replace('jmp', 'nop')
            else:
                print("nop swap")
                cmd = cmd.replace('nop', 'jmp')        
        executed_commands.add(pc)
        acc, pc = parse_command(cmd, acc, pc)

    return acc




if __name__ == "__main__":
    data = read_file('data.txt')
    print(part1(data))
    print(part2(data))
