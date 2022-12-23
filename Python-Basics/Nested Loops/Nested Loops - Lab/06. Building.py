floors_count = int(input())
rooms_per_floor = int(input())
index = ""
for floors in range(floors_count, 0, -1):
    if floors == floors_count:
        index = "L"
    elif floors % 2 == 0:
        index = "O"
    else:
        index = "A"
    for rooms in range(0, rooms_per_floor):
        if rooms != rooms_per_floor-1:
            print(f"{index}{floors}{rooms} ", end="")
        else:
            print(f"{index}{floors}{rooms} ", end="")
            print()
            break