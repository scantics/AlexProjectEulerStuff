import prime

N = 4

def nextPermInOrder(curr):

    for k in range(N-2,-1,-1):
        if curr[k] < curr[k+1]:
            break

    for l in range(N-1,-1,-1):
        if curr[k] < curr[l]:
            tmp = curr[k]
            curr[k] = curr[l]
            curr[l] = tmp
            break

    toReverse = curr[k+1:N]
    j = len(toReverse)-1
    for i in range(k+1,N):
        curr[i] = toReverse[j]
        j += -1

    return curr

def perms(n):
    lsn = list(str(n))
    perms = []
    for i in range(24):
        lsn = nextPermInOrder(lsn)
        nextn = int(''.join(lsn))
        if not nextn in perms:
            perms.append(nextn)
    return perms

primes = []

pFlags = prime.sieveAndSet(10000,primes)

for n in primes:
    if n < 1000 or n >= 10000:
        continue
    diff = 0
    perm = perms(n)
    if n == 1487: print(perm)
    if n in perm:
        perm.remove(n)
    for higher in perm:
        diff = higher - n
        if higher + diff in perm:
            if pFlags[higher] and pFlags[higher+diff]:
                tup = n, higher, higher+diff
                print(tup)
