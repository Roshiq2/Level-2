def fun(n):
    n1=n
    n=n*2+1
    for i in range(n):
        for j in range(n):
            print(n1-(min(i,j,abs(n-i-1),abs(n-j-1))),end='')
        print()

fun(4)