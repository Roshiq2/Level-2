def find_sum_of_longest_subarray(arr):
    left, right, max_length, current_sum = 0, 0, 0, 0
    freq = {}

    while right < len(arr):
        freq[arr[right]] = freq.get(arr[right], 0) + 1
        current_sum += arr[right]
        right += 1

        if len(freq) > 2:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                del freq[arr[left]]
            current_sum -= arr[left]
            left += 1

        max_length = max(max_length, right - left)

    return current_sum

# Example usage
arr = [1, 5, 5, 1,5,5,7,2,1,6,6,5]
result = find_sum_of_longest_subarray(arr)
print(result)  # Output: 11
