def num2bin(num:int):
    return "{0:b}".format(num).zfill(36)

def bin2num(bin_str:int):
    return int(bin_str, base=2)

def part1(data:list):
    mem = {}
    mask = None
    for line in data:
        var, value = tuple(map(lambda x: x.strip(), line.split("=")))
        if (var == 'mask'):
            mask = value
        else:

            #Get position
            addr = int(var.split('[')[1][:-1])
            

            #Get value
            value = int(value)
            b_value = num2bin(value)

            #Translate Value
            acc = []
            for a_digit, m_digit in zip(b_value, mask):
                if m_digit == 'X':
                    acc.append(a_digit)
                else:
                    acc.append(m_digit)

            #Add it to the memory
            mem[addr] = bin2num("".join(acc))

    return sum(mem.values())


def part2(data:list):
    mem = {}
    mask = None
    for line in data:
        var, value = tuple(map(lambda x: x.strip(), line.split("=")))
        if (var == 'mask'):
            mask = value
        else:

            #Get position
            addr = int(var.split('[')[1][:-1])
            b_addr = num2bin(addr)

            #Get value
            value = int(value)

            #Translate address
            acc = []
            for a_digit, m_digit in zip(b_addr, mask):
                combi = []
                if m_digit == 'X':
                    pass
                elif m_digit == '0':
                    pass
                else:
                    pass

            #Add it to the memory
            mem[addr] = bin2num("".join(acc))

    return sum(mem.values())


with open('data.txt') as file:
    data = file.readlines()

print(part1(data))