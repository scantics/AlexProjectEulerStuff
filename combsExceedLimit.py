import combin

def numNcrExceed(n,limit,factSet):
    r = 0
    while(combin.ncr(n,r,factSet) < limit):
        r += 1
        if r == n: return 0
    return (n - 2*r + 1)

total = 0

factSet = combin.factLookup(100)

limit = int(input("Please enter limit: "))

for n in range(1,101):
    total += numNcrExceed(n,limit,factSet)
    print(n)

print(total)
