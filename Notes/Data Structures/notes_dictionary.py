# Dictionary
dict1 = {"key1":1, "key2":2, "key3":3}
print(dict1)
print(dict1["key1"])

# Adding element in Dictionary
dict1["key4"] = 4
print(dict1)

# Removing element in Dictionary
del dict1["key2"]
print(dict1)

# To get all the keys
print(dict1.keys())

# To get all the values
print(dict1.values())

# Boolean field to determine whether the element is present in Dictionary or not
print("key4" in dict1)
print("key4" in dict1)
print("key7" in dict1)

# Text field to determine whether the element is present in Dictionary or not with a customized message
print(dict1.get("key4"))
print(dict1.get("key7","key 7 not found" ))