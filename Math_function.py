num=int(input())

def fun(n,a,b):
    if n==1:
        return a
    elif n==2:
        return b
    t=[a,b]
    for i in range(2,n):
        temp=t[1]-t[0]
        t[0]=t[1]
        t[1]=temp
    return (temp)%((10**9)+7)

l=[]
for i in range(num):
    r=list(input().split(" "))
    l.append(r)

for r in l:
    print("output:" ,fun(int(r[0]),int(r[1]),int(r[2])))



