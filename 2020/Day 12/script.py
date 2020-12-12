def calculate1(data:list, waypoint = (0,1)):
    """Calculate the values"""
    '''Direction
        1: North
        2: East
        3: South
        4: West
    '''

    waypoint_map = {
        'N': lambda x,y: (x, y),
        'E': lambda x,y: (y, -x),
        'S': lambda x,y: (-x, -y),
        'W': lambda x,y: (-y, x),
    }

    movement_mapping = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0,-1),
        'W': (-1,0),
    }

    dirs = {
        'N': 0, 0: 'N',
        'E': 1, 1: 'E',
        'S': 2, 2: 'S',
        'W': 3, 3: 'W',
    }

    curr_dir = 'E'
    position = [0, 0] #x, y

    for movement in data:

        direction = movement[0]
        space = int(movement[1:])

        # Get current direction
        if direction == 'F':
            x_change, y_change = waypoint_map[curr_dir](*waypoint)
            position[0] += x_change * space
            position[1] += y_change * space
            continue

        if (direction in movement_mapping.keys()):

            #Shift the position
            x_change, y_change = movement_mapping[direction]
            position[0] += x_change * space
            position[1] += y_change * space
            continue

        #Change direction
        change = space // 90
        dir_num = dirs[curr_dir]
        if direction == 'R':
            d = (dir_num + change)
        elif direction == 'L':
            d = (dir_num - change)
        else:
            raise Exception(f"Not suppose to be here {direction}")
        curr_dir = dirs[d % 4]

    return tuple(position)


def part1(data:tuple):
    '''Part 1 solution'''
    #Calculate position
    position = calculate1(data)

    #Return pos1 + pos2
    return abs(position[0] + position[1])

def calculate2(data:list, waypoint:list):
    '''Direction
        1: North
        2: East
        3: South
        4: West
    '''

    movement_mapping = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0,-1),
        'W': (-1,0),
    }

    position = [0, 0] #x, y

    for movement in data:

        direction = movement[0]
        space = int(movement[1:])

        # Get current direction
        if direction == 'F':
            x_change, y_change = waypoint
            position[0] += x_change * space
            position[1] += y_change * space
            continue

        if (direction in movement_mapping.keys()):

            #Shift the position
            x_change, y_change = movement_mapping[direction]
            waypoint[0] += x_change * space
            waypoint[1] += y_change * space
            continue

        #Change direction
        change = space // 90
        if direction == 'R':
            for _ in range(change):
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
        elif direction == 'L':
            for _ in range(change):
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
        else:
            raise Exception(f"Not suppose to be here {direction}")

    return tuple(position)

def part2(data:tuple):
    waypoint = [10, 1]
    position = calculate2(data, waypoint) 
    return abs(position[0]) + abs(position[1])

with open('data.txt') as file:
    data = tuple(map(lambda x: x.strip(), file.readlines()))

print(part1(data))
print(part2(data))