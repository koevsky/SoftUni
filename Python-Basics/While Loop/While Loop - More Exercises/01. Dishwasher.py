detergent_bottles = int(input())
detergent_qty = detergent_bottles * 750
counter = 1
pots_count = 0
dishes_count = 0
while True:
    data = input()
    if data == "End":
        print("Detergent was enough!")
        print(f"{dishes_count} dishes and {pots_count} pots were washed.")
        print(f"Leftover detergent {detergent_qty} ml.")
        break
    object_count = int(data)
    if counter % 3 == 0:
        detergent_used = object_count * 15
    else:
        detergent_used = object_count * 5

    if detergent_qty - detergent_used < 0:
        detergent_needed = abs(detergent_used - detergent_qty)
        print(f"Not enough detergent, {detergent_needed} ml. more necessary!")
        break
    else:
        if counter % 3 == 0:
            pots_count += object_count
        else:
            dishes_count += object_count
        detergent_qty -= detergent_used
        counter += 1