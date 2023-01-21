size = 5

field = [input().split() for _ in range(size)]

cmd_count = int(input())

shooter_position = [(x, y) for y in range(size) for x in range(size) if field[x][y] == "A"]

total_targets = len([field[x][y] for y in range(size) for x in range(size) if field[x][y] == "x"])
targets_hit = []

directions = {

    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

shooter_row, shooter_col = shooter_position[0]

for _ in range(cmd_count):

    line = input().split()

    if line[0] == "move":

        way, steps = line[1], int(line[2])
        r, c = directions[way]
        new_row, new_col = shooter_row + (r*steps), shooter_col + (c*steps)

        if 0 <= new_row < size and 0 <= new_col < size:

            if field[new_row][new_col] == ".":
                field[shooter_row][shooter_col] = "."
                shooter_row, shooter_col = new_row, new_col

    elif line[0] == "shoot":

        way = line[1]
        r, c = directions[way]
        current_row, current_col = shooter_row, shooter_col

        while True:

            current_row += r
            current_col += c

            if not 0 <= current_row < size or not 0 <= current_col < 5:
                break

            if field[current_row][current_col] == "x":
                field[current_row][current_col] = "."
                targets_hit.append([current_row, current_col])
                total_targets -= 1
                break

        if total_targets == 0:
            print(f"Training completed! All {len(targets_hit)} targets hit.")
            break

else:
    print(f"Training not completed! {total_targets} targets left.")

if targets_hit:
    [print(r) for r in targets_hit]