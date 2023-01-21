rows, cols = list(map(int, input().split(", ")))
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

res_list = []

for col in range(cols):
    col_sum = 0
    for row in range(rows):
        col_sum += matrix[row][col]
    res_list.append(col_sum)

print("\n".join(str(x) for x in res_list))