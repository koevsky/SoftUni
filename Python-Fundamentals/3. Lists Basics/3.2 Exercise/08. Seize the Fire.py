fire_list = input().split("#")
water_qty = int(input())
effort, total_fire = 0, 0
put_out_cells = []
for fire in fire_list:
    fire = fire.split(" = ")
    fire_type, cell_value = fire[0], int(fire[1])
    if fire_type == "Low" and 1 <= cell_value <= 50:
        if water_qty - cell_value >= 0:
            water_qty -= cell_value
            total_fire += cell_value
            put_out_cells.append(cell_value)
            effort += cell_value * 25/100

    elif fire_type == "Medium" and 51 <= cell_value <= 80:
        if water_qty - cell_value >= 0:
            water_qty -= cell_value
            total_fire += cell_value
            put_out_cells.append(cell_value)
            effort += cell_value * 25/100

    elif fire_type == "High" and 81 <= cell_value <= 125:
        if water_qty - cell_value >= 0:
            water_qty -= cell_value
            total_fire += cell_value
            put_out_cells.append(cell_value)
            effort += cell_value * 25/100

print("Cells:")
for x in put_out_cells:
    print(f" - {x}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
