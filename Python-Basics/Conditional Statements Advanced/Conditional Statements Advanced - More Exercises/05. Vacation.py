import math
budget = float(input())
season = input()

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 65/100
    else:
        location = "Morocco"
        price = budget * 45/100

elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 80/100
    else:
        location = "Morocco"
        price = budget * 60/100

elif budget > 3000:
    accommodation = "Hotel"
    price = budget * 90 / 100
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"

print(f"{location} - {accommodation} - {round(price, 4):.2f}")

