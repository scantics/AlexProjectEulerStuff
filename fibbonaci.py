
prev = 0
n = 1
count = 1

while len(str(n)) < 1000:
    tmp = n
    n += prev
    prev = tmp
    count += 1
    if n < 200:
        print(str(count) + ": " + str(n))

print(count)
