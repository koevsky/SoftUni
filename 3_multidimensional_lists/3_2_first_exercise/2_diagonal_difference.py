n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
primary_diagonal = [matrix[x][x] for x in range(n)]
secondary_diagonal = [matrix[y][n-1-y] for y in range(n)]
primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)
difference = abs(primary_sum - secondary_sum)
print(difference)