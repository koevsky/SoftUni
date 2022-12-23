first_start_value, second_start_value = int(input()), int(input())
first_value_diff, second_value_diff = int(input()), int(input())
is_x, is_y = False, False
for x in range(first_start_value, first_start_value+first_value_diff+1):
    for y in range(second_start_value, second_start_value+second_value_diff+1):
        for check_x in range(2, x):
            if x % check_x == 0:
                is_x = True
                break
        for check_y in range(2, y):
            if y % check_y == 0:
                is_y = True
                break
        if (not is_x) and (not is_y):
            print(f"{x}{y}")
        else:
            is_x, is_y = False, False