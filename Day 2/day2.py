with open('day2.txt', 'r') as file:
    data = file.readlines()

acc = 0
for item in data:
    count, letter, password = item.split(" ")
    lower, higher = list(map(int, count.split("-")))
    letter = letter[0]
    if lower <= password.count(letter) <= higher:
        acc += 1

print(acc)
