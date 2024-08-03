def Calculate(n, A):
    # Write your code here
    cost=0
    while True:
        i=n//2
        if i!= 0 and i!= n-1:
            cost+=min(A[i-1],A[i+1])
        print(A.pop(i))
        print(A)
        if len(A)<=2:
            break
    return cost




N = int(input())

Arr = []
for _ in range(N):
    Arr.append(int(input()))

result = Calculate(N, Arr)

print(result)


