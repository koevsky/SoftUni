from collections import deque
materials_boxes = list(map(int, input().split()))
magic_values = deque(list(map(int, input().split())))

presents = {}


def present_add(num, presents_dict):
    if num == 150:
        item = "Doll"
        if item not in presents_dict.keys():
            presents_dict[item] = 1
        else:
            presents_dict[item] += 1
    elif num == 250:
        item = "Wooden train"
        if item not in presents_dict.keys():
            presents_dict[item] = 1
        else:
            presents_dict[item] += 1
    elif num == 300:
        item = "Teddy bear"
        if item not in presents_dict.keys():
            presents_dict[item] = 1
        else:
            presents_dict[item] += 1
    elif num == 400:
        item = "Bicycle"
        if item not in presents_dict.keys():
            presents_dict[item] = 1
        else:
            presents_dict[item] += 1
    else:
        return False

    return presents_dict


while magic_values and materials_boxes:
    product = materials_boxes[-1] * magic_values[0]
    if product in [150, 250, 300, 400]:
        presents = present_add(product, presents)
        magic_values.popleft()
        materials_boxes.pop()
    else:
        if product < 0:
            result_num = materials_boxes[-1] + magic_values[0]
            magic_values.popleft()
            materials_boxes.pop()
            materials_boxes.append(result_num)
        elif product > 0:
            magic_values.popleft()
            materials_boxes[-1] += 15
        elif product == 0:
            if magic_values[0] == 0:
                magic_values.popleft()
            if materials_boxes[-1] == 0:
                materials_boxes.pop()

if ("Doll" in presents.keys() and "Wooden train" in presents.keys()) or ("Teddy bear" in presents.keys() and "Bicycle" in presents.keys()):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_boxes:
    print(f"Materials left: {', '.join(reversed(list(map(str, materials_boxes))))}")
if magic_values:
    print(f"Magic left: {', '.join(list(map(str, magic_values)))}")

presents = dict(sorted(presents.items(), key=lambda x: x[0]))
for k, v in presents.items():
    print(f"{k}: {v}")
