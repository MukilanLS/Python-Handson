# Set
set = {1,2,3,4,5,6,7,8,1,2,3,6}
print(set)

# Adding one element in set
set.add(9)
print(set)

# Removing one element in set
set.remove(1)
print(set)

# Boolean field to determine whether the element is present in set or not
print(1 in set)
print(2 in set)

# Intersection and Union in set
set1 = {1,2,3,4}
set2 = {6,7,3,2,1}
print(set1 & set2)
print(set1 | set2)
print(set1.union(set2))

# Subset in set
set3 = {1,2,3,4}
print(set3.issubset(set1))
print(set3.issubset(set2))