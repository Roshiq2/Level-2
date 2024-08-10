num=int(input("Enter num:")) #5
for i in range(1,num+1):
    print(i,end=' ')
    n=num-1
    x=i
    for j in range(1,i):
        x+=n
        print(x,end=' ')
        n-=1
    print('')