def part1(data):
    num = -1
    for i in range(25, len(data)):
        flag = False
        s = set()
        for j in range(i-25, i):
            s.add(data[j])
        for num in s:
            if (data[i] - num) in s:
                flag = True
                break

        if flag:
            continue
        else:
            return num
    return None



def part2(data, num):
    max_ind = data.index(num)
    start, end = None, None
    flag = False
    for i in range(max_ind):
        s = 0
        for j in range(i, max_ind):
            s += data[j]
            if s == num:
                start = i
                end = j
                flag = True
                break
        if flag:
            break
        
    
    return min(data[i:j+1]) + max(data[i:j+1])

if __name__ == "__main__":
    with open('data.txt') as file:
        data = tuple(map(int, file.readlines()))
    target = part1(data)
    print(target)
    print(part2(data, 258585477))
        






