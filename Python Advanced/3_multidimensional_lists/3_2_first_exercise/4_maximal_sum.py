import sys

rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

biggest_square = []
biggest_sum = -sys.maxsize


for row in range(rows-2):
    for col in range(cols-2):
        sub_square = [[matrix[x][y] for y in range(col, col+3)] for x in range(row, row+3)]
        current_sum = sum([sum(i) for i in sub_square])
        if current_sum > biggest_sum:
            biggest_square = sub_square
            biggest_sum = current_sum

print(f"Sum = {biggest_sum}")
[print(*r) for r in biggest_square]