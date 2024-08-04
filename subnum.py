def find_subsets(data):
  subsets = []
  subsets.append([])
  for num in data:
    new_subsets = []
    for subset in subsets:
      new_subset = subset + [num]
      new_subsets.append(new_subset)
    subsets.extend(new_subsets)

  return subsets

# Example usage
data = [1,5,3,4]
all_subsets = find_subsets(data)

print("All subsets of the list:")
for subset in all_subsets:
    if sum(subset)==8:
        print(subset)
