
zero  = 0
one   = 3
two   = 3
three = 5
four  = 4
five  = 4
six   = 3
seven = 5
eight = 5
nine  = 4

ones = { 0:zero, 1:one, 2:two, 3:three, 4:four, 5:five,
         6:six, 7:seven, 8:eight, 9:nine }


fourteen  = 5
sixteen   = 4
seventeen = 6
nineteen  = 5

teens = { 0:zero, 1:one, 2:two, 3:three, 4:fourteen, 5:five,
          6:sixteen, 7:seventeen, 8:eight, 9:nineteen}


ten     = 3
twenty  = 6
thirty  = 6
forty   = 5
fifty   = 5
sixty   = 5
seventy = 7
eighty  = 6
ninety  = 6

tens = { 0:zero, 1:ten, 2:twenty, 3:thirty, 4:forty, 5:fifty, 6:sixty,
         7:seventy, 8:eighty, 9:ninety }

hundred = 7
aand    = 3

count = one + two + three + four + five + six + seven + eight + nine



for n in range(10, 100):
    te = int(n/10)
    on = n%10

    count += tens[te]
    
    if te == 1: count += teens[on]
    else:       count += ones[on]
    

for n in range(100, 1000):
    if not n%100 == 0:
         count += aand

    hund = int(n/100)
    te   = int(n/10)%10
    on   = n%10

    count += hundred
    count += ones[hund]

    count += tens[te]
    
    if te == 1: count += teens[on]
    else:       count += ones[on]

oneThousand = 11
count += oneThousand

print(count)
