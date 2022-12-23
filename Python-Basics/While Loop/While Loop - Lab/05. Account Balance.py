total_money = 0
while True:
    data = input()
    if data == "NoMoreMoney":
        print(f"Total: {total_money:.2f}")
        break
    elif float(data) < 0:
        print("Invalid operation!")
        print(f"Total: {total_money:.2f}")
        break
    data = float(data)
    total_money += data
    print(f"Increase: {data:.2f}")