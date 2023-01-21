rows, cols = [int(x) for x in input().split()]

lair = [list(input()) for _ in range(rows)]

directions_list = list(input())

player_position = [(x, lair[x].index("P")) for x in range(rows) if "P" in lair[x]]

movement = {
    "U": (-1, 0),   # up
    "D": (1, 0),    # down
    "L": (0, -1),   # left
    "R": (0, 1)     # right
}

player_row, player_col = player_position[0]     # unpack player coordinates
final_line = ""

for direction in directions_list:

    player_dead = False
    player_escaped = False

    r, c = movement[direction]
    new_r, new_c = player_row + r, player_col + c

    if not 0 <= new_r < rows or not 0 <= new_c < cols:  # checks if the player escaped
        final_line = f"won: {player_row} {player_col}"
        player_escaped = True

    lair[player_row][player_col] = "."  # no mater escaped or not, previous position becomes free

    if not player_escaped:  # if not escaped, player moves inside the lair (matrix)

        if lair[new_r][new_c] == "B":   # player encountered a bunny
            final_line = f"dead: {new_r} {new_c}"
            player_dead = True

        elif lair[new_r][new_c] == ".":     # player reached free space
            lair[new_r][new_c] = "P"
            player_row, player_col = new_r, new_c

    # bunnies spread after player move
    bunnies_positions = [(x, y) for y in range(cols) for x in range(rows) if lair[x][y] == "B"]

    for bunny_pos in bunnies_positions:     # for every bunny we have found

        bunny_r, bunny_c = bunny_pos    # bunny current position

        for spread_pos in movement.values():    # we spread from its current position

            b_r, b_c = spread_pos
            spread_row, spread_col = bunny_r + b_r, bunny_c + b_c

            if not 0 <= spread_row < rows or not 0 <= spread_col < cols: # check if spread pos is inside lair(matrix)
                continue # if not check next coordinates

            if lair[spread_row][spread_col] == ".":     # free spaces becomes bunny
                lair[spread_row][spread_col] = "B"

            elif lair[spread_row][spread_col] == "P":   # if player is encountered, bunnies kill player
                lair[spread_row][spread_col] = "B"
                final_line = f"dead: {player_row} {player_col}"
                player_dead = True

    if player_dead or player_escaped:
        break

[print("".join(r)) for r in lair]
print(final_line)

