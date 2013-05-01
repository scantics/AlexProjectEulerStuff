import prime

def fourDistinct(ls):
    if len(ls) == 4:
        return True
    else: return False

primes = []
pFlags = prime.sieveAndSet(10000,primes)

consec = 0

for n in range(1000000):
    factors = prime.primeFactors(n,primes)[0]
    if fourDistinct(factors):
        consec += 1
    else:
        consec = 0

    if consec == 4:
        print(n-3)
