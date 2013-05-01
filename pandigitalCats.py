
def findPandigital(n):
    digs = [0]*9
    cat = str(n)
    mult = 2
    while(len(cat) < 9):
        cat  += str(n*mult)
        mult += 1
    for c in cat:
        digs[int(c)-1] += 1
    if digs == [1]*9:
        return int(cat)
    else: return 0


maxPan = 123456789

for n in range(90,100):
    cand = findPandigital(n)
    if cand > maxPan: maxPan = cand
    
for n in range(9000,10000):
    cand = findPandigital(n)
    if cand > maxPan: maxPan = cand

print(maxPan)
