budget = float(input())
season = input()

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        price = budget * 30/100
    else:
        place = "Hotel"
        price = budget * 70/100

elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        price = budget * 40 / 100
    else:
        place = "Hotel"
        price = budget * 80 / 100

elif budget > 1000:
    destination = "Europe"
    place = "Hotel"
    price = budget * 90/100

print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")
