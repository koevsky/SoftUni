digits, letters, others = "", "", ""
line = input()
for x in line:
    if x.isdigit():
        digits += x
    elif x.isalpha():
        letters += x
    elif not x.isalnum():
        others += x
print(digits)
print(letters)
print(others)