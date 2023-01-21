total_presents = int(input())

size = int(input())

field = [input().split() for _ in range(size)]

santa_position = [(x, y) for y in range(size) for x in range(size) if field[x][y] == "S"]

presents_nice_kids = 0

directions = {

    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
cookie_spread = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

santa_row, santa_col = santa_position[0]

while True:
    line = input()
    if line == "Christmas morning":
        break

    r, c = directions[line]
    new_row, new_col = santa_row + r, santa_col + c

    if not 0 <= new_row < size or not 0 <= new_col < size:
        continue

    field[santa_row][santa_col] = "-"

    if field[new_row][new_col] in ["-", "X"]:
        field[new_row][new_col] = "S"
        santa_row, santa_col = new_row, new_col

    elif field[new_row][new_col] == "V":
        total_presents -= 1
        presents_nice_kids += 1
        field[new_row][new_col] = "S"
        santa_row, santa_col = new_row, new_col

    elif field[new_row][new_col] == "C":
        field[new_row][new_col] = "S"
        santa_row, santa_col = new_row, new_col

        for pos in cookie_spread:

            r, c = pos
            spread_row, spread_col = santa_row + r, santa_col + c

            if field[spread_row][spread_col] in ["V", "X"] and total_presents > 0:
                total_presents -= 1

                if field[spread_row][spread_col] == "V":
                    presents_nice_kids += 1

                field[spread_row][spread_col] = "-"

    if total_presents == 0:
        break

total_nice_kids_left = len([field[x][y] for x in range(size) for y in range(size) if field[x][y] == "V"])

if total_presents == 0 and total_nice_kids_left > 0:
    print("Santa ran out of presents!")

[print(*r) for r in field]

if total_nice_kids_left == 0:
    print(f"Good job, Santa! {presents_nice_kids} happy nice kid/s.")

elif total_nice_kids_left > 0:
    print(f"No presents for {total_nice_kids_left} nice kid/s.")