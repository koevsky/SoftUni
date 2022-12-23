nylon_needed = int(input())
paint_needed = int(input())
diluent = int(input())
working_hours = int(input())

paint_needed += 10/100*paint_needed
nylon_needed += 2

materials_price = nylon_needed * 1.50 + paint_needed * 14.50 + diluent * 5 + 0.40
workers_price = working_hours * materials_price * 30/100

total_price = materials_price + workers_price
print(total_price)
