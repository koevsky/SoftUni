inherited_money = float(input())
year_to_reach = int(input())
years_age = 18

for years in range(1800, year_to_reach+1):
    if years % 2 == 0:
        inherited_money -= 12000
        years_age += 1
    else:
        inherited_money -= 12000 + 50 * years_age
        years_age += 1

if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
else:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")
