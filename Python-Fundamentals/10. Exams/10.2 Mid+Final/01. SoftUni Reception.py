emp_1_per_h, emp_2_per_h, emp_3_per_h, students = int(input()), int(input()), int(input()), int(input())
total_time = 0
while students > 0:
    total_time += 1
    if total_time % 4 != 0:
        students -= emp_1_per_h
        students -= emp_2_per_h
        students -= emp_3_per_h

print(f"Time needed: {total_time}h.")
