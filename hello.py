import functools
# memory = {} #5:120
# def memoize_factorial(f):
# 	def inner(num):
# 		if num not in memory:
# 			memory[num] = f(num)
		
# 		return memory[num]

# 	return inner
	
# @functools.cache
def facto(num):
	if num == 1:
		return 1
	else:
		return num * facto(num-1)

print(facto(99))