line = input().split(" ")
res = ""
for x in line:
    res += x*len(x)
print(res)