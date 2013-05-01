total = 0
big = 1

for n in range(1,1000):
    big = big*2
    print big

for digit in str(big):
    total += int(digit)

print total
