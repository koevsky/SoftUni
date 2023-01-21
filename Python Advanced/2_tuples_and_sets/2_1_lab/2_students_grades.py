n = int(input())
res_dict = {}
for _ in range(n):
    name, mark = input().split()
    if name not in res_dict.keys():
        res_dict[name] = []
    res_dict[name].append(float(mark))

for key, val in res_dict.items():
    average = sum(val) / len(val)
    print(f"{key} -> {' '.join([f'{x:.2f}' for x in val])} (avg: {average:.2f})")