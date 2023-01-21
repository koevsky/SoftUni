n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bomb_coordinates = input().split()

bomb_spread = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

for b in bomb_coordinates:

    bomb = [int(x) for x in b.split(",")]
    b_row, b_col = bomb
    bomb_value = matrix[b_row][b_col]

    if bomb_value > 0:

        for r, c in bomb_spread:
            spread_row, spread_col = r+b_row, c+b_col

            if 0 <= spread_row < n and 0 <= spread_col < n:

                if matrix[spread_row][spread_col] > 0:
                    matrix[spread_row][spread_col] -= bomb_value


alive_cells = sum(len([y for y in x if y > 0]) for x in matrix)
alive_cells_sum = sum([sum([y for y in x if y > 0]) for x in matrix])

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_cells_sum}")
[print(*row) for row in matrix]