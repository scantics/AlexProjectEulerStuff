primes = [2,3,5,7,11,13]
bigUp = 0

def primeCheck(x, prep=True):
    if prep:
        if x > primes[len(primes)-1]: prepPrimes(int(x))
        
    for i in range(0,len(primes)):
        if x % primes[i] == 0:
            if x == primes[i]:
                return True
            else: return False
        if primes[i] > abs(x):
            return True
    primes.append(x)
    return True

def prepPrimes(up):
    for i in range(primes[len(primes)-1],up):
        primeCheck(i, False)
    bigUp = up
		
		

dopeSet = (0, 0, 0)
prepPrimes(1000)

print(primes)

for i in range(0,len(primes)):
    b = primes[i]
    print(b)
    if b > 1000: break
    
    for a in range(-999,1000, 2):
        n = 0
        if b == 41 & a == 1: print("hi")
        while primeCheck(n*n + a*n + b):
            if n > dopeSet[2]:
                dopeSet = (a, b, n)
                print(dopeSet)
            n += 1

    b = 0-b
    for a in range(-999,1000, 2):
        n = 0
        while primeCheck(n*n + a*n + b):
            if n > dopeSet[2]:
                dopeSet = (a, b, n)
                print(dopeSet)
            n += 1

print(dopeSet)




















