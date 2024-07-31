num=15
k=1
x=num+1
for i in range(num):
    print(k,end=' ')
    k+=1
    x=1
    y=x
    for j in range(0,i):
        print(k+y, end=' ')
        y+=1
    x-=1
    print()