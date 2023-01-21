n = int(input())

directions_list = input().split()

matrix = [input().split() for _ in range(n)]

movement = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
            }

miner_position = [(x, matrix[x].index("s")) for x in range(n) if "s" in matrix[x]]

coal_count = len([matrix[x][y] for y in range(n) for x in range(n) if matrix[x][y] == "c"])

miner_row, miner_col = miner_position[0]

for direction in directions_list:

    r, c = movement[direction]
    new_r, new_c = miner_row + r, miner_col + c

    if not 0 <= new_r < n or not 0 <= new_c < n:
        continue

    matrix[miner_row][miner_col] = "*"

    if matrix[new_r][new_c] == "c":
        coal_count -= 1
        matrix[new_r][new_c] = "*"
        miner_row, miner_col = new_r, new_c
        if coal_count == 0:
            print(f"You collected all coal! ({miner_row}, {miner_col})")
            break

    elif matrix[new_r][new_c] == "e":
        miner_row, miner_col = new_r, new_c
        print(f"Game over! ({miner_row}, {miner_col})")
        break

    elif matrix[new_r][new_c] == "*":
        miner_row, miner_col = new_r, new_c

else:
    print(f"{coal_count} pieces of coal left. ({miner_row}, {miner_col})")

