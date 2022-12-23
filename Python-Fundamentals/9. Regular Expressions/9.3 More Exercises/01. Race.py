import re
names_list = input().split(", ")
racers_dict = {}

names_pattern = r"[^\W\d_]"
numbers_pattern = r"(\d)"

while True:
    line = input()
    if line == "end of race":
        break
    name = "".join(re.findall(names_pattern, line))
    distance = re.findall(numbers_pattern, line)
    distance = sum([int(x) for x in distance])
    if name in names_list:
        if name not in racers_dict.keys():
            racers_dict[name] = int(distance)
        else:
            racers_dict[name] += int(distance)

racers_dict_sorted = dict(sorted(racers_dict.items(), key=lambda x: -x[1]))
counter = 0
for key in racers_dict_sorted.keys():
    counter += 1
    if counter == 1:
        print(f"1st place: {key}")
    elif counter == 2:
        print(f"2nd place: {key}")
    elif counter == 3:
        print(f"3rd place: {key}")
    else:
        break