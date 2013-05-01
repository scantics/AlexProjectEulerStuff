count = 0

for pd in range(0,3): #number of pounds
    for ft in range(0,int((200-100*pd)/50)+1): #number of 50p
        for ty in range(0,int((200-100*pd-50*ft)/20)+1): #number of 20p - first to have a possible remainder
            for tn in range(0,int((200-100*pd-50*ft-20*ty)/10)+1): #number of 10p
                for fe in range(0,int((200-100*pd-50*ft-20*ty-10*tn)/5)+1): #number of 5p
                    for to in range(0,int((200-100*pd-50*ft-20*ty-10*tn-5*fe)/2)+1): #number of 2p
                        #the remaining amount is necessarily filled in by a single amount of 1p
                        if (100*pd+50*ft+20*ty+10*tn+5*fe+2*to) >= 200:
                            arr = [pd, ft, ty, tn, fe, to]
                            print(100*pd+50*ft+20*ty+10*tn+5*fe+2*to)
                            print(arr)
                        count += 1
print(count)
