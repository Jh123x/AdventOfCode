from copy import deepcopy
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


def generate_combinations(bin_addr:str, bit_mask:str):
    """Generate the combinations based on the mask"""
    combinations = [[]]
    for index, (bin_digit, mask_digit) in enumerate(zip(bin_addr, bit_mask)):
        
        if bin_digit == mask_digit:
            for item in combinations:
                item.append(mask_digit)

        elif mask_digit == '1':
            for item in combinations:
                item.append('1')

        elif mask_digit == '0':
            for item in combinations:
                item.append(bin_digit)

        else:
            curr_len = len(combinations)
            combinations += deepcopy(combinations)

            for i in range(0, curr_len):
                combinations[i].append('1')

            for i in range(curr_len, curr_len * 2):
                combinations[i].append('0')

    return tuple(map(lambda x: "".join(x), combinations))
            


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
            combinations = generate_combinations(b_addr, mask)
            for combi in combinations:
                mem[combi] = value
                

    return sum(mem.values())


with open('data.txt') as file:
    data = file.readlines()

print(part1(data))
print(part2(data))