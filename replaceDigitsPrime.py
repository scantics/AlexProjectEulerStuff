import prime

primes = []
pFlags = prime.sieveAndSet(1000000, primes)

def replaceOneDigit(stn, i, rep):
    lsn = list(stn)
    lsn[i] = str(rep)
    return int(''.join(lsn))

def replaceTwoDigits(stn, i, j, rep):
    lsn = list(stn)
    lsn[i] = str(rep)
    lsn[j] = str(rep)
    return int(''.join(lsn))

def replaceThreeDigits(stn, i, j, k, rep):
    lsn = list(stn)
    lsn[i] = str(rep)
    lsn[j] = str(rep)
    lsn[k] = str(rep)
    return int(''.join(lsn))

def replaceFourDigits(stn, i, j, k, l, rep):
    lsn = list(stn)
    lsn[i] = str(rep)
    lsn[j] = str(rep)
    lsn[k] = str(rep)
    lsn[l] = str(rep)
    return int(''.join(lsn))

def countRepPrimesOne(stp,i):
    count = 0
    for rep in range(10):
        modP = replaceOneDigit(stp,i,rep)
        if len(str(modP)) < len(stp): continue
        if pFlags[modP]:
            count += 1
    return count

def countRepPrimesTwo(stp, i, j):
    count = 0
    for rep in range(10):
        modP = replaceTwoDigits(stp,i,j,rep)
        if len(str(modP)) < len(stp): continue
        if pFlags[modP]:
            count += 1
    return count

def countRepPrimesThree(stp, i, j, k):
    count = 0
    for rep in range(10):
        modP = replaceThreeDigits(stp,i,j,k,rep)
        if len(str(modP)) < len(stp): continue
        if pFlags[modP]:
            count += 1
    return count

def countRepPrimesFour(stp, i, j, k, l):
    count = 0
    for rep in range(10):
        modP = replaceFourDigits(stp,i,j,k,l,rep)
        if len(str(modP)) < len(stp): continue
        if pFlags[modP]:
            count += 1
    return count

for p in primes:
    if p <= 10000: continue
    stp = str(p)
    for i in range(len(stp)-3):
        if countRepPrimesOne(stp,i) >= 8:
            print(stp+": "+i)
        for j in range(i+1, len(stp)-2):
            if countRepPrimesTwo(stp,i,j) >= 8:
                print(stp+": "+str(i)+", "+str(j))
            for k in range(j+1, len(stp)-1):
                if countRepPrimesThree(stp,i,j,k) >= 8:
                    print(stp+": "+str(i)+", "+str(j)+", "+str(k))
                for l in range(k+1, len(stp)):
                    if countRepPrimesFour(stp,i,j,k,l) >= 8:
                        print(stp+": "+str(i)+", "+str(j)+", "+str(k)+", "+str(l))
