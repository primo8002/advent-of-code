# day3.py

def get_input():
	return str(open("day3.in", "r").readlines())

def p1():
    def house_tracker(x, y, houses):
        houses[(x, y)] = 1

    def calc_move(x, y, move):
        if move == '^':
            y += 1
        # north
        elif move == 'v':
            y -= 1
        # south
        elif move == '>':
            x += 1
        # east
        elif move == '<':
            x -= 1
        # west
        return (x, y)

    santaX = 0
    # santa x coordinate location
    santaY = 0
    # santa y coordinate location
    houses = {}
    # dictionary for houses
    house_tracker(santaX, santaY, houses)
    for i in get_input():
        santaX, santaY = calc_move(santaX, santaY, i)
        house_tracker(santaX, santaY, houses)
    print(len(houses))
    # prints the amount of houses that recieved at least 1 present

def p2():
    def house_tracker(x, y, houses):
        houses[(x, y)] = 1
    def calc_move(x, y, move):
        if move == '^':
            y += 1
        # north
        elif move == 'v':
            y -= 1
        # south
        elif move == '>':
            x += 1
        # east
        elif move == '<':
            x -= 1
        # west
        return (x, y)

    santaX = 0
    # santa x coordinate location
    santaY = 0
    # santa y coordinate location
    robosantaX = 0
    # robosanta x coordinate location
    robosantaY = 0
    # robosanta y coordinate location
    houses = {}
    # dictionary for houses
    house_tracker(santaX, santaY, houses)
    moveSanta = True
    # decides whether Santa moves or Robo-Santa, starts with Santa
    for i in get_input():
        if moveSanta == True:
            santaX, santaY = calc_move(santaX, santaY, i)
            house_tracker(santaX, santaY, houses)
            moveSanta = False
            # because now it is Robo-Santa's turn, it will change it 
			# to false then run his thing 
            # and then change it back to true and repeat
        elif moveSanta == False:
            robosantaX, robosantaY = calc_move(robosantaX, robosantaY, i)
            house_tracker(robosantaX, robosantaY, houses)
            moveSanta = True
    print(len(houses))
p1()
p2()
