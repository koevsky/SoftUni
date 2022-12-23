desired_income = float(input())
money_collected = 0

while True:
    cocktail_name = input()
    if cocktail_name == "Party!":
        print(f"We need {abs(desired_income-money_collected):.2f} leva more.")
        break
    cocktail_count = int(input())
    price = cocktail_count * len(cocktail_name)
    if price % 2 != 0:
        price -= price * 25/100
    money_collected += price
    if money_collected >= desired_income:
        print("Target acquired.")
        break
print(f"Club income - {money_collected:.2f} leva.")
