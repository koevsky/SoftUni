budget = float(input())
season = input()

if budget <= 100:
    class_type = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = budget * 35/100
    else:
        car_type = "Jeep"
        car_price = budget * 65 / 100

elif 100 < budget <= 500:
    class_type = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = budget * 45 / 100
    else:
        car_type = "Jeep"
        car_price = budget * 80 / 100

elif budget > 500:
    class_type = "Luxury class"
    car_type = "Jeep"
    car_price = budget * 90 / 100

print(f"{class_type}")
print(f"{car_type} - {car_price:.2f}")