string = input("Text: ")
rot = int(input("Choose rot: "))
res = ""
for x in string:
    res += chr(ord(x) + rot)

print(res, f"+{rot}")