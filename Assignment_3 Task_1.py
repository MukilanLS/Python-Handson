user_input = int(input("Enter a number: "))
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

number = factorial(user_input)
print("The factorial of", user_input , "is:", number)