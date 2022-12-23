event_list = input().split("|")

energy = 100
coins = 100
is_closed = False
for event in event_list:
    event = event.split("-")
    action, number = event[0], int(event[1])
    if action == "rest":
        if energy + number > 100:
            energy_gained = 100 - energy
            energy = 100
        else:
            energy_gained = number
            energy += number
        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {energy}.")

    elif action == "order":
        if energy - 30 >= 0:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins - number >= 0:
            coins -= number
            print(f"You bought {action}.")
        else:
            print(f"Closed! Cannot afford {action}.")
            is_closed = True
            break
if not is_closed:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
