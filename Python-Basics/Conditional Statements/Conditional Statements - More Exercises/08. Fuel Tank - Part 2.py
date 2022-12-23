fuel_type = input()
fuel_qty = float(input())
club_card = input()

if fuel_type == "Gas":
    price = fuel_qty*0.93
    if club_card == "Yes":
        price -= fuel_qty*0.08
    if 20 <= fuel_qty <= 25:
        price -= price*8/100
    elif fuel_qty > 25:
        price -= price*10/100
elif fuel_type == "Gasoline":
    price = fuel_qty*2.22
    if club_card == "Yes":
        price -= fuel_qty*0.18
    if 20 <= fuel_qty <= 25:
        price -= price*8/100
    elif fuel_qty > 25:
        price -= price*10/100
elif fuel_type == "Diesel":
    price = fuel_qty*2.33
    if club_card == "Yes":
        price -= fuel_qty*0.12
    if 20 <= fuel_qty <= 25:
        price -= price*8/100
    elif fuel_qty > 25:
        price -= price*10/100

print(f"{price:.2f} lv.")