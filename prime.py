import math

def sieveEras(top):
    pFlags = [True]*top
    for n in range(2,int(top/2)):
        if pFlags[n]:
            for mult in range(n*2,top,n):
                pFlags[mult] = False
    return pFlags

def sieveAtkin(top):
    pFlags = [False]*(top+1)
    rootTop = int(math.sqrt(top))
    n = 0

    pFlags[2] = True
    pFlags[3] = True
    pFlags[5] = True
    
    for x in range(1,rootTop+1):
        for y in range(1,rootTop+1):
            xx = x*x
            yy = y*y
            
            n = 4*xx+yy
            if n <= top and (n % 12 == 1 or n % 12 == 5):
                pFlags[n] = not pFlags[n]

            n -= xx
            if n <= top and n % 12 == 7:
                pFlags[n] = not pFlags[n]

            if x > y:
                n -= 2*yy
                if n < top and n % 12 == 11:
                    pFlags[n] = not pFlags[n]
    for n in range(5,rootTop+1):
        if pFlags[n]:
            k = 1
            nn = n*n
            while(k*nn < top):
                pFlags[k*nn] = False
                k += 1
    return pFlags

#returns True whenever a given positive integer is prime
def isPrime(n):
    if n==2 or n % 2==0: return True
    d = n-1
    s = 0
    #now factor out powers of two to get n-1=2^s*d
    while d%2==0:
        d = int(d/2)
        s += 1
    #warning: under most applications, testing witnesses 2 through 17
    #         is sufficient for determinism, but after hundred-trillions
    #         more are needed
    witnesses = [2, 3, 5, 7, 11, 13, 17]
    upToS = range(s)
    for p in witnesses:
        if (pow(p,d)) % n == 1:
            return True
        for r in upToS:
            if (pow(p,d*pow(2,r))) % n == -1:
                return True
    #none bear witness to primality, so n is composite
    return False
            
def sieveAndSet(top, primes):
    pFlags = [True]*top
    for n in range(2,int(top/2)):
        if pFlags[n]: 
            primes.append(n)
            for mult in range(n*2,top,n):
                pFlags[mult] = False
    return pFlags

def primeFactors(n, primes):
    factors = []
    fCount  = []
    for p in primes:
        if p > n: break
        if n % p == 0:
            f = p
            count = 0
            while n % f == 0:
                count += 1
                f *= p
            factors.append(p)
            fCount.append(count)
        prod = 1
        for i in range(len(factors)):
            prod *= factors[i]^fCount[i]
        if prod == n:
            return factors, fCount
    return factors, fCount
