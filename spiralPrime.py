import prime

#36 35 34 33 32 31
#17 16 15 14 13 30
#18  5  4  3 12 29
#19  6  1  2 11 28
#20  7  8  9 10 27
#21 22 23 24 25 26


spCorner = 1    #current number being visited along spiral
cornerCount = 0 #how many corners have been traversed
primeCount  = 0 #how many primes ahve been traversed, for ratio
step = 2        #addition step increases every four corners


while((primeCount+1)/ float(cornerCount+1) > .1):
    for corner in range(4):
        spCorner += step
        if spCorner % 4000 <= 200:
            print(spCorner)
            print(primeCount/ float(cornerCount+1))
        if prime.isPrime(spCorner): primeCount += 1
    step += 2
    cornerCount += 4
    
   
    if primeCount / cornerCount < .1:
        print(str(cornerCount/2 + 1) + " at num="+str(spCorner))


print("Done")
print(primeCount / cornerCount)
