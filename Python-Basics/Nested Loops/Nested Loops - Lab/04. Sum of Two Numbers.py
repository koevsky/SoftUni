interval_start = int(input())
interval_finish = int(input())
magic_number = int(input())
magic_combination = 0
total_combinations = 0
is_found = False
for x in range(interval_start, interval_finish +1):
    if is_found:
        break
    for y in range(interval_start, interval_finish+1):
        total_combinations += 1
        if x + y == magic_number:
            magic_combination = total_combinations
            print(f"Combination N:{magic_combination} ({x} + {y} = {magic_number})")
            is_found = True
            break


if not magic_combination:
    print(f"{total_combinations} combinations - neither equals {magic_number}")
