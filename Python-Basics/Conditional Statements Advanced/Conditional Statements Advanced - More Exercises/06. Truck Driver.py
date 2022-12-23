season = input()
km_per_month = float(input())

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        money = km_per_month * 4 * 0.75
    elif season == "Summer":
        money = km_per_month * 4 * 0.90
    elif season == "Winter":
        money = km_per_month * 4 * 1.05

elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        money = km_per_month * 4 * 0.95
    elif season == "Summer":
        money = km_per_month * 4 * 1.10
    elif season == "Winter":
        money = km_per_month * 4 * 1.25

elif 10000 < km_per_month <= 20000:
    money = km_per_month * 4 * 1.45

money -= money * 10/100

print(f"{money:.2f}")