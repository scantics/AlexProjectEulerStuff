sequence = []

#returns false if no need to insert
def search(x):
    for i in range(len(sequence)):
        if x == sequence[i]:
            return False, 0
        if x < sequence[i]:
            return True, i
    return True, len(sequence)

for a in range(2,101):
    for b in range(2,101):
        n  = a**b
        sr = search(n)
        if sr[0]:
            sequence.insert(sr[1],n)

print(len(sequence))
            
