import math
solutions = [0]*1005
maxSol = 3
maxP = 120

for p in range(100,1001):
    if p == 300: print("Benchmark 1")
    if p == 700: print("Benchmark 2")
    for c in range(int(p/3),int(p/2)):
        for a in range(1,int(p/3)):
            b = math.sqrt(c**2 - a**2)
            if b == int(b):
                if a + b + c == p:
                    trip = (a,b,c)
                    solutions[p] += 1
    if solutions[p] > maxSol:
        maxSol = solutions[p]
        maxP   = p

print(maxP)
