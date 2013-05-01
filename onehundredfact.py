fact = 1
total = 0

for n in range(1, 100):
    fact = fact*n

for digit in str(fact):
    total += int(digit)

print total
