file = open('names.txt')

names = file.read().split('","')
names = sorted(names)

total = 0

for i in range(0,len(names)):
    name = names[i]
    score = 0
    for letter in name:
        score += ord(letter)-64
    score = score*(i+1)
    total += score

print(total)
