total = 1
add = 1

for skip in range(2, 1001, 2):
    for corner in range(4):
        add += skip
        total += add
    skip += 2

print(total)
