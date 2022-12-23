month = input()
period = int(input())

if month == "May" or month == "October":
    studio_price = period * 50
    apartment_price = period * 65
    if 7 < period <= 14:
        studio_price -= studio_price * 5/100
    elif period > 14:
        studio_price -= studio_price * 30/100
        apartment_price -= apartment_price * 10/100

elif month == "June" or month == "September":
    studio_price = period * 75.20
    apartment_price = period * 68.70
    if period > 14:
        studio_price -= studio_price * 20 / 100
        apartment_price -= apartment_price * 10 / 100

elif month == "July" or month == "August":
    studio_price = period * 76
    apartment_price = period * 77
    if period > 14:
        apartment_price -= apartment_price * 10 / 100

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")