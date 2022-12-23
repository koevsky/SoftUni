bad_marks_threshold = int(input())
bad_marks_counter = 0
marks_counter = 0
total_marks_value = 0
last_problem = ""
while True:
    problem_name = input()
    if problem_name == "Enough":
        print(f"Average score: {(total_marks_value / marks_counter):.2f}")
        print(f"Number of problems: {marks_counter}")
        print(f"Last problem: {last_problem}")
        break
    mark = int(input())
    marks_counter += 1
    total_marks_value += mark
    if mark <= 4:
        bad_marks_counter += 1
        if bad_marks_counter == bad_marks_threshold:
            print(f"You need a break, {bad_marks_counter} poor grades.")
            break
    last_problem = problem_name
