# File Handling
# Method 1
file = open("my_file.txt", "r+")
write = file.write("Hello World")
print(write)
file.close()

file = open("my_file.txt", "a")
append = file.write("\nThis is Mukilan L S\n")
print(append)
file.close()

file = open("my_file.txt", "r+")
read = file.read()
print("Output 1", read)
# readline = file.readlines(3)
# print("Output 2",readline)
file.close()

# Method 2
with open("my_file.txt", "r+") as file:
    write = file.write("Hello World")
    print(write)

with open("my_file.txt", "a") as file:
    append = file.write("\nThis is Mukilan L S\n")
    print(append)

with open("my_file.txt", "r+") as file:
    read = file.read()
    print("Output 1", read)
    # readline = file.readlines()
    # print("Output 2",readline)

# Exception Handling
l = int(input("Enter a number: "))
m = int(input("Enter a number: "))

try:
    print(l/m)
except ZeroDivisionError:
    print("You can't divide by zero")
finally:
    print("Rest of the code will execute")

# Factorial
a = int(input("Enter a number: "))
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(a)
print("The factorial of", a, "is", result)

# Recursion
import sys

sys.setrecursionlimit(2)
n = 0
i = sys.getrecursionlimit()
print("The recursion limit is", i)

def python():
    global n
    n = n + 1
    print("Python", n)
    python()

python()

# Modules
from math import *
print(pi)

from math import pi
print(pi)

import math
print(math.pi)

# Passing Functions as Arguments
def add(x,y):
    return x + y
def square(z):
    return z * z

result = square(add(1,6))
print(result)

# Functions
def add(a,b):
    print(a+b)

add(1,2)

# Range Function
n = list(range(2,11,3))
print(n)

# General Functions
a = (1, 2, 3)
print(max(a))
print(min(a))
print(sum(a))
print(abs(-3035))
print(pow(2,30))

# Calculate Simple Interest
p = input("Principal, p: ")
n = input("Number of years, n: ")
r = input("Rate of Interest, r: ")

p = int(p)
n = int(n)
r = float(r)

si = (p*n*r)/100
print("Simple Interest is ", si)

# Convert Celsius to Fahrenheit and Fahrenheit to Celsius
c = input("Celsius: ")
f = input("Fahrenheit: ")

c = float(c)
f = float(f)

d = (c * 9/5) + 32
g = (f - 32) * 5/9

print("Fahrenheit: ", d)
print("Celsius: ", g)

# Print
print('Hello World')

# Input Function
a = input("What is your name? ")
print("Hi " + a)