drink_type, sugar_qty, drink_count = input(), input(), int(input())
price = 0
if drink_type == "Espresso":
    if sugar_qty == "Without":
        price = 0.90 * drink_count
        price -= price * 35/100
    elif sugar_qty == "Normal":
        price = 1 * drink_count
    elif sugar_qty == "Extra":
        price = 1.20 * drink_count
    if drink_count >= 5:
        price -= price * 25/100

elif drink_type == "Cappuccino":
    if sugar_qty == "Without":
        price = 1 * drink_count
        price -= price * 35/100
    elif sugar_qty == "Normal":
        price = 1.20 * drink_count
    elif sugar_qty == "Extra":
        price = 1.60 * drink_count

elif drink_type == "Tea":
    if sugar_qty == "Without":
        price = 0.50 * drink_count
        price -= price * 35/100
    elif sugar_qty == "Normal":
        price = 0.60 * drink_count
    elif sugar_qty == "Extra":
        price = 0.70 * drink_count

if price > 15:
    price -= price * 20/100

print(f"You bought {drink_count} cups of {drink_type} for {price:.2f} lv.")


