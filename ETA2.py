def isprime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

primes=[]
x=int(input())
y=int(input())

for i in range(x,y+1):
    if isprime(i):
        primes.append(i)

print(primes)