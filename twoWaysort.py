def twoWaySort(arr, n): 
	# To store odd Numbers 
	odd = [] 
	# To store Even Numbers 
	even = [] 
	for i in range(n): 
		# If number is even push them to even vector 
		if arr[i] % 2 == 0: 
			even.append(arr[i]) 
		# If number is odd push them to odd vector 
		else: 
			odd.append(arr[i]) 
	# Sort even array in ascending order 
	even.sort() 
	# Sort odd array in descending order 
	odd.sort(reverse=True) 
	i = 0
	# First store odd numbers to array 
	for j in range(len(odd)): 
		arr[i] = odd[j] 
		i += 1
	# Then store even numbers to array 
	for j in range(len(even)): 
		arr[i] = even[j] 
		i += 1


arr = [1, 3, 2, 7, 5, 4] 
n = len(arr) 
twoWaySort(arr, n) 
for i in range(n): 
	print(arr[i], end=" ") 
