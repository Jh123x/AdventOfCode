from collections import deque

def parse_front(front:str):
    return front.strip()

def parse_back(back:str):
    acc = {}
    for item in back.strip().split(","):
        count, res = item.strip().split(" ", 1)
        if count == 'no':
            break
        acc[res] = int(count.strip())
    return acc

def parse_line(line:str):
    front, back = line.replace("bags", "bag").replace(".", "").split(" contain ")
    return parse_front(front), parse_back(back)

def parse_data(lines:list):
    acc = []
    for item in lines:
        acc.append(parse_line(item))
    return acc

def read_file(filename:str):
    """Read the file with filename"""
    with open(filename) as file:
        return parse_data(file.readlines())


def part1(data:tuple):
    #Make a directed graph
    graph = {}

    #Iterate through the items
    for bag, contents in data:
        for inner_bag in contents:
        
            #Invert the arrows as we are going bottom up
            if(not inner_bag in graph):
                graph[inner_bag] = []

            #Add the bag to al
            graph[inner_bag].append(bag)

    # Flood fill to get those reachable by the golden bag
    reachable = set() #Also acts as visited

    #BFS from 'shiny gold bag'
    bfs_q = deque()

    #Put the starting item
    bfs_q.append('shiny gold bag')

    #Flood fill
    while(len(bfs_q) > 0):

        #Get first element
        ele = bfs_q.popleft()
        
        if ele in reachable:
            continue

        reachable.add(ele)
        
        if ele not in graph.keys():
            continue

        for bag in graph[ele]:
            bfs_q.append(bag)

    return len(reachable) - 1



def part2(data:tuple):
    #Make a directed graph
    graph = {}

    #Iterate through the items
    for bag, contents in data:
        for inner_bag, count in contents.items():
            #Do not invert the arrows as we are going down
            if(not bag in graph):
                graph[bag] = {}

            #Add the bag to al
            graph[bag][inner_bag] = count

    # Flood fill to get those reachable by the golden bag
    memoise = {} #For memoizing to make it faster / Also acts as visited

    #Put the starting item
    bag = 'shiny gold bag'

    def get_num_bags(bag:str):

        if bag in memoise:
            return memoise[bag]

        result = 0
        if bag in graph:
            for item, count in graph[bag].items():
                result += (get_num_bags(item) + 1) * count
        print(bag, result)
        memoise[bag] = result
        return result

    return get_num_bags(bag)


    
        




if __name__ == '__main__':
    data = read_file('data.txt')
    print(part1(data)) #Part 1
    print(part2(data)) #Part 2



