# Character and Character Sequences

import re

string_1 = "It is a 77 dog"

# ^ - Matches the beginning of the line
pattern_1 = "^It"
print(re.findall(pattern_1, string_1, flags=0))

# $ - Natches the end of the line
pattern_2 = "dog$"
print(re.findall(pattern_2, string_1, flags=0))

# . - Natches any character
pattern_3 = "."
print(re.findall(pattern_3, string_1, flags=0))
pattern_4 = "^I..."
print(re.findall(pattern_4, string_1, flags=0))

# \d - Matches any digit
pattern_5 = r'\d'
print(re.findall(pattern_5, string_1, flags=0))

# \D - Matches any digit
pattern_6 = r'\D'
print(re.findall(pattern_6, string_1, flags=0))

# \s - Matches any digit
pattern_7 = r'\s'
print(re.findall(pattern_7, string_1, flags=0))

# \S - Matches any digit
pattern_8 = r'\S'
print(re.findall(pattern_8, string_1, flags=0))

string_2 = "mail ID: lsmukilan77@gmail.com"

# * - Repeats a character zero or more times
pattern_9 = "ma*"
print(re.findall(pattern_9, string_2, flags=0))

# + - Repeats a character one or more times
pattern_10 = "ma+"
print(re.findall(pattern_10, string_2, flags=0))

# ? - Matches the expression 0 to 1 times
pattern_11 = "^m.*?"
print(re.findall(pattern_11, string_2, flags=0))

pattern_12 = "^m.+?"
print(re.findall(pattern_12, string_2, flags=0))

# ( - Indicates where the string extraction is to start
# ) - Indicates where the string extraction is to end
pattern_13 = r"^mail ID: (\S+@\S+)"
print(re.findall(pattern_13, string_2, flags=0))

pattern_19 = "@([^ ]*)"
print(re.findall(pattern_19, string_2, flags=0))

string_3 = "Python 3.0"

# [aeiou] - Matches a single character in the listed set
pattern_14 = "[aeiou]"
print(re.findall(pattern_14, string_3, flags=0))

# [^xyz] - Matches a single character
pattern_15 = "[^xyz]"
print(re.findall(pattern_15, string_3, flags=0))

# [a-z 0-9] - set pf characters include a range
pattern_16 = "[a-z 0-9]"
print(re.findall(pattern_16, string_3, flags=0))
pattern_17 = "[A-Z]"
print(re.findall(pattern_17, string_3, flags=0))

string_4 = "pythonn"

# {}
pattern_18 = "python{0}"
print(re.findall(pattern_18, string_4, flags=0))