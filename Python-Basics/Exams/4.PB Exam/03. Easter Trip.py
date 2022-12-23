destination, period = input(), input()
nights_count = int(input())
price = 0
if destination == "France":
    if period == "21-23":
        price = nights_count * 30
    elif period == "24-27":
        price = nights_count * 35
    elif period  == "28-31":
        price = nights_count * 40

elif destination == "Italy":
    if period == "21-23":
        price = nights_count * 28
    elif period == "24-27":
        price = nights_count * 32
    elif period  == "28-31":
        price = nights_count * 39

elif destination == "Germany":
    if period == "21-23":
        price = nights_count * 32
    elif period == "24-27":
        price = nights_count * 37
    elif period  == "28-31":
        price = nights_count * 43

print(f"Easter trip to {destination} : {price:.2f} leva.")