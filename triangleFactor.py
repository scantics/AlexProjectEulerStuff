import bisect

def triangle(n):
    return (n*n + n) / 2


def factorize(currTri):
    factors = []
    n = 2
    upper = currTri/2 #upper bound on new factors

    while n < (upper):
        if currTri % n == 0:
            upper = currTri/n
            factors.append(n)
            factors.append(upper)
        n += 1
    return factors

for n in range(10000, 100000):
    currTri = triangle(n)
    if len(factorize(currTri)) >= 500:
        print currTri
