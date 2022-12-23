town_name, package_type, vip_discount = input(), input(), input()
days_stay = int(input())
price = 0
is_invalid = False
if town_name == "Bansko" or town_name == "Borovets":
    if package_type == "withEquipment":
        price = 100 * days_stay
        if days_stay > 7:
            price -= 100
        if vip_discount == "yes":
            price -= price * 10/100
    elif package_type == "noEquipment":
        price = 80 * days_stay
        if days_stay > 7:
            price -= 80
        if vip_discount == "yes":
            price -= price * 5/100
    else:
        is_invalid = True

elif town_name == "Varna" or town_name == "Burgas":
    if package_type == "withBreakfast":
        price = 130 * days_stay
        if days_stay > 7:
            price -= 130
        if vip_discount == "yes":
            price -= price * 12/100
    elif package_type == "noBreakfast":
        price = 100 * days_stay
        if days_stay > 7:
            price -= 100
        if vip_discount == "yes":
            price -= price * 7/100
    else:
        is_invalid = True
else:
    is_invalid = True

if days_stay < 1:
    print("Days must be positive number!")
elif is_invalid:
    print("Invalid input!")
else:
    print(f"The price is {price:.2f}lv! Have a nice time!")


