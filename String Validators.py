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