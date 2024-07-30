def bs(li,fi=5):
    if fi>li[-1]:
        return -1
    low=0
    high=len(li)-1
    while low<=high:
        mid=low+(high-low)//2
        if li[mid] == fi:
            return mid
        elif li[mid] < fi:
            low=mid+1
        else:
            high=mid-1
    else:
        return high #low for ceil. for floor return high

li=[2,4,6,8,10]



print(bs(li))





