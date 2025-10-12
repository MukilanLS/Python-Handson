# MAP

# Map using function
def square(x):
    return x*x

numbers = [1,2,3,4,5,6,7,8,9,10]

# Syntax - map (function, iterable)
result = list(map(square,numbers))
print(list(result))

# Map using Lambda Function
result = list(map(lambda x: x * x, numbers))
print(result)

result = list(map(lambda x: x * x, range(11)))
print(result)

# Map using function
def even(a):
    return a % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]

# Syntax - map (function, iterable)
result = list(map(even,numbers))
print(list(result))

# Map using Lambda Function
result = list(map(lambda a: a % 2 == 0, numbers))
print(result)
