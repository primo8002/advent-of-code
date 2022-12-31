# AoC 2015 - Day 5

def get_input():
	return open("day5.in", "r").readlines()

def p1():
	def is_nice(string):
		num_vowels = 0
		test1 = False
		test2 = False
		test3 = False
		for character in string:
			if character in "aeiou":
				num_vowels += 1
		if num_vowels >= 3:
			test1 = True
		else:
			return False
	
		if test1 == True:
			for i in range(len(string) - 1):
				if string[i] == string[i + 1]:
					test2 = True
			if test2 == False:
				return False
		if test2 == True:
			if "ab" in string or "cd" in string or "pq" in string or "xy" in string:
				return False
			else:
				test3 = True
		if test3 == True:
			return True
		
	nice_count = 0
	for line in get_input():
		if is_nice(line):
			nice_count += 1
	print(nice_count)
# p1()

def p2():
	def is_nice(s):
		pair = False
		letter_repeat = False
		for i in range(len(s) - 2):
			if s[i : i + 2] in s[i + 2:]:
				pair = True
				
			if s[i] == s[i + 2]:
				letter_repeat = True
				
			if pair == True and letter_repeat == True:
				return True
				break
	
	nice_count = 0
	for line in get_input():
		line = line.strip()
		if is_nice(line) == True:
			nice_count += 1

	print(nice_count)

p1()
p2()
