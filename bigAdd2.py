f = open('50digits.txt', 'r')

big = long(0)

for i in range(100):
    big += long(f.readline())

print big
