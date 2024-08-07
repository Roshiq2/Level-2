a=[10,25,35,40,20,50,10]
f=60
res=[]
for i in range(len(a)): #10
    r=a[i]
    li=[a[i]]
    for j in range(i+1,len(a)):
        if a[i]+a[j]==f:
            res.append([a[i],a[j]])
        elif r+a[j]<=f:
            li.append(a[j])
            r+=a[j]
            if r==f:
                res.append(li)
                break
        else:
            break

# for i in range(len(a)-1):
#         if a[i]+a[i+1]==f:
#                 res.append([a[i],a[i+1]])

print(res)
            

            



    
