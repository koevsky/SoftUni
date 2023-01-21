from collections import deque

subs_line = deque(input().split())

all_colors = ["red", "yellow", "blue", "orange", "purple", "green"]
primary = ["red", "yellow", "blue"]
secondary = ["orange", "purple", "green"]

total_colors_found = []

while subs_line:

    if len(subs_line) >= 2:
        left_part = subs_line.popleft()
        right_part = subs_line.pop()

    else:
        left_part = subs_line.popleft()
        right_part = ""

    variant_1, variant_2 = left_part + right_part, right_part + left_part

    if variant_1 in all_colors:
        total_colors_found.append(variant_1)

    elif variant_2 in all_colors:
        total_colors_found.append(variant_2)

    else:
        left_part = left_part[:len(left_part)-1]
        right_part = right_part[:len(right_part)-1]
        middle = len(subs_line) // 2
        if left_part:
            subs_line.insert(middle, left_part)
        if right_part:
            subs_line.insert(middle, right_part)


result_colors = []

for color in total_colors_found:

    if color in primary:
        result_colors.append(color)

    elif color in secondary:

        set_colors = set(total_colors_found)

        if color == "orange" and {"red", "yellow"}.issubset(set_colors):
            result_colors.append(color)
        elif color == "purple" and {"red", "blue"}.issubset(set_colors):
            result_colors.append(color)
        elif color == "green" and {"yellow", "blue"}.issubset(set_colors):
            result_colors.append(color)

print(result_colors)