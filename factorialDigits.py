def fact(x):
    result = 1
    for i in range(1,x+1):
        result = result*i
    return result

def sumFact(n):
    result = 0
    for dig in str(n):
        result += fact(int(dig))
    return result

total = 0

for n in range(2540160):
    if n == sumFact(n):
        print(n)
        total += n

print(total)
