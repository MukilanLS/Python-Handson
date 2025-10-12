# List
numbers = [1,2,3,4,5]
print(numbers)
print(numbers[1])

# Mutable --> Can change values
numbers[0] = 0
print(numbers)

colors = ["Yellow","Red","Green"]
print(colors)
print(colors.count("Yellow"))
print(colors[0])

mix = [1,"Yellow",2,"Green"]
print(mix)
print(mix[1])

# Index of an element
print(mix.index("Yellow"))

# Length of the list
print(len(mix))

# Blank List
blank_list = []
print(blank_list)

# Adding lists
list1 = [1,"Yellow",2,"Green"]
list2 = [3,"Blue",4,"White"]
print(list1 + list2)

# Adding one element in list
# Method 1
list1.append("Purple")
print(list1)

# Method 2
list1.insert(0,"Brown")
print(list1)

# Adding multiple elements in list
list1.extend(["Orange", "Blue" ])
print(list1)

# Replacing an element in list
list3 = [1,"Mukilan","Aus", 77, "Test",8,82,13,"L S"]
list3[2] = "Aussies"
print(list3)

# Removing one element in list
# Method 1
list3.remove(1)
print(list3)

# Method 2
list3.pop(3)
print(list3)

# Removing multiple elements in list
del list3[2:3]
print(list3)

# Removing all elements in list
list4 = [7,8,9,0,12,13]
list4.clear()
print(list4)

# Multiplying the values in the list
n = (1,2,3,4,5)
print(n * 4)

# Boolean field to determine whether the element is present in list or not
print("Yellow" in list1)
print("Black" in list1)

# Sorting
numbers2 = [1000,256,6541,31,351,65165,1651,651,61,165,5]
print(numbers2)
numbers2.sort()
print(numbers2)

# Reversing the list
numbers2.reverse()
print(numbers2)

# List Slicing --> [Start Index : End Index : Interval]
num = [10,20,30,40,50,60,70,80]
print(num[0:5])
print(num[:4])
print(num[3:])
print(num[:])
print(num[0:5:2])

# List Comprehension
# Sample Program 1
x = []
for i in range(11):
    z = i ** 2
    x.append(z)
print(x)

y = [i ** 2 for i in range(11)] # Expression for item in list
print(y)

# Sample Program 2
m = []
for i in range(11):
    if i % 2 == 0:
        o = i ** 2
        m.append(o)
print(m)

y = [i ** 2 for i in range(11) if i ** 2 % 2 == 0] # Expression for item in list if (test expression)
print(y)

# Remove Duplicates
l1 = [1,2,2,3,13,151,62,3,1,2,1,2,12,2]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l1)
print(l2)