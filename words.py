def sumLetters(word):
    total = 0
    for char in word:
        total += ord(char) - 64
    return total

f = open("words.txt")
words = f.read()

words = words.split("   ")

count = 0

for word in words:
    tryTri = sumLetters(word)
    n = 1
    while tryTri > 0:
        tryTri += -n
        n += 1
    if tryTri == 0:
        count += 1

print(count)
