#Project Euler 13

import numpy

f = open('50digits.txt', 'r')

numbers = []

result = []

strTotal = []

carry = [0]*52

for i in range(100):
    numbers.append(list(f.readline()))

for x in range(49,-1,-1):
    total = 0
    
    for y in range(100):
        total += int(numbers[y][x])
        
    total += carry[x+2]

    strTotal = str(total)
    
    result.insert(0, strTotal[len(strTotal)-1])
    
    for c in range(0, len(strTotal)-1):
        carry[x+c] += int(strTotal[c])
        if carry[x+c] > 9:
            car = list(str(carry[x+c]))
            carry[x-1+c] += int(car[0])
            carry[x+c]    = int(car[1])

print carry

for c in range(len(strTotal)-2, -1, -1):
    result.insert(0, strTotal[c])

print result
        
