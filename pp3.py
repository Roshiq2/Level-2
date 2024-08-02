# Import the random module
import random

# Define the A function that reverses a string
def A(S):
  return S[::-1]

# Define the B function that shuffles a string
def B(S):
  # Convert the string to a list of characters
  chars = list(S)
  # Shuffle the list using the random module
  random.shuffle(chars)
  # Convert the list back to a string and return it
  return "".join(chars)

# Define the C function that merges two strings randomly
def C(S, T):
  # Initialize an empty list to store the merged characters
  merged = []
  # Initialize two pointers to track the positions in S and T
  i = 0
  j = 0
  # Loop until both pointers reach the end of their strings
  while i < len(S) and j < len(T):
    # Choose a random number between 0 and 1
    r = random.randint(0, 1)
    # If r is 0, append the character from S and increment i
    if r == 0:
      merged.append(S[i])
      i += 1
    # Else, append the character from T and increment j
    else:
      merged.append(T[j])
      j += 1
  # Append the remaining characters from S or T if any
  merged.extend(S[i:])
  merged.extend(T[j:])
  # Convert the list to a string and return it
  return "".join(merged)

# Define a function to find the lexicographically smallest N
def find_N(M):
  # Initialize an empty set to store all possible candidates for N
  candidates = set()
  # Loop over all possible lengths of N from 1 to half of M
  for l in range(1, len(M) // 2 + 1):
    # Extract the substring of length l from M as a candidate for N
    N = M[:l]
    # Check if C(A(N), B(N)) equals M by repeating the C function many times
    for _ in range(100):
      if C(A(N), B(N)) == M:
        # Add N to the set of candidates
        candidates.add(N)
        # Break the inner loop as we found a valid N
        break
  # Return the lexicographically smallest candidate or None if no candidate exists
  return min(candidates) if candidates else None

# Read the input
M = input()

# Print the output
print(find_N(M))
#abcdefgabcdefg