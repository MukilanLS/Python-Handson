# LAMBDA Function

# One variable using function
def add(a):
    return a+1

result = add(2)
print(result)

# One variable using LAMBDA
# Syntax - lambda argument : expression
add = lambda a: a + 1

result = add(2)
print(result)

# Two variable using function
def add(a,b):
    return a+b

result = add(1,2)
print(result)

# Two variable using LAMBDA
# Syntax - lambda argument : expression
add = lambda a,b: a + b

result = add(1,2)
print(result)
