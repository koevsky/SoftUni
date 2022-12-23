line = input()
index = 0
res = ""
total_power = 0
while index <= len(line) - 1:
    if line[index] != ">":
        res += line[index]
        index += 1
    elif line[index] == ">" and line[index+1].isdigit():
        res += line[index]
        index += 1
        exp_value = int(line[index])
        index_to_add = 0
        for x in line[index: index+exp_value+total_power]:
            if x == ">":
                break
            else:
                index_to_add += 1
        index += index_to_add
        total_power += exp_value - index_to_add
print(res)
