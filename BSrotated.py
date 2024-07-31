
d=[66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63]
p =[66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77]
w =[61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16]


def bs(li,fi):
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
        return high
    
di=dict({})

for i,j in zip(d,p):
    di[i]=j

for x,y in zip(sorted(di),range(len(d))):
    d[y]=x
    p[y]=di[x]

w=sorted(w)

ros=0
for i in range(len(w)):
    if w[i]< d[0]:
        ros+=0;
    else:
        sam=(bs(d,w[i]))
        if sam==-1:
            ros+=max(p)
        else:
            ros+=max(p[:sam+1])

print(ros)








# sum=0
# for i in w:
#     if i in d:
#         sum+=p[max(d[0:d.index(i)+1])]
#     else:
#         ros=len(d)-1
#         for j in range(len(d)):
#             if d[j]>i:
#                 break
#             else:
#                 ros=j
#         sum+=max(p[:ros+1])
# print(sum)

