def checkDay(day):
    if day % 7 == 0:
        return True
    return False


day = 2 #Tuesday

count = 0

for year in range(1901, 2001): #last year is 2000

    if checkDay(day): count+=1
    
    day += 31 #January
    if checkDay(day): count+=1

    if year % 4 == 0: #leap year
        day += 29     #February
    else: day += 28
    if checkDay(day): count+=1

    day += 31 #March
    if checkDay(day): count+=1

    day += 30 #April
    if checkDay(day): count+=1

    day += 31 #May
    if checkDay(day): count+=1

    day += 30 #June
    if checkDay(day): count+=1

    day += 31 #July
    if checkDay(day): count+=1

    day += 31 #August
    if checkDay(day): count+=1

    day += 30 #September
    if checkDay(day): count+=1

    day += 31 #October
    if checkDay(day): count+=1

    day += 30 #November
    if checkDay(day): count+=1

    day += 31 #December
    #not counting until next year because otherwise jan1, 2001 counted

print count








    
