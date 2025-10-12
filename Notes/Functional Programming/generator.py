# GENERATOR

# Program 1
def fn():
    yield 1
    yield 2
    yield 3

# Method 1
for x in fn():
    print(x)

# Method 2
values = fn()
print(next(values))
print(next(values))
print(values.__next__())

# Program 2
def square():
    n = 1
    while n <= 5:
        square = n ** 2
        yield square
        n = n + 1

# Method 1
for y in square():
    print(y)

# Method 2
result = square()
print(next(result))
print(next(result))
print(result.__next__())
print(next(result))
print(result.__next__())