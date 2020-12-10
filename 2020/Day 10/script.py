def get_min_max(lst):
    mini = lst[0]
    maxi = lst[0]
    for i in lst:
        if i > maxi:
            maxi = i
        elif i < mini:
            mini = i
    return mini, maxi

#Sort the array
def counting_sort(lst):
    mini, maxi = get_min_max(lst)
    arr = [0] * (maxi - mini + 3)
    for i in lst:
        arr[i-mini] += 1

    ind = 0
    for i, value in enumerate(arr):
        while(value > 0):
            value -= 1
            lst[ind] = i + mini
            ind += 1
    return lst

def part1(data):
    sorted_data = counting_sort(data)
    d = {
        1: 0,
        2: 0,
        3: 1,
    }
    for i in range(len(sorted_data) - 1):
        d[sorted_data[i+1] - sorted_data[i]] += 1

    return (d[1] * d[3])



def part2(data):

    #Sort the data O(n)
    _, maxi = get_min_max(data)
    sorted_data = [0] + counting_sort(data) + [maxi + 3]

    #Turn the problem into a graph problem
    d = {}

    # Form a tree O(n^2)
    for index, value in enumerate(sorted_data):
        d[value] = []
        for i in range(index + 1, len(sorted_data)):
            if sorted_data[i] > value + 3:
                break
            else:
                d[value].append(sorted_data[i])

    #O(n) dp
    mem = {}
    for value in reversed(sorted_data):
        if(value == maxi + 3):
            result = 1
        else:
            result = 0
            for i in d[value]:
                result += mem[i]
        mem[value] = result

    #Return value at 0
    return mem[0]


with open('data.txt') as file:
    data = list(map(int, file.readlines()))
        
print(part1([0] + data))
print(part2(data))