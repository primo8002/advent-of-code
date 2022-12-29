# AoC 2015 - Day 2

def get_input():
    return open("day2.in", "r").readlines()

def p1():
    sqft = 0

    for line in get_input():
        line = line.strip()
        # print(line)

        length, width, height = line.split("x")
        length, width, height = int(length), int(width), int(height)
        surface_area = (2*length*width) + (2*width*height) + (2*height*length)
        extra = min(length*width, width*height, height*length)
        sqft += surface_area + extra
    
    print(sqft)
        
def p2():
    ribbon_ft = 0

    for line in get_input():
        line = line.strip()

        length, width, height = line.split("x")
        length, width, height = int(length), int(width), int(height)
        ribbon = 2 * min(length + width, width + height, height + length)
        # Finding perimeter, which is twice the smallest
        bow = length * width * height
        # The bow is the cubic feet of volume of the present
        ribbon_ft += ribbon + bow

    print(ribbon_ft)

p1()        
p2()

