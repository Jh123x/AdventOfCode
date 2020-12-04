# Get the data
with open("data.txt",'r') as file:
    data = file.readlines()

# Change the data into a set
data = set(map(lambda x: int(x.strip()), data))


def part1(data):
    for i in data:
        com = (2020 - i)
        if com in data:
            print(com * i)

def part2(data):
    for i in data:
        for j in data:
            if i == j:
                continue
            com = (2020-i-j)
            if com in data:
                print(com * i * j)


#Part 1
part1(data)

#Part 2
part2(data)

