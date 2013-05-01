import sys
import math

def checkPent(tryPent, second=False):
    n = (math.sqrt(24*tryPent+1)+1)/6
    if n - int(n) == 0:
        return True, n
    else: return False, n

##def checkAddToPent(lowP, lowI, highP, highI):
##    step = 0
##    total = 0
##    while total < lowP:
##        total += 1+3*(highI+step)
##        step += 1
##    if total == lowP:
##        return True, step
##    if step == 1: return False, -1
##    return False, 0



maxLowI =  100000000
minD = sys.maxsize


for highI in range(1,10000000):
    highP = highI*(3*highI-1)/2
    
    for lowI in range(1,highI):
        lowP = lowI*(3*lowI-1)/2
        

        if lowI > maxLowI: continue
        tup = checkPent(highP - lowP)
        if tup[0]:

            tupe = checkPent(highP + lowP)
            if tupe[0]:
                if highP-lowP < minD:
                    minD = highP-lowP
                    print(highP-lowP)
                    print(tup[1])
                    print(tupe[1])
                    print("J: "+str(lowI)+" K: "+str(highI))
                    break
            
print(minD)
