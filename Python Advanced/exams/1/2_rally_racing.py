n = int(input())
car_id = input()

field = [input().split() for _ in range(n)]

total_km = 0

movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
car_r, car_c = 0, 0

while True:
    text = input()

    if text == "End":
        field[car_r][car_c] = "C"
        print(f"Racing car {car_id} DNF.")
        break

    r, c = movement[text]
    new_r, new_c = car_r + r, car_c + c

    if field[new_r][new_c] == ".":

        car_r, car_c = new_r, new_c
        total_km += 10

    elif field[new_r][new_c] == "T":

        field[new_r][new_c] = "."
        tunnel_exit = [(x, y) for y in range(n) for x in range(n) if field[x][y] == "T"]
        total_km += 30
        car_r, car_c = tunnel_exit[0]
        field[car_r][car_c] = "."

    elif field[new_r][new_c] == "F":

        total_km += 10
        field[new_r][new_c] = "C"
        print(f"Racing car {car_id} finished the stage!")
        break

print(f"Distance covered {total_km} km.")

[print("".join(row)) for row in field]



