def xToTheX(x):
    result = x
    while x > 1:
        result = result*result
        x = x - int(x/2)
    result = result**x
    return result

total = 0

for x in range(1000):
    total += xToTheX(x+1)

print(total)
