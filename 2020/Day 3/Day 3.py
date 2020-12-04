import numpy

with open('data.txt','r') as file:
    data = file.readlines()
    adj_mat = list(map(lambda x : list(x.strip()), data))

def compute(adj_mat, x_change, y_change):
    height = len(adj_mat)
    width = len(adj_mat[0])
    curr_x, curr_y = 0, 0
    acc = 0

    while(curr_y < height):

        #Check if current coord is a tree
        if(adj_mat[curr_y][curr_x] == '#'):
            acc += 1

        #Update the coordinates
        curr_x = (curr_x + x_change) % width
        curr_y += y_change

    return acc

change = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
arr = []

for x_change, y_change in change:
    arr.append(compute(adj_mat, x_change, y_change))

#Part 1
print(arr[1])

#Part 2
print(numpy.prod(arr))