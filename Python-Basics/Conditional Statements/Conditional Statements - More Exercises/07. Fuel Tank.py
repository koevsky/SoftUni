fuel_type = input()
fuel_in_tank = float(input())

if fuel_in_tank >= 25:
    if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print("Invalid fuel!")
else:
    if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
        print(f"Fill your tank with {fuel_type.lower()}!")
    else:
        print("Invalid fuel!")