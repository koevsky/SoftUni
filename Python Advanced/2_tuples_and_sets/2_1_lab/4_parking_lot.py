n = int(input())
parking_lot = set()

for _ in range(n):
    direction, plate = input().split(", ")
    if direction == "IN":
        parking_lot.add(plate)
    elif direction == "OUT":
        parking_lot.remove(plate)

if parking_lot:
    print("\n".join(parking_lot))
else:
    print("Parking Lot is Empty")