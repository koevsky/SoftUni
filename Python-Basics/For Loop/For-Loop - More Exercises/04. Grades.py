students_count = int(input())

top_students = 0
very_good_students = 0
good_students = 0
failed_students = 0

total_result = 0

for x in range(students_count):
    exam_mark = float(input())
    total_result += exam_mark
    if exam_mark >= 5:
        top_students += 1
    elif 4 <= exam_mark <= 4.99:
        very_good_students += 1
    elif 3 <= exam_mark <= 3.99:
        good_students += 1
    elif exam_mark < 3:
        failed_students += 1

average_mark = total_result / students_count

top_percentage = top_students / students_count * 100
very_good_percentage = very_good_students / students_count * 100
good_percentage = good_students / students_count * 100
failed_percentage = failed_students / students_count * 100

print(f"Top students: {top_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {very_good_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {good_percentage:.2f}%")
print(f"Fail: {failed_percentage:.2f}%")
print(f"Average: {average_mark:.2f}")
