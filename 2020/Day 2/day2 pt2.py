with open('day2.txt', 'r') as file:
    data = file.readlines()

acc = 0
for item in data:
    count, letter, password = item.split(" ")
    lower, higher = list(map(lambda x: int(x) - 1, count.split("-")))
    letter = letter[0]

    if lower >= len(password) or password[lower] == password[higher] == letter:
        continue
    elif password[lower] == letter:
        acc += 1
    elif password[higher] == letter:
        acc += 1


print(acc)