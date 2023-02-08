field = [input().split() for _ in range(6)]

directions = input().split(', ')

movement = {'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
            }

deposits_name = {'W': 'Water', 'M': 'Metal', 'C': 'Concrete'}
deposits_collection = {'W': 0, 'M': 0, 'C': 0}


rover_cords = [(x, field[x].index("E")) for x in range(6) if "E" in field[x]]

rover_row, rover_col = rover_cords[0]

for dirn in directions:

    r, c = movement[dirn]
    rover_row, rover_col = rover_row + r, rover_col + c

    if rover_row < 0:
        rover_row = 5

    elif rover_row > 5:
        rover_row = 0

    if rover_col < 0:
        rover_col = 5

    elif rover_col > 5:
        rover_col = 0

    item = field[rover_row][rover_col]

    if item in deposits_name.keys():
        deposits_collection[item] += 1
        print(f"{deposits_name[item]} deposit found at ({rover_row}, {rover_col})")

    elif item == 'R':
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

if 0 not in deposits_collection.values():
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")


