rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_squares_counter = 0

for row in range(rows-1):
    for col in range(cols-1):
        current_square = [matrix[x][y] for y in range(col, col+2) for x in range(row, row+2)]
        if "".join(current_square) == 4*current_square[0]:
            valid_squares_counter += 1

print(valid_squares_counter)
