num1 = "123"
num2 = "456"

n,m=0,0

for i in num1:
    n*=10
    x=ord(i)-48
    n+=x

for i in num2:
    m *= 10
    x = ord(i) - 48
    m += x

print(n*m)

