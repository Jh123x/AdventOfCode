from math import prod

def parse_data(data:list):
    leaving_time = int(data[0])
    buses = []
    delay = []
    for index, value in enumerate(data[1].split(",")):
        if value == 'x':
            continue
        buses.append(int(value))
        delay.append(index)
    return leaving_time, buses, delay

def calc_waiting(time:int, bus:int):
    return (bus - time) % bus

def part1(leaving_time:int, buses:tuple):
    minimum = buses[0]
    waiting_time = calc_waiting(leaving_time, buses[0])
    for no in buses:
        wait = calc_waiting(leaving_time, no)
        if (wait < waiting_time):
            minimum = no
            waiting_time = wait
    return minimum * waiting_time


def check_cond(buses, delay, number):
    for d, bus in zip(delay, buses):
        result = calc_waiting(number, bus)
        if result != d:
            return False
    return True


def euclid_algo(number, mod):
    pass

def part2(buses, delay):

    #Start with 0
    target = 0

    #Accumulate the results
    n = 1

    #Iterate through all the bus and their delay
    for d, bus in zip(delay, buses):

        #Check if the current number fulfils the condition
        while (target + d) % bus != 0: 

            #Add n to target if it does not fulfill the condition
            target += n

        #Increase n by the bus number
        n *= bus

    return target

with open('data.txt') as file:
    data = tuple(map(lambda x: x.strip(), file.read().split("\n")))

leaving_time, buses, delay = parse_data(data)
print(part1(leaving_time, buses))
print(part2(buses, delay))
