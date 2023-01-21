rows, cols = input().split(", ")
matrix_sum = 0
matrix = []

for row in range(int(rows)):
    m = [int(x) for x in input().split(", ")]
    matrix.append(m)
    matrix_sum += sum(m)

print(matrix_sum)
print(matrix)