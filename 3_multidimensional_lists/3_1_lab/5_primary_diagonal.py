n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
diagonal_sum = sum([matrix[x][x] for x in range(n)])
print(diagonal_sum)