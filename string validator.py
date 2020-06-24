"""Python has built-in string validation methods for basic data.
 It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc."""

s='tqA4'


print(any(c.isalnum()  for c in s))
print (any(c.isalpha() for c in s))
print (any(c.isdigit() for c in s))
print (any(c.islower() for c in s))
print (any(c.isupper() for c in s))