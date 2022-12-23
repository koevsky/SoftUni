lv_1_count = int(input())
lv_2_count = int(input())
lv_5_count = int(input())
searched_sum = int(input())

for lv_1 in range(0, lv_1_count+1):
    for lv_2 in range(0, lv_2_count+1):
        for lv_5 in range(0, lv_5_count+1):
            if lv_1 * 1 + lv_2 * 2 + lv_5 * 5 == searched_sum:
                print(f"{lv_1} * 1 lv. + {lv_2} * 2 lv. + {lv_5} * 5 lv. = {searched_sum} lv.")
