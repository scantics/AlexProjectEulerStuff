def xToTheX(x):
    result = 1
    for n in range(x):
        result = x*result
    return result

total = 0

for x in range(1000):
    total += xToTheX(x+1)

print(total)
