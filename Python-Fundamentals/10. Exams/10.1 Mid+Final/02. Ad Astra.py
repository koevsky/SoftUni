import re
pattern = r"(#|\|)(([A-Za-z ]+)\1([0-9]{2})/([0-9]{2})/([0-9]{2})\1([0-9]+))\1"
line = input()
items_list = []
matches = re.findall(pattern, line)
for item in matches:
    text = str(item[1])
    if item[0] == "#":
        text = text.split("#")
    elif item[0] == "|":
        text = text.split("|")
    product, date, kcal = text[0], text[1], int(text[2])
    items_list.append([product, date, kcal])
calories = sum([x[2] for x in items_list])
days = calories // 2000
print(f"You have food to last you for: {days} days!")
for x in items_list:
    print(f"Item: {x[0]}, Best before: {x[1]}, Nutrition: {x[2]}")
