
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
    stn = ''
    for char in ls:
        stn = stn+char
    return int(stn)

primes = [2, 3, 5, 7, 11, 13, 17]

def checkSubStrDiv(ls):
    for d in range(1,8):
        if makeInt(ls[d:d+3]) % primes[d-1] != 0:
            return False
    else: return True
    

total = 0
a = ['0','1','2','3','4','5','6','7','8','9']
maxA = 9876543210
aInt = makeInt(a)
while aInt < maxA:
    a = nextPermInOrder(a)
    aInt = makeInt(a)
    if checkSubStrDiv(a):
        total += aInt
        print(aInt)
print(total)
