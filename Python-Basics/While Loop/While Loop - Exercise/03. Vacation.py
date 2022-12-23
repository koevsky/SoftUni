excursion_cost = float(input())
current_money = float(input())
five_in_a_row = 0
day_counter = 0

while True:
    action = input()
    money = float(input())
    day_counter += 1
    if action == "save":
        five_in_a_row = 0
        current_money += money
        if current_money >= excursion_cost:
            print(f"You saved the money for {day_counter} days.")
            break
    else:
        five_in_a_row += 1
        if current_money - money <= 0:
            current_money = 0
        else:
            current_money -= money

        if five_in_a_row == 5:
            print(f"You can't save the money.")
            print(f"{day_counter}")
            break
