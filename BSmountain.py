def fun(li): 
    start=0
    end=len(li)-1
    while start<end:
        mid=start+(end-start)//2
        if li[mid]>li[mid+1]:
            end=mid
        else:
            start=mid+1
    return li[start]

li=[1,3,6,7,8,9,0,1,2,8]
print(fun(li))
