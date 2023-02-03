# AoC 2016 - Day 2

def get_input():
	return [l.strip() for l in open("day2.in", "r").readlines()]

def p1():
	def get_bathroom_code(code_input):
		keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
		x , y = 1, 1 # starting at middle position
		
		code_str = "" 
		for i in code_input:
			for move in i:
				if move == 'U':
					x = max(0, x - 1)
				elif move == 'D':
					x = min(2, x + 1)
				elif move == 'L':
					y = max(0, y-1)
				elif move == 'R':
					y = min(2, y + 1)
			
			# we are using max and min to make sure it stays in the keypad range
			
			code_str += keypad[x][y]
	
		return code_str

	return print(get_bathroom_code(get_input()))

def p2():
	def get_bathroom_code(code_input):
		keypad = [['0', '0', '1', '0', '0'],
             	 ['0', '2', '3', '4', '0'],
             	 ['5', '6', '7', '8', '9'],
             	 ['0', 'A', 'B', 'C', '0'],
             	 ['0', '0', 'D', '0', '0']]
		x , y = 2, 0 # starting at position "5"
		
		code_str = "" 
		for i in code_input:
			for move in i:
				if move == 'U':
					x = max(0, x-1)
					print(x) 
				elif move == 'D':
					x = min(4, x+1)
					print(x)
				elif move == 'L':
					y = max(0, y-1)
					print(y)
				elif move == 'R':
					y = min(4, y+1)
					print(y)
				if keypad[x][y] == '0':
					if move == 'U':
						x += 1 
					elif move == 'D':
						x -= 1
					elif move == 'L':
						y += 1
					elif move == 'R':
						y -= 1
			
			# we are using max and min to make sure it stays in the keypad range
			# we are doing min(4, something) because it has a max height of 4 and
			# it shouldn't exceed this height
			
			code_str += keypad[x][y]
	
		return code_str

	return print(get_bathroom_code(get_input()))

p1()
p2()
