arr=[5,3,2,7,8,4,6]

def max(a,last):
    m=0
    for i in range(1,last+1):
        if a[m]<a[i]:
            m=i
    return m

for i in range(len(arr)):
    last=len(arr)-i-1
    m=max(arr,last)
    arr[last],arr[m]=arr[m],arr[last]

print(arr)