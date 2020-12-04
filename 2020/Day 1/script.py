def get_min_max(arr:list, key) -> tuple:
    min = arr[0]
    max = arr[0]
    for num in arr:
        if key(num) < key(min):
            min = num
        elif key(num) > key(max):
            max = num
    return min,max

def counting_sort(arr:list, key) -> list:

    #Get minimum and maximum
    minimum, maximum = get_min_max(arr, key)

    #Generate the table
    counting_table = []
    for _ in range(key(minimum), key(maximum) + 1):
        counting_table.append([])

    #Counting sort the item
    for item in arr:
        counting_table[key(item) - key(minimum)].append(item)
    
    #Put the items back to the original arr
    index = 0
    for lst in counting_table:
        while(len(lst) > 0):
            arr[index] = lst.pop(0)
            index += 1

    return arr

# Get the data
with open("data.txt",'r') as file:
    data = file.readlines()

# Change the data into a set
data = list(map(lambda x: int(x.strip()), data))

counting_sort(data, lambda x:x)

print(data)


# 272423970

