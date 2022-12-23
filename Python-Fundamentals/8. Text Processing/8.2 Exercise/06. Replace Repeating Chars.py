line = input()
res = ""
previous_letter = ""
for x in line:
    if x != previous_letter:
        res += x
        previous_letter = x
print(res)

