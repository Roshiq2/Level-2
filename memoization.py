def fib(r):
    a,b=0,1
    if r==1:
        return a
    elif r==0:
        return b
    for i in range(2,r+1):
        a,b=b,a+b
    return b

print(fib(10000))

# 218922995834555169026
# 354224848179261915075