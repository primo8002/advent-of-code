# AoC 2016 - Day 1

def get_input():
	return [l.strip() for l in open("day1.in", 'r').readlines()]

def manhattan_distance(x, y):
	return abs(x) + abs(y)

def p1():
	x = 0
	y = 0
	directions = ["N", "E", "S", "W"] # list of directions
	direction_index = 0 
	for line in get_input():
		for move in line.split(", "):
			turn, distance = move[0], int(move[1:])
			if turn == "R":
				direction_index = (direction_index + 1) % 4 # turns right, we are doing % 4 so it stays in the list range
			elif turn == "L":
				direction_index = (direction_index - 1) % 4 # turns left, same modulo rule as before
		
			if directions[direction_index] == "N":
				y += distance
			elif directions[direction_index] == "E":
				x += distance
			elif directions[direction_index] == "S":
				y -= distance
			elif directions[direction_index] == "W":
				x -= distance
	
	distance = manhattan_distance(x, y)
	print(distance)

def p2():
	directions = ['N', 'E', 'S', 'W'] # list of directions
	direction_index = 0

	x, y = 0, 0
	visited = set((x,y)) # keeps track of the visited places 

	for line in get_input():
		for move in line.split(", "):
			turn, distance = move[0], int(move[1:])
			# print(turn, distance)

			if turn == "R":
				# turns right, we are doing % 4 so it stays in the list range
				direction_index = (direction_index + 1) % 4 
			elif turn == "L":
				# turns left, same modulo rule as before
				direction_index = (direction_index - 1) % 4 
		
			if directions[direction_index] == "N":
				for i in range(distance):
					y += 1
					if (x, y) in visited:
						return manhattan_distance(x, y)
					else:
						visited.add((x, y))
			elif directions[direction_index] == "E":
				for i in range(distance):
					x += 1
					if (x, y) in visited:
						return manhattan_distance(x, y)
					else:
						visited.add((x, y))
			elif directions[direction_index] == "S":
				for i in range(distance):
					y -= 1
					if (x, y) in visited:
						return manhattan_distance(x, y)
					else:
						visited.add((x, y))
			elif directions[direction_index] == "W":
				for i in range(distance):
					x -= 1
					if (x, y) in visited:
						return manhattan_distance(x, y)
					else:
						visited.add((x, y))
p1()
print(p2())
