# ITERATOR

list = [1,2,3,4,5]

# Method 1
print(list[1])

# Method 2
for item in list:
    print(item)

# Method 3
iterator = iter(list)
print(next(iterator))
print(next(iterator))
print(iterator.__next__())
print(next(iterator))
print(iterator.__next__())


