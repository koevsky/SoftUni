def grade(mark):
    result = ""
    if 2 <= mark <= 2.99:
        result = "Fail"
    elif 3 <= mark <= 3.49:
        result = "Poor"
    elif 3.50 <= mark <= 4.49:
        result = "Good"
    elif 4.50 <= mark <= 5.49:
        result = "Very Good"
    elif 5.50 <= mark <= 6.00:
        result = "Excellent"
    return result

current_mark = float(input())
print(grade(current_mark))