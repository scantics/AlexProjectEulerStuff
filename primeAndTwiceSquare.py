import prime
import math

pFlags = prime.sieve(10000000)

for comp in range(1,10000000,2):
    if pFlags[comp]: continue
    noSum = True
    for d in range(1,int(math.sqrt(comp/2))+1):
        dSquare = (d*d)*2
        if pFlags[comp-dSquare]:
            noSum = False
            break
    if noSum: print(comp)
