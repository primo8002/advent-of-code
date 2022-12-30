# AoC 2015 - Day 3

def get_input():
	return open("day3.in", "r").readlines()

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

def p1():
	santaX, santaY = 0, 0 # santa x,y coordinate location
	houses = {} # dictionary for houses

	house_tracker(santaX, santaY, houses)
	for move in str(get_input()):
		santaX, santaY = calc_move(santaX, santaY, move)
		house_tracker(santaX, santaY, houses)

	print(len(houses))

def p2():
	santaX, santaY = 0, 0
	robosantaX, robosantaY = 0, 0
	houses = {}
	house_tracker(santaX, santaY, houses)
	moveSanta = True # decides whether Santa moves or Robo-Santa, starts with Santa
	for move in str(get_input()):
		if moveSanta == True:
			santaX, santaY = calc_move(santaX, santaY, move)
			house_tracker(santaX, santaY, houses)
			moveSanta = False
			# because now it is Robo-Santa's turn, it will change it 
			# to false then run his thing 
			# and then change it back to true and repeat
		elif moveSanta == False:
			robosantaX, robosantaY = calc_move(robosantaX, robosantaY, move)
			house_tracker(robosantaX, robosantaY, houses)
			moveSanta = True

	print(len(houses))

p1()
p2()
