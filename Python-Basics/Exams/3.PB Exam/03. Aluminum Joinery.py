joinery_count = int(input())
joinery_type = input()
delivery = input()

if joinery_count >= 10:
    price = 0
    if joinery_type == "90X130":
        price = joinery_count * 110
        if 60 >= joinery_count > 30:
            price -= price * 5 / 100
        elif joinery_count > 60:
            price -= price * 8 / 100

    elif joinery_type == "100X150":
        price = joinery_count * 140
        if 80 >= joinery_count > 40:
            price -= price * 6 / 100
        elif joinery_count > 80:
            price -= price * 10 / 100

    elif joinery_type == "130X180":
        price = joinery_count * 190
        if 50>= joinery_count > 20:
            price -= price * 7 / 100
        elif joinery_count > 50:
            price -= price * 12 / 100

    elif joinery_type == "200X300":
        price = joinery_count * 250
        if 50 >= joinery_count > 25:
            price -= price * 9 / 100
        elif joinery_count > 50:
            price -= price * 14 / 100

    if delivery == "With delivery":
        price += 60

    if joinery_count > 99:
        price -= price * 4 / 100

    print(f"{price:.2f} BGN")

else:
    print("Invalid order")
