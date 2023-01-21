import sys

rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

biggest_matrix = []
biggest_sum = -sys.maxsize


for row in range(rows-1):
    for col in range(cols-1):
        current_matrix = [[matrix[x][y] for y in range(col, col+2)] for x in range(row, row+2)]
        current_sum = sum([sum(i) for i in current_matrix])
        if current_sum > biggest_sum:
            biggest_matrix = current_matrix
            biggest_sum = current_sum

[print(*r) for r in biggest_matrix]
print(biggest_sum)