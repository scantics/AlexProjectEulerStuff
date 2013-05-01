def factorize(number):
    factors = []
    n = 2
    upper = number/2 #upper bound on new factors

    while n < (upper):
        if number % n == 0:
            upper = number/n
            factors.append(n)
            if not n*n == number:
                factors.append(upper)
        n += 1
    return factors

def checkAbundant(number):
    if (number % 2 != 0) and (number % 3 != 0): return False
    factors = factorize(number)
    if (sum(factors) + 1) > number:
        return True
    else: return False


knownAb = [False]*20162
abArray = []
oddAb = []
        

def abSumSearch(n):
    if n % 2 == 1:
        for i in range(0,len(oddAb)):
            need = n-oddAb[i]
            if knownAb[need]: return True
        return False

    if n <= 48:
        for i in range(0, len(abArray)):
            need = n-abArray[i]
            if knownAb[need]: return True
        return False
    
    return True



total = 1+2+3+4+5+6+7+8+9+10+11

for n in range(12, 20162):
    
    if checkAbundant(n):
        knownAb[n] = True
        abArray.append(n)
        if n % 2 == 1:
            oddAb.append(n)

    if not abSumSearch(n):
        total += n

print(total)
    
    

