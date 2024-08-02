# def cost_function(x, y):
#     if x < y:
#         return x
#     else:
#         return cost_function(x // y, y) + x % y

# def find_smallest_y(x, c):
#     if x == c:
#         return x+1
    
#     for y in range(2, x + 1):
#         if cost_function(x, y) == c:
#             return y
    
#     return -1

# # Read input values
# x = int(input())
# c = int(input())

# # Find the smallest value of y
# result = find_smallest_y(x, c)

# # Print the result
# print(result)
def cost(x, y):
    return x % y + (x // y)

def smallest(x, c):
    if x == c:
        return x+1
    
    for y in range(2, x + 1):
        if cost(x, y) == c:
            return y
    
    return -1

x = int(input())
c = int(input())

result = smallest(x, c)
print(result)
