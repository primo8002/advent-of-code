# AoC 2015 - Day 4

import hashlib

def p1():
    secret_key = "yzbqklnj"
    number = 1

    while True:
        input_string = secret_key + str(number)
        thehash = hashlib.md5(input_string.encode()).hexdigest()
    
        if thehash.startswith("00000"):
            print(number)
            break
    
        number += 1

def p2():
    secret_key = "yzbqklnj"
    number = 1

    while True:
        input_string = secret_key + str(number)
        thehash = hashlib.md5(input_string.encode()).hexdigest()
    
        if thehash.startswith("000000"):
            print(number)
            break
    
        number += 1

p1()
p2()
