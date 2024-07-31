def bs(li,fi=83):
    x,y=0,1
    while fi>y:
        x=y+1
        y=x*2
        
    low=x
    high=y
   
    while low<=high:
        mid=low+(high-low)//2
        if li[mid] == fi:
            return mid
        elif li[mid] < fi:
            low=mid+1
        else:
            high=mid-1
    else:
        return low #low for ceil. for floor return high

li=[x for x in range(100)]

print(bs(li))