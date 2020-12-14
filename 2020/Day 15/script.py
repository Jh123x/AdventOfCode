def part1(data:list, limit:int = 2020):

    #Store when the number was last spoken
    d = {}

    #Go through the data and store the timestamp
    for index,value in enumerate(data):
        if not value in d:
            d[value] = []
        d[value].append(index)


    #Initialise start value
    curr_index = len(data)
    while (curr_index <= limit - 1):
        prev_value = data[curr_index-1]
        if (len(d[prev_value]) == 1):
            curr_value = 0
        else:
            curr_value = curr_index - d[prev_value][-2] - 1

        data.append(curr_value)
        #Add current value to table
        if not curr_value in d:
            d[curr_value] = []
        d[curr_value].append(curr_index)
        curr_index += 1

    return data[limit - 1]

with open('data.txt') as file:
    data = list(map(lambda x: int(x.strip()), file.read().split(",")))


# print(part1([0,3,6]))
# print(part1([1,3,2]))
print(part1(data))


# print(part1([0,3,6], 30000000))
print(part1(data, 30000000))