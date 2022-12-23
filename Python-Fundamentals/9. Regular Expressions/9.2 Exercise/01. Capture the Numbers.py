import re
pattern = r"([0-9]+)"
res_list = []
while True:
    line = input()
    if line:
        result = re.findall(pattern, line)
        for x in result:
            res_list.append(x)
    else:
        break
print(" ".join(res_list))



