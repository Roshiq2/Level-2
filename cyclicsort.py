arr=[1,4,3,5,6,2,8,10]

i=0
while i<len(arr):
    c=arr[i]-1
    if arr[i]<len(arr) and arr[i]!=arr[c]:
        arr[i],arr[c]=arr[c],arr[i]
    else:
        i+=1
print(arr)