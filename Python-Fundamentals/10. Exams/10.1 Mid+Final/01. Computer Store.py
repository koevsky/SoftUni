total_price_nt, taxes, total_price = 0, 0, 0
while True:
    line = input()
    if line == "special" or line == "regular":
        total_price = total_price_nt + taxes
        if total_price != 0:
            if line == "special":
                total_price -= total_price * 10/100
            print("Congratulations you've just bought a new computer!")
            print(f"Price without taxes: {total_price_nt:.2f}$")
            print(f"Taxes: {taxes:.2f}$")
            print("-----------")
            print(f"Total price: {total_price:.2f}$")
        else:
            print("Invalid order!")
        break
    money = float(line)
    if money >= 0:
        total_price_nt += money
        taxes += money * 20/100
    else:
        print("Invalid price!")
