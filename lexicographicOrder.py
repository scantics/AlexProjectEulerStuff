N = 10
NUMBER = 1000000

def nextPermInOrder(curr):

    for k in range(N-2,-1,-1):
        if curr[k] < curr[k+1]:
            break

    for l in range(N-1,-1,-1):
        if curr[k] < curr[l]:
            tmp = curr[k]
            curr[k] = curr[l]
            curr[l] = tmp
            break

    toReverse = curr[k+1:N]
    j = len(toReverse)-1
    for i in range(k+1,N):
        curr[i] = toReverse[j]
        j += -1

    return curr

a = list(range(N))

for count in range(NUMBER-1):
    a = nextPermInOrder(a)

print(a)
