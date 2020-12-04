import re
with open("data.txt", 'r') as file:
    data = file.read()

attributes = set(("byr","iyr", "eyr", "hgt", "hcl", "ecl", "pid"))

acc = 0
datachunk = tuple(map(lambda x: tuple(map(lambda y: y[:3], re.split("\n| ", x.strip()))), data.split("\n\n")))
for d in datachunk:
    if attributes.issubset(d):
        acc += 1
    
print(acc)
            