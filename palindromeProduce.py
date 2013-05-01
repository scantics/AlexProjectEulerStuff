#a Lychrel number will fail to generate a palindrome

def reverseAdd(x):
    strx = str(x)
    
    rev = 0
    for i in range(len(strx)):
        rev += int(strx[i])*(10**i)
        
    return x + rev

def checkPal(x):
    strx = str(x)
    for i in range(int(len(strx)/2)):
        if not strx[i] == strx[len(strx)-i-1]:
            return False
    return True

count = 0

for n in range(1,10000):
    
    for i in range(50):
        n = reverseAdd(n)
        if checkPal(n):
            break
    else:
        count += 1

print(count)
