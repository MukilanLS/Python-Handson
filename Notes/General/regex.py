# Regular Expression - Regex0

import re

pattern = "apple"

# match (Pattern, Strings, flags) - Checks the first characters in the pattern
if re.match(pattern, "ballapple"):
    print("Match True")
# Search (Pattern, Strings, flags) = Checks the Strings is present in the pattern
if re.search(pattern, "ballapple"):
    print("Search True")
else:
    print("False")

# findall (Pattern, Strings, flags)
string = re.findall('apple',pattern)
print(string)

# sub (Pattern, repl, Strings, flags)
a = "This is Mukilan"
b = "Mukilan"
print(re.sub(b,"Mukilan L S", a))
