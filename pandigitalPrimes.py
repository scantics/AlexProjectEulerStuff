pFlags = [1]*10000000

def nextPermInOrder(curr):

    for k in range(len(curr)-2,-1,-1):
        if curr[k] < curr[k+1]:
            for l in range(len(curr)-1,-1,-1):
                if curr[k] < curr[l]:
                    tmp = curr[k]
                    curr[k] = curr[l]
                    curr[l] = tmp
                    break
            break
    else: return curr

    toReverse = curr[k+1:len(curr)]
    j = len(toReverse)-1
    for i in range(k+1,len(curr)):
        curr[i] = toReverse[j]
        j += -1

    return curr

def makeInt(ls):
    strn = ''.join(ls)
    return int(strn)

def prepFlags(pFlags):
    for i in range(2,int(len(pFlags)/2)):
        if pFlags[i]:
            for mult in range(2*i,len(pFlags),i):
                pFlags[mult] = 0

prepFlags(pFlags)
maxPrime = 0



a = ['1','2','3','4','5','6','7']
maxA = 987654321
aInt = makeInt(a)
while aInt < maxA:
    a = nextPermInOrder(a)
    aInt = makeInt(a)
    if pFlags[aInt]:
        maxPrime = aInt
        print(maxPrime)
print(maxPrime)
