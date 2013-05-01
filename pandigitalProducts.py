
def checkFacts(a,b):
    digits = [0]*9
    
    p = a*b
    expr = str(a)+str(b)+str(p)
    if not len(expr) == 9:
        return False

    for d in expr:
        if int(d) == 0: return False
        digits[int(d)-1] += 1
        
    if digits == [1,1,1,1,1,1,1,1,1]:
        return True
    
    return False

panProducts = []

def search(x):
    for i in range(len(panProducts)):
        if x == panProducts[i]:
            return False, 0
        if x < panProducts[i]:
            return True, i
    return True, len(panProducts)
    

for i in range(123,5000):   
    for j in range(2,int(10000/i)):
        if checkFacts(i,j):
            print("Made it to 1")
            panProduct = i*j
            sr = search(panProduct)
            if sr[0]:
                panProducts.insert(sr[1],panProduct)

print(sum(panProducts))
