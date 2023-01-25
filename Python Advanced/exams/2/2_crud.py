


matrix = [input().split() for _ in range(6)]
start_position = [int(x) for x in input().strip("()").split(', ')]


movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

row, col = start_position
while True:
    command = input()

    if command == "Stop":
        break

    key_word, *vals = command.split(", ")

    if key_word == "Create":

        r, c = movement[vals[0]]
        char = vals[1]
        row, col = r + row, c + col
        if matrix[row][col] == ".":
            matrix[row][col] = char

    elif key_word == "Update":

        r, c = movement[vals[0]]
        char = vals[1]
        row, col = r + row, c + col
        if matrix[row][col] != ".":
            matrix[row][col] = char

    elif key_word == "Delete":

        r, c = movement[vals[0]]
        row, col = r + row, c + col
        if matrix[row][col] != ".":
            matrix[row][col] = "."

    elif key_word == "Read":

        r, c = movement[vals[0]]
        row, col = r + row, c + col
        if matrix[row][col] != ".":
            print(matrix[row][col])

[print(" ".join(row)) for row in matrix]