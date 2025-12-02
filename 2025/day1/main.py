from typing import List



def read_file(file_name: str) -> List[str]:
    with open(file_name) as f:
        return list(map(lambda x: x.strip(), f.readlines()))

if __name__ == '__main__':
    input_file = './input.txt'
    #input_file = 'test_input.txt'
    data = read_file(input_file)
    hits = 0
    hits2 = 0
    current = 50
    for move in data:
        direction = move[0]
        spaces = int(move[1:])
        for _ in range(spaces):
            if direction == 'R':
               current += 1
            else:
                current -= 1 
            current %= 100
            if current == 0:
                hits2 += 1
        if current == 0:
            hits += 1

    print("Part 1:",hits)
    print("Part 2:",hits2)
