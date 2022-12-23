initial_qty = int(input())
eggs_sold = 0
while True:
    command = input()
    if command == "Close":
        print("Store is closed!")
        print(f"{eggs_sold} eggs sold.")
        break
    eggs_count = int(input())
    if command == "Buy":
        if initial_qty - eggs_count < 0:
            print("Not enough eggs in store!")
            print(f"You can buy only {initial_qty}.")
            break
        else:
            initial_qty -= eggs_count
            eggs_sold += eggs_count
    elif command == "Fill":
        initial_qty += eggs_count
