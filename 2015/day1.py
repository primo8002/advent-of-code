# AoC 2015 - Day 1

def get_input():
    return open("day1.in", "r").readlines()

def p1():
    floor = 0

    for line in get_input():
        line = line.strip()

        for c in line:
            if str(c) == "(":
                floor += 1
            elif str(c) == ")":
                floor -= 1

    print(floor)

def p2():
    floor = 0
    position = 1

    for line in get_input():
        line = line.strip()

        for c in line:
            if str(c) == "(":
                floor += 1
            elif str(c) == ")":
                floor -= 1
                
            if floor == -1:
                break

            position += 1

    print(position)

p1()
p2()

