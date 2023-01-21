import sys

n = int(input())

field = [input().split() for _ in range(n)]

bunny_position = [(x, y) for y in range(n) for x in range(n) if field[x][y] == "B"]

bunny_path = []
biggest_num = -sys.maxsize
dir_name = ""

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for direction, move in directions.items():

    bunny_row, bunny_col = bunny_position[0]
    current_path = []

    while True:

        bunny_row += move[0]
        bunny_col += move[1]
        if not 0 <= bunny_row < n or not 0 <= bunny_col < n:
            break

        if field[bunny_row][bunny_col] == "X":
            break

        else:
            current_path.append([bunny_row, bunny_col])

    current_path_sum = sum([int(field[x][y]) for x, y in current_path])

    if current_path_sum > biggest_num and current_path:
        biggest_num = current_path_sum
        bunny_path = current_path
        dir_name = direction

print(dir_name)
[print(r) for r in bunny_path]
print(biggest_num)