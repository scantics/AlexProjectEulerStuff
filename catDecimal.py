
needDig = 1
pos = 0
digs = []

for n in range(1,300000):
    sn = str(n)
    pos += len(sn)
    if pos >= needDig:
        digs.append(sn[len(sn)-1-(pos-needDig)])
        needDig = needDig*10
        if needDig > 1000000: break

print(digs)
        
