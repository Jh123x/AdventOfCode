import re

cond = {
    "byr": lambda x : 1920 <= int(x) <= 2002,
    "iyr": lambda x : 2010 <= int(x) <= 2020,
    "eyr": lambda x : 2020 <= int(x) <= 2030,
    "hgt": lambda x : 150 <= int(x[:-2]) <= 193 if x[-2:].lower() == "cm" else 59 <= int(x[:-2]) <= 76,
    "ecl": lambda x : x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"], # amb blu brn gry grn hzl oth
    "hcl": lambda x : re.match("(#[0-9a-f]{6})", x) != None and len(x) == 7, 
    "pid": lambda x : re.match("(\d{9})", x) != None and len(x) == 9,
}

def makeDict(data:tuple):
    d = {}
    for i in data:
        key, value = i.strip().split(":")
        d[key] = value
    return d

def checkValid(d:dict):
    for i in cond.keys():
        if (i not in d) or (not cond[i](d[i])):
            return False
    return True

with open("data.txt", 'r') as file:
    data = file.read()


attributes = set(("byr","iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
datachunk = tuple(map(lambda x: tuple(re.split("\n| ", x.strip())), data.split("\n\n")))
d = tuple(map(makeDict, datachunk))
acc = len(tuple(filter(checkValid, d)))
print(acc)
            