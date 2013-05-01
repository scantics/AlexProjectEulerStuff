pFlags = [1]*1000000

pFlags[0] = 0
pFlags[1] = 0

def prepFlags(pFlags):
    for i in range(2,int(len(pFlags)/2)):
        if pFlags[i]:
            for mult in range(i+i,len(pFlags),i):
                pFlags[mult] = 0

def truncations(n):
    sn = str(n)
    truncs = []
    for i in range(1,len(sn)):
        truncs.append(int(sn[i:]))
        truncs.append(int(sn[:i]))

    return truncs

prepFlags(pFlags)
total = 0
tPrimes = []

for n in range(8,len(pFlags)):
    if pFlags[n]:
        for t in truncations(n):
            if not pFlags[t]:
                break
        else:
            total += n
            tPrimes.append(n)

print(total)
print(tPrimes)

