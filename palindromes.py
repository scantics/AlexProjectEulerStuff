def checkPal(n):
    bn = bin(n)
    dn = str(n)
    for i in range(int(len(bn)/2)):
        if not bn[i+2] == bn[len(bn)-1-i]:
            return False

    for i in range(len(dn)):
        if not dn[i] == dn[len(dn)-1-i]:
            return False

    return True

total = 0

for n in range(1, 1000000, 2):
    if n % 10 == 0: continue
    if checkPal(n):
        total += n

print(total)
