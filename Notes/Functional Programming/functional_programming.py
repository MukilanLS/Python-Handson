# Functional Programming
def add(a, b):
    return a + b

# Return a function from function
def call(i,j):
    return add(i,j)

# Passing a function to function
def pas(i,j,fn):
    return fn(i,j)

result = pas(1, 2, call)
print(result)