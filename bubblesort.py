arr=[2,6,4,3,5,8]
for i in range(len(arr)-1):
    swapped=False
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True
    if not swapped:
        break
print(arr)