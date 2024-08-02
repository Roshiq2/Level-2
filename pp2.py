def bitcount(x):
    count = 0
    while x > 0:
        count += x & 1
        x >>= 1
    return count

def maxSumSubarray(A):
    N = len(A)
    dp = [0] * N
    
    for i in range(N):
        curr_value = 0
        max_value = float('-inf')
        for j in range(i, -1, -1):
            curr_value = (curr_value & A[j]) | A[j]
            bits = bitcount(curr_value)
            subarray_sum = bits * A[i]
            if j > 0:
                subarray_sum += dp[j - 1]
            max_value = max(max_value, subarray_sum)
        dp[i] = max_value
        
    return dp[N - 1]

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

result = maxSumSubarray(A)
print(result)
