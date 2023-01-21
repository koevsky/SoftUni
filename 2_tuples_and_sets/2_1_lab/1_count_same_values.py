nums_list = [float(x) for x in input().split()]
res_dict = {}
for x in nums_list:
    if x not in res_dict.keys():
        res_dict[x] = 0
    res_dict[x] += 1

[print(f"{k} - {v} times") for k, v in res_dict.items()]
