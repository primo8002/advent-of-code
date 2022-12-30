# AoC 2015 - Day 3 version 2

def get_input():
    return str(open("day3.in", "r").readlines())

def p1():
    x, y = (0, 0)
    visited = {(x, y)}
    
    for direction in get_input():
        if direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1
        elif direction == '>':
            x += 1
        elif direction == '<':
            x -= 1
        visited.add((x, y))

    print(len(visited))

def p2():
    x, y = 0, 0
    visited = {(x, y)}
    robo_x, robo_y = 0, 0
    
    for i, direction in enumerate(get_input()):
        tx = x if i % 2 == 0 else robo_x
        ty = y if i % 2 == 0 else robo_y 

        if direction == '^':
            ty += 1
        elif direction == 'v':
            ty -= 1
        elif direction == '>':
            tx += 1
        elif direction == '<':
            tx -= 1
        
        if i % 2 == 0: 
            x, y = tx, ty
        else: 
            robo_x, robo_y = tx, ty

        visited.add((tx, ty))

    print(len(visited))

p1()
p2()

