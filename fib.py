def fib(n):
    t=[0,1]
    for i in range(2,n):
        t[0],t[1]=t[1],t[0]+t[1]
    return t[-1]
print(fib(15))



n* (n-1)+(n-2)