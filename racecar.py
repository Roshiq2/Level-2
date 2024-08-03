s='roshiqroshiq'
m=len(s)//2
change=False
mid=m
r=m

if len(s)%2!=0:
    for i in range(len(s)):
        if not change:
            for j in range(len(s)):
                if j==mid:
                    print(s[j],end="")
                    if mid!=m:
                        r+=1
                    mid-=1
            
                if j==r and j!=m:
                    print(s[j],end="")
                else:
                    print(" ",end=' ')
    
            if mid==-1:
                change=True
                mid+=2
                r-=1
        else:
            
            for k in range(len(s)):
                if k==m and i==len(s)-1:
                    print(s[k],end='')
                    break
                elif k==mid:
                    print(s[k],end='')
                else:
                    print(" ",end=" ")
                if k==r:
                    print(s[k],end=" ")
                    r-=1
                
            mid+=1

                
                    
        print("")
else:
    print("Not Possible")
