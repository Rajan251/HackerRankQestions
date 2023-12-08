s = input()
anum = False
abetic = False
digit = False
lower = False
upper = False
for i in s:
    if i.isalnum():
        anum = True
    if i.isalpha():
        abetic = True
    if i.isdigit():
        digit = True
    if i.islower():
        lower = True
    if i.isupper():
        upper = True

print(anum)
print(abetic)
print(digit)
print(lower)
print(upper)

# String Validators
# Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

# str.isalnum()
# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

# str.isalpha()
# This method checks if all the characters of a string are alphabetical (a-z and A-Z).

# >>> print 'abcD'.isalpha()
# True
# >>> print 'abcd1'.isalpha()
# False

# str.isdigit()
# This method checks if all the characters of a string are digits (0-9).

# >>> print '1234'.isdigit()
# True
# >>> print '123edsd'.isdigit()
# False

# str.islower()
# This method checks if all the characters of a string are lowercase characters (a-z).

# >>> print 'abcd123#'.islower()
# True
# >>> print 'Abcd123#'.islower()
# False


# str.isupper()
# This method checks if all the characters of a string are uppercase characters (A-Z).

# >>> print 'ABCD123#'.isupper()
# True
# >>> print 'Abcd123#'.isupper()
# False