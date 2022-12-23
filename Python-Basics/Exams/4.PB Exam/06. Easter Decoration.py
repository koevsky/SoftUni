client_count = int(input())
total_money = 0

for p in range(client_count):
    current_money = 0
    purchase_count = 0
    while True:
        text = input()
        if text == "Finish":
            if purchase_count % 2 == 0:
                current_money  -= current_money * 20/100
            print(f"You purchased {purchase_count} items for {current_money:.2f} leva.")
            total_money += current_money
            break
        elif text == "basket":
            current_money += 1.50
        elif text == "wreath":
            current_money += 3.80
        elif text == "chocolate bunny":
            current_money += 7
        purchase_count += 1
print(f"Average bill per client is: {(total_money / client_count):.2f} leva.")
