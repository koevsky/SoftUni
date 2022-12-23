while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    total_money = 0
    while total_money < budget:
        total_money += float(input())
    print(f"Going to {destination}!")
