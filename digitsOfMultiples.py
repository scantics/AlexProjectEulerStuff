def digitCount(n):
    digCounts = [0,0,0,0,0,0,0,0,0,0]
    lsn = list(str(n))
    for dig in lsn:
        digCounts[int(dig)] += 1
    return digCounts

def cmpDigitsOfMults(n):
    nCount = digitCount(n)
    if nCount == digitCount(2*n):
        if nCount == digitCount(3*n):
            if nCount == digitCount(4*n):
                if nCount == digitCount(5*n):
                    if nCount == digitCount(6*n):
                        return True
    return False

x = 1
while not cmpDigitsOfMults(x):
    x += 1

print(x)
