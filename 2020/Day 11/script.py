def check(prev:list, row:int, col:int, rows:int, cols:int):

    #Get current state
    curr_state = prev[row][col]

    #If it is the floor just return the floor
    if(curr_state == '.'):
        return '.'

    #For iteration
    row_iter = [1, 1, 1, -1, -1, -1, 0, 0]
    col_iter = [-1, 0, 1, -1, 0, 1, 1, -1]
    
    #Count number of occupied seats
    acc = 0

    #Iterate through all 8 of the adj seats
    for i in range(8):

        #Check for resulting row and col
        row_check = row + row_iter[i]
        col_check = col + col_iter[i]

        #If out of range, skip it
        if(row_check < 0 or row_check >= rows or col_check < 0 or col_check >= cols):
            continue

        else:
            #Check if it is occupied
            if (prev[row_check][col_check] == '#'):

                #Increase Acc if it is occupied
                acc += 1

    #If seat is occupied
    if(curr_state == '#' and acc >= 4):
        new_state = 'L'
    elif(curr_state == 'L' and acc == 0):
        new_state = '#'
    else:
        new_state = curr_state

    return new_state

def part_iter(data, check_func):
    prev = None
    new = data
    rows = len(data)
    cols = len(data[0])
    changes = 0
    while (prev != new):

        prev = new
        total = []

        for row in range(rows):
            curr_row = []
            for col in range(cols):
                curr_row.append(check_func(prev, row, col, rows, cols))
            total.append(tuple(curr_row))

        #Set new one
        new = tuple(total)
        changes += 1
    return sum(map(lambda x: len(tuple(filter(lambda y: y == '#', x))), total))

def part1(data:tuple):
    return part_iter(data, check)

def check2(prev:list, row:int, col:int, rows:int, cols:int):

    #Get current state
    curr_state = prev[row][col]

    #If it is the floor just return the floor
    if(curr_state == '.'):
        return '.'

    #For iteration
    row_iter = [1, 1, 1, -1, -1, -1, 0, 0]
    col_iter = [-1, 0, 1, -1, 0, 1, 1, -1]
    
    #Count number of occupied seats
    acc = 0

    #Iterate through all 8 of the adj seats
    for i in range(8):

        #Check for resulting row and col
        row_check = row + row_iter[i]
        col_check = col + col_iter[i]

        #If out of range, skip it
        if(row_check < 0 or row_check >= rows or col_check < 0 or col_check >= cols):
            continue

        while not (row_check < 0 or row_check >= rows or col_check < 0 or col_check >= cols):
            
            if prev[row_check][col_check] == '.':
                row_check += row_iter[i]
                col_check += col_iter[i]
            else:
                #Check if it is occupied
                if (prev[row_check][col_check] == '#'):

                    #Increase Acc if it is occupied
                    acc += 1
                break

    #If seat is occupied
    if(curr_state == '#' and acc >= 5):
        new_state = 'L'
    elif(curr_state == 'L' and acc == 0):
        new_state = '#'
    else:
        new_state = curr_state

    return new_state

def part2(data):
    return part_iter(data, check2)

with open('data.txt') as file:
    data = tuple(map(lambda x: tuple(x.strip()), file.readlines()))

print(part1(data))
print(part2(data))

