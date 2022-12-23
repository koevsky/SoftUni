line = input().upper()
unique_symbols = ""
res = ""
current = ""
number = ""
index = 0
while index <= len(line) - 1:
    if not line[index-1].isdigit() and line[index].isdigit() and int(line[index]) > 0:
        index_to_add = 0
        for x in line[index:]:
            if x.isdigit():
                number += x
                index_to_add+=1
            else:
                break
        res += int(number) * current
        current = ""
        number = ""
        index += index_to_add
    elif not line[index].isdigit():
        current += line[index]
        unique_symbols += line[index]
        index += 1
print(f"Unique symbols used: {len(set(unique_symbols))}")
print(res)