def getMinimumCost(k, c):
    c.sort(reverse=True)
    purchased=0
    minimum=0
    for i in range(len(c)):
        minimum=minimum+c[i]*(purchased+1)
        if ((i+1)&k) == 0:
            purchased+=1
    return minimum
    
print(getMinimumCost(3,[1,3,5,7,9]))