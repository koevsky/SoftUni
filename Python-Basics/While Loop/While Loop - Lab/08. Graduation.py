student_name = input()

grade = 0
failed_times = 0
total_mark = 0
while True:
    mark = float(input())
    if mark >= 4:
        grade +=1
        total_mark += mark
        if grade == 12:
            print(f"{student_name} graduated. Average grade: {(total_mark / 12):.2f}")
            break

    else:
        failed_times += 1
        if failed_times == 2:
            print(f"{student_name} has been excluded at {grade+1} grade")
            break

