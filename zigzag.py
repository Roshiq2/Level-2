ar=[[1,2,3],
    [4,5,6],
    [7,8,9]]
r=c=0
l=len(ar)-1
res=[]
direction=True

for _ in range(len(ar)**2):
    res.append(ar[r][c])
    
    if direction:
        if r==0 and c!=l:
            c+=1
            direction=False
        elif c==l:
            r+=1
            direction=False
        else:
            r-=1
            c+=1
    else:
        if c==0 and r!=l:
            r+=1
            direction=True
        elif r==l:
            c+=1
            direction=True
        else:
            c-=1
            r+=1
print(res)
