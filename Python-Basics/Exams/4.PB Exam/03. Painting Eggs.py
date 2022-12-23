eggs_size, eggs_color = input(), input()
count = int(input())
price = 0
if eggs_size == "Large":
    if eggs_color == "Red":
        price = count * 16
    elif eggs_color == "Green":
        price = count * 12
    elif eggs_color == "Yellow":
        price = count * 9

elif eggs_size == "Medium":
    if eggs_color == "Red":
        price = count * 13
    elif eggs_color == "Green":
        price = count * 9
    elif eggs_color == "Yellow":
        price = count * 7

elif eggs_size == "Small":
    if eggs_color == "Red":
        price = count * 9
    elif eggs_color == "Green":
        price = count * 8
    elif eggs_color == "Yellow":
        price = count * 5

price -= price * 35 / 100

print(f"{price:.2f} leva.")
