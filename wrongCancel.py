
def checkCancel(numer, denom):
    if numer == denom:
        return False
    goal = numer/denom
    strn = str(numer)
    strd = str(denom)
    
    if int(strd[1]) == 0: return False
    
    if strd[0] == strn[1]:
        if int(strn[0])/int(strd[1]) == goal:
            return True



fractions = []

for denom in range(11,100):
    for numer in range(10,denom):
        if checkCancel(numer,denom):
            tup = (numer,denom)
            fractions.append(tup)

print(fractions)
