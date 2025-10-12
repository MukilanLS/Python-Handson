# String Formatting
name = "Mukilan"
number = len(name) * 7
print("Hello {}, Your licky number is {}.".format(name, number))

example = "format () method"
print("This is an example of {} on a String.".format(example))

first = "Apple"
second = "Ball"
third = "Cat"
print("A for {}, B for {}, C for {}.".format(first, second, third))
print("A for {0}, C for {2}, B for {1}.".format(first, second, third))

price = 150
price_with_tax = price + 50
print(price_with_tax)
print("The Price of an Icecream: Rs {:.2f}\nThe Price of an Icecream with tax: Rs {:.2f}".format(price, price_with_tax))