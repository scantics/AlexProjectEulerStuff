UPPER_LIMIT = 354294

def digitsToTheFifth(n):
    result = 0
    for dig in str(n):
        result += int(dig)**5
    return result


total = 0
for n in range(10, UPPER_LIMIT):
    if n == digitsToTheFifth(n):
        print(n)
        total += n

print(total)
