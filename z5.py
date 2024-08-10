li=[-1,2,1,-4]
k=1
arr=[]
for i in range(len(li)-2):
    for j in range(i+1,len(li)-1):
        for l in range(j+1,len(li)):
            arr.append([li[i],li[j],li[l]])
print(sum(min(arr,key=lambda i: abs(sum(i)-k))))
