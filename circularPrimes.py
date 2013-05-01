import bisect

pFlags = [1]*1000000
primes = [2,3,5,7,11,13,17]
bigUp  = 17

def primeCheck(x, prep=False):
    if not prep:
        if x > bigUp:
            prepPrimes(x)
    for i in range(0,len(primes)):
        if x % primes[i] == 0:
            if x == primes[i]:
                return True
            else: return False
        if primes[i] > x:
            return True
    primes.append(x)
    return True

def prepPrimes(up):
    for i in primes:
        if primeCheck(i, True): pFlags[i] = 1
    bigUp = up

def prepFlags(pFlags):
    for i in range(2,int(len(pFlags)/2)):
        if pFlags[i]:
            for mult in range(i+i,len(pFlags),i):
                pFlags[mult] = 0



def rotations(n):
    rot = []
    lsn = [d for d in str(n)]
    for i in range(len(lsn)-1):
        tmp = lsn.pop(0)
        lsn.append(tmp)
        stn = ''.join(lsn)
        rot.append(int(stn))
    return rot
        

circPrimes = []
prepFlags(pFlags)

print("Starting circs")

for n in range(2,len(pFlags)):
    if pFlags[n]:
        if n in circPrimes:
            continue
        rot = rotations(n)
        for c in rot:
            if not pFlags[c]:
                break
        else:
            bisect.insort(circPrimes, n)
            for c in rot:
                bisect.insort(circPrimes, c)
        
    if n == 100000: print(n)
            
print(len(circPrimes))
print(circPrimes)
        




    
