season = input()
group_type = input()
student_count = int(input())
nights_count = int(input())

if season == "Winter":
    if group_type == "boys":
        price = student_count * 9.60 * nights_count
        sport = "Judo"
    elif group_type == "girls":
        price = student_count * 9.60 * nights_count
        sport = "Gymnastics"
    else:
        price = student_count * 10 * nights_count
        sport = "Ski"

elif season == "Spring":
    if group_type == "boys":
        price = student_count * 7.20 * nights_count
        sport = "Tennis"
    elif group_type == "girls":
        price = student_count * 7.20 * nights_count
        sport = "Athletics"
    else:
        price = student_count * 9.50 * nights_count
        sport = "Cycling"

elif season == "Summer":
    if group_type == "boys":
        price = student_count * 15 * nights_count
        sport = "Football"
    elif group_type == "girls":
        price = student_count * 15 * nights_count
        sport = "Volleyball"
    else:
        price = student_count * 20 * nights_count
        sport = "Swimming"

if student_count >= 50:
    price -= price * 50/100
elif 20 <= student_count < 50:
    price -= price * 15/100
elif 10 <= student_count < 20:
    price -= price * 5/100

print(f"{sport} {price:.2f} lv.")