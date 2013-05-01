def fact(n):
    if abs(n) <= 1: return 1
    product = 1
    for i in range(2,abs(n)+1):
        product *= i
    if n < 0: return (0 - product)
    return product

def factLookup(top):
    factSet = [1]*(top+1)
    product = 1
    for i in range(1,top+1):
        product *= i
        factSet[i] = product
    return factSet

def ncr(n,r):
    if n < r: return 0
    return fact(n)/(fact(r)*fact(n-r))

def ncr(n,r,factSet):
    if n < r: return 0
    return factSet[n] / (factSet[r] * factSet[n-r])
