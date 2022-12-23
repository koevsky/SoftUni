projection_type = input()
row_count = int(input())
column_count = int(input())

if projection_type == "Premiere":
    price = row_count*column_count*12
elif projection_type == "Normal":
    price = row_count*column_count*7.50
elif projection_type == "Discount":
    price = row_count*column_count*5
print(f"{price:.2f} leva")