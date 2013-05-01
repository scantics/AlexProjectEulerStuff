def binomialCoeff(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
    return result

def rsimplex(r, n):
    result = 1

    if r == 0: return result
    
    result = binomialCoeff(n+r-1,r)

    return result


#number of paths that may turn starting on rth from bottom row
totalpaths = rsimplex(20, 21)

print totalpaths
