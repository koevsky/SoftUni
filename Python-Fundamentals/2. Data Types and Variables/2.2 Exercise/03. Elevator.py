people, capacity = int(input()), int(input())
if people <= capacity:
    print(1)
else:
    courses = people // capacity
    people_left = people - courses * capacity
    if people_left:
        courses += 1
    print(courses)
