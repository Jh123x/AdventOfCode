with open("data.txt",'r') as file:
    data = list(map(lambda x: x.strip(), file.readlines()))

# data = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

def calc(col, row):
    return row * 8 + col

max_row = 127 #Inclusive
max_col = 7 #Inclusive
seats = set()
for seat in data:
    max_r, min_r = max_row, 0
    max_c, min_c = max_col, 0
    for letter in seat:
        mid_r = (max_r + min_r) // 2
        mid_c = (max_c + min_c) // 2
        if(letter == "F"):
            max_r = mid_r
        elif(letter == "B") :
            min_r = mid_r + 1
        elif (letter == "R"):
            min_c = mid_c + 1
        else:
            max_c = mid_c
    res = calc(min_c, min_r)
    seats.add(res)

print(max(seats)) #Part 1


#Part 2
for res in range(13, 822):
        if(res not in seats):
            print(res)

