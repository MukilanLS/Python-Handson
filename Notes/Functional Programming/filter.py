# FILTER

# Filter using function
def even(a):
    return a % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]

# Syntax - filter (function, iterable)
result = list(filter(even,numbers))
print(list(result))
print(set(result))
print(tuple(result))

# Filter using Lambda Function
result = list(filter(lambda a: a % 2 == 0, numbers))
print(result)

result = list(filter(lambda a: a % 2 == 0, range(11)))
print(result)
