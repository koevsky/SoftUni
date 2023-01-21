n = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
primary_diagonal = [matrix[x][x] for x in range(n)]
secondary_diagonal = [matrix[y][n-1-y] for y in range(n)]
primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)
print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}.", end=" ")
print(f"Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}.", end=" ")
print(f"Sum: {secondary_sum}")

