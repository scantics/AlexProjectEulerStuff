import bitstring

def clearRight(i, x):
    if i == (len(x)-1): return x
    for s in range(i+1,len(x)):
        x[s] = 0
    return x

def addOne(i, x):
    if x[i] == '0': x[i] = '1'
    if x[i] == '1':
        x[i] = '0'
        if i == 0:
            x.insert(0,'1')
        else: addOne(i-1,x)
    return x

#rules out 111 and 000
def checkTriple(x):
    if len(x) < 3: return x
    
    for i in range(len(x)-2):
        if x[i]==x[i+1] and x[i]==x[i+2]:
            x = addOne(i+2,x)
            x = clearRight(i+2,x)
            #print x
            x = checkTriple(x)
            return x
    return x

#rules out 00100 and 11011
def checkFatSandwich(x):
    if len(x) < 5: return x
    
    for i in range(len(x)-4):
        if  (x[i] == x[i+1] and not(x[i] == x[i+2])
        and  x[i] == x[i+3]     and x[i] == x[i+4]):
               x = addOne(i+4,x)
               x = clearRight(1+4,x)
               x = checkFatSandwich(x)
               return x
    return x

x = [0]
count = 0
fuck = False

while not fuck:
    addOne(x, len(x))
    temp = bin(x)
    #fucking hate windows for being the one with games and chrome
    strx = 
    print(strx)
    strx = checkTriple(strx)
    strx = checkFatSandwich(strx)
    x = int(str(strx), 2)
    print(x)
    count += 1
    if x > 5000: fuck = True












    
    













