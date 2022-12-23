sq_meters = float(input())

final_price = sq_meters * 7.61 - (sq_meters * 7.61 * 18/100)
discount = sq_meters * 7.61 * 18/100

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")

