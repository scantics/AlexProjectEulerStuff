import math

def checkPent(tryPent):
    n = (math.sqrt(24*tryPent+1)+1)/6
    if n - int(n) == 0:
        return True, n
    else: return False, n

def checkHex(tryHex):
    n = (math.sqrt(8*tryHex+1)+1)/4
    if n - int(n) == 0:
        return True, n
    else: return False, n



for n in range(286,1000000):
    tryTri = n*(n+1)/2
    if checkPent(tryTri)[0]:
        if checkHex(tryTri)[0]:
            print(n)
            print(tryTri)
            break
