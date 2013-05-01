MAXDIGS  = 10000
MAXCYCLE = 1000

topCycle = 0
topDenom = 2

def dropTheZero(x):
    x = x*10
    return x

def findCycle(digs):

    final = 0

    for i in range(5):
        if not digs[i] == 0:
            start = i
            break
    
    for length in range(1, MAXCYCLE):
        noFail = True

        #find beginning of potential cycle
        for i in range(start, start+10):
            if digs[i] == digs[i+length]:
                start = i
                break
            

        #check for three repeats
        for i in range(start, start+length*2):
            if not digs[i] == digs[i+length]:
                noFail = False
                break
        
        if noFail: return length
    return 0
    
for denom in range(2, 1000):
    qdigs  = [0] #digits of quotient

    rdr = 1 #remainder
    for i in range(MAXDIGS):

        
        product = qdigs[i]*denom
        rdr     = rdr-product
        if rdr == 0: break
        
        rdr     = dropTheZero(rdr)
        qdigs.append(int(rdr/denom))

        if i == MAXDIGS-1:
            cand = findCycle(qdigs)
            if cand == 0: print("Too long: " + str(denom))
            #print(str(denom)+": "+str(cand))
            if cand > topCycle:
                topCycle = cand
                topDenom = denom


print(topDenom)
print(topCycle)
