import prime

primes = []
pFlags = prime.sieveAndSet(1000000,primes)

longSum = (0,0)

for bottom in range(len(primes)):
    total = 0
    for top in range(bottom,len(primes)):
        total += primes[top]
        if total > 1000000: break
        
        if pFlags[total]:
            if top-bottom > longSum[0]:
                longSum = (top-bottom,total)
                print(longSum)
           
print(longSum)
