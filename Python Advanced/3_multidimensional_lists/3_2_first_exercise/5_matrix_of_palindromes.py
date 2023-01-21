rows, cols = [int(x) for x in input().split()]
matrix = [[f"{chr(97+x)}{chr(97+x+y)}{chr(97+x)}" for y in range(cols)] for x in range(rows)]
[print(*row) for row in matrix]