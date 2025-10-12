# Strings Functions
a = "mukIlanls"
print(a.capitalize()) #
print(a.upper())
print(a.lower())
print(a.isnumeric())
print(a.isalpha())

b = "7"
print(b.capitalize())
print(b.isupper())
print(b.islower())
print(b.isnumeric())
print(b.isalpha())

c = "Mukilan is a good boy"
print(c.startswith("Mukil"))
print(c.endswith("boy"))
print(c.replace("Mukilan", "Mukilan L S"))
print(c.find("Mukilan"))
print(c.find("s"))
print(c.split())
print(c.split(" "))
print(c.splitlines())

d = " Mukilan"
e = "Mukilan    "
print(d.lstrip())
print(e.rstrip())

f = "Mukilan", "L S"
g = " "
print(g.join(f))
